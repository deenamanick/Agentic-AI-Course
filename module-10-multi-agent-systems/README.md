# Module 10 — Multi-Agent Systems

## Goal

Coordinate specialized agents when decomposition provides measurable value.

## Topics

- Supervisor, router, sequential, hierarchical, and peer patterns
- Role and responsibility boundaries
- Structured handoff contracts
- Shared versus isolated context
- Parallel fan-out and result aggregation
- Conflict resolution and review agents
- Delegation depth, budgets, and termination
- When a single graph is better than multiple agents

## Practicals

1. [Design roles and handoff contracts](module-10-1-roles-handoffs.md)
2. [Build a supervisor workflow](module-10-2-supervisor.md)
3. [Parallel research and aggregation](module-10-3-parallel-agents.md)
4. [Review, terminate, and compare](module-10-4-review-baseline.md)

## Deliverable

A deep-research workflow that produces a cited report plus a machine-readable execution record of agents, handoffs, evidence, and revisions.

## Completion criteria

- Delegation depth and total model calls are bounded.
- Failed child tasks are surfaced rather than silently ignored.
- Multi-agent quality improvement is measured against the baseline.
