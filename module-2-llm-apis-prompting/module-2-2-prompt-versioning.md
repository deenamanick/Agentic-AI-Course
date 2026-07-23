# Practical 2.2 — Version Prompts

## Build

Use `PROMPT_VERSION` to switch between `v1` and `v2`. Return the selected version in the API response and attach it to trace metadata.

## Practice

Send the same ten requests to both versions. Store inputs, outputs, latency, and observations instead of relying on memory.

## Success checklist

- [ ] Unknown versions fail or fall back explicitly.
- [ ] Every result identifies its prompt version.
- [ ] Prompts can change without editing request-handling logic.
