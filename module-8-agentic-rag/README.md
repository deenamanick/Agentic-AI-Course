# Module 8: Agentic RAG and Verifiable Research

This module is about giving your AI agent access to **your own documents**. So far, the agent can only answer from its training data. Here you will teach it to read PDFs, search through them, and answer with **page-level citations**.

> **👨‍🎓 Student Guide: How to follow this Module**
> 1. **Phase 1: Concepts (Practical 0)** - Understand what RAG is and why Agentic RAG is different.
> 2. **Phase 2: Build the Pipeline (Practicals 1-2)** - Ingest documents, chunk them, and retrieve evidence.
> 3. **Phase 3: Make it Smart (Practical 3)** - Build a corrective RAG graph that retries when evidence is weak.
> 4. **Phase 4: Make it Trustworthy (Practical 4)** - Add citations, defend against prompt injection, and evaluate.

### What you'll build

A **PDF research assistant** that:
- Reads and chunks your PDF documents
- Stores them in a vector database for search
- Retrieves the most relevant evidence for any question
- Answers with page-level citations (e.g., "According to page 5 of document X...")
- Defends against prompt injection in untrusted documents
- Refuses to answer when evidence is insufficient

### What's in this folder

- `module-8-0-what-is-rag.md` — What is RAG? Standard vs Agentic RAG (concepts only)
- `module-8-1-ingestion-chunking.md` — Ingest and chunk documents
- `module-8-2-retrieval-reranking.md` — Retrieve and rerank evidence
- `module-8-3-corrective-rag.md` — Build a corrective RAG graph (LangGraph)
- `module-8-4-citations-evaluation.md` — Citations, injection defense, and evaluation

### Recommended order

1. What is RAG? (concepts)
2. Ingestion & Chunking (prepare your documents)
3. Retrieval & Reranking (search your documents)
4. Corrective RAG Graph (smart retry logic)
5. Citations & Evaluation (trustworthy answers)

---

## How RAG Works (mental model)

```text
User asks a question
        |
        v
Agent searches your documents (Vector DB)
        |
        v
Retrieves the most relevant chunks (evidence)
        |
        v
Grades the evidence — is it good enough?
        |
       / \
      /   \
   Yes     No
    |       |
    v       v
 Answer   Rewrite the query & retry once
 with       |
citations   v
          Still weak? → "Insufficient evidence"
```

---

## Key Concepts at a Glance

| Concept | What it means | Simple analogy |
| :--- | :--- | :--- |
| **RAG** (Retrieval-Augmented Generation) | The AI searches your documents before answering | Like a student who checks their textbook before answering an exam question |
| **Chunking** | Splitting a big document into small, searchable pieces | Like cutting a book into index cards |
| **Embeddings** | Converting text into numbers so the computer can measure similarity | Like converting words into GPS coordinates — similar words are nearby |
| **Vector DB** | A database optimized for finding similar embeddings | Like a library where books are arranged by topic, not alphabetically |
| **Reranking** | Re-scoring search results to put the best evidence first | Like a teacher reviewing student answers and putting the best one on top |
| **Corrective RAG** | The agent retries with a rewritten query if evidence is weak | Like asking the librarian "Can you search again with different keywords?" |
| **Citations** | Linking each claim to the exact source page | Like footnotes in an academic paper |

---

## Prerequisites

- Python 3.10+
- A Groq account and API key
- Completed Module 7 (Memory & Stateful Agents)

---

## Checklist

- [ ] You understand the difference between Standard RAG and Agentic RAG.
- [ ] You can explain what chunking, embeddings, and vector databases do.
- [ ] You successfully ingested documents and retrieved relevant evidence.
- [ ] Your agent provides page-level citations with every answer.
- [ ] Your agent refuses to answer when evidence is insufficient.
