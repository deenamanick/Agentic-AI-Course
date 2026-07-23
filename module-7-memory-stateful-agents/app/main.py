import os
import uuid
from typing import Any, Dict

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from langfuse import get_client
from langfuse.langchain import CallbackHandler

load_dotenv()

# ─── REQUEST & RESPONSE SHAPES ───────────────────────────────────────

class AgentRequest(BaseModel):
    user_query: str = Field(..., description="The user's message.")
    thread_id: str = Field(..., description="Unique ID for the conversation thread. Required for memory.")

class AgentResponse(BaseModel):
    answer: str
    request_id: str

# ─── AGENT SETUP WITH MEMORY ─────────────────────────────────────────

def build_llm():
    provider = os.getenv("LLM_PROVIDER", "groq").lower()
    if provider == "groq":
        return ChatGroq(model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"), temperature=0.5)
    if provider == "ollama":
        return ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama4:scout"), temperature=0.5)
    raise ValueError("Unsupported LLM_PROVIDER.")

# 1. Create the database (in RAM)
# NOTE: In production, you would use PostgresSaver or SqliteSaver here!
memory_saver = MemorySaver()

def get_agent():
    llm = build_llm()
    
    # 2. We pass the memory_saver to the checkpointer argument.
    # The agent is now stateful!
    return create_react_agent(
        model=llm, 
        tools=[],  # No tools needed for a simple chat companion
        checkpointer=memory_saver
    )

# ─── FASTAPI APP ─────────────────────────────────────────────────────

app = FastAPI(title="Jeevisoft Mental Health Companion API", version="0.7.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.post("/agent/chat", response_model=AgentResponse)
async def chat_endpoint(req: AgentRequest) -> AgentResponse:
    request_id = str(uuid.uuid4())
    langfuse_handler = CallbackHandler()
    
    agent = get_agent()
    
    # We create a calming persona for the companion.
    sys_msg = SystemMessage(content="""
    You are an empathetic, calming, and supportive Mental Health Companion.
    Your goal is to listen to the user, validate their feelings, and offer 
    gentle mindfulness or breathing exercises if they are stressed.
    Always be polite and keep your answers relatively short.
    Remember what the user tells you over time!
    """)
    human_msg = HumanMessage(content=req.user_query)
    
    metadata = {
        "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
        "request_id": request_id,
        "langfuse_session_id": request_id,
        "langfuse_tags": ["Module:Memory-Companion"],
    }
    
    # 3. We pass the thread_id inside the config dictionary.
    # LangGraph automatically loads the past history for this thread, runs the LLM, 
    # and saves the new history back to the checkpointer!
    config = {
        "configurable": {"thread_id": req.thread_id},
        "callbacks": [langfuse_handler],
        "metadata": metadata
    }
    
    result = await agent.ainvoke(
        {"messages": [sys_msg, human_msg]},
        config=config
    )
    
    get_client().flush()
    
    final_answer = result["messages"][-1].content
    return AgentResponse(answer=str(final_answer), request_id=request_id)
