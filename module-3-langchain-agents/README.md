# Module 3 — LangChain Agents (Tools + Agent Executor)

## What you will build

In this module you build your first **tool-using agent** behind an API.

- A FastAPI endpoint: `POST /agent/chat`
- A LangChain **ReAct agent** powered by Ollama (`ChatOllama`)
- A small toolset that the agent can choose from
- Tracing/observability via Langfuse

---

## What’s in this folder

- `app/main.py`
  - `POST /agent/chat`
  - Tools: `calculator`, `now_unix`, `echo`
- `.env.example`
- `requirements.txt`
- `scripts/test_agent.sh`

## Practicals

1. [Create typed agent tools](module-3-1-typed-tools.md)
2. [Understand the ReAct loop](module-3-2-react-loop.md)
3. [Build and run the agent executor](module-3-3-agent-executor.md)
4. [Test tool selection and failures](module-3-4-agent-tests.md)

---

## Prerequisites

- Python 3.10+
- Ollama installed and running
- (Optional but recommended) Langfuse keys

---

## Setup

From this folder (`module-3-langchain-agents/`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

---

## Run

### 1) Start Ollama and pull the model

```bash
ollama serve
```

In another terminal:

```bash
ollama pull llama4:scout
```

### 2) Start the API server

```bash
uvicorn app.main:app --reload
```

---

## Test

```bash
bash scripts/test_agent.sh
```

---

## Lab 1 — Verify tool usage

Try queries that should trigger tools:

- Math:

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"Compute (125 * 8) - 17."}'
```

- Time:

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is the current Unix timestamp?"}'
```

---

## Lab 2 — Change the toolset (student exercise)

Add a new tool and re-run:

- `word_count(text: str) -> str`
- `to_upper(text: str) -> str`

Acceptance:

- The agent uses the tool when asked
- The API still returns quickly and reliably

---

## Checkpoint (Module 3)

- [ ] I can run `POST /agent/chat` locally.
- [ ] The agent can solve a math query using the `calculator` tool.
- [ ] The agent can answer a time query using the `now_unix` tool.
- [ ] I can find the run in Langfuse using `request_id`.
