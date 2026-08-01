# Module 8.2: What is Chunking? 🍞

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: The Bread Analogy** - Understand why we split documents.
> 2. **Phase 2: Visual Studio Code Practice** - See how chunks are represented in our code.

---

### Step 1 — The Loaf of Bread Analogy

Suppose your PDF has **300 pages**.

Can we search all 300 pages every single time someone asks a question?
**No. It's too slow and too big.**

Instead, we cut the document into **small pieces**.

> Think of a 300-page PDF like a giant loaf of bread. You can't eat it all in one bite. You have to slice it into smaller pieces.

Each slice is called a **chunk**.

When a user asks a question, we don't give the AI the whole loaf of bread. We search through the slices, find the 2 or 3 slices that actually talk about the user's question, and give ONLY those slices to the AI.

### Step 2 — Fixed-Size Chunking (The Easiest Way)

How big should a chunk be? 
The simplest method is **Fixed-Size Chunking**. 

You tell the computer: *"Cut a slice every 500 words."*

Most chunks in the real world are around 300 to 600 words (or "tokens"). This is big enough to contain a full thought (like a paragraph), but small enough to search quickly.

---

## 🌊 Visual Studio Code Practice

> **👨‍💻 Code Mapping:** Open `app/main.py` and look at **Line 17** again. 

```python
knowledge_base = [
    "Vacation Policy: Employees get 20 days of paid time off per year.",
    "Work Hours: Standard hours are 9:00 AM to 5:00 PM, Monday to Friday.",
    # ...
]
```

In our code, **each string in that list represents one chunk!** 

Instead of writing complex code to slice a giant document, we have provided you with pre-sliced chunks. 

When a user asks a question, our system will search through these 5 chunks to find the right one.

---

## 💡 Key Takeaways

- You cannot search a massive document all at once efficiently.
- You must slice the document into smaller pieces called **chunks**.
- When the AI answers, we only provide the 2 or 3 most relevant chunks.

## Checklist

- [ ] You can explain what chunking is using the loaf of bread analogy.
- [ ] You understand that each string in our `knowledge_base` represents a single chunk.
