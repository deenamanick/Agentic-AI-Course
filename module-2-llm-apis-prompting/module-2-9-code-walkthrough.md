# Practical 2.9 — Understand the Module 2 Code (Guided Walkthrough)

## Why

The file `app/main.py` looks long because it contains several small ideas. Let's read it **section by section** instead of trying to understand everything at once — just like the chunking technique from Practical 2.4!

---

## 🧩 Section 1: Imports and Configuration

```python
import json          # For parsing JSON strings
import os            # For reading .env settings
import uuid          # For generating unique request IDs

# Load environment variables from the .env file (API keys, model settings, etc.)
from dotenv import load_dotenv

# FastAPI is our web server; HTTPException lets us return error codes
from fastapi import FastAPI, HTTPException
# CORS allows our React frontend to connect to this backend
from fastapi.middleware.cors import CORSMiddleware
# BaseModel and Field define/validate the shape of requests/responses
from pydantic import BaseModel, Field

# LangChain tools for talking to AI models
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq      # Groq Cloud (fast, no GPU needed)
from langchain_ollama import ChatOllama  # Ollama (local, runs on your computer)

# Langfuse tracks and traces our AI requests
from langfuse import get_client
from langfuse.langchain import CallbackHandler

# Read the .env file and load all settings into the system
load_dotenv()
```

**💡 What changed from Module 1?** We added `import json` (for parsing structured output) and `HTTPException` (for returning error codes when the AI gives us unusable JSON).

---

## 🧩 Section 2: Prompt Versions (NEW in Module 2!)

```python
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
SYSTEM_PROMPT_V2 = (
    SYSTEM_PROMPT_V1
    + " "
    + "Prefer short answers. Use headings. "
    + "Ask one clarifying question when requirements are unclear."
)


def get_system_prompt(prompt_version: str) -> str:
    """Pick the right prompt based on the PROMPT_VERSION setting in .env"""
    if prompt_version == "v2":
        return SYSTEM_PROMPT_V2
    return SYSTEM_PROMPT_V1
```

**💡 Key insight:** `v2` reuses `v1` and **adds** rules. This makes the difference visible and easy to test. The `get_system_prompt()` function acts like a switch — it reads which version to use.

---

## 🧩 Section 3: API Contracts (Request & Response Shapes)

```python
class ChatRequest(BaseModel):
    user_query: str = Field(min_length=1, max_length=4000)
    # The student's question. Must be 1–4000 characters.

class ChatResponse(BaseModel):
    answer: str          # The AI's text response
    request_id: str      # Unique ID to track this request
    prompt_version: str  # Which prompt version generated this answer

class StructuredChatResponse(BaseModel):
    summary: str         # A short summary of the answer
    steps: list[str]     # Step-by-step instructions as a list
    request_id: str      # Unique ID for tracking
    prompt_version: str  # Which prompt version was used
```

**💡 What changed from Module 1?**
- `ChatResponse` now includes `prompt_version` so you can see which prompt was used.
- `StructuredChatResponse` is entirely NEW — it returns structured JSON instead of plain text.
- Pydantic validates these shapes automatically. If the frontend sends the wrong data, FastAPI rejects it.

---

## 🧩 Section 4: Provider Selection (Same as Module 1)

```python
def build_llm() -> BaseChatModel:
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        return ChatGroq(...)      # Groq Cloud — no student GPU needed
    if provider == "ollama":
        return ChatOllama(...)    # Optional local path
    raise ValueError("Unsupported LLM_PROVIDER")
```

**💡 This is identical to Module 1.** The "Kitchen" stays the same. Only the "Recipe" (prompt) changes. Both providers return a LangChain chat model, so the endpoints use the same `ainvoke()` call.

---

## 🧩 Section 5: Normal Chat Endpoint (`POST /chat`)

```python
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    # Step 1: Generate a unique ID
    request_id = str(uuid.uuid4())
    # Step 2: Get the AI model client
    llm = build_llm()
    # Step 3: Prepare Langfuse tracker
    langfuse_handler = CallbackHandler()
    # Step 4: Read prompt version from .env
    prompt_version = os.getenv("PROMPT_VERSION", "v1")
    # Step 5: Build the conversation
    messages = [
        SystemMessage(content=get_system_prompt(prompt_version)),
        HumanMessage(content=req.user_query),
    ]
    # Step 6: Send to AI and wait
    result = await llm.ainvoke(messages, config={...})
    # Step 7: Flush tracking data
    get_client().flush()
    # Step 8: Return answer + metadata
    return ChatResponse(
        answer=result.content,
        request_id=request_id,
        prompt_version=prompt_version,
    )
```

**💡 What changed from Module 1?** Two things:
1. It reads `PROMPT_VERSION` from `.env` (Step 4).
2. It includes `prompt_version` in the response (Step 8).

---

## 🧩 Section 6: Structured Chat Endpoint (`POST /chat/structured`)

This is the most interesting new section! It forces the AI to return **predictable JSON** instead of free-form text.

```python
@app.post("/chat/structured", response_model=StructuredChatResponse)
async def chat_structured(req: ChatRequest) -> StructuredChatResponse:
    # Steps 1-3: Same as above

    # Step 4: Define the JSON shape we want
    schema = {"summary": "string", "steps": ["string"]}

    # Step 5: Add strict output instructions to the prompt
    messages = [
        SystemMessage(
            content=(
                get_system_prompt(prompt_version)
                + " Return ONLY valid JSON with keys: summary and steps."
                + f" Schema example: {json.dumps(schema)}"
            )
        ),
        HumanMessage(content=req.user_query),
    ]

    # Step 6: Send to AI
    result = await llm.ainvoke(messages, config={...})

    # Step 8: VALIDATE the response (the AI might not follow instructions!)
    try:
        parsed = json.loads(result.content)       # Is it valid JSON?
        summary = parsed["summary"]               # Does "summary" exist?
        steps = parsed["steps"]                   # Does "steps" exist?
        # Are the types correct?
        if not isinstance(summary, str) or not isinstance(steps, list):
            raise ValueError("Invalid JSON shape")
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        raise HTTPException(status_code=502, detail="Model did not return valid JSON.")
```

**💡 Key insight:** The AI is told to return JSON, but **we still validate it**! This is the "trust but verify" principle from Practical 2.1b. If the model returns a paragraph instead of JSON, our code catches it and returns HTTP 502 instead of crashing.

---

## Complete Data Flow

```text
ChatRequest
   -> Read PROMPT_VERSION from .env
   -> get_system_prompt(version) picks v1 or v2
   -> build_llm() creates Groq or Ollama client
   -> SystemMessage + HumanMessage
   -> ainvoke() sends to AI
   -> Text response (/chat) or JSON validation (/chat/structured)
   -> ChatResponse or StructuredChatResponse
```

---

## Practice

1. Change one sentence in `SYSTEM_PROMPT_V2` and compare the output.
2. Add a `GET /health` endpoint that returns `{"status": "ok"}`.
3. Send an empty query and observe the Pydantic validation error.
4. Set `LLM_PROVIDER` to an unsupported value and read the error.
5. Remove "Return ONLY valid JSON" from the structured prompt and see what happens.

## Success checklist

- [ ] I can find prompt selection, provider selection, and both endpoints in the code.
- [ ] I can explain both response models (`ChatResponse` vs `StructuredChatResponse`).
- [ ] I understand why structured model text must be parsed and validated.
- [ ] I can draw the complete request flow from start to finish.
