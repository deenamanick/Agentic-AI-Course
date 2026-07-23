# Practical 2.1 — Separate System and User Prompts

## Why

System instructions define application behavior; user content supplies the task. Mixing them makes behavior harder to control and test.

## Practice

Identify the system and user messages in `app/main.py`. Test the same user request under two system roles. Add a user message that attempts to override the system role and observe the result.

## Success checklist

- [ ] User data remains separate from system policy.
- [ ] Prompt inputs are visible and testable.
- [ ] Untrusted text is never inserted as system instructions.
