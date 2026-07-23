# Practical 5.4 — Planning and Pattern Comparison

## Why

Planning helps multi-step tasks, but adds little value to simple requests.

## What you will build

Create a planner/executor graph. The planner returns no more than five typed steps. The executor records the result of each step, and a finalizer summarizes completed and failed work.

## Practice

Run simple and multi-step tasks through direct, ReAct, and plan-and-execute designs. Compare quality, latency, tokens, tool calls, and failure rate.

## Success checklist

- [ ] Plans have a validated schema and maximum length.
- [ ] Failed steps are visible in the final result.
- [ ] Your architecture decision is supported by measurements.
