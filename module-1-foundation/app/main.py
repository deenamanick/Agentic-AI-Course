import os
import uuid

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

from langfuse import get_client
from langfuse.langchain import CallbackHandler


load_dotenv()


SYSTEM_PROMPT = (
    "You are the Lead AI Architect at Jeevisoft. "
    "You provide expert advice on serverless full-stack backends and Cloudflare. "
    "Be professional, high-energy, and slightly witty."
)


class ChatRequest(BaseModel):
    user_query: str


class ChatResponse(BaseModel):
    answer: str
    request_id: str


def build_llm() -> ChatOllama:
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "llama4:scout")

    return ChatOllama(
        model=model,
        base_url=base_url,
        temperature=0.7,
        model_kwargs={
            "num_ctx": 32768,
        },
    )


app = FastAPI(title="Jeevisoft Local AI Backend", version="0.1.0")


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    request_id = str(uuid.uuid4())

    llm = build_llm()
    langfuse_handler = CallbackHandler()

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
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
                "langfuse_session_id": request_id,
                "langfuse_tags": [
                    f"Project:{os.getenv('APP_PROJECT', 'Jeevi-Academy')}",
                    f"Environment:{os.getenv('APP_ENV', 'Development')}",
                ],
            },
        },
    )

    # Flush so the trace shows up immediately in Langfuse.
    get_client().flush()

    return ChatResponse(answer=result.content, request_id=request_id)
