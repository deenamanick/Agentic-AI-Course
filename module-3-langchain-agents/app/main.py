import ast
import os
import time
import uuid
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from langfuse import get_client
from langfuse.langchain import CallbackHandler


load_dotenv()


class AgentChatRequest(BaseModel):
    user_query: str


class AgentChatResponse(BaseModel):
    answer: str
    request_id: str


def build_llm() -> ChatOllama:
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "llama4:scout")

    return ChatOllama(
        model=model,
        base_url=base_url,
        temperature=float(os.getenv("OLLAMA_TEMPERATURE", "0.2")),
    )


def _safe_eval_arithmetic(expression: str) -> str:
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

    try:
        return _safe_eval_arithmetic(expression)
    except Exception as e:
        return f"error: {e}"


@tool
def now_unix() -> str:
    """Return the current Unix timestamp in seconds."""

    return str(int(time.time()))


@tool
def echo(text: str) -> str:
    """Echo back the given text."""

    return text


def build_agent_executor(llm: ChatOllama) -> AgentExecutor:
    tools = [calculator, now_unix, echo]

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful agent. Use tools when they help. "
                "If you use a tool, follow the ReAct format and keep the final answer concise.",
            ),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

    max_iterations = int(os.getenv("AGENT_MAX_ITERATIONS", "6"))
    return AgentExecutor(
        agent=agent,
        tools=tools,
        max_iterations=max_iterations,
        verbose=False,
        handle_parsing_errors=True,
    )


app = FastAPI(title="Jeevisoft Agents API", version="0.3.0")


@app.post("/agent/chat", response_model=AgentChatResponse)
async def agent_chat(req: AgentChatRequest) -> AgentChatResponse:
    request_id = str(uuid.uuid4())

    llm = build_llm()
    executor = build_agent_executor(llm)
    langfuse_handler = CallbackHandler()

    result: dict[str, Any] = await executor.ainvoke(
        {"input": req.user_query},
        config={
            "callbacks": [langfuse_handler],
            "metadata": {
                "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
                "environment": os.getenv("APP_ENV", "Development"),
                "request_id": request_id,
                "langfuse_session_id": request_id,
                "langfuse_tags": [
                    f"Project:{os.getenv('APP_PROJECT', 'Jeevi-Academy')}",
                    f"Environment:{os.getenv('APP_ENV', 'Development')}",
                    "Module:LangChain-Agents",
                ],
            },
        },
    )

    get_client().flush()

    output = result.get("output")
    if not isinstance(output, str):
        output = str(output)

    return AgentChatResponse(answer=output, request_id=request_id)
