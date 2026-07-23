# Practical 2.6 — Version Prompts

## Why, in simple terms

A prompt is part of the product. If we change it, we need to know which version produced an answer.

Think of a recipe:

- `v1` says “cook until ready.”
- `v2` gives the time, temperature, and checks.

We compare both before replacing the old recipe.

## Guided build

Use `PROMPT_VERSION` to switch between `v1` and `v2`. Return the selected version in the API response and attach it to trace metadata.

## Practice

Send the same ten requests to both versions. Store inputs, outputs, latency, and observations instead of relying on memory.

## Success checklist

- [ ] I can explain prompt versioning without code.
- [ ] Unknown versions fail or fall back explicitly.
- [ ] Every result identifies its prompt version.
- [ ] Prompts can change without editing request-handling logic.
