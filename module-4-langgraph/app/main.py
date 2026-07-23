import os
import uuid
from typing import Any, Dict, Optional, TypedDict

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_core.language_models.chat_models import BaseChatModel

from langfuse import get_client
from langfuse.langchain import CallbackHandler
from langgraph.graph import StateGraph, START, END

load_dotenv()

# ─── REQUEST & RESPONSE SHAPES ───────────────────────────────────────

class ResumeRequest(BaseModel):
    raw_text: str = Field(..., description="The user's messy text about their experience and skills.")

class ResumeResponse(BaseModel):
    markdown_resume: str
    request_id: str

# ─── EXTRACTION SCHEMA ───────────────────────────────────────────────
# This is the "mold" we force the AI to fill in Node 1.

class ExtractedResumeData(BaseModel):
    name: str = Field(description="The person's full name, if provided. If not, return 'Unknown'.")
    skills: list[str] = Field(description="A list of technical and soft skills.")
    experience: list[str] = Field(description="A list of past work experience, jobs, or roles.")

# ─── GRAPH STATE (THE BUCKET) ────────────────────────────────────────

class ResumeState(TypedDict):
    raw_text: str
    name: Optional[str]
    skills: list[str]
    experience: list[str]
    summary: Optional[str]
    final_resume: str
    llm: BaseChatModel            # Pass the LLM through state for convenience
    langfuse_handler: CallbackHandler # Pass the tracker

# ─── MODEL PROVIDER ──────────────────────────────────────────────────

def build_llm() -> BaseChatModel:
    provider = os.getenv("LLM_PROVIDER", "groq").lower()
    
    if provider == "groq":
        return ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            temperature=0.1,
            max_retries=2,
        )
    if provider == "ollama":
        return ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "llama4:scout"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            temperature=0.1,
        )
    raise ValueError("Unsupported LLM_PROVIDER. Choose 'groq' or 'ollama'.")

# ─── NODE 1: EXTRACT ─────────────────────────────────────────────────

async def extract_node(state: ResumeState) -> Dict[str, Any]:
    """
    Node 1: Reads raw_text and extracts structured JSON data.
    """
    llm = state["llm"]
    handler = state["langfuse_handler"]
    raw_text = state["raw_text"]

    # Force the LLM to return data matching our Pydantic schema
    extractor = llm.with_structured_output(ExtractedResumeData)
    
    prompt = f"Extract the name, skills, and experience from this text:\n\n{raw_text}"
    
    result = await extractor.ainvoke(prompt, config={"callbacks": [handler]})
    
    # Update the bucket
    return {
        "name": result.name,
        "skills": result.skills,
        "experience": result.experience
    }

# ─── NODE 2: DRAFT ───────────────────────────────────────────────────

async def draft_summary_node(state: ResumeState) -> Dict[str, Any]:
    """
    Node 2: Drafts a professional summary based on the extracted data.
    """
    llm = state["llm"]
    handler = state["langfuse_handler"]
    
    name = state.get("name", "User")
    skills = ", ".join(state.get("skills", []))
    exp = ", ".join(state.get("experience", []))
    
    prompt = f"""
    Write a 3-sentence professional resume summary for {name}.
    They have these skills: {skills}.
    They have this experience: {exp}.
    Make it sound highly professional and impactful. Do not use the word "I".
    """
    
    response = await llm.ainvoke(prompt, config={"callbacks": [handler]})
    
    # Update the bucket
    return {"summary": response.content}

# ─── NODE 3: FORMAT ──────────────────────────────────────────────────

def format_node(state: ResumeState) -> Dict[str, Any]:
    """
    Node 3: Combines all state data into a final formatted Markdown resume.
    Notice this function is NOT async and does NOT call the LLM!
    """
    name = state.get("name", "Unknown Name")
    summary = state.get("summary", "No summary provided.")
    skills = state.get("skills", [])
    experience = state.get("experience", [])
    
    # Create the markdown string
    md = f"# {name.upper()}\n\n"
    
    md += "## PROFESSIONAL SUMMARY\n"
    md += f"{summary}\n\n"
    
    md += "## SKILLS\n"
    for skill in skills:
        md += f"- {skill}\n"
    md += "\n"
    
    md += "## EXPERIENCE\n"
    for exp in experience:
        md += f"- {exp}\n"
        
    # Update the bucket
    return {"final_resume": md}

# ─── BUILD THE GRAPH ─────────────────────────────────────────────────

def build_graph():
    workflow = StateGraph(ResumeState)

    # Add workers
    workflow.add_node("extract", extract_node)
    workflow.add_node("draft", draft_summary_node)
    workflow.add_node("format", format_node)

    # Define the strict, deterministic workflow
    workflow.add_edge(START, "extract")
    workflow.add_edge("extract", "draft")
    workflow.add_edge("draft", "format")
    workflow.add_edge("format", END)

    return workflow.compile()

# ─── FASTAPI APP ─────────────────────────────────────────────────────

app = FastAPI(title="Jeevisoft Resume Builder Workflow API", version="0.4.0")

# Add CORS for the Lovable UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.post("/resume/build", response_model=ResumeResponse)
async def build_resume(req: ResumeRequest) -> ResumeResponse:
    request_id = str(uuid.uuid4())

    llm = build_llm()
    langfuse_handler = CallbackHandler()

    # Initial empty bucket
    app_state: ResumeState = {
        "raw_text": req.raw_text,
        "name": None,
        "skills": [],
        "experience": [],
        "summary": None,
        "final_resume": "",
        "llm": llm,
        "langfuse_handler": langfuse_handler,
    }

    metadata = {
        "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
        "environment": os.getenv("APP_ENV", "Development"),
        "request_id": request_id,
        "langfuse_session_id": request_id,
        "langfuse_tags": ["Module:LangGraph-Resume"],
    }

    runnable = build_graph()

    # Run the graph
    result_state: Dict[str, Any] = await runnable.ainvoke(
        app_state,
        config={
            "callbacks": [langfuse_handler],
            "metadata": metadata,
        },
    )

    get_client().flush()

    # Get the final markdown from the completed bucket
    final_md = result_state.get("final_resume", "")

    return ResumeResponse(markdown_resume=final_md, request_id=request_id)
