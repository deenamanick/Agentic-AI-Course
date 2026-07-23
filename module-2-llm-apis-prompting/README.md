# Module 2 — Talking to AI Clearly: Prompts, Roles, and Structured Answers

## Beginner promise

Module 2 begins with conversation and roleplay—not Python changes. Learners first experience how instructions change an AI response, then gradually connect that behavior to the existing code.

You may complete Practicals 2.1–2.5 using the chat interface or Ollama before opening `app/main.py`.

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

1. [Meet the LLM through roleplay](module-2-1-llm-roleplay.md)
2. [Turn vague requests into structured prompts](module-2-2-structured-prompts.md)
3. [Separate system and user prompts](module-2-3-prompt-roles.md)
4. [Break a large task into small prompts](module-2-4-prompt-chunking.md)
5. [Refine prompts and check AI mistakes](module-2-5-refine-and-verify.md)
6. [Version prompts](module-2-6-prompt-versioning.md)
7. [Return structured output](module-2-7-structured-output.md)
8. [Compare prompts with repeatable tests](module-2-8-prompt-comparison.md)

---

## Prerequisites

- Module 1 understanding-level activities
- Ability to send a message through the chat UI or Ollama
- Python practicals are helpful but not required for the first five lessons
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
