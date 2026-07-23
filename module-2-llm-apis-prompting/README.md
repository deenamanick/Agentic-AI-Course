# Module 2 — Talking to AI Clearly: Prompts, Roles, and Structured Answers

## Beginner promise

Module 2 begins with conversation and roleplay—not Python changes. Learners first experience how instructions change an AI response, then gradually connect that behavior to the existing code.

You may complete Practicals 2.1–2.5 using the chat interface or Groq-backed API before opening `app/main.py`.

Every practical has three levels:

- **Understand:** Explain the idea without code.
- **Practice:** Use a guided prompt or working command.
- **Challenge:** Change the implementation when ready.

The challenge level is optional. A learner can understand prompting without being an experienced Python developer.

## What you will practice

In this module you take the Module 1 `/chat` API idea and turn it into a **prompt engineering lab**:

- Prompt versioning using `PROMPT_VERSION` (`v1` vs `v2`)
- System prompts and user prompts
- Breaking large requests into smaller prompts
- Reviewing and refining AI answers
- Comparing outputs across prompt versions
- Producing **reliable structured JSON** output from an LLM
- Testing both normal and failure cases
- Tracing requests in Langfuse with useful metadata

---

## What’s in this folder

- `app/main.py`
  - `POST /chat` (includes `prompt_version` in the response)
  - `POST /chat/structured` (returns `summary` + `steps` as JSON)
  - Uses Groq by default and optional Ollama through `LLM_PROVIDER`
- `requirements.txt`
  - Python packages used by the lab
- `.env.example`
  - Model provider, prompt version, tracing, and frontend settings
- `scripts/test_chat.sh`
  - Tests normal text output
- `scripts/test_chat_structured.sh`
  - Tests structured JSON output

## Practicals

0. [Start here: how Module 2 extends Module 1](module-2-0-bridge-from-module-1.md)
1. [Meet the LLM through roleplay](module-2-1-llm-roleplay.md)
2. [Turn vague requests into structured prompts](module-2-2-structured-prompts.md)
3. [Separate system and user prompts](module-2-3-prompt-roles.md)
4. [Break a large task into small prompts](module-2-4-prompt-chunking.md)
5. [Refine prompts and check AI mistakes](module-2-5-refine-and-verify.md)
6. [Version prompts](module-2-6-prompt-versioning.md)
7. [Return structured output](module-2-7-structured-output.md)
8. [Compare prompts with repeatable tests](module-2-8-prompt-comparison.md)
9. [Understand the Module 2 code](module-2-9-code-walkthrough.md)
10. [Understand and use the test scripts](module-2-10-test-scripts.md)
11. [Create a Lovable Prompt Lab UI](module-2-11-lovable-prompt-lab.md)

---

## Prerequisites

- Module 1 understanding-level activities
- Ability to send a message through the Module 1 chat API
- Python practicals are helpful but not required for the first five lessons
- Groq account and individual API key for the recommended no-GPU path
- Ollama only for optional local inference
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

### Recommended: Groq Cloud

Set in `.env`:

```text
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_your_individual_key
GROQ_MODEL=llama-3.1-8b-instant
PROMPT_VERSION=v1
```

No GPU or local model download is required.

### Optional: local Ollama

Set `LLM_PROVIDER=ollama`, then run:

```bash
ollama serve
ollama pull llama4:scout
```

### Start the API server

```bash
uvicorn app.main:app --reload
```

---

## Lab: Prompt versions

The application reads `PROMPT_VERSION` when handling a request. Set it in `.env` and restart Uvicorn:

```text
PROMPT_VERSION=v1
```

Run:

```bash
bash scripts/test_chat.sh
```

Change `.env` to `PROMPT_VERSION=v2`, restart the server, and run the same script again.

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

- [ ] I can explain the difference between an LLM, RAG, and an agent.
- [ ] I can improve a vague prompt using Role, Task, Context, Rules, and Output.
- [ ] I can separate system instructions from user content.
- [ ] I can break one large request into smaller reviewable prompts.
- [ ] I review AI answers instead of automatically trusting them.
- [ ] I can run `POST /chat` and see `prompt_version` in the response.
- [ ] I can switch between `PROMPT_VERSION=v1` and `PROMPT_VERSION=v2` and observe output differences.
- [ ] I can run `POST /chat/structured` and get valid JSON (no extra text).
- [ ] I can locate the request in Langfuse and see metadata including `prompt_version`.

## Common problems

- **HTTP 401 from Groq:** Check `GROQ_API_KEY` and restart Uvicorn.
- **HTTP 429 from Groq:** The project reached a request or token limit. Wait and retry; use individual student keys.
- **Prompt version does not change:** Update `.env`, save it, and restart Uvicorn.
- **HTTP 502 from `/chat/structured`:** The model did not return the required JSON shape. Retry once, then inspect the prompt and trace.
- **Connection refused:** Start Uvicorn and confirm port `8000`.
