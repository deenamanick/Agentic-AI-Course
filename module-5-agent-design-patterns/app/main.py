import os
import uuid
from typing import Any, Dict, TypedDict

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

from langfuse import get_client
from langfuse.langchain import CallbackHandler
from langgraph.graph import StateGraph, START, END

load_dotenv()

# ─── REQUEST & RESPONSE SHAPES ───────────────────────────────────────

class AnalyzerRequest(BaseModel):
    raw_cv: str = Field(..., description="The user's messy CV text.")
    job_title: str = Field(..., description="The role they are applying for.")

class AnalyzerResponse(BaseModel):
    final_review: str
    request_id: str

# ─── GRAPH STATE (THE BUCKET) ────────────────────────────────────────

class JobAnalyzerState(TypedDict):
    raw_cv: str            # Input
    job_title: str         # Input
    
    draft_review: str      # Output of Node 1
    critique: str          # Output of Node 2
    final_review: str      # Output of Node 3
    
    llm: BaseChatModel
    langfuse_handler: CallbackHandler

# ─── MODEL PROVIDER ──────────────────────────────────────────────────

def build_llm() -> BaseChatModel:
    provider = os.getenv("LLM_PROVIDER", "groq").lower()
    
    if provider == "groq":
        return ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            temperature=0.4,
            max_retries=2,
        )
    if provider == "ollama":
        return ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "llama4:scout"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            temperature=0.4,
        )
    raise ValueError("Unsupported LLM_PROVIDER. Choose 'groq' or 'ollama'.")

# ─── NODE 1: ANALYZER (DRAFT) ────────────────────────────────────────

async def analyzer_node(state: JobAnalyzerState) -> Dict[str, Any]:
    """Node 1: Draft the initial CV review."""
    llm = state["llm"]
    handler = state["langfuse_handler"]
    
    prompt = f"""
    You are an expert recruiter. Analyze this CV for a {state['job_title']} role.
    Provide strengths, weaknesses, and an overall score out of 100.
    Format your response in Markdown.
    
    CV:
    {state['raw_cv']}
    """
    
    result = await llm.ainvoke(prompt, config={"callbacks": [handler]})
    return {"draft_review": result.content}

# ─── NODE 2: CRITIQUE ────────────────────────────────────────────────

async def critique_node(state: JobAnalyzerState) -> Dict[str, Any]:
    """Node 2: The Harsh Critic reviews the draft."""
    llm = state["llm"]
    handler = state["langfuse_handler"]
    
    prompt = f"""
    You are a harsh Senior HR Manager. Review the CV analysis below.
    Find 3 specific things the reviewer missed or could improve. 
    Did they include a clear score? Is the formatting professional? Are they too nice?
    Be extremely critical. Do NOT rewrite the review, just list the flaws.
    
    Draft Review:
    {state['draft_review']}
    """
    
    result = await llm.ainvoke(prompt, config={"callbacks": [handler]})
    return {"critique": result.content}

# ─── NODE 3: REFINE ──────────────────────────────────────────────────

async def refine_node(state: JobAnalyzerState) -> Dict[str, Any]:
    """Node 3: Refine the review based on the critique."""
    llm = state["llm"]
    handler = state["langfuse_handler"]
    
    prompt = f"""
    You are an expert recruiter. You wrote a draft CV review, but your manager critiqued it.
    Rewrite the final review, fixing ALL the issues raised by your manager.
    Output only the final Markdown review.
    
    Your Draft:
    {state['draft_review']}
    
    Manager's Critique:
    {state['critique']}
    """
    
    result = await llm.ainvoke(prompt, config={"callbacks": [handler]})
    return {"final_review": result.content}

# ─── BUILD THE GRAPH ─────────────────────────────────────────────────

def build_graph():
    workflow = StateGraph(JobAnalyzerState)

    workflow.add_node("analyzer", analyzer_node)
    workflow.add_node("critique", critique_node)
    workflow.add_node("refine", refine_node)

    # The Reflection Pattern (1-cycle limit for API speed)
    workflow.add_edge(START, "analyzer")
    workflow.add_edge("analyzer", "critique")
    workflow.add_edge("critique", "refine")
    workflow.add_edge("refine", END)

    return workflow.compile()

# ─── FASTAPI APP ─────────────────────────────────────────────────────

app = FastAPI(title="Jeevisoft Job Analyzer API", version="0.5.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.post("/analyzer/score", response_model=AnalyzerResponse)
async def score_cv(req: AnalyzerRequest) -> AnalyzerResponse:
    request_id = str(uuid.uuid4())

    llm = build_llm()
    langfuse_handler = CallbackHandler()

    app_state: JobAnalyzerState = {
        "raw_cv": req.raw_cv,
        "job_title": req.job_title,
        "draft_review": "",
        "critique": "",
        "final_review": "",
        "llm": llm,
        "langfuse_handler": langfuse_handler,
    }

    metadata = {
        "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
        "environment": os.getenv("APP_ENV", "Development"),
        "request_id": request_id,
        "langfuse_session_id": request_id,
        "langfuse_tags": ["Module:DesignPatterns-Reflection"],
    }

    runnable = build_graph()

    result_state: Dict[str, Any] = await runnable.ainvoke(
        app_state,
        config={
            "callbacks": [langfuse_handler],
            "metadata": metadata,
        },
    )

    get_client().flush()

    final_md = result_state.get("final_review", "Error: No review generated.")

    return AnalyzerResponse(final_review=final_md, request_id=request_id)
