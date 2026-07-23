# Practical 1.8 — Trace AI Requests with Langfuse

## Why, in simple terms

When an AI answer is slow, expensive, or incorrect, normal server logs are not enough. A trace records what happened during one AI request.

Langfuse is optional in this beginner module.

## What a trace can show

- Request ID
- Model name
- Prompt version
- Input and output
- Start and finish time
- Token usage
- Errors

## How this application traces

`CallbackHandler()` listens to the LangChain model call. The metadata includes:

- Project
- Environment
- Request ID
- Session ID
- Tags

`get_client().flush()` sends buffered trace data immediately.

## Setup

Add your Langfuse values to `.env`:

```text
LANGFUSE_PUBLIC_KEY=...
LANGFUSE_SECRET_KEY=...
LANGFUSE_BASE_URL=...
```

Restart FastAPI, send two requests, and find them using the returned `request_id`.

## Privacy rule

Do not trace:

- Passwords
- API keys
- Private financial or health information
- Entire documents unless explicitly required and protected

## Practice tasks

1. Compare two request durations.
2. Find the model and environment tags.
3. Stop or misconfigure Langfuse and observe the behavior.
4. Decide which fields should be redacted in a real application.

## Success checklist

- [ ] I can explain a trace.
- [ ] I can find a request using its ID.
- [ ] I understand why secrets must not be traced.
- [ ] I understand that observability should not become a privacy leak.
