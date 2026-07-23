# Practical 12.2 — Defend Against Prompt Injection

## Build

Place malicious instructions in a retrieved document and tool result. Keep untrusted content in a data boundary, restrict tool access in code, and validate generated actions independently.

## Success checklist

- [ ] Retrieved text cannot change system policy.
- [ ] Tool allowlists are enforced outside the prompt.
- [ ] The attack becomes an automated regression case.
