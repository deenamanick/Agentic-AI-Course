# Module 8.2: Retrieve and Rerank Evidence 🔎

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Understand the Goal** - Learn why vector similarity alone isn't enough.
> 2. **Phase 2: Visual Studio Code Practice** - Build a retrieval pipeline with reranking.
> 3. **Phase 3: The Brain** - Measure retrieval quality with labeled questions.

### Why (in simple terms)

Your documents are chunked and stored. Now when a user asks a question, you need to **find the right chunks**. But vector similarity search (finding the closest embeddings) can sometimes return chunks that *sound* similar but aren't actually relevant.

To fix this, we add a **reranking** step that re-scores the results and puts the best evidence on top.

### What you'll learn
1. **Dense Retrieval**: How vector similarity search works.
2. **Keyword Retrieval**: When exact word matching beats semantic search.
3. **Reranking**: How to re-score results to improve quality.
4. **Evaluation**: How to measure if your retrieval is actually working.

---

## 🔍 Retrieval Strategies

| Strategy | How it works | Best for | Weakness |
| :--- | :--- | :--- | :--- |
| **Dense (Semantic)** | Converts query to embedding, finds closest chunks | Questions with meaning but different words (e.g., "vacation days" finds "PTO policy") | Can return plausible but wrong chunks |
| **Sparse (Keyword)** | Exact word matching (like a search engine) | Finding exact terms, names, codes (e.g., "Policy HR-2024-05") | Misses synonyms and paraphrases |
| **Hybrid** | Combines dense + sparse and merges results | Best of both worlds | More complex to implement |

---

## 🏆 What is Reranking?

After retrieval returns, say, 10 results, a **reranker** re-scores them based on how well each chunk actually answers the question.

### Before vs After Reranking:

| Rank | Before Reranking | After Reranking |
| :--- | :--- | :--- |
| 1 | ❌ A chunk about "office hours" (similar words, wrong topic) | ✅ The exact paragraph about "vacation policy" |
| 2 | ✅ The actual vacation policy paragraph | ❌ A chunk about "office hours" |
| 3 | ❌ A chunk about "company culture" | ❌ A chunk about "company culture" |

Without reranking, the AI might use the wrong chunk (rank 1) and give an incorrect answer!

---

## 🌊 Visual Studio Code Practice: Building the Retrieval Pipeline

### Step 1: Create labeled test questions

Create at least 20 questions where you know the correct answer and which document/page it comes from:

| Question | Expected source | Expected page |
| :--- | :--- | :--- |
| "What is the vacation policy?" | HR Policy Manual | Page 5 |
| "Who approved the Q3 budget?" | Board Minutes | Page 12 |
| "What's the refund deadline?" | Terms of Service | Page 3 |

### Step 2: Measure retrieval quality

For each question, check if the correct chunk appears in the results:

| Metric | What it measures | How to calculate |
| :--- | :--- | :--- |
| **Top-1 Accuracy** | Is the correct chunk the #1 result? | Correct at rank 1 ÷ total questions |
| **Top-3 Accuracy** | Is the correct chunk in the top 3? | Correct in top 3 ÷ total questions |
| **Top-5 Accuracy** | Is the correct chunk in the top 5? | Correct in top 5 ÷ total questions |

### Step 3: Compare before and after reranking

Run the same 20 questions before and after reranking. You should see Top-1 accuracy improve significantly.

---

## 🎭 Dialogue: Why Reranking Matters

**Alex:** If vector search already finds similar chunks, why do we need reranking?

**Jeevi:** Because "similar" doesn't always mean "relevant"! Imagine you ask "What is the vacation policy?" Vector search might return a chunk about "office hours" because both are about workplace rules — similar topic, but wrong answer. The reranker is smarter — it actually reads the chunk and the question together and asks: "Does this chunk ANSWER this question?"

**Alex:** So it's like a quality check?

**Jeevi:** Exactly! Think of it like this: vector search is the librarian who brings you 10 books on the right shelf. The reranker is the expert who opens each book and says "This one actually answers your question. These others are just nearby."

---

## Quick Practice Tasks
- **20 questions**: Create 20 labeled questions with known answers and source pages.
- **Compare strategies**: Try dense-only, sparse-only, and hybrid retrieval on the same questions.
- **Measure reranking**: Compare Top-1, Top-3, Top-5 accuracy before and after reranking.

---

## 💡 Key Takeaways

- Vector similarity alone can return plausible but weak evidence.
- Reranking re-scores results to put the best evidence first.
- Always evaluate retrieval separately from generation.
- Metadata filters prevent exposing another user's documents.

## Checklist

- [ ] You understand the difference between dense, sparse, and hybrid retrieval.
- [ ] You created at least 20 labeled test questions.
- [ ] Retrieval is evaluated separately from generation.
- [ ] Filters cannot expose another user's documents.
- [ ] Reranking improvement is measured (before vs after).
- [ ] Scores and source metadata are traceable.
