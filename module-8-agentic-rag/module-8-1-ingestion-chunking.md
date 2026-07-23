# Practical 8.1 — Ingest and Chunk Documents

## Why

Retrieval quality begins with clean text, useful chunks, and traceable metadata.

## What you will build

Ingest a small PDF collection. Store document ID, page, section, chunk index, checksum, and source title with each chunk.

## Practice

Compare fixed-size and section-aware chunking. Inspect chunks manually. Re-ingesting an unchanged document must not create duplicates.

## Success checklist

- [ ] Every chunk maps back to a page and source.
- [ ] Duplicate ingestion is idempotent.
- [ ] Empty and unreadable pages are handled.
- [ ] Chunking choices are documented.
