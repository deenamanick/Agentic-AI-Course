# Module 8 — Agentic RAG and Verifiable Research

## Goal

Build an agent that retrieves evidence, evaluates it, and answers with verifiable citations.

## Topics

- Ingestion, chunking, metadata, and embeddings
- Dense, sparse, and hybrid retrieval
- Query rewriting and decomposition
- Reranking
- Corrective and iterative retrieval
- Citation construction and evidence boundaries
- Retrieval evaluation
- Prompt injection in untrusted documents

## Theory: Agentic RAG vs Standard RAG

While a Standard RAG pipeline retrieves chunks from a Vector DB, an **Agentic RAG** can dynamically route between entirely different data sources (both structured and unstructured). 

For example, using a **Supervisor Agent** (Router):
- **Document Query Agent:** Searches unstructured PDFs/Text using tools like Cortex Search.
- **SQL Query Agent:** Searches structured SQL databases using tools like Cortex Analyst to fetch numeric insights (e.g., "Top 3 sales agents for Product X").

The Supervisor routes the query, the sub-agents retrieve the context, and the Supervisor synthesizes the final contextualized response.

## Practicals

1. [Ingest and chunk documents](module-8-1-ingestion-chunking.md)
2. [Retrieve and rerank evidence](module-8-2-retrieval-reranking.md)
3. [Build a corrective RAG graph](module-8-3-corrective-rag.md)
4. [Citations, injection defense, and evaluation](module-8-4-citations-evaluation.md)

## Deliverable

A PDF research assistant that provides page-level citations and never presents retrieved instructions as trusted system instructions.

## Completion criteria

- Every factual answer is linked to retrieved evidence.
- The evaluation set contains answerable and unanswerable questions.
- Retrieval precision and citation correctness are reported.
