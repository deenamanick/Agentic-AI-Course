# Practical 2.3 — Return Structured Output

## Build

Call `POST /chat/structured` and inspect the `summary` and `steps` schema. Test normal, ambiguous, and intentionally difficult prompts.

## Practice

Add validation limits for non-empty summaries and a bounded list of non-empty steps. Decide what the API should do when model output is invalid.

## Success checklist

- [ ] Clients receive a stable JSON schema.
- [ ] Invalid model output is detected.
- [ ] Validation failure does not expose raw internal errors.
