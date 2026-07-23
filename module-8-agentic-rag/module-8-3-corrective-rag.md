# Practical 8.3 — Build a Corrective RAG Graph

## Why

An agent should retry retrieval only when the available evidence is insufficient.

## What you will build

Create a LangGraph flow:

```text
route -> retrieve -> grade evidence -> answer
                         |
                         +-> rewrite query -> retrieve once
```

## Practice

Use structured evidence grades. Limit rewriting to one attempt. If evidence remains weak, return `insufficient_evidence`.

## Success checklist

- [ ] The graph has a visible stop condition.
- [ ] Retrieval retries are bounded.
- [ ] Unsupported questions do not receive invented answers.
- [ ] Each node is traced.
