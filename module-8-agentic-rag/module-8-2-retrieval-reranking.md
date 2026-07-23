# Practical 8.2 — Retrieve and Rerank Evidence

## Why

Vector similarity alone can return plausible but weak evidence.

## What you will build

Implement dense or local semantic retrieval, keyword retrieval, metadata filtering, and a reranking stage.

## Practice

Create at least 20 labeled questions. Measure whether the correct source appears in the top 1, 3, and 5 results. Compare retrieval before and after reranking.

## Success checklist

- [ ] Retrieval is evaluated separately from generation.
- [ ] Filters cannot expose another user’s documents.
- [ ] Reranking improvement is measured.
- [ ] Scores and source metadata are traceable.
