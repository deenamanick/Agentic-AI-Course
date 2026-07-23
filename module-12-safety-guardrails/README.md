# Module 12 — Safety, Security, and Human Approval

## Goal

Prevent agents from turning untrusted text or model mistakes into unauthorized actions.

## Topics

- Prompt injection and indirect prompt injection
- Tool least privilege and allowlists
- Authentication, resource ownership, and anti-IDOR checks
- PII, credentials, and trace redaction
- Content and domain guardrails
- Human-in-the-loop approval
- Confidence-based escalation
- Sandboxing, rate limiting, and abuse prevention
- Incident logging and safe failure

## Practicals

1. [Threat model an agent system](module-12-1-threat-model.md)
2. [Defend against prompt injection](module-12-2-prompt-injection.md)
3. [Enforce authorization and least privilege](module-12-3-authorization.md)
4. [Add human approval and runtime budgets](module-12-4-approval-budgets.md)

## Deliverable

A threat model, abuse-case test suite, and approval-gated agent workflow.

## Completion criteria

- Untrusted content cannot change system policy.
- Denied actions do not execute even if the model requests them.
- Internal error details and secrets are never returned to clients.
