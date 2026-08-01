# Module 8: Agentic RAG and Verifiable Research

This module teaches you how to give your AI agent access to **your own documents** (PDFs, Company Policies, Research Papers) using Retrieval-Augmented Generation (RAG).

> **👨‍🎓 Student Guide: How to follow this Module**
> This module is split into two halves:
> 
> **Part A: RAG Fundamentals**
> We start with simple stories and analogies (like "loaves of bread" and "Google Maps") to help you build a basic, working PDF chatbot.
> 
> **Part B: Production RAG**
> Once your bot is working, we introduce the advanced engineering concepts (Hybrid Search, Re-ranking, Contextual Chunking) required to put RAG into production safely.

### What you'll build

A **PDF research assistant** that:
- Loads chunks of knowledge into an in-memory Vector Database.
- Uses semantic search to find the right paragraphs.
- Features a **Corrective LangGraph workflow** to grade evidence and retry if it fails.
- Provides a beautiful chat interface using Lovable.

---

## 📚 Course Outline

### Part A: RAG Fundamentals (Everyone Can Understand)
1. [Why do we need RAG?](module-8-0-why-rag.md)
2. [Document Ingestion](module-8-1-document-ingestion.md)
3. [What is Chunking?](module-8-2-chunking-basics.md)
4. [Embeddings & Vector Databases](module-8-3-embeddings-vector-db.md)
5. [Building the Basic RAG Bot](module-8-4-basic-rag-bot.md)

### Part B: Production RAG (Agentic AI Engineering)
6. [Hybrid Retrieval](module-8-5-hybrid-retrieval.md)
7. [Re-ranking](module-8-6-reranking.md)
8. [Contextual Chunking](module-8-7-contextual-chunking.md)
9. [Corrective RAG (Agentic Workflow)](module-8-8-corrective-rag.md)
10. [Trustworthy RAG (Citations & Defenses)](module-8-9-trustworthy-rag.md)
11. [RAG Evaluation Metrics](module-8-10-evaluation.md)

### UI Integration
12. [Create a Lovable Chat UI for RAG](module-8-11-lovable-rag-ui.md)

---

## Prerequisites

- Python 3.10+
- A Groq account and API key
- Completed Module 7 (Memory & Stateful Agents)

## Quick Start (Running the API)

From this folder (`module-8-agentic-rag/`):

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your API Key
cp .env.example .env
# Edit .env and add your GROQ_API_KEY

# 3. Start the API
uvicorn app.main:app --reload
```

Your API will be available at `http://localhost:8000/agent/chat`. You can test it by sending a POST request or connecting your Lovable UI (see Module 8.11).
