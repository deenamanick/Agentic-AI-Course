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

## Theory: Agent Observability

Observability for AI Agents is far more challenging than traditional microservices due to the lack of a **global observer**. 

Because agents operate autonomously, in parallel, and bind dynamically at runtime, you cannot predict the execution path. We solve this by enforcing **Stateful Execution** (via LangGraph checkpoints). This allows us to run four types of queries against the execution graph:
1. **Local queries:** Answered using the local state of a single agent.
2. **Composite queries:** Expressed across the states of multiple parallel agents.
3. **Historical queries:** Analyzing the execution history of the entire composition.
4. **Relationship queries:** Tracking how the state of one agent influenced another.

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
