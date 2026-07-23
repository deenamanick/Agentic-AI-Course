# Module 13 — Observability, Cost, and Performance

## Goal

Make agent behavior explainable enough to debug and economical enough to operate.

## Topics

- Trace, span, session, user, and request identifiers
- Prompt and model versioning
- Tool-call and graph-node instrumentation
- Structured error categories
- Token, latency, and cost attribution
- User feedback and evaluation linkage
- Sampling and sensitive-data redaction
- Caching, routing, batching, and smaller-model strategies

## Practicals

1. [Instrument end-to-end traces](module-13-1-tracing.md)
2. [Build operational metrics](module-13-2-metrics.md)
3. [Diagnose failures safely](module-13-3-failure-analysis.md)
4. [Optimize cost and latency](module-13-4-optimization.md)

## Deliverable

An observability runbook and before/after optimization report.

## Completion criteria

- A failed request can be diagnosed from its request ID.
- Sensitive inputs are redacted.
- Optimization decisions are supported by evaluation results.
