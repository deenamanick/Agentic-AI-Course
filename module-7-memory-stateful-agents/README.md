# Module 7: Memory & Stateful Agents

This module is about giving your AI agent **real memory**. So far, every agent you built forgets you the moment a request finishes. Here you will:

- Understand why LLMs are stateless ("goldfish memory")
- Learn how Thread IDs separate memories for different users
- Use LangGraph Checkpointers to store conversation history
- Build a **Mental Health Companion** that remembers you across sessions
- Connect it to a beautiful Lovable UI

### What's in this folder

- `app/main.py` — A ReAct agent powered by `MemorySaver` with a `/agent/chat` endpoint.
- `.env.example` — Configuration for Groq and Langfuse.
- `requirements.txt` — Python dependencies.

### Practicals

- `module-7-0-why-memory.md` — Why do Agents need Memory?
- `module-7-1-thread-ids.md` — Thread IDs (keeping memories separated)
- `module-7-2-checkpointers.md` — LangGraph Checkpointers (`MemorySaver`)
- `module-7-3-test-companion.md` — Testing the Mental Health Companion
- `module-7-4-lovable-companion-ui.md` — Create a Lovable Companion UI

### Recommended order

1. Why Memory? (concepts)
2. Thread IDs (concepts)
3. Checkpointers (code walkthrough)
4. Test Companion (hands-on curl tests)
5. Lovable UI (full-stack integration)

---

## Prerequisites

- Python 3.10+
- A Groq account and API key

---

## Setup

> **👨‍🎓 Student Guide: Follow these steps in order!**

From this folder (`module-7-memory-stateful-agents/`):

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

Fill in your `GROQ_API_KEY` in `.env`.

---

## Run

### Start the API server

```bash
uvicorn app.main:app --reload
```

---

## Quick Test (2 curl commands)

You must send two requests to test the memory. **Make sure you use the exact same `thread_id` for both!**

**Request 1 (Tell it a secret):**
```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Hi, I have a big exam tomorrow and I am feeling incredibly anxious.",
    "thread_id": "test-user-1"
  }'
```

**Request 2 (Check its memory):**
```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Hi, I am back.",
    "thread_id": "test-user-1"
  }'
```
*The AI should immediately ask you about your exam!*

---

## Checklist

- [ ] You understand why an LLM API doesn't remember your previous requests by default.
- [ ] You know what a `thread_id` is used for.
- [ ] You can explain what a LangGraph Checkpointer (like `MemorySaver`) does.
- [ ] You successfully tested the memory using two `curl` requests with the same `thread_id`.
