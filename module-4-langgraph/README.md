# Module 4 — LangGraph (Deterministic Workflows)

## What you will build

In Module 3, you built an **autonomous agent** that decided on its own what tools to use. But what happens when you need 100% predictable, reliable results?

In this module, you will build a **deterministic workflow** using LangGraph. We are going to build the **Resume Builder Agent** (Task 5 from the real-world projects list).

You will expose a single API endpoint:
- `POST /resume/build`

Instead of letting the agent "freestyle", you will force it through an exact 3-step pipeline:
1. `extract_node`: Reads a messy text dump from the user and extracts structured JSON (Name, Skills, Experience) using `with_structured_output`.
2. `draft_node`: Uses the JSON to draft a professional summary.
3. `format_node`: A pure-Python (no AI) step that combines the data into a beautifully formatted Markdown resume.

---

## What's in this folder

- `app/main.py`
  - `POST /resume/build`
  - The `ResumeState` definition
  - The 3-node LangGraph workflow
- `.env.example`
  - Configuration for Groq (default), optional Ollama, and Langfuse
- `requirements.txt`

## Practicals

0. [Why do we need Workflows? (Agents vs Workflows)](module-4-0-why-workflows.md)
1. [Defining the Graph State](module-4-1-graph-state.md)
2. [Node 1: Structured Extraction](module-4-2-extraction-node.md)
3. [Nodes 2 & 3: Generation & Formatting](module-4-3-generation-nodes.md)
4. [Compile and Run the Graph](module-4-4-compile-run.md)
5. [Create a Lovable Resume UI](module-4-5-lovable-resume-ui.md)

---

## Prerequisites

- Module 3 understanding
- Python 3.10+
- A Groq account and API key (recommended) OR Ollama installed locally
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

### Start the API server

```bash
uvicorn app.main:app --reload
```

---

## Test Locally

Send a messy brain dump to your API:

```bash
curl -sS -X POST "http://127.0.0.1:8000/resume/build" \
  -H "Content-Type: application/json" \
  -d '{
    "raw_text": "Hey I am Sarah. I have been working as a data scientist for 4 years at Meta. I know SQL, Python, and PyTorch. Before that I was an intern at a small startup doing frontend dev with React."
  }'
```

You should receive a beautifully formatted Markdown resume in the `markdown_resume` field!

---

## Checkpoint (Module 4)

- [ ] I understand the difference between an autonomous agent and a deterministic workflow.
- [ ] I understand how the `ResumeState` is passed from node to node.
- [ ] I know how to force an LLM to return valid JSON using `with_structured_output`.
- [ ] I understand why the `format_node` uses standard Python instead of an LLM.
- [ ] I successfully generated a UI in Lovable that renders the Markdown resume.
