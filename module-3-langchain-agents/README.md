# Module 3 — From Chatbot to Agent: Tools & the ReAct Pattern

## What you will build

In Modules 1–2, you built a chatbot that can only **talk**. In Module 3, you'll build an **agent** that can **think AND act** — by choosing and using tools.

- A FastAPI endpoint: `POST /agent/chat`
- A **LangGraph ReAct agent** powered by Groq (default) or Ollama (optional)
- A toolset: `calculator`, `now_unix`, `echo`
- A survey of the agent framework landscape
- Tracing/observability via Langfuse

> [!NOTE]
> This module uses **LangGraph** (the modern industry standard), NOT the deprecated `AgentExecutor`. We use LangChain only for model interfaces (`ChatGroq`, `ChatOllama`) and tool definitions (`@tool`).

---

## What's in this folder

- `app/main.py`
  - `POST /agent/chat` — an AI agent that can choose and use tools
  - Tools: `calculator`, `now_unix`, `echo`
  - Uses LangGraph's `create_react_agent`
- `.env.example`
  - Configuration for Groq (default), optional Ollama, Langfuse, and app metadata
- `requirements.txt`
  - Python dependencies (includes `langgraph`)
- `scripts/test_agent.sh`
  - Quick test script

## Practicals

0. [Start here: how Module 3 extends Module 2](module-3-0-bridge.md)
1. [What makes an agent different from a chatbot?](module-3-1-chatbot-vs-agent.md)
2. [What are tools? (The Librarian's Phone)](module-3-2-what-are-tools.md)
3. [The ReAct pattern: Think → Act → Observe](module-3-3-react-pattern.md)
4. [Build your first tool-using agent (LangGraph)](module-3-4-first-agent.md)
5. [Agent framework landscape (2025/2026)](module-3-5-framework-landscape.md)
6. [When NOT to use an agent](module-3-6-when-not-to-use-agent.md)
7. [Test your agent](module-3-7-agent-tests.md)

---

## Prerequisites

- Module 2 understanding-level activities
- Python 3.10+
- A Groq account and API key (recommended) OR Ollama installed locally
- (Optional but recommended) Langfuse keys
- No previous agent or LangGraph experience required

---

## Setup

From this folder (`module-3-langchain-agents/`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in your `GROQ_API_KEY` in `.env`.

---

## Run

### Option A — Groq Cloud (recommended, no GPU needed)

Set in `.env`:

```text
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_your_individual_key
GROQ_MODEL=llama-3.1-8b-instant
```

### Option B — Ollama (optional local mode)

```bash
ollama serve
ollama pull llama4:scout
```

Set `LLM_PROVIDER=ollama` in `.env`.

### Start the API server

```bash
uvicorn app.main:app --reload
```

---

## Test

```bash
bash scripts/test_agent.sh
```

Or test manually:

### Math (should use calculator):

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"Compute (125 * 8) - 17."}'
```

### Time (should use now_unix):

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is the current Unix timestamp?"}'
```

### General (should answer without tools):

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is Python used for?"}'
```

---

## Student Exercise: Add a New Tool

Add one of these tools and verify the agent uses it:

- `word_count(text: str) -> str` — Count words in text
- `to_upper(text: str) -> str` — Convert text to uppercase
- `reverse_text(text: str) -> str` — Reverse a string

---

## Checkpoint (Module 3)

- [ ] I can explain the difference between a chatbot and an agent.
- [ ] I understand tools, the ReAct pattern, and why LangGraph replaces AgentExecutor.
- [ ] I can run `POST /agent/chat` and the agent uses the correct tool.
- [ ] I can name at least 4 agent frameworks and their main use case.
- [ ] I know when NOT to use an agent (cost, speed, simplicity).
- [ ] I can find the agent's reasoning trace in Langfuse.

---

## What's next

In **Module 4**, you'll go deeper into LangGraph:
- Define custom graph states
- Add conditional routing (math vs general vs summarization)
- Build plan-execute workflows
- Create deterministic, production-ready agent graphs
