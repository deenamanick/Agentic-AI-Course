# Practical 1.5 — Understand the Existing AI Backend Code

## What you are reading

The real application is `app/main.py`. It combines the Python and FastAPI concepts from the earlier practicals.

## Section 1: Imports

```python
import os
import uuid
```

- `os` reads environment variables.
- `uuid` creates a unique request ID.

The other imports provide FastAPI, Pydantic, Ollama messages, the model client, and Langfuse tracing.

## Section 2: Load configuration

```python
load_dotenv()
```

This reads `.env` and makes its values available through `os.getenv(...)`.

## Section 3: System prompt

`SYSTEM_PROMPT` defines the assistant’s role, subject, and communication style.

The user does not replace this prompt. Their question is added separately.

## Section 4: Request and response models

```python
class ChatRequest(BaseModel):
    user_query: str


class ChatResponse(BaseModel):
    answer: str
    request_id: str
```

These classes define the JSON contract.

## Section 5: Build the model

`build_llm()`:

1. Reads the Ollama URL.
2. Reads the model name.
3. Creates `ChatOllama`.
4. Configures temperature and context size.

`temperature=0.7` allows some creativity. Lower values are usually more predictable.

## Section 6: Create FastAPI

```python
app = FastAPI(title="Jeevisoft Local AI Backend", version="0.1.0")
```

Uvicorn finds this variable using:

```bash
uvicorn app.main:app --reload
```

This means: open `app/main.py`, find `app`, and run it.

## Section 7: The `/chat` endpoint

```python
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
```

`async` lets the server wait for Ollama without unnecessarily blocking other work.

Inside the function:

1. Create a request ID.
2. Build the model.
3. Create the trace handler.
4. Create system and human messages.
5. Await the model response.
6. Flush the trace.
7. Return validated JSON.

## Request flow

```text
ChatRequest
   -> chat()
   -> build_llm()
   -> Ollama
   -> result.content
   -> ChatResponse
```

## Practice tasks

1. Change the FastAPI title.
2. Change the system prompt to a beginner Python tutor.
3. Set temperature to `0.2` and compare responses.
4. Add `GET /health`.
5. Open `/docs` and verify both endpoints.

## Success checklist

- [ ] I can identify configuration, schema, model, and endpoint sections.
- [ ] I can explain why request IDs are useful.
- [ ] I understand the system and human messages.
- [ ] I can describe the `/chat` flow without reading the code.
