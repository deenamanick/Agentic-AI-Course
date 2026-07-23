import ast
import os
import time
import uuid
from typing import Any

"""
================================================================================
WHAT MAKES THIS AN "AGENT" AND NOT JUST A CHATBOT?
--------------------------------------------------------------------------------
1. TOOLS (The Hands): Python functions (like `calculator`) that the AI can use.
2. BRAIN (The LLM): The AI model (Groq or Ollama) that makes decisions.
3. LOOP (The ReAct Pattern): The agent doesn't just answer immediately. It loops:
   - THINK: "Do I need a tool for this user's question?"
   - ACT: Call the tool (e.g., calculator).
   - OBSERVE: Read the tool's result.
   - REPEAT: Keep thinking/acting until it has the final answer.
================================================================================
"""

# Load environment variables from the .env file
from dotenv import load_dotenv

# FastAPI is our web server framework
from fastapi import FastAPI
# BaseModel and Field define the request/response shapes
from pydantic import BaseModel, Field

# ─── LangGraph (Modern Agent Framework) ──────────────────────────────
# We use LangGraph's prebuilt ReAct agent instead of the deprecated AgentExecutor.
# LangGraph is the industry standard for production agents (2025/2026).
from langgraph.prebuilt import create_react_agent

# LangChain tools — the @tool decorator lets the AI call Python functions
from langchain_core.tools import tool
# LangChain model interfaces — same as Module 1 & 2
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_groq import ChatGroq      # Groq Cloud (fast, no GPU needed)
from langchain_ollama import ChatOllama  # Ollama (local, runs on your computer)

# Langfuse tracks and traces our agent's reasoning steps
from langfuse import get_client
from langfuse.langchain import CallbackHandler


# Read the .env file and load all settings
load_dotenv()


# ─── REQUEST & RESPONSE SHAPES ───────────────────────────────────────

class AgentChatRequest(BaseModel):
    user_query: str = Field(min_length=1, max_length=4000)
    # The user's question. Must be 1–4000 characters.


class AgentChatResponse(BaseModel):
    answer: str      # The agent's final answer
    request_id: str  # Unique ID for tracking in Langfuse


# ─── MODEL PROVIDER SELECTION ─────────────────────────────────────────
# Same pattern as Module 1 & 2 — the "Kitchen" stays the same.
# Now we support BOTH Groq (cloud) and Ollama (local) for agents too!
def build_llm() -> BaseChatModel:
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        # Groq Cloud — fast inference, no local GPU needed
        return ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            temperature=float(os.getenv("LLM_TEMPERATURE", "0.2")),
            timeout=30,
            max_retries=2,
        )

    if provider == "ollama":
        # Ollama — runs locally on your computer (optional path)
        return ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "llama4:scout"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            temperature=float(os.getenv("LLM_TEMPERATURE", "0.2")),
        )

    raise ValueError(
        "Unsupported LLM_PROVIDER. Choose 'groq' or 'ollama'."
    )


# ─── TOOLS ────────────────────────────────────────────────────────────
# Tools are Python functions that the AI agent can decide to call.
# The @tool decorator tells LangChain "the AI is allowed to use this."
# The docstring is what the AI reads to decide WHEN to use each tool.

def _safe_eval_arithmetic(expression: str) -> str:
    """
    Safely evaluate an arithmetic expression WITHOUT using dangerous eval().
    Only allows: +, -, *, /, **, //, % and numbers.
    Blocks: function calls, imports, variable access.
    """
    node = ast.parse(expression, mode="eval")

    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.FloorDiv,
        ast.Mod,
        ast.Pow,
        ast.USub,
        ast.UAdd,
        ast.Constant,
        ast.Load,
        ast.Call,
        ast.Name,
    )

    for subnode in ast.walk(node):
        if not isinstance(subnode, allowed_nodes):
            raise ValueError("Unsupported expression")
        if isinstance(subnode, ast.Call):
            raise ValueError("Function calls are not allowed")
        if isinstance(subnode, ast.Name):
            raise ValueError("Names are not allowed")

    result = eval(compile(node, "<expr>", "eval"), {"__builtins__": {}}, {})
    return str(result)


@tool
def calculator(expression: str) -> str:
    """Evaluate a simple arithmetic expression, e.g. "(17 * 23) + 5"."""
    # The AI will call this when users ask math questions.
    # We use _safe_eval_arithmetic to prevent code injection attacks.
    try:
        return _safe_eval_arithmetic(expression)
    except Exception as e:
        return f"error: {e}"


@tool
def now_unix() -> str:
    """Return the current Unix timestamp in seconds."""
    # The AI will call this when users ask about the current time.
    return str(int(time.time()))


@tool
def echo(text: str) -> str:
    """Echo back the given text."""
    # A simple test tool — useful for verifying that tool calling works.
    return text


# ─── BUILD THE AGENT (LangGraph) ─────────────────────────────────────
# This creates a ReAct agent using LangGraph.
# The agent follows the Think → Act → Observe loop from Practical 3.3.
#
# Flow:
#   START → agent_node (Brain thinks: should I use a tool?)
#             ↓ YES → tool_node (calls the tool) → agent_node (reads result)
#             ↓ NO  → END (return final answer)

def build_agent(llm: BaseChatModel):
    """Create a LangGraph ReAct agent with our tools."""
    tools = [calculator, now_unix, echo]

    # create_react_agent builds the complete Think→Act→Observe graph
    # This replaces the deprecated AgentExecutor from old LangChain
    agent = create_react_agent(
        model=llm,
        tools=tools,
    )

    return agent


# ─── CREATE THE FASTAPI APP ──────────────────────────────────────────
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Jeevisoft Agents API", version="0.3.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("FRONTEND_ORIGIN", "http://localhost:5173"),
    ],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


# ─── ENDPOINT: Agent Chat ────────────────────────────────────────────
# This endpoint lets the AI decide which tools to use for each question.
# Compare this to Module 2's POST /chat which just returns text directly.
@app.post("/agent/chat", response_model=AgentChatResponse)
async def agent_chat(req: AgentChatRequest) -> AgentChatResponse:
    # Step 1: Generate a unique ID for this request
    request_id = str(uuid.uuid4())

    # Step 2: Get the AI model (Groq or Ollama) and build the agent
    llm = build_llm()
    agent = build_agent(llm)

    # Step 3: Prepare the Langfuse tracker
    langfuse_handler = CallbackHandler()

    # Step 4: Run the agent!
    # The agent will automatically:
    #   - Read the user's question
    #   - Decide if it needs a tool
    #   - Call the tool if needed
    #   - Return the final answer
    max_iterations = int(os.getenv("AGENT_MAX_ITERATIONS", "6"))

    result = await agent.ainvoke(
        {"messages": [("user", req.user_query)]},
        config={
            "callbacks": [langfuse_handler],
            "recursion_limit": max_iterations * 2,  # LangGraph uses recursion_limit
            "metadata": {
                "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
                "environment": os.getenv("APP_ENV", "Development"),
                "request_id": request_id,
                "langfuse_session_id": request_id,
                "langfuse_tags": [
                    f"Project:{os.getenv('APP_PROJECT', 'Jeevi-Academy')}",
                    f"Environment:{os.getenv('APP_ENV', 'Development')}",
                    "Module:LangGraph-Agents",
                ],
            },
        },
    )

    # Step 5: Flush tracking data to Langfuse
    get_client().flush()

    # Step 6: Extract the final answer from the agent's messages
    # The last message in the list is the agent's final response
    messages = result.get("messages", [])
    if messages:
        output = messages[-1].content
    else:
        output = "No response generated."

    if not isinstance(output, str):
        output = str(output)

    # Step 7: Return the answer and request ID
    return AgentChatResponse(answer=output, request_id=request_id)
