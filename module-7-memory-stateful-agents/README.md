# Module 7 — Memory and Stateful Agents

## Goal

Give an agent useful continuity without creating unsafe or inaccurate permanent memory.

## Topics

- Working and conversation memory
- Long-term semantic memory
- Episodic execution memory
- Entity and user-preference memory
- Summarization and context-window management
- Memory extraction, confidence, correction, expiration, and deletion
- Tenant isolation and consent
- Vector storage versus relational storage

## Practicals

1. [Working and conversation memory](module-7-1-working-memory.md)
2. [Long-term and semantic memory](module-7-2-long-term-memory.md)
3. [Safe memory lifecycle](module-7-3-safe-memory.md)
4. [Build a stateful tutor](module-7-4-stateful-tutor.md)

## Deliverable

A stateful tutor that remembers learning goals and previous mistakes across sessions while supporting inspect, correct, and forget operations.

## Completion criteria

- Cross-user memory access tests fail closed.
- Unapproved model guesses are not stored as facts.
- Memory retrieval quality and token savings are measured.
