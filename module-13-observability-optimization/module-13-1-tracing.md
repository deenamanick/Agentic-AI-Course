# Practical 13.1 — Instrument End-to-End Traces

## Build

Trace one request across API, graph nodes, model calls, retrieval, tools, and final response. Attach request ID, session ID, prompt version, model, latency, tokens, and status.

## Success checklist

- [ ] A request ID finds the whole execution.
- [ ] Parent/child spans reflect the workflow.
- [ ] Secrets and sensitive text are redacted.
