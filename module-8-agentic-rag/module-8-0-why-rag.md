# Module 8.0: Why do we need RAG? 🔍

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: The Problem** - Understand the limits of ChatGPT.
> 2. **Phase 2: The Bad Solutions** - See why obvious fixes don't work.
> 3. **Phase 3: The Good Solution** - Learn what RAG is in plain English.

---

### Step 1 — The Problem

Imagine your company has:
- 500 PDFs
- 100 internal policies
- 200 technical documents

You ask ChatGPT:
> *"How many annual leaves do employees get?"*

Can ChatGPT answer?
**No.**

Because it has **never seen your company's documents**. Its knowledge stops at the date it was trained, and it doesn't have access to your private files. 

If you force it to answer, it will **hallucinate** (make up a confident-sounding answer that is completely wrong).

---

### Step 2 — The Bad Solutions

When people realize ChatGPT doesn't know their data, they try three obvious solutions.

**Option 1: Copy and paste the entire PDF into ChatGPT**
- ❌ **Doesn't scale.** A 200-page PDF is too big to fit in the chat box (the "context window").

**Option 2: Retrain GPT on your documents**
- ❌ **Too expensive.** Retraining a model takes days and costs thousands of dollars. And what happens when a policy changes tomorrow? You'd have to retrain it again!

**Option 3: Search for only the relevant pages, and give just those to ChatGPT**
- ✅ **This works.** This is the secret to building AI that knows your data.

---

### Step 3 — RAG in Plain English

Instead of giving the AI everything, we do this:

1. **User asks a question** ("How many vacation days do I get?")
2. **Search** your documents for the words "vacation" or "annual leave"
3. **Find** the 2 or 3 most useful paragraphs
4. **Give** only those paragraphs to the AI
5. **AI answers** the question using ONLY those paragraphs

This 5-step process has a fancy name in the AI industry.

> This process is called **Retrieval-Augmented Generation (RAG).**

### Breaking down the name:
- **Retrieval:** We search and *retrieve* the right paragraphs.
- **Augmented:** We *augment* (add to) the prompt with those paragraphs.
- **Generation:** The AI *generates* a helpful answer.

---

## 💡 Key Takeaways

- ChatGPT cannot answer questions about your private documents because it has never seen them.
- Copying the whole PDF is too big, and retraining the model is too expensive.
- **RAG (Retrieval-Augmented Generation)** is the industry-standard solution: you search for the relevant paragraphs and give them to the AI to read.

## Checklist

- [ ] You can explain why ChatGPT fails at answering company-specific questions.
- [ ] You understand why retraining a model isn't the right solution for document search.
- [ ] You can explain what RAG does in plain English.
