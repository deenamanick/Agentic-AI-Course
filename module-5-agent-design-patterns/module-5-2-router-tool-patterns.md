# Practical 5.2 — Router and Tool-Use Patterns

## Why

A router makes an explicit choice between known paths. A tool agent chooses an action dynamically. They solve different problems.

## What you will build

Create a LangGraph workflow with `general`, `math`, and `unknown` routes. The math route may call a typed calculator tool.

## Practice

Validate the router output with a fixed enum. Reject invalid routes, limit the calculator to supported operations, and trace the selected route and tool arguments.

Test direct questions, calculations, ambiguous messages, and malformed model output.

## Success checklist

- [ ] Router output is structured and validated.
- [ ] Tool arguments are validated before execution.
- [ ] Unsupported requests follow a controlled fallback path.
