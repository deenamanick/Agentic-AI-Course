# Module 2 — LLM APIs & Prompting (Prompt versions + Structured Output)

## What you will practice

In this module you take the Module 1 `/chat` API idea and turn it into a **prompt engineering lab**:

- Prompt versioning using `PROMPT_VERSION` (`v1` vs `v2`)
- Comparing outputs across prompt versions
- Producing **reliable structured JSON** output from an LLM
- Tracing requests in Langfuse with useful metadata

---

## What’s in this folder

- `app/main.py`
  - `POST /chat` (includes `prompt_version` in the response)
  - `POST /chat/structured` (returns `summary` + `steps` as JSON)
- `requirements.txt`
- `.env.example`
- `scripts/test_chat.sh`
- `scripts/test_chat_structured.sh`

## Practicals

1. [Separate system and user prompts](module-2-1-prompt-roles.md)
2. [Version prompts](module-2-2-prompt-versioning.md)
3. [Return structured output](module-2-3-structured-output.md)
4. [Compare prompts with repeatable tests](module-2-4-prompt-comparison.md)

---

## Prerequisites

- Python 3.10+
- Ollama installed and running
- (Optional but recommended) Langfuse account + keys

---

## Setup

From this folder (`module-2-llm-apis-prompting/`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

---

## Run

### 1) Start Ollama + pull model

```bash
ollama serve
```

In a different terminal:

```bash
ollama pull llama4:scout
```

### 2) Start the API server

```bash
uvicorn app.main:app --reload
```

---

## Lab: Prompt versions

### Run `v1`

```bash
export PROMPT_VERSION=v1
bash scripts/test_chat.sh
```

### Run `v2`

```bash
export PROMPT_VERSION=v2
bash scripts/test_chat.sh
```

Compare:

- The response text style
- Whether the model asks a clarifying question (in `v2` when appropriate)

---

## Lab: Structured output

### Call the structured endpoint

```bash
export PROMPT_VERSION=v1
bash scripts/test_chat_structured.sh
```

Expected:

- Valid JSON only
- Keys:
  - `summary`: string
  - `steps`: array of strings
  - `request_id`: string
  - `prompt_version`: `v1` or `v2`

If the model returns invalid JSON, the API returns HTTP `502`.

---

## Checkpoint B — Acceptance checklist

- [ ] I can run `POST /chat` and see `prompt_version` in the response.
- [ ] I can switch between `PROMPT_VERSION=v1` and `PROMPT_VERSION=v2` and observe output differences.
- [ ] I can run `POST /chat/structured` and get valid JSON (no extra text).
- [ ] I can locate the request in Langfuse and see metadata including `prompt_version`.
