# Module 1: Python, FastAPI, and Your First AI API

This module is designed for students who are new to Python and backend development. You will learn the foundations needed for the **entire Agentic AI course**.

> **👨‍🎓 Student Guide: How to follow this Module**
> 1. **Phase 1: Concepts (Practicals 0-4)** - Understand AI Evolution, Agentic AI Capabilities, Python basics, and web APIs.
> 2. **Phase 2: Build (Practicals 5-7)** - Build your first FastAPI server and connect it to an LLM.
> 3. **Phase 3: Test & Observe (Practicals 8-9)** - Test with curl and trace with Langfuse.
> 4. **Phase 4: Full Stack (Practical 10)** - Create a Lovable chat UI and connect it to your API.

### What you'll build

- A FastAPI server with a `POST /chat` endpoint
- A hosted Llama connection using Groq and LangChain — no student GPU required
- An optional local Ollama path for learners who want offline inference
- A shell script that tests the API using `curl`
- Optional request tracing with Langfuse
- A beginner-friendly chat interface designed with Lovable

### This module is for everyone

Students may come from project management, DevOps, UX design, operations, teaching, homemaking, or software development. Existing coding experience changes how quickly someone types — it does not decide whether they can understand the system.

Every practical has three levels:

- **Understand:** Explain the idea using an everyday example.
- **Practice:** Copy, run, and change a small working example.
- **Challenge:** Extend the example when the learner is ready.

### What's in this folder

- `app/main.py` — Defines the FastAPI app, the `/chat` endpoint, and the LLM client.
- `.env.example` — Environment variable template for Groq, Ollama, and Langfuse.
- `requirements.txt` — Python dependencies.
- `scripts/test_chat.sh` — Quick curl script to call `POST /chat`.

### Practicals

- `module-1-0-welcome.md` — AI Evolution, Agentic AI Capabilities, and the big picture
- `module-1-1-python-basics.md` — Python basics for AI agents
- `module-1-2-python-project-basics.md` — Functions, packages, and environment variables
- `module-1-2b-internet-basics.md` — How the Internet works (Frontend vs Backend)
- `module-1-3-web-api-basics.md` — How web APIs, HTTP, and JSON work
- `module-1-4-fastapi-basics.md` — Build your first FastAPI application
- `module-1-5-code-walkthrough.md` — Understand the existing AI backend code
- `module-1-6-groq-ollama.md` — Connect FastAPI to Groq or Ollama
- `module-1-7-test-script.md` — Understand the Bash and curl test script
- `module-1-8-langfuse.md` — Trace AI requests with Langfuse
- `module-1-9-lovable-chat-ui.md` — Create a Lovable chat UI and connect it

### Recommended order

1. Welcome & Big Picture (concepts — AI Evolution + 3 Capabilities)
2. Python basics
3. Python functions & packages
4. How the Internet works
5. Web APIs, HTTP, JSON
6. Build FastAPI app
7. Code walkthrough
8. Connect to Groq/Ollama
9. Test with curl
10. Langfuse tracing
11. Lovable chat UI

---

## Request flow (mental model)

```text
Student types a question
        |
        v
Chat screen sends POST /chat with {"user_query": "..."}
        |
        v
FastAPI validates the payload (Pydantic model)
        |
        v
App reads LLM_PROVIDER → builds ChatGroq or ChatOllama client
        |
        v
App sends system prompt + user query to the model
        |
        v
Langfuse callback records the request trace
        |
        v
FastAPI returns {"answer": "...", "request_id": "..."}
        |
        v
Chat screen displays the answer
```

---

## Prerequisites

- Basic computer and terminal usage
- Visual Studio Code
- Python 3.10+ (3.11 recommended)
- Node.js (for running the React frontend)
- A Groq account and individual API key for the recommended path
- Ollama only for the optional local path
- No previous FastAPI or AI-agent experience required

---

## Setup

> **👨‍🎓 Student Guide: Follow these steps in order!**

From this folder (`module-1-foundation/`):

```bash
# Step 1: Create a virtual environment
python3 -m venv .venv

# Step 2: Activate it
source .venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Copy the env template & fill in your keys
cp .env.example .env
```

Fill in your keys in `.env`:

| Variable | Required? | What it is |
| :--- | :--- | :--- |
| `LLM_PROVIDER` | ✅ Yes | Set to `groq` (recommended) or `ollama` |
| `GROQ_API_KEY` | ✅ Yes (if using Groq) | Your individual Groq API key |
| `GROQ_MODEL` | ✅ Yes (if using Groq) | e.g., `llama-3.1-8b-instant` |
| `OLLAMA_BASE_URL` | Only if using Ollama | Default: `http://localhost:11434` |
| `OLLAMA_MODEL` | Only if using Ollama | e.g., `llama4:scout` |
| `LANGFUSE_PUBLIC_KEY` | Optional | For request tracing |
| `LANGFUSE_SECRET_KEY` | Optional | For request tracing |
| `LANGFUSE_BASE_URL` | Optional | Default: `https://cloud.langfuse.com` |

---

## Run

### Option A — Groq Cloud (recommended)

Set these values in `.env`:

```text
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_your_individual_key
GROQ_MODEL=llama-3.1-8b-instant
```

No local model download or GPU is needed.

### Option B — Ollama (optional local mode)

Set `LLM_PROVIDER=ollama`, then start Ollama:

```bash
ollama serve
ollama pull llama4:scout
```

If you change `OLLAMA_MODEL` in your `.env`, pull that model instead.

### Start the API server

```bash
uvicorn app.main:app --reload
```

Your API will be available at `http://127.0.0.1:8000`.

---

## Quick Test

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

**Expected response:**

```json
{
  "answer": "The model's response text...",
  "request_id": "a-unique-uuid"
}
```

---

## Troubleshooting

| Problem | What to check |
| :--- | :--- |
| **Groq authentication error** | Confirm `GROQ_API_KEY` is in `.env`. Restart Uvicorn after changes. Never commit keys! |
| **Groq rate-limit (HTTP 429)** | Wait and retry. Use individual student keys, not one shared key. |
| **Ollama connection error** | Confirm Ollama is running: `ollama serve`. Check `OLLAMA_BASE_URL`. |
| **Model not found** | Pull the model: `ollama pull <model>`. Match `OLLAMA_MODEL` exactly. |
| **Langfuse no traces** | Verify `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, and `LANGFUSE_BASE_URL`. |

---

## What you'll do next

After Module 1, this API becomes the foundation for adding:

| Module | What you'll add |
| :--- | :--- |
| **Module 2** | Better prompting + structured outputs |
| **Module 3** | Tool calling (LangChain agents) |
| **Module 4** | Agent graphs (LangGraph) |
| **Module 5** | Agent design patterns |
| **Module 6** | Custom tools (stock prices + email) |
| **Module 7** | Memory & stateful agents |

---

## Checklist

- [ ] You can name the 4 stages of AI evolution and the 3 core Agentic AI capabilities.
- [ ] You successfully set up the virtual environment and installed dependencies.
- [ ] You can start the API server with `uvicorn`.
- [ ] You successfully tested the API with curl and received a response.
- [ ] You understand the request flow from frontend → FastAPI → LLM → response.
