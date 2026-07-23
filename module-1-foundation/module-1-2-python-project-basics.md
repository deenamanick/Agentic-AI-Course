# Practical 1.2 — Functions, Packages, and Environment Variables

## Why, in simple terms

A real project should not place every instruction in one long file.

- A **function** is a reusable action.
- An **import** uses code from another file or package.
- A **package** is code someone prepared for us.
- A **virtual environment** keeps this project’s packages separate.
- An **environment variable** stores configuration outside the code.

## Part 1: Functions

Create `python_functions.py`:

```python
def create_greeting(name: str, topic: str) -> str:
    return f"Hello {name}. Let us learn {topic}!"


message = create_greeting("Anu", "FastAPI")
print(message)
```

In this function:

- `name: str` says the name should be text.
- `-> str` says the function returns text.
- `return` sends the result back.

## Part 2: Create a virtual environment

From `module-1-foundation`:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Your terminal should show `(.venv)`.

Install the project packages:

```bash
pip install -r requirements.txt
```

`requirements.txt` lists:

- `fastapi`: creates the API
- `uvicorn`: runs the API server
- `langchain`: supplies the common model interface
- `langchain-groq`: connects the app to hosted Groq models
- `langchain-ollama`: supports optional local Ollama models
- `langfuse`: records AI traces
- `python-dotenv`: loads `.env`
- `httpx`: makes HTTP requests

## Part 3: Environment variables

Copy the example:

```bash
cp .env.example .env
```

The application reads values such as:

```text
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_...
GROQ_MODEL=llama-3.1-8b-instant

# Optional local provider
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama4:scout
```

This lets us change the provider or model without editing Python.

Never commit real API keys and never place `GROQ_API_KEY` in frontend code.

## Success checklist

- [ ] I can define and call a function.
- [ ] My virtual environment is active.
- [ ] I understand what `requirements.txt` does.
- [ ] I understand why `.env` is separate from Python code.

## Common problems

**`No module named ...`**

Activate `.venv` and run `pip install -r requirements.txt`.

**The wrong Python is running**

Check:

```bash
which python
```

The path should contain `.venv`.
