# Module 1 — Python, FastAPI, and Your First Local AI API

## What you will build

This module is designed for a student who is new to Python and backend development.

You will first learn the small amount of Python needed for this course. Then you will build:

- A FastAPI server with a `POST /chat` endpoint
- A local AI connection using Ollama and LangChain
- A shell script that tests the API using `curl`
- Optional request tracing with Langfuse
- A beginner-friendly chat interface designed with Lovable

You do not need to master all of Python before starting.

## Beginner learning rule

For every practical:

1. Understand the idea in plain English.
2. Type a small example.
3. Run it immediately.
4. Change something and run it again.
5. Break it safely and understand the error.

## What’s in this folder

- `app/main.py`
  - Defines the FastAPI app and the `/chat` endpoint
  - Creates a LangChain `ChatOllama` client based on environment variables
  - Sends traces to Langfuse
- `requirements.txt`
  - Python dependencies for the module
- `.env.example`
  - Environment variable template for Ollama, Langfuse, and app metadata
- `scripts/test_chat.sh`
  - Quick curl script to call `POST /chat`

## Practicals

1. [Python basics for AI agents](module-1-1-python-basics.md)
2. [Python functions, packages, and environment variables](module-1-2-python-project-basics.md)
3. [How web APIs, HTTP, and JSON work](module-1-3-web-api-basics.md)
4. [Build your first FastAPI application](module-1-4-fastapi-basics.md)
5. [Understand the existing AI backend code](module-1-5-code-walkthrough.md)
6. [Connect FastAPI to Ollama](module-1-6-ollama.md)
7. [Understand the Bash and curl test script](module-1-7-test-script.md)
8. [Trace AI requests with Langfuse](module-1-8-langfuse.md)
9. [Create a Lovable chat UI and connect it](module-1-9-lovable-chat-ui.md)

---

## Request flow (mental model)

1. You send `POST /chat` with `{ "user_query": "..." }`
2. FastAPI validates the payload (Pydantic model)
3. The app builds an LLM client:
   - `OLLAMA_BASE_URL` (default `http://localhost:11434`)
   - `OLLAMA_MODEL` (default `llama4:scout`)
4. The app sends two messages to the model:
   - A **system prompt** (role + style)
   - Your **user query**
5. Langfuse callback records the request trace
6. The endpoint returns:
   - `answer` (model output)
   - `request_id` (unique ID you can also use as trace/session ID)

---

## Prerequisites

- Basic computer and terminal usage
- Visual Studio Code
- Python 3.10+ (3.11 recommended)
- Ollama
- No previous FastAPI or AI-agent experience required

---

## Setup

### 1) Create a virtual environment and install dependencies

From this folder (`module-1-foundation/`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Configure environment variables

Create a `.env` file:

```bash
cp .env.example .env
```

Fill in:

- `OLLAMA_BASE_URL`
- `OLLAMA_MODEL`
- `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` / `LANGFUSE_BASE_URL`
- `APP_ENV`, `APP_PROJECT`

---

## Run

### 1) Start Ollama and pull the model

In one terminal:

```bash
ollama serve
```

In another terminal:

```bash
ollama pull llama4:scout
```

If you change `OLLAMA_MODEL` in your `.env`, pull that model instead.

### 2) Start the API server

```bash
uvicorn app.main:app --reload
```

Your API will be available at:

- `http://127.0.0.1:8000`

---

## Test

### Option A: Use the provided script

```bash
bash scripts/test_chat.sh
```

### Option B: Curl manually

```bash
curl -sS -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"Design a serverless full-stack backend on Cloudflare for a small SaaS. Keep it concise."}'
```

---

## Expected response

You should get JSON back like:

- `answer`: the model’s response text
- `request_id`: a unique identifier for the request (also used for Langfuse metadata)

---

## Troubleshooting

- **Ollama connection errors**
  - Confirm Ollama is running: `ollama serve`
  - Confirm `OLLAMA_BASE_URL` matches where Ollama is listening (default `http://localhost:11434`)

- **Model not found**
  - Pull the model: `ollama pull <model>`
  - Make sure your `.env` `OLLAMA_MODEL` matches the pulled model name exactly

- **Langfuse errors / no traces**
  - Verify `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, and `LANGFUSE_BASE_URL`
  - If you’re using Langfuse Cloud, the default base URL is `https://cloud.langfuse.com`

---

## What you’ll do next

After Module 1, this API becomes the foundation for adding:

- Better prompting + structured outputs
- Tool calling (LangChain tools)
- Agent graphs (LangGraph)
- Multi-step workflows and agentic patterns
