# Module 8.0: What is RAG? 🔍

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: The Problem** - Understand why LLMs can't answer questions about YOUR documents.
> 2. **Phase 2: The Solution** - Learn what RAG is and how it works.
> 3. **Phase 3: The Upgrade** - See how Agentic RAG is smarter than Standard RAG.

### Why (in simple terms)

Your AI agent (from Modules 1-7) can answer general questions because it was trained on internet data. But what if you ask it:
- *"What does page 12 of our company policy say about remote work?"*
- *"Summarize the key findings from this research paper I uploaded."*
- *"What is the refund policy in our terms of service?"*

The AI will **hallucinate** (make up an answer) because it has never seen your private documents!

### What you'll learn
1. **The Hallucination Problem**: Why LLMs make things up when they don't know.
2. **RAG**: How we fix this by giving the AI access to real documents.
3. **Standard vs Agentic RAG**: Why smart agents need smarter retrieval.

---

## 📚 The Problem: LLMs Don't Know Your Data

| What you ask | What the AI does WITHOUT RAG | What the AI does WITH RAG |
| :--- | :--- | :--- |
| "What's on page 12 of our policy?" | ❌ Makes up a plausible-sounding answer | ✅ Searches your PDF, finds page 12, and quotes it |
| "Summarize this research paper" | ❌ Invents findings that sound real | ✅ Reads the actual paper and summarizes it |
| "What's our refund policy?" | ❌ Guesses based on common refund policies | ✅ Finds the exact clause in your Terms of Service |

**The core problem:** LLMs are trained on public internet data. They have never seen your private documents, company policies, or research papers.

---

## 🔌 What is RAG? (Retrieval-Augmented Generation)

RAG is a technique where we **retrieve** relevant information from your documents and **augment** the AI's prompt with that information before it **generates** a response.

### The RAG Pipeline (step by step):

| Step | What happens | Analogy |
| :--- | :--- | :--- |
| **1. Ingest** | Your PDFs/documents are loaded and split into small chunks | Cutting a textbook into index cards |
| **2. Embed** | Each chunk is converted into a numerical vector (embedding) | Converting each card into GPS coordinates |
| **3. Store** | Embeddings are stored in a Vector Database | Filing the cards in a special library sorted by topic |
| **4. Query** | The user's question is also converted to an embedding | Getting GPS coordinates for your question |
| **5. Retrieve** | The system finds the chunks most similar to the question | Finding the closest cards in the library |
| **6. Augment** | The retrieved chunks are added to the AI's prompt | Handing the student the relevant index cards |
| **7. Generate** | The AI reads the chunks and generates an answer | The student writes an answer using the cards as evidence |

---

## 🧠 Standard RAG vs Agentic RAG

Standard RAG follows a simple pipeline: Retrieve → Generate. But what if the retrieval returns bad results?

| Feature | Standard RAG | Agentic RAG |
| :--- | :--- | :--- |
| **Retrieval** | Single search, one data source | Dynamic routing across multiple sources |
| **Quality Check** | None — uses whatever it finds | Grades evidence quality before answering |
| **Retry Logic** | None — answers with bad evidence | Rewrites the query and retries if evidence is weak |
| **Data Sources** | Only Vector DB (unstructured text) | Vector DB + SQL DB + APIs + Web Search |
| **Refusal** | Rarely refuses — often hallucinates | Returns "insufficient evidence" when it can't find an answer |

### Agentic RAG uses a Supervisor Agent:

```text
User Question
      |
      v
Supervisor Agent (Router)
      |
     / \
    /   \
   v     v
Document   SQL Query
Query      Agent
Agent      (structured data)
(PDFs)        |
   |          v
   v      "Top 3 sales agents 
"Page 5   for Product X"
says..."      |
   \         /
    \       /
     v     v
Supervisor synthesizes
final answer with citations
```

> [!TIP]
> Think of Standard RAG as a student who looks at one textbook. Agentic RAG is like a research assistant who checks textbooks, databases, AND the internet — and tells you "I couldn't find enough evidence" when the data isn't there.

---

## 🎭 Dialogue: Why RAG Matters

**Alex:** So before RAG, the AI would just... make things up?

**Jeevi:** Exactly! If you asked it "What does our company policy say about vacation days?" it would generate a perfectly written paragraph — but the content would be completely invented. This is called **hallucination**.

**Alex:** And RAG fixes this by actually looking at the policy document first?

**Jeevi:** Yes! RAG forces the AI to "do its homework" before answering. It searches your actual documents, pulls out the relevant paragraphs, and uses them as evidence. If it can't find anything relevant, a good Agentic RAG system will say "I don't have enough evidence to answer this."

**Alex:** That's way more trustworthy than a system that always gives confident-sounding answers.

**Jeevi:** Exactly. That's why citations matter — they let the human verify every claim. We'll build all of this in the next few practicals.

---

## 💡 Key Takeaways

- LLMs hallucinate when asked about data they haven't seen.
- RAG solves this by retrieving real documents and using them as evidence.
- **Standard RAG** is a simple pipeline (retrieve → generate).
- **Agentic RAG** adds quality grading, retry logic, multi-source routing, and refusal when evidence is weak.

## Checklist

- [ ] You understand why an LLM hallucinates when asked about private documents.
- [ ] You can explain the 7 steps of the RAG pipeline (Ingest → Embed → Store → Query → Retrieve → Augment → Generate).
- [ ] You understand the difference between Standard RAG and Agentic RAG.
