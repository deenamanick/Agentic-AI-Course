import json
import os
import uuid
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

from langfuse import get_client
from langfuse.langchain import CallbackHandler


load_dotenv()


SYSTEM_PROMPT_V1 = (
    "You are the Lead AI Architect at Jeevisoft. "
    "You provide expert advice on serverless full-stack backends and Cloudflare. "
    "Be professional, high-energy, and slightly witty."
)

SYSTEM_PROMPT_V2 = (
    SYSTEM_PROMPT_V1
    + " "
    + "Prefer short answers. Use headings. Ask one clarifying question when requirements are unclear."
)


def get_system_prompt(prompt_version: str) -> str:
    if prompt_version == "v2":
        return SYSTEM_PROMPT_V2
    return SYSTEM_PROMPT_V1


class ChatRequest(BaseModel):
    user_query: str = Field(min_length=1, max_length=4000)


class ChatResponse(BaseModel):
    answer: str
    request_id: str
    prompt_version: str


class StructuredChatResponse(BaseModel):
    summary: str
    steps: list[str]
    request_id: str
    prompt_version: str


def build_llm() -> BaseChatModel:
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        return ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            temperature=0.7,
            timeout=30,
            max_retries=2,
        )

    if provider == "ollama":
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


app = FastAPI(title="Jeevisoft Prompting Lab API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("FRONTEND_ORIGIN", "http://localhost:5173"),
    ],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    request_id = str(uuid.uuid4())

    llm = build_llm()
    langfuse_handler = CallbackHandler()

    prompt_version = os.getenv("PROMPT_VERSION", "v1")

    messages = [
        SystemMessage(content=get_system_prompt(prompt_version)),
        HumanMessage(content=req.user_query),
    ]

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

    get_client().flush()

    return ChatResponse(
        answer=result.content,
        request_id=request_id,
        prompt_version=prompt_version,
    )


@app.post("/chat/structured", response_model=StructuredChatResponse)
async def chat_structured(req: ChatRequest) -> StructuredChatResponse:
    request_id = str(uuid.uuid4())

    llm = build_llm()
    langfuse_handler = CallbackHandler()

    prompt_version = os.getenv("PROMPT_VERSION", "v1")

    schema: dict[str, Any] = {
        "summary": "string",
        "steps": ["string"],
    }

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

    get_client().flush()

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

    return StructuredChatResponse(
        summary=summary,
        steps=steps,
        request_id=request_id,
        prompt_version=prompt_version,
    )
