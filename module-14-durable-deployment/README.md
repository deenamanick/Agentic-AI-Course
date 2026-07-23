# Module 14 — Durable Deployment and Operations

## Goal

Deploy long-running agent work without tying execution to one HTTP request.

## Target architecture

Use the Jeevisoft **Durable Orchestrator** pattern:

1. A standalone Cloudflare Worker authenticates and validates a request.
2. It creates a user-owned job and immediately returns `202 Accepted`.
3. A Cloudflare Workflow performs long-running agent steps.
4. D1 stores job state, ownership, progress, retries, and result metadata.
5. R2 stores large generated artifacts when needed.
6. The client polls a job-status endpoint or receives event-driven updates.

## Topics

- Job APIs and state machines
- Idempotency keys
- Checkpointing and recovery
- Retry policies, backoff, and timeouts
- Cancellation and compensation
- Parallel fan-out and aggregation
- Dead-letter handling
- Rate limiting, ownership, and structured logging

## Practicals

1. [Design the asynchronous job API](module-14-1-job-api.md)
2. [Model durable state and ownership](module-14-2-job-state.md)
3. [Add retries, checkpoints, and idempotency](module-14-3-recovery.md)
4. [Deploy and operate the workflow](module-14-4-deployment-operations.md)

## Deliverable

A deployed or locally emulated durable research job with polling, retries, cancellation, and recovery tests.

## Completion criteria

- Long-running requests return `202` promptly.
- Job state transitions are explicit and auditable.
- Retries cannot duplicate external side effects.
