# Practical 1.6 — Connect FastAPI to Ollama

## Why, in simple terms

FastAPI handles web requests. Ollama runs the language model. LangChain connects our Python application to Ollama.

## Step 1: Start Ollama

```bash
ollama serve
```

Keep this terminal running.

## Step 2: Pull the configured model

Open another terminal:

```bash
ollama pull llama4:scout
```

If your computer cannot run this model comfortably, select a smaller Ollama chat model and update `OLLAMA_MODEL` in `.env`.

## Step 3: Test Ollama directly

```bash
ollama run llama4:scout
```

Ask a simple question, then exit.

## Step 4: Start FastAPI

Activate `.venv`, then run:

```bash
uvicorn app.main:app --reload
```

## Step 5: Test in API docs

Open:

```text
http://127.0.0.1:8000/docs
```

Use `POST /chat` with:

```json
{
  "user_query": "Explain an AI agent in three simple points."
}
```

## What is LangChain doing?

`ChatOllama` gives the application one consistent chat interface:

```python
result = await llm.ainvoke(messages)
```

Later modules can add tools and graphs around this model call.

## Failure practice

1. Stop Ollama and call `/chat`.
2. Use a model name that is not installed.
3. Put the wrong Ollama port in `.env`.
4. Restore each setting and test again.

## Success checklist

- [ ] Ollama answers directly.
- [ ] FastAPI receives an answer from Ollama.
- [ ] I understand the roles of FastAPI, LangChain, and Ollama.
- [ ] I can diagnose a stopped service or missing model.
