# Practical 1.7 — Understand the Bash and curl Test Script

## Why, in simple terms

Clicking buttons is useful, but developers also need a quick repeatable test.

The file `scripts/test_chat.sh` sends one request to the API.

## What is a script?

A script is a saved list of commands. Instead of typing the same long command every time, run:

```bash
bash scripts/test_chat.sh
```

## Line-by-line explanation

### Line 1

```bash
#!/usr/bin/env bash
```

This tells the computer to use Bash.

### Safety settings

```bash
set -euo pipefail
```

- `-e`: stop when a command fails.
- `-u`: stop when an unknown variable is used.
- `pipefail`: detect failure anywhere in a command pipeline.

### Send the HTTP request

```bash
curl -sS -X POST "http://127.0.0.1:8000/chat"
```

- `curl` sends web requests.
- `-sS` hides progress but still shows errors.
- `-X POST` selects the POST method.
- The URL points to our local `/chat` endpoint.

### Tell FastAPI we are sending JSON

```bash
-H "Content-Type: application/json"
```

`-H` adds an HTTP header.

### Send the JSON body

```bash
-d '{"user_query":"Explain AI agents simply."}'
```

`-d` sends data.

### Display the result

```bash
| cat
```

The pipe `|` sends curl’s output to `cat`, which prints it.

## Full mental model

```text
test_chat.sh
  -> curl
  -> POST http://127.0.0.1:8000/chat
  -> JSON request
  -> FastAPI
  -> Ollama
  -> JSON response
  -> terminal
```

## Practice tasks

1. Change the question in the script.
2. Change the port to `9999` and observe the connection error.
3. Remove `user_query` and observe validation.
4. Create `scripts/test_health.sh` for `GET /health`.
5. Add `-i` to curl to display response headers and status.

## Success checklist

- [ ] I know why the script exists.
- [ ] I can explain `POST`, `-H`, and `-d`.
- [ ] I understand the pipe symbol.
- [ ] I can modify and rerun the test.

## Common problems

**Connection refused**

Start FastAPI and verify port `8000`.

**Validation error**

Check that the JSON contains a string named `user_query`.

**JSON quoting error**

Keep the outer JSON quotes single and the JSON field quotes double.
