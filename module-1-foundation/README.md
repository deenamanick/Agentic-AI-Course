# Module 1 — Foundation: Local-first AI Backend (FastAPI + Ollama + Langfuse)

## What you will build

In this module you build a small **local-first AI backend**.

- A **FastAPI** server exposing a single endpoint: `POST /chat`
- The endpoint calls a local LLM running in **Ollama** using **LangChain** (`ChatOllama`)
- Each request is traced to **Langfuse** (observability)

By the end, you will be able to send a JSON request to your local server and get an AI-generated response back.

---

## Why this module exists

Agentic systems need a reliable “home base” backend before you add tools, memory, graphs, or multi-agent orchestration.

This module sets up:

- A clean API boundary (`/chat`)
- Local inference (no external LLM API required)
- Tracing so you can see what happened inside each request

---

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

1. [Set up the local AI environment](module-1-1-local-environment.md)
2. [Understand and run the chat API](module-1-2-chat-api.md)
3. [Connect and test Ollama](module-1-3-ollama.md)
4. [Trace requests with Langfuse](module-1-4-langfuse.md)

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

- Python 3.10+ (3.11 recommended)
- Ollama installed and working
- (Optional but recommended) Langfuse account + keys

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
