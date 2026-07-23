import os
import uuid

# Load environment variables from the .env file (like API keys)
from dotenv import load_dotenv

# FastAPI is the framework we use to build the web server
from fastapi import FastAPI
# CORS allows our React frontend to talk to this backend securely
from fastapi.middleware.cors import CORSMiddleware
# BaseModel helps us define what data we expect in requests and responses
from pydantic import BaseModel

# LangChain tools for talking to AI models easily
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

# Langfuse is used to track and trace our AI requests (like a black box flight recorder)
from langfuse import get_client
from langfuse.langchain import CallbackHandler


# This actually reads the .env file and loads the variables into the system
load_dotenv()


# The System Prompt tells the AI how it should behave and answer questions
SYSTEM_PROMPT = (
    "You are the Lead AI Architect at Jeevisoft. "
    "You provide expert advice on serverless full-stack backends and Cloudflare. "
    "Be professional, high-energy, and slightly witty."
)


# This defines the expected structure of the incoming request from the user
class ChatRequest(BaseModel):
    user_query: str  # We expect the user to send a message called "user_query"


# This defines the structure of the response we will send back to the user
class ChatResponse(BaseModel):
    answer: str      # The AI's generated response
    request_id: str  # A unique ID for this specific chat


# This function decides whether to use Groq (Cloud) or Ollama (Local) based on the .env file
def build_llm() -> BaseChatModel:
    # Read the provider from .env, default to "groq" if not found
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        # Create a connection to Groq's fast AI models
        return ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            temperature=0.7, # 0.0 is robotic, 1.0 is very creative
            timeout=30,      # Wait up to 30 seconds for an answer
            max_retries=2,   # Try again twice if it fails
        )

    if provider == "ollama":
        # Create a connection to a local Ollama model running on your computer
        return ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "llama4:scout"),
            base_url=os.getenv(
                "OLLAMA_BASE_URL",
                "http://localhost:11434", # Default port for Ollama
            ),
            temperature=0.7,
            model_kwargs={
                "num_ctx": 32768, # How much memory/context the model can hold
            },
        )

    # If the user put something invalid in the .env file, crash with a helpful error
    raise ValueError(
        "Unsupported LLM_PROVIDER. Choose 'groq' or 'ollama'."
    )


# Create the actual FastAPI application (The "Kitchen" from our Restaurant analogy)
app = FastAPI(title="Jeevisoft AI Backend", version="0.1.0")

# Add CORS middleware so our React frontend (The "Dining Room") is allowed to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("FRONTEND_ORIGIN", "http://localhost:5173"), # Port 5173 is the default for Vite/React
    ],
    allow_credentials=False,
    allow_methods=["POST"],          # Allow POST requests (sending data)
    allow_headers=["Content-Type"],  # Allow JSON headers
)


# This tells FastAPI: "When someone sends a POST request to /chat, run this function"
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    # 1. Generate a unique ID for this request so we can track it in our logs
    request_id = str(uuid.uuid4())

    # 2. Get our AI model client (either Groq or Ollama)
    llm = build_llm()
    
    # 3. Prepare the Langfuse tracker
    langfuse_handler = CallbackHandler()

    # 4. Prepare the conversation history: The instructions first, then the user's question
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=req.user_query),
    ]

    # 5. Actually send the message to the AI model and wait for the result
    result = await llm.ainvoke(
        messages,
        config={
            "callbacks": [langfuse_handler], # Send tracking data to Langfuse
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

    # 6. Flush so the trace shows up immediately in the Langfuse dashboard
    get_client().flush()

    # 7. Return the final answer and ID back to the user (the React frontend)
    return ChatResponse(answer=result.content, request_id=request_id)
