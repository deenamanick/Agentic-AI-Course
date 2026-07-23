# Practical 1.3 — Connect and Test Ollama

## Steps

1. Start Ollama.
2. Pull the configured model.
3. Verify the model responds directly.
4. Set `OLLAMA_BASE_URL` and `OLLAMA_MODEL`.
5. Call the FastAPI endpoint with `scripts/test_chat.sh`.

## Failure practice

Try an unknown model and a stopped Ollama service. Observe how the API fails, then improve the error without leaking internals.

## Success checklist

- [ ] The configured model answers through the API.
- [ ] Connection failures produce a controlled error.
