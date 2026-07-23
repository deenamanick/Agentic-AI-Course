# Practical 7.2 — Long-Term and Semantic Memory

## Why

Long-term memory should retrieve useful facts, not replay every old conversation.

## What you will build

Store approved learning preferences and past lesson outcomes with user ID, source, timestamp, confidence, and expiration metadata.

## Practice

Retrieve memories by semantic relevance and metadata filters. Compare relational lookup and vector retrieval. Do not store raw model guesses as facts.

## Success checklist

- [ ] Every memory has provenance and an owner.
- [ ] Retrieval filters by authenticated user.
- [ ] Low-confidence candidates require review.
- [ ] Irrelevant memories are excluded from context.
