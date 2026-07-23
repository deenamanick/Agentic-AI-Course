# Practical 14.3 — Retries, Checkpoints, and Idempotency

## Build

Checkpoint after each durable step. Add bounded exponential backoff and idempotency keys around external writes.

Kill execution after a checkpoint, restart it, and prove completed effects are not repeated.

## Success checklist

- [ ] Retryable and permanent failures are distinct.
- [ ] Recovery resumes from stored state.
- [ ] Duplicate delivery cannot duplicate side effects.
