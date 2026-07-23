# Practical 1.4 — Build Your First FastAPI Application

## Why, in simple terms

FastAPI turns Python functions into web API endpoints.

Before connecting AI, build the smallest possible API.

## Step 1: Create a learning file

Create `simple_api.py`:

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="My First API")


class GreetingRequest(BaseModel):
    name: str


class GreetingResponse(BaseModel):
    message: str


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "API is working"}


@app.post("/greet", response_model=GreetingResponse)
def greet(request: GreetingRequest) -> GreetingResponse:
    return GreetingResponse(message=f"Hello, {request.name}!")
```

## Step 2: Understand the code

- `FastAPI()` creates the application.
- `BaseModel` describes valid JSON.
- `@app.get("/")` connects a URL to a function.
- `@app.post("/greet")` creates a POST endpoint.
- `response_model` checks the returned JSON.

The `@` line is called a **decorator**. For now, remember: it connects the function below it to an API route.

## Step 3: Run it

```bash
uvicorn simple_api:app --reload
```

- `simple_api` is the filename without `.py`.
- `app` is the FastAPI variable.
- `--reload` restarts the server after code changes.

Open:

```text
http://127.0.0.1:8000/docs
```

Test `GET /` and `POST /greet`.

## Step 4: Add the AI model builder

Our simple `/greet` endpoint creates its answer directly in Python. The real `/chat` endpoint needs an AI model.

We create the model connection inside a function named `build_llm()`:

```python
import os

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama


def build_llm() -> BaseChatModel:
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        return ChatGroq(
            model=os.getenv(
                "GROQ_MODEL",
                "llama-3.1-8b-instant",
            ),
            temperature=0.7,
            timeout=30,
            max_retries=2,
        )

    if provider == "ollama":
        return ChatOllama(
            model=os.getenv(
                "OLLAMA_MODEL",
                "llama4:scout",
            ),
            base_url=os.getenv(
                "OLLAMA_BASE_URL",
                "http://localhost:11434",
            ),
            temperature=0.7,
            model_kwargs={"num_ctx": 32768},
        )

    raise ValueError(
        "Unsupported LLM_PROVIDER. Choose 'groq' or 'ollama'."
    )
```

### Why use a function?

`build_llm()` keeps all model configuration in one place:

```text
build_llm()
    |
    | reads configuration from .env
    v
chooses Groq or Ollama
    |
    v
returns the model connection
```

The `/chat` endpoint can now request a configured model:

```python
llm = build_llm()
```

### Line-by-line explanation

```python
import os
```

The `os` module lets Python read environment variables.

```python
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
```

`ChatGroq` connects to hosted models through Groq. `ChatOllama` connects to an optional local model.

```python
def build_llm() -> BaseChatModel:
```

- `def` creates a function.
- `build_llm` is its name.
- The empty `()` means it does not require arguments.
- `-> BaseChatModel` tells readers that it returns a LangChain chat model, regardless of provider.

```python
provider = os.getenv("LLM_PROVIDER", "groq").lower()
```

Python reads the provider name. If it is missing, the classroom-friendly Groq path is used.

Each provider reads its own model configuration:

```python
os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
os.getenv("OLLAMA_MODEL", "llama4:scout")
```

This lets us change the model in `.env` without editing Python.

```python
return ChatGroq(...)
```

Groq is the recommended classroom path because the model runs in the cloud and students do not need a GPU. The API key remains in the backend `.env`.

### Model settings

| Setting | Simple meaning |
|---|---|
| `provider` | Whether Groq Cloud or local Ollama supplies the model |
| `model` | Which provider model to use |
| `base_url` | Where optional Ollama is running |
| `temperature` | How predictable or creative answers may be |
| `timeout` | How long Groq may take before the request stops |
| `max_retries` | How many bounded Groq retries are allowed |
| `num_ctx` | Maximum context size requested from the model |

`temperature=0.7` allows some variation. A lower value such as `0.2` is usually more predictable.

The actual context supported depends on the selected model and available computer resources.

## Step 5: Load and verify the configuration

Make sure `.env` contains:

```text
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_your_individual_key
GROQ_MODEL=llama-3.1-8b-instant

# Optional local mode
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama4:scout
```

The application must load `.env` before calling `build_llm()`:

```python
from dotenv import load_dotenv

load_dotenv()
```

For a quick learning check, temporarily add:

```python
llm = build_llm()
print(llm)
```

Run the file and confirm that Python creates a `ChatGroq` object.

Creating this object does not prove that the key, network, or provider is working. Practical 1.6 makes a real model request.

## Practice tasks

1. Add an `age` integer to `GreetingRequest`.
2. Include the age in the response.
3. Send text instead of a number and inspect the validation error.
4. Add `GET /health` that returns `{"status": "ok"}`.
5. Change `GROQ_MODEL` in `.env` and confirm `build_llm()` reads it.
6. Set `LLM_PROVIDER=ollama` and identify which branch runs.
7. Change `temperature` from `0.7` to `0.2`.

## Success checklist

- [ ] I can explain an endpoint.
- [ ] I can run Uvicorn.
- [ ] I can test an endpoint in `/docs`.
- [ ] I understand that Pydantic validates JSON.
- [ ] I can explain what `build_llm()` returns.
- [ ] I know why the provider, model, and API key belong in `.env`.
- [ ] I understand that creating the client and calling the model are separate steps.

## Lovable practice prompt

```text
Build a beginner-friendly "API Learning Dashboard" using React and Tailwind CSS.

Requirements:
- Show two API cards: GET /health and POST /greet.
- Each card explains the HTTP method in one simple sentence.
- Add a name input for POST /greet.
- Add a "Send Request" button.
- Show request JSON on the left and response JSON on the right.
- Show status code using green for success and red for error.
- Use a clean classroom theme with large readable text.
- Frontend only. Use mock responses for now.
```
