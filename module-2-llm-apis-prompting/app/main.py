import json
import os
import uuid
from typing import Any

# Load environment variables from the .env file (API keys, model settings, etc.)
from dotenv import load_dotenv

# FastAPI is our web server framework; HTTPException lets us return error codes
from fastapi import FastAPI, HTTPException
# CORS allows our React frontend to connect to this backend
from fastapi.middleware.cors import CORSMiddleware
# BaseModel and Field help us define and validate the shape of requests/responses
from pydantic import BaseModel, Field

# LangChain tools for talking to AI models
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq      # Groq Cloud (fast, no GPU needed)
from langchain_ollama import ChatOllama  # Ollama (local, runs on your computer)

# Langfuse tracks and traces our AI requests (like a flight recorder for AI)
from langfuse import get_client
from langfuse.langchain import CallbackHandler


# Read the .env file and load all settings into the system
load_dotenv()


# ─── PROMPT VERSIONS ─────────────────────────────────────────────────
# v1 is the basic prompt — it tells the AI WHO it is and HOW to behave.
SYSTEM_PROMPT_V1 = (
    "You are the Lead AI Architect at Jeevisoft. "
    "You provide expert advice on serverless full-stack backends and Cloudflare. "
    "Be professional, high-energy, and slightly witty."
)

# v2 EXTENDS v1 by adding extra rules:
#   - Keep answers short
#   - Use headings for readability
#   - Ask a clarifying question if the request is unclear
# This lets us compare how different instructions change the AI's behavior.
SYSTEM_PROMPT_V2 = (
    SYSTEM_PROMPT_V1
    + " "
    + "Prefer short answers. Use headings. Ask one clarifying question when requirements are unclear."
)


def get_system_prompt(prompt_version: str) -> str:
    """Pick the right prompt based on the PROMPT_VERSION setting in .env"""
    if prompt_version == "v2":
        return SYSTEM_PROMPT_V2
    return SYSTEM_PROMPT_V1


# ─── REQUEST & RESPONSE SHAPES (Pydantic Models) ─────────────────────
# These define the "contract" between the frontend and backend.
# If the frontend sends the wrong shape, FastAPI will reject it automatically.

class ChatRequest(BaseModel):
    user_query: str = Field(min_length=1, max_length=4000)
    # The student's question. Must be 1–4000 characters (not empty, not huge).


class ChatResponse(BaseModel):
    answer: str          # The AI's text response
    request_id: str      # Unique ID to track this request in logs/Langfuse
    prompt_version: str  # Which prompt version (v1 or v2) generated this answer


class StructuredChatResponse(BaseModel):
    summary: str         # A short summary of the answer
    steps: list[str]     # Step-by-step instructions as a list
    request_id: str      # Unique ID for tracking
    prompt_version: str  # Which prompt version was used


# ─── MODEL PROVIDER SELECTION ─────────────────────────────────────────
# This function reads LLM_PROVIDER from .env and creates the right AI client.
# Identical to Module 1 — the "Kitchen" stays the same, only the "Recipe" changes.
def build_llm() -> BaseChatModel:
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        # Groq Cloud — fast inference, no local GPU needed
        return ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            temperature=0.7,  # 0.0 = robotic, 1.0 = very creative
            timeout=30,
            max_retries=2,
        )

    if provider == "ollama":
        # Ollama — runs locally on your computer (optional path)
        return ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "llama4:scout"),
            base_url=os.getenv(
                "OLLAMA_BASE_URL",
                "http://localhost:11434",
            ),
            temperature=float(
                os.getenv("OLLAMA_TEMPERATURE", "0.7")
            ),
            model_kwargs={
                "num_ctx": int(
                    os.getenv("OLLAMA_NUM_CTX", "32768")
                ),
            },
        )

    raise ValueError(
        "Unsupported LLM_PROVIDER. Choose 'groq' or 'ollama'."
    )


# ─── CREATE THE FASTAPI APP ──────────────────────────────────────────
app = FastAPI(title="Jeevisoft Prompting Lab API", version="0.2.0")

# Allow our React frontend (port 5173) to talk to this backend (port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("FRONTEND_ORIGIN", "http://localhost:5173"),
    ],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


# ─── ENDPOINT 1: Normal Chat (Returns plain text) ────────────────────
# This is the same /chat endpoint from Module 1, but now it also:
#   - Reads PROMPT_VERSION from .env (v1 or v2)
#   - Returns prompt_version in the response so we can trace which prompt was used
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    # Step 1: Generate a unique ID for this request
    request_id = str(uuid.uuid4())

    # Step 2: Get the AI model client (Groq or Ollama)
    llm = build_llm()
    # Step 3: Prepare the Langfuse tracker
    langfuse_handler = CallbackHandler()

    # Step 4: Read the prompt version from .env (defaults to "v1")
    prompt_version = os.getenv("PROMPT_VERSION", "v1")

    # Step 5: Build the conversation — system instructions first, then the user's question
    messages = [
        SystemMessage(content=get_system_prompt(prompt_version)),
        HumanMessage(content=req.user_query),
    ]

    # Step 6: Send to the AI model and wait for the response
    result = await llm.ainvoke(
        messages,
        config={
            "callbacks": [langfuse_handler],
            "metadata": {
                "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
                "environment": os.getenv("APP_ENV", "Development"),
                "request_id": request_id,
                "prompt_version": prompt_version,
                "langfuse_session_id": request_id,
                "langfuse_tags": [
                    f"Project:{os.getenv('APP_PROJECT', 'Jeevi-Academy')}",
                    f"Environment:{os.getenv('APP_ENV', 'Development')}",
                    f"PromptVersion:{prompt_version}",
                ],
            },
        },
    )

    # Step 7: Flush tracking data to Langfuse immediately
    get_client().flush()

    # Step 8: Return the answer, the request ID, and which prompt version was used
    return ChatResponse(
        answer=result.content,
        request_id=request_id,
        prompt_version=prompt_version,
    )


# ─── ENDPOINT 2: Structured Chat (Returns JSON with summary + steps) ─
# This endpoint forces the AI to return data in a predictable JSON format.
# Why? Because software needs structured data, not paragraphs of text.
# Example: { "summary": "...", "steps": ["Step 1", "Step 2", "Step 3"] }
@app.post("/chat/structured", response_model=StructuredChatResponse)
async def chat_structured(req: ChatRequest) -> StructuredChatResponse:
    # Step 1: Generate a unique request ID
    request_id = str(uuid.uuid4())

    # Step 2: Get the AI model and tracker
    llm = build_llm()
    langfuse_handler = CallbackHandler()

    # Step 3: Read prompt version
    prompt_version = os.getenv("PROMPT_VERSION", "v1")

    # Step 4: Define the JSON shape we want the AI to return
    schema: dict[str, Any] = {
        "summary": "string",
        "steps": ["string"],
    }

    # Step 5: Build the conversation — notice we ADD extra instructions
    #   telling the AI to return ONLY valid JSON (no extra text!)
    messages = [
        SystemMessage(
            content=(
                get_system_prompt(prompt_version)
                + " "
                + "Return ONLY valid JSON with keys: summary (string) and steps (array of strings)."
                + f" Schema example: {json.dumps(schema)}"
            )
        ),
        HumanMessage(content=req.user_query),
    ]

    # Step 6: Send to the AI model
    result = await llm.ainvoke(
        messages,
        config={
            "callbacks": [langfuse_handler],
            "metadata": {
                "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
                "environment": os.getenv("APP_ENV", "Development"),
                "request_id": request_id,
                "prompt_version": prompt_version,
                "langfuse_session_id": request_id,
                "langfuse_tags": [
                    f"Project:{os.getenv('APP_PROJECT', 'Jeevi-Academy')}",
                    f"Environment:{os.getenv('APP_ENV', 'Development')}",
                    f"PromptVersion:{prompt_version}",
                ],
            },
        },
    )

    # Step 7: Flush tracking data
    get_client().flush()

    # Step 8: VALIDATE the AI's response
    # The AI might not follow instructions perfectly, so we MUST check:
    #   - Did it return valid JSON? (not a paragraph)
    #   - Does it have "summary" (a string) and "steps" (a list of strings)?
    # If any check fails, return HTTP 502 (Bad Gateway) — meaning
    # "our upstream dependency (the AI) gave us something unusable."
    try:
        parsed = json.loads(result.content)
        summary = parsed["summary"]
        steps = parsed["steps"]
        if not isinstance(summary, str) or not isinstance(steps, list) or not all(
            isinstance(s, str) for s in steps
        ):
            raise ValueError("Invalid JSON shape")
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        raise HTTPException(
            status_code=502,
            detail="Model did not return the required structured response.",
        ) from None

    # Step 9: Return the validated structured response
    return StructuredChatResponse(
        summary=summary,
        steps=steps,
        request_id=request_id,
        prompt_version=prompt_version,
    )

