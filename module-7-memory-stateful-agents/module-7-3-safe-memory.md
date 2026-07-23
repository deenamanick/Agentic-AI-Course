# Practical 7.3 — Safe Memory Lifecycle

## Why

Persistent false or sensitive memories can repeatedly harm future answers.

## What you will build

Add endpoints or commands to inspect, approve, correct, expire, and delete memories.

## Practice

Test cross-user access, correction, deletion, expiration, duplicate facts, and malicious instructions stored inside a memory. Treat memory text as untrusted data.

## Success checklist

- [ ] Users can see and delete their stored memory.
- [ ] Ownership checks fail closed.
- [ ] Deleted memory is no longer retrieved.
- [ ] Stored text cannot override system instructions.
