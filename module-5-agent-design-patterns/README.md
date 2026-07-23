# Module 5 — Agent Design Patterns (Reflection)

## What you will build

In this module, you will learn about **Agent Design Patterns**. Specifically, you will master the **Reflection / Critique Pattern** by building the **Job Analyzer Agent** (Task 1).

You will expose a single API endpoint:
- `POST /analyzer/score`

This API uses three separate LLM calls to generate perfect feedback:
1. `analyzer_node`: Writes a draft review of the user's CV.
2. `critique_node`: Acts as a Harsh Senior Manager to find flaws in the draft.
3. `refine_node`: Fixes the flaws and returns the final polished review.

---

## What's in this folder

- `app/main.py`
  - `POST /analyzer/score`
  - The `JobAnalyzerState` definition
  - The 3-node Reflection graph
- `.env.example`
  - Configuration for Groq (default), optional Ollama, and Langfuse
- `requirements.txt`

## Practicals

0. [What are Agent Design Patterns?](module-5-0-what-are-patterns.md)
1. [The Reflection Pattern](module-5-1-the-reflection-pattern.md)
2. [Coding the Job Analyzer](module-5-2-job-analyzer-code.md)
3. [Compile and Test the Job Analyzer](module-5-3-compile-and-test.md)
4. [Create a Lovable Analyzer UI](module-5-4-lovable-analyzer-ui.md)

---

## Prerequisites

- Module 4 understanding (LangGraph basics)
- Python 3.10+
- A Groq account and API key (recommended) OR Ollama installed locally
- (Optional but recommended) Langfuse keys

---

## Setup

From this folder (`module-5-agent-design-patterns/`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in your `GROQ_API_KEY` in `.env`.

---

## Run

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

Send a terribly formatted CV to the API to see how the Harsh Critic handles it:

```bash
curl -sS -X POST "http://127.0.0.1:8000/analyzer/score" \
  -H "Content-Type: application/json" \
  -d '{
    "raw_cv": "hi my name alex i do coding i know python n sum html. i worked at google for 2 weeks den quit.",
    "job_title": "Senior Staff Software Engineer"
  }'
```

*Note: This request takes 4-6 seconds because it makes 3 separate LLM calls under the hood!*

---

## Checkpoint (Module 5)

- [ ] I can name the 4 core agent design patterns.
- [ ] I understand the Reflection pattern (Draft -> Critique -> Refine).
- [ ] I traced the 3-step execution in my Langfuse dashboard.
- [ ] I successfully generated a multi-step loading UI in Lovable to handle the 6-second latency.
