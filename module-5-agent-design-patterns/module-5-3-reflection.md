# Practical 5.3 — Reflection with Bounded Revision

## Why

Reflection can repair an output, but an unlimited critic/revision loop can waste time and money.

## What you will build

Generate a structured answer, validate it, and run one critic/revision pass only when validation fails.

## Practice

The critic must return specific issues as structured data. The reviser receives the original task, draft, and issues. If the second validation fails, return a controlled failure rather than trying forever.

Compare the first-pass and revised success rates on at least 20 cases.

## Success checklist

- [ ] Reflection runs only after a failed check.
- [ ] Revision is limited to one attempt.
- [ ] The evaluation shows whether reflection adds measurable value.
