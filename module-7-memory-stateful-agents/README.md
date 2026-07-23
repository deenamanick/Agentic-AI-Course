# Module 7 — Memory & Stateful Agents

## What you will build

So far, all your agents have had "goldfish memory." They forget who you are the moment the request finishes.

In this module, you will build **Task 14: Mental Health Companion**. This agent will use **LangGraph Checkpointers** to remember the user's state across multiple conversations. 

If a user connects on Monday and says they are stressed, and connects again on Wednesday, the agent will remember their stress and follow up with them!

---

## What's in this folder

- `app/main.py`
  - `POST /agent/chat`
  - A ReAct agent powered by `MemorySaver`.
  - Requires a `thread_id` to be passed in the request body.
- `.env.example`
  - Configuration for Groq and Langfuse.
- `requirements.txt`

## Practicals

0. [Why do Agents need Memory?](module-7-0-why-memory.md)
1. [Thread IDs](module-7-1-thread-ids.md)
2. [LangGraph Checkpointers](module-7-2-checkpointers.md)
3. [Testing the Mental Health Companion](module-7-3-test-companion.md)
4. [Create a Lovable Companion UI](module-7-4-lovable-companion-ui.md)

---

## Prerequisites

- Python 3.10+
- A Groq account and API key

---

## Setup

From this folder (`module-7-memory-stateful-agents/`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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

## Test Locally

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

## Checkpoint (Module 7)

- [ ] I understand why an LLM API doesn't remember my previous requests by default.
- [ ] I know what a `thread_id` is used for.
- [ ] I can explain what a LangGraph Checkpointer (like `MemorySaver`) does.
- [ ] I successfully tested the memory using two `curl` requests with the same `thread_id`.
