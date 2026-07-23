# Practical 2.10 — Understand and Use the Test Scripts

## Why

The scripts send the same request repeatedly. This makes prompt comparison fairer than typing a different question each time.

## Script 1: Normal chat

Run:

```bash
bash scripts/test_chat.sh
```

The script sends:

```text
POST /chat
Content-Type: application/json
{"user_query": "..."}
```

The expected response contains:

```json
{
  "answer": "model response",
  "request_id": "unique ID",
  "prompt_version": "v1"
}
```

## Script 2: Structured chat

Run:

```bash
bash scripts/test_chat_structured.sh
```

It calls `POST /chat/structured`. The expected response contains:

```json
{
  "summary": "short summary",
  "steps": ["step one", "step two"],
  "request_id": "unique ID",
  "prompt_version": "v1"
}
```

## Why both scripts use the same Bash safety line

```bash
set -euo pipefail
```

- `-e`: stop after a failed command.
- `-u`: stop when an unknown variable is used.
- `pipefail`: detect failures inside pipelines.

## Fair comparison activity

1. Set `PROMPT_VERSION=v1` in `.env`.
2. Restart Uvicorn.
3. Run both scripts and save the results.
4. Set `PROMPT_VERSION=v2`.
5. Restart Uvicorn.
6. Run the same scripts.
7. Compare clarity, format, questions, and validity.

## Failure practice

1. Stop Uvicorn and run a script.
2. Remove `user_query` from the JSON.
3. Break one JSON quotation mark.
4. Use the wrong endpoint.
5. Restore each change and explain the error.

## Success checklist

- [ ] I know why fixed test scripts improve comparison.
- [ ] I can explain the endpoint, header, and JSON body.
- [ ] I can distinguish normal and structured responses.
- [ ] I can diagnose connection, validation, and formatting errors.
