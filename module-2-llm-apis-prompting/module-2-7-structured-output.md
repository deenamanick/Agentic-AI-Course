# Practical 2.7 — Return Structured Output

## Why, in simple terms

A paragraph is comfortable for a person, but software needs predictable fields.

```text
Human-friendly: "Buy milk, bread, and fruit."
Software-friendly: { "items": ["milk", "bread", "fruit"] }
```

## Guided build

Call `POST /chat/structured` and inspect the `summary` and `steps` schema. Test normal, ambiguous, and intentionally difficult prompts.

## Practice

Add validation limits for non-empty summaries and a bounded list of non-empty steps. Decide what the API should do when model output is invalid.

## Success checklist

- [ ] I can explain why applications need structured data.
- [ ] Clients receive a stable JSON schema.
- [ ] Invalid model output is detected.
- [ ] Validation failure does not expose raw internal errors.
