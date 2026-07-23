import json
import os
import uuid
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from langchain_core.messages import HumanMessage, SystemMessage
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
    user_query: str


class ChatResponse(BaseModel):
    answer: str
    request_id: str
    prompt_version: str


class StructuredChatResponse(BaseModel):
    summary: str
    steps: list[str]
    request_id: str
    prompt_version: str


def build_llm() -> ChatOllama:
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "llama4:scout")

    return ChatOllama(
        model=model,
        base_url=base_url,
        temperature=float(os.getenv("OLLAMA_TEMPERATURE", "0.7")),
        model_kwargs={
            "num_ctx": int(os.getenv("OLLAMA_NUM_CTX", "32768")),
        },
    )


app = FastAPI(title="Jeevisoft Prompting Lab API", version="0.2.0")


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
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Model did not return valid structured JSON: {e}",
        )

    return StructuredChatResponse(
        summary=summary,
        steps=steps,
        request_id=request_id,
        prompt_version=prompt_version,
    )
