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

## Theory: Enterprise Guardrails

When building autonomous agents, "Write" tools (like sending emails or making payments) are inherently dangerous. We protect the system using three core concepts:

**1. The Human-in-the-Loop (HITL) Strategy:**
- **Co-plan:** Validate that the agent's generated execution graph matches user intent.
- **Co-execute:** Pause execution allowing the user to provide feedback if the agent strays.
- **Co-comply:** Mark critical/irreversible tasks (e.g., payments) to require explicit approval after verifying guardrails.

**2. Automated Guardrails Pipeline:**
Policies shouldn't just be prompt instructions. They should be mapped to specific tools, compiled into validation code, and invoked *before* the agent executes a tool. If the guardrail fails, the agent is prompted to reflect and adapt.

**3. Privacy Inference Attacks:**
LLMs are vulnerable to **Membership Inference** (detecting if a user's data was in the training set) and **Property Inference** (reconstructing properties of the dataset) even via Black Box API attacks. We mitigate this via strict authorization constraints.

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
