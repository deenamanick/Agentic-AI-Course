# Module 8.3: Build a Corrective RAG Graph 🔄

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Understand the Goal** - Learn why an agent should retry retrieval when evidence is weak.
> 2. **Phase 2: Visual Studio Code Practice** - Build a LangGraph flow with evidence grading and query rewriting.
> 3. **Phase 3: The Brain** - Understand stop conditions and why the agent must refuse when evidence is insufficient.

### Why (in simple terms)

In Module 8.2, you built a retrieval pipeline. But what happens when the first search returns weak or irrelevant chunks?

A **Standard RAG** system would just use the bad chunks and generate a hallucinated answer. A **Corrective RAG** system is smarter — it grades the evidence, and if it's not good enough, it rewrites the query and tries again. If it STILL can't find good evidence, it honestly says "I don't have enough information."

### What you'll learn
1. **Evidence Grading**: How the agent judges if retrieved chunks are good enough.
2. **Query Rewriting**: How the agent rephrases the question to improve results.
3. **Stop Conditions**: Why retry logic MUST be bounded (no infinite loops!).
4. **Honest Refusal**: Why returning "insufficient evidence" is better than hallucinating.

---

## 🔄 The Corrective RAG Flow

Here is the LangGraph flow you'll build:

```text
User Question
      |
      v
  [Route] → Decide which data source to search
      |
      v
  [Retrieve] → Search the Vector DB for relevant chunks
      |
      v
  [Grade Evidence] → Are the chunks good enough?
      |
     / \
    /   \
  Yes    No
   |      |
   v      v
[Answer]  [Rewrite Query] → Rephrase the question
  with        |
 citations    v
           [Retrieve Again] → Search one more time
                |
                v
           [Grade Again] → Still weak?
                |
               / \
              /   \
           Yes    No
            |      |
            v      v
         [Answer]  [Return "Insufficient Evidence"]
```

### How the nodes map to a table:

| Node | What it does | Example |
| :--- | :--- | :--- |
| **Route** | Decides which data source to search | "This is a policy question → search HR documents" |
| **Retrieve** | Searches the Vector DB | Returns top 5 chunks |
| **Grade Evidence** | Scores each chunk: relevant or not? | "3 out of 5 chunks are relevant → evidence is acceptable" |
| **Answer** | Generates a response using the relevant chunks | "According to page 5, the vacation policy is..." |
| **Rewrite Query** | Rephrases the question for better results | "vacation policy" → "PTO days allowed per year" |
| **Insufficient Evidence** | Honest refusal when evidence is still weak after retry | "I couldn't find enough evidence to answer this question." |

---

## 🚦 Stop Conditions (Critical!)

> [!CAUTION]
> You MUST limit retries. If the agent rewrites the query and retrieves forever, you'll waste API credits and time. Always set a maximum retry count!

| Rule | Why |
| :--- | :--- |
| **Maximum 1 rewrite** | Prevents infinite loops |
| **Structured grading** | Use a clear scoring system (e.g., "relevant" / "partially relevant" / "irrelevant") |
| **Honest refusal** | If evidence is still weak after 1 retry, return "insufficient evidence" — never hallucinate |

---

## 🎭 Dialogue: Why Refusal is a Feature

**Alex:** Isn't it bad if the agent says "I don't know"?

**Jeevi:** No! It's actually a **feature**, not a bug. Think about it — would you rather have an AI that confidently gives you a wrong answer about your company's legal policy, or one that honestly says "I couldn't find enough evidence in your documents"?

**Alex:** The honest one, obviously. Especially for legal or medical questions.

**Jeevi:** Exactly! In production systems, a confident wrong answer can cause lawsuits. An honest "I don't know" just means the human needs to look it up themselves. That's always safer.

---

## Quick Practice Tasks
- **Build the graph**: Implement the corrective RAG flow in LangGraph with route → retrieve → grade → answer/rewrite nodes.
- **Test with weak questions**: Ask questions that your documents DON'T cover. Verify the agent returns "insufficient evidence."
- **Test with strong questions**: Ask questions your documents DO cover. Verify the agent answers with citations.
- **Check stop conditions**: Verify the rewrite only happens once (no infinite loops).

---

## 💡 Key Takeaways

- An agent should retry retrieval only when the available evidence is insufficient.
- Use structured evidence grades (relevant / partially relevant / irrelevant).
- Limit rewriting to one attempt — no infinite loops!
- If evidence remains weak, return "insufficient evidence" — never hallucinate.
- Every node in the graph should be traced for debugging.

## Checklist

- [ ] Your graph has a visible stop condition (max 1 rewrite).
- [ ] Retrieval retries are bounded.
- [ ] Unsupported questions do NOT receive invented answers.
- [ ] The agent returns "insufficient evidence" when appropriate.
- [ ] Each node is traced for debugging.
