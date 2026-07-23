# Practical 2.6 — Version Prompts

## Why, in simple terms

A prompt is part of the product. If we change it, we need to know which version produced an answer.

Think of a recipe:

- `v1` says “cook until ready.”
- `v2` gives the time, temperature, and checks.

We compare both before replacing the old recipe.

## Guided build

The application contains:

```python
SYSTEM_PROMPT_V1 = (...)

SYSTEM_PROMPT_V2 = (
    SYSTEM_PROMPT_V1
    + " Prefer short answers. Use headings."
    + " Ask one clarifying question when requirements are unclear."
)
```

The selection function is:

```python
def get_system_prompt(prompt_version: str) -> str:
    if prompt_version == "v2":
        return SYSTEM_PROMPT_V2
    return SYSTEM_PROMPT_V1
```

The response includes `prompt_version`, so the output can be traced back to its instructions.

## Step-by-step practice

1. Set this in `.env`:

   ```text
   PROMPT_VERSION=v1
   ```

2. Restart Uvicorn.
3. Run:

   ```bash
   bash scripts/test_chat.sh
   ```

4. Save the response.
5. Change `.env` to `PROMPT_VERSION=v2`.
6. Restart Uvicorn.
7. Run the same script.
8. Compare the answers using the same criteria.

## Practice

Send the same ten requests to both versions. Store inputs, outputs, latency, and observations instead of relying on memory.

Suggested cases:

- A clear request
- An unclear request
- A request needing a short answer
- A request needing steps
- A request outside the assistant’s role

## Why restart Uvicorn?

`load_dotenv()` runs when the application starts. Restarting ensures the process reads the changed `.env`.

## Practice levels

### Understand

Explain prompt versions using the recipe analogy.

### Practice

Compare `v1` and `v2` on five fixed requests.

### Challenge

Create `v3` with one justified change and predict which test cases it should improve.

## Common problems

**The response still says `v1`.**

Save `.env`, confirm its location, and restart Uvicorn.

**Every answer is different.**

Model generation can vary. Use several cases and defined criteria rather than comparing exact wording.

## Success checklist

- [ ] I can explain prompt versioning without code.
- [ ] Unknown versions fail or fall back explicitly.
- [ ] Every result identifies its prompt version.
- [ ] Prompts can change without editing request-handling logic.
- [ ] I can run a fair `v1` versus `v2` comparison.
