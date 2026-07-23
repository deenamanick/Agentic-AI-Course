# Module 9 — Agent Framework Comparison

## Goal

Understand framework tradeoffs instead of treating framework selection as the architecture.

## Frameworks

- LangGraph
- CrewAI
- AutoGen

## Comparison dimensions

- Control flow and state
- Tool integration
- Human approval
- Persistence and recovery
- Observability
- Testing
- Parallelism
- Vendor and framework coupling

## Practicals

1. [Create a framework-neutral contract](module-9-1-neutral-contract.md)
2. [Implement the workflow in LangGraph](module-9-2-langgraph.md)
3. [Implement it in CrewAI and AutoGen](module-9-3-crewai-autogen.md)
4. [Benchmark and choose a framework](module-9-4-framework-decision.md)

## Deliverable

A decision matrix and short architecture decision record selecting a framework for:

- A deterministic approval workflow
- A collaborative research team
- A conversational multi-agent simulation

## Completion criteria

- Claims are supported by working prototypes.
- Business logic is kept separate from framework adapters.
- Quality, latency, cost, and implementation complexity are compared.
