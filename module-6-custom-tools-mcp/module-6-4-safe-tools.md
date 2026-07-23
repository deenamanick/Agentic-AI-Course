# Practical 6.4 — Secure, Test, and Approval-Gate Tools

## Why

Read operations and consequential writes must not have the same permission model.

## What you will build

Add a simulated `create_notification` write tool with:

- User ownership checks
- An idempotency key
- A preview
- Explicit human approval

## Practice

Test denial, approval, duplicate submission, wrong-user access, timeout, and upstream failure. Log the decision without storing secret content.

## Success checklist

- [ ] A model cannot approve its own action.
- [ ] Duplicate idempotency keys cannot duplicate writes.
- [ ] Authorization is checked inside the tool.
- [ ] Denied actions leave no side effects.
