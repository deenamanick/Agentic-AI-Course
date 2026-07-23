# Practical 9.2 — Implement the Workflow in LangGraph

## Build

Represent research, fact-checking, revision, and finalization as explicit graph nodes. Persist state between nodes and limit revision to one pass.

## Test

Trace node transitions, simulate a failed tool, and prove the graph reaches a controlled terminal state.

## Success checklist

- [ ] State and routing are visible.
- [ ] Retries and revisions are bounded.
- [ ] Framework code is isolated in an adapter.
