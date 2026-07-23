# Practical 3.2 — Understand the ReAct Loop

## Why

ReAct alternates reasoning about the next action with observing tool results. Production code must bound this loop.

## Practice

Trace a math request, a time request, and a request needing no tool. Identify the decision, tool call, observation, and final answer.

## Success checklist

- [ ] Relevant requests select the correct tool.
- [ ] General questions can answer without tools.
- [ ] A maximum iteration count prevents loops.
