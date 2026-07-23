# Module 5 — Agent Design Patterns and Autonomy

## Goal

Learn to choose the least autonomous design that can reliably solve a task.

## Topics

- LLM vs RAG vs agent
- Basic responder, router, tool-caller, multi-agent, and autonomous-loop levels
- Reflection and self-correction
- ReAct
- Planning and plan-and-execute
- Deterministic graphs versus autonomous agents
- Stop conditions, step budgets, and fallback paths

## Practicals

1. [Agent autonomy levels](module-5-1-autonomy-levels.md)
2. [Router and tool-use patterns](module-5-2-router-tool-patterns.md)
3. [Reflection with bounded revision](module-5-3-reflection.md)
4. [Planning and pattern comparison](module-5-4-planning-comparison.md)

## Deliverable

An architecture decision record explaining which pattern should be used for three example business problems and why.

## Completion criteria

- No workflow can loop indefinitely.
- Invalid plans fail with a controlled error.
- The comparison includes at least 20 repeatable test prompts.
