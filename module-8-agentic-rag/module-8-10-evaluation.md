# Module 8.10: RAG Evaluation 📊

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Good vs Bad Retrieval** - The simplest way to evaluate RAG.
> 2. **Phase 2: Industry Metrics** - The terms engineers use in production.

---

### Step 1 — Good vs Bad Retrieval

When you build a RAG system, how do you know if it's actually working?

You ask a simple question:
> **Did we retrieve the correct paragraph?**
> - **YES** → Good retrieval. The AI will probably answer correctly.
> - **NO** → Bad retrieval. The AI will hallucinate.

Many developers waste time tweaking the LLM's prompt when the AI gives a bad answer. But 90% of the time, the problem isn't the LLM — the problem is that the Vector Database retrieved the wrong paragraph!

**Retrieval quality determines RAG quality.**

### Step 2 — Production Retrieval Metrics

Once you move past "Good vs Bad", production engineers use four specific metrics to evaluate their Vector Databases. 

You don't need to know the math behind these, but you should understand what they mean when you hear them in a meeting:

| Metric | What it means in plain English |
| :--- | :--- |
| **Precision** | How many of the retrieved chunks were actually relevant? (Did we bring back a bunch of garbage?) |
| **Recall** | Did we miss any relevant chunks? (Are there important paragraphs we failed to retrieve?) |
| **MRR** (Mean Reciprocal Rank) | How quickly did we find the first correct chunk? (Was the right answer rank #1, or did we have to scroll down to rank #5?) |
| **NDCG** | Were the *most* relevant chunks ranked near the top, and the *less* relevant ones near the bottom? |

---

## 💡 Key Takeaways

- If your RAG system gives a bad answer, check the retrieval first! Bad retrieval guarantees a bad answer.
- **Precision** measures if you brought back garbage.
- **Recall** measures if you missed something important.
- **MRR** and **NDCG** measure if the best results were at the very top of the list.

## Checklist

- [ ] You understand that retrieval quality is the biggest bottleneck in RAG.
- [ ] You can explain the difference between Precision and Recall in simple terms.
- [ ] You recognize the acronyms MRR and NDCG as ranking metrics.
