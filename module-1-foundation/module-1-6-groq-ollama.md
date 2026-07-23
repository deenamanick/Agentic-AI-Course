# Practical 1.6 — Connect FastAPI to Groq or Ollama

## Why, in simple terms

FastAPI handles web requests. A model provider generates the answer. LangChain gives our application a similar interface for different providers.

Use:

- **Groq Cloud** for the normal classroom path. It needs internet access and an API key, but no student GPU or model download.
- **Ollama** as an optional local path. It can work offline after downloading a model, but needs enough RAM and computing power.

## Recommended path: Groq Cloud

### Step 1: Create an individual API key

Create a Groq project and API key. Do not share the key in chat, screenshots, source code, or the frontend.

### Step 2: Configure `.env`

```text
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_your_key
GROQ_MODEL=llama-3.1-8b-instant
```

`llama-3.1-8b-instant` is a production model suitable for fast beginner exercises. Model availability can change, so instructors should verify the current supported-model list before a course.

### Step 3: Start FastAPI

```bash
uvicorn app.main:app --reload
```

### Step 4: Test the endpoint

Open `http://127.0.0.1:8000/docs` and call `POST /chat`.

Groq may return HTTP `429` when a project exceeds a request or token limit. Learners should use individual keys where possible rather than one key for the whole classroom.

## Optional path: Ollama

Choose this path when the computer can run the selected model:

```text
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama4:scout
```

Start and prepare Ollama:

```bash
ollama serve
ollama pull llama4:scout
```

Then run FastAPI and use the same `/chat` endpoint.

## What stays the same?

The endpoint still calls:

```python
result = await llm.ainvoke(messages)
```

Only `build_llm()` changes which provider supplies `llm`. This prepares students for later model comparisons without rewriting the API.

## Provider comparison

| Question | Groq | Ollama |
|---|---|---|
| Student GPU needed? | No | Depends on model |
| Internet needed? | Yes | Not after setup |
| API key needed? | Yes | No |
| Model download needed? | No | Yes |
| Classroom setup | Easier | Hardware-dependent |

## Failure practice

1. Remove `GROQ_API_KEY` and observe authentication failure.
2. Set an unsupported `LLM_PROVIDER`.
3. Set an invalid model name.
4. For optional Ollama mode, stop Ollama and call `/chat`.

## Success checklist

- [ ] FastAPI receives an answer from Groq without a local GPU.
- [ ] My API key exists only in backend environment configuration.
- [ ] I can explain Groq versus Ollama.
- [ ] I can switch providers using `LLM_PROVIDER`.
