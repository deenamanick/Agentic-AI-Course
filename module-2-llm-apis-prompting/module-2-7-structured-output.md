# Practical 2.7 — Return Structured Output

## Why, in simple terms

A paragraph is comfortable for a person, but software needs predictable fields.

```text
Human-friendly: "Buy milk, bread, and fruit."
Software-friendly: { "items": ["milk", "bread", "fruit"] }
```

## Guided build

Call `POST /chat/structured` and inspect the `summary` and `steps` schema. Test normal, ambiguous, and intentionally difficult prompts.

## The output contract

```json
{
  "summary": "A short explanation",
  "steps": [
    "First step",
    "Second step"
  ]
}
```

The API adds `request_id` and `prompt_version` to the validated response.

## Human roleplay

One learner is the model and writes an answer. Another is the validator.

Test these outputs:

1. Correct JSON
2. JSON missing `steps`
3. `steps` written as one string
4. A paragraph before the JSON
5. Broken quotation marks

Only the first output follows the contract.

## How the code checks the model

```python
parsed = json.loads(result.content)
summary = parsed["summary"]
steps = parsed["steps"]
```

Then it checks:

- `summary` is text
- `steps` is a list
- Every step is text

If any check fails, FastAPI returns HTTP `502`. The backend received an unusable response from its model dependency.

## Step-by-step practice

1. Start the API.
2. Run:

   ```bash
   bash scripts/test_chat_structured.sh
   ```

3. Identify all four response fields.
4. Change the requested number of steps.
5. Test an ambiguous request.
6. Inspect the corresponding trace.

## Practice

Add validation limits for non-empty summaries and a bounded list of non-empty steps. Decide what the API should do when model output is invalid.

## Practice levels

### Understand

Sort examples into valid and invalid JSON shapes.

### Practice

Call the structured endpoint and explain every field.

### Challenge

Add a typed field such as `difficulty` with allowed values `beginner`, `intermediate`, and `advanced`.

## Common problem

**The endpoint returns HTTP 502.**

The model returned text that could not be parsed or did not match the expected shape. Inspect the trace and output instructions; do not expose the raw internal exception to users.

## Success checklist

- [ ] I can explain why applications need structured data.
- [ ] Clients receive a stable JSON schema.
- [ ] Invalid model output is detected.
- [ ] Validation failure does not expose raw internal errors.
- [ ] I can explain why JSON syntax and schema validation are different checks.
