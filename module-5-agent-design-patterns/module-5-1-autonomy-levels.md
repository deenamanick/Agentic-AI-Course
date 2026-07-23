# Practical 5.1 — Agent Autonomy Levels

## Why

More autonomy adds cost and new failure modes. Start with the simplest design that completes the task.

## What you will build

Implement one support request as:

1. A basic responder
2. A router
3. A tool-calling agent

Use the same model, prompt, and ten test requests.

## Practice

Record task success, model calls, latency, and tokens for each version. Include easy, ambiguous, and unsupported requests. Add an explicit response for requests outside the system’s capability.

## Success checklist

- [ ] All three levels use the same test set.
- [ ] Every workflow has a step limit.
- [ ] You can explain why the least autonomous successful version is preferable.

## Common problem

If results cannot be compared, remove unrelated prompt and model differences.
