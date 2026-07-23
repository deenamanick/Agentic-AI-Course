# Module 15 — Production Capstone

## Goal

Design, build, evaluate, and defend a production-ready agent system.

## Recommended capstones

- Deep research agent with verifiable citations
- Personalized tutoring agent with consent-based memory
- Customer-support agent with human escalation
- Incident-response multi-agent workflow
- Documentation agent for a source repository
- Financial analysis assistant with approval-gated actions

## Mandatory capabilities

- Typed API and tool contracts
- At least one deterministic workflow and one justified agentic decision
- MCP or an equivalent reusable tool boundary
- Grounded retrieval with citations when factual documents are used
- User-scoped state or memory
- Automated evaluation dataset and regression report
- Prompt-injection and unauthorized-action defenses
- Human approval for consequential writes
- End-to-end tracing, cost, and latency metrics
- Durable asynchronous execution with retries and cancellation

## Required artifacts

1. Architecture diagram and decision record
2. Threat model
3. API and tool documentation
4. Evaluation dataset and report
5. Operations runbook
6. Cost and latency report
7. Live demonstration and failure-recovery demonstration

## Practicals

1. [Select the problem and define success](module-15-1-problem-success.md)
2. [Design architecture and security](module-15-2-architecture-security.md)
3. [Build and evaluate the system](module-15-3-build-evaluate.md)
4. [Release, demonstrate, and defend](module-15-4-release-defense.md)

## Review rubric

| Area | Weight |
|---|---:|
| Task quality and groundedness | 20% |
| Evaluation and testing | 20% |
| Safety and authorization | 20% |
| Reliability and recovery | 15% |
| Architecture and code quality | 10% |
| Observability and operations | 10% |
| Communication and documentation | 5% |

## Release gate

The capstone is complete only when critical safety tests pass, no known cross-user access is possible, retries are idempotent, evaluation thresholds are met, and a failed execution can be diagnosed and recovered.
