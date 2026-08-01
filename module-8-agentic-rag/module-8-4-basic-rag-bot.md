# Module 8.4: Building the Basic RAG Bot 🤖

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Semantic Search** - Learn how we match questions to chunks.
> 2. **Phase 2: Visual Studio Code Practice** - Test your basic RAG bot in the terminal!

---

### Step 1 — Semantic Search (Finding the best match)

When a user asks:
> *"How much PTO do I get?"*

Notice that the user said **"PTO"**. 
Our document says **"Vacation"**. 

If we used a standard keyword search (like `Ctrl+F`), it would fail because the exact word "PTO" isn't in the document.

But because we are using **Embeddings** (meaning), the computer knows that "PTO" and "Vacation" have coordinates that are very close to each other. 

It calculates the distance between the question's coordinates and every chunk's coordinates. The chunk with the closest distance is returned. This is called **Semantic Search**.

---

## 🌊 Visual Studio Code Practice

Let's test the retrieval logic!

> **👨‍💻 Code Mapping:** Open `app/main.py` and look at **Line 58**. 

Find the `retrieve_knowledge(query)` function. 
Notice how it:
1. Converts the user's query into an embedding.
2. Uses `cosine_similarity` to measure the distance between the query and all our chunks.
3. Sorts them to find the highest score (the closest match).

### Step 2 — Run the App!

Open a terminal in the `module-8-agentic-rag` folder. Ensure your virtual environment is active and you have installed `requirements.txt`.

Set your Groq key:
```bash
export GROQ_API_KEY=gsk_your_real_key_here
```

Start the API:
```bash
uvicorn app.main:app --reload
```

In a *second* terminal, let's ask a question using Semantic Search:
```bash
curl -X POST http://127.0.0.1:8000/agent/chat \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What should I wear to the office?"}'
```

**Look at the Uvicorn terminal logs!**
You should see:
```text
🔄 Generating embeddings for knowledge base using Groq...
✅ Generated 5 embeddings
-> RETRIEVE
🔍 Query: 'What should I wear to the office?' | Best match score: 0.742
-> GRADE EVIDENCE
   Evidence graded as: good (Score: 0.742)
-> GENERATE ANSWER
```

Notice the user asked "What should I wear?" and the bot successfully found the chunk about the "Dress Code" because the *meaning* was similar, even if the exact words didn't match!

---

## 💡 Key Takeaways

- Semantic Search finds documents based on *meaning*, not just exact keywords.
- Cosine Similarity is the math equation used to calculate how close two vectors (embeddings) are.
- Your bot is fully functional! It retrieved the right chunk, passed it to the LLM, and generated an answer.

## Checklist

- [ ] You understand why Semantic Search is better than Keyword Search for questions like "PTO vs Vacation".
- [ ] You ran `uvicorn app.main:app` and started the API.
- [ ] You successfully asked a question via `curl` and received an answer based on the knowledge base.
- [ ] You watched the logs and saw the "Best match score" printed out.
