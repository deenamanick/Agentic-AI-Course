# Module 4 — LangGraph (Deterministic Agentic Workflows)

## What you will build

In this module you build an **agentic workflow** using **LangGraph**.

You will expose a single API endpoint:

- `POST /graph/chat`

Instead of letting an agent “freestyle”, you will define an explicit graph:

- `route` (decide if the request is math vs general)
- `math_tool` (safe local arithmetic)
- `plan` (LLM creates a short plan)
- `execute` (LLM answers using the plan)
- `finalize` (store final output)

Every request is traced with Langfuse.

---

## Why LangGraph

Agents are powerful but can be unpredictable. LangGraph gives you:

- Deterministic steps
- Clear state transitions
- Conditional routing
- Easier debugging and evaluation

---

## What’s in this folder

- `app/main.py`
  - `POST /graph/chat`
  - Graph definition and nodes
- `.env.example`
- `requirements.txt`
- `scripts/test_graph.sh`

## Practicals

1. [Define graph state and nodes](module-4-1-state-nodes.md)
2. [Add conditional routing](module-4-2-routing.md)
3. [Plan, execute, and finalize](module-4-3-plan-execute.md)
4. [Trace and test the graph](module-4-4-graph-tests.md)

---

## Prerequisites

- Python 3.10+
- Ollama installed and running
- (Optional but recommended) Langfuse keys

---

## Setup

From this folder (`module-4-langgraph/`):

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
bash scripts/test_graph.sh
```

---

## Lab 1 — Routing

Send two prompts:

- A general planning query
- A math query

Confirm the response includes a `route` value that changes accordingly.

---

## Lab 2 — Extend routing (student exercise)

Improve the `route_node` to detect:

- date/time questions
- summarization questions

Add new routes and nodes.

---

## Checkpoint (Module 4)

- [ ] I can run `POST /graph/chat` locally.
- [ ] The system routes math queries to the `math_tool` node.
- [ ] The system routes general queries through `plan -> execute`.
- [ ] I can find the run in Langfuse using `request_id`.
