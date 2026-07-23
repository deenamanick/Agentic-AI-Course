# Practical 2.9 — Understand the Module 2 Code

## Why

The file `app/main.py` looks long because it contains several small ideas. Read it in sections instead of trying to understand everything at once.

## Section 1: Imports and configuration

```python
load_dotenv()
```

This loads provider, model, prompt-version, tracing, and frontend configuration from `.env`.

## Section 2: Prompt versions

```python
SYSTEM_PROMPT_V1 = (...)
SYSTEM_PROMPT_V2 = SYSTEM_PROMPT_V1 + (...)
```

`v2` reuses `v1` and adds rules. This makes the difference visible.

```python
def get_system_prompt(prompt_version: str) -> str:
```

This function selects the prompt used for one request.

## Section 3: API contracts

- `ChatRequest` accepts `user_query`.
- `ChatResponse` returns text, request ID, and prompt version.
- `StructuredChatResponse` returns summary, steps, request ID, and prompt version.

Pydantic validates these shapes.

## Section 4: Provider selection

```python
def build_llm() -> BaseChatModel:
```

The function reads `LLM_PROVIDER`:

- `groq` creates `ChatGroq` and needs no student GPU.
- `ollama` creates optional `ChatOllama`.
- Any other value raises a clear configuration error.

Both return a LangChain chat model, so the endpoints use the same `ainvoke()` call.

## Section 5: Normal chat

`POST /chat`:

1. Creates a request ID.
2. Selects the model.
3. Reads the prompt version.
4. Builds system and human messages.
5. Calls the model asynchronously.
6. Returns text plus metadata.

## Section 6: Structured chat

`POST /chat/structured` adds strict output instructions:

```text
summary: string
steps: array of strings
```

The model still returns text. Python uses `json.loads()` and checks the field types before returning `StructuredChatResponse`.

If parsing fails, the endpoint returns a safe HTTP `502` message without exposing internal details.

## Section 7: Tracing

Trace metadata includes:

- Project and environment
- Request ID
- Prompt version
- Tags

This lets instructors compare `v1` and `v2` requests later.

## Complete data flow

```text
ChatRequest
   -> prompt version
   -> build_llm()
   -> system + user messages
   -> ainvoke()
   -> text or JSON validation
   -> response model
```

## Practice

1. Change one sentence in `SYSTEM_PROMPT_V2`.
2. Add a `GET /health` endpoint.
3. Send an empty query and observe Pydantic validation.
4. Set `LLM_PROVIDER` to an unsupported value.
5. Explain which errors belong to user input, provider configuration, and model output.

## Success checklist

- [ ] I can find prompt selection, provider selection, and endpoints.
- [ ] I can explain both response models.
- [ ] I understand why structured model text is parsed and validated.
- [ ] I can draw the complete request flow.
