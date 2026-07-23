# Practical 2.1 — Meet the LLM Through Roleplay

## Why, in simple terms

An LLM predicts a useful continuation from the instructions and text it receives. It does not automatically know your private goal, current company data, or whether its answer is true.

## 🎭 Classroom Dialogue: "Can AI Tell Me Tomorrow's Weather?"

**Alex (Product Manager):** Jeevi, can AI tell me tomorrow's weather?

**Jeevi (Developer):** It *sounds* like it can. Let me show you...

*[Jeevi asks the AI: "What will the weather be in Chennai tomorrow?"]*

*[The AI confidently responds with a detailed forecast.]*

**Alex:** See! It works!

**Jeevi:** Wait — look at the date. That forecast is from its training data. It's giving you *yesterday's* weather and presenting it as tomorrow's!

**Alex:** But it sounded so confident!

**Jeevi:** Exactly! That's called a **hallucination**. The AI is a brilliant writer, but it doesn't have live data. It's like a brilliant librarian who hasn't left the library in 2 years — they know a LOT, but they can't tell you today's stock price.

**Alex:** So how do we fix that?

**Jeevi:** That's exactly why we build **Agents** — we give the librarian a phone so they can call for current information! In this course, we'll learn to give AI access to **tools** like weather APIs, databases, and web search.

---

## 🧩 Human Prediction Game

Ask learners to complete these sentences:

- "Twinkle, twinkle, little…" → Easy! The AI has seen this thousands of times.
- "The capital of France is…" → Easy! General knowledge from training data.
- "For this customer, the correct refund is…" → ❌ The AI has NO idea! It doesn't have your company's policy or customer details.

**💡 Key Insight:** The first two have familiar patterns. The third lacks company policy and customer details. This demonstrates why **context** matters.

---

## LLM, RAG, and Agent — The Three Levels

| Concept | Everyday Comparison | What it Can Do |
|---|---|---|
| **LLM** | A brilliant librarian answering from memory | Answer general questions, write text |
| **RAG** | The librarian first opens the correct reference book | Answer questions about YOUR specific data |
| **Agent** | The librarian decides which book or tool to use and performs steps | Take actions, call APIs, search the web |

---

## 🎭 Roleplay Activity (3 Learners)

Use three learners and act this out:

1. **User:** "What's the weather tomorrow in Chennai?"
2. **LLM (Learner 2):** Can ONLY answer from memory. Must admit: *"I don't have live data, but historically Chennai is warm in July."*
3. **Agent (Learner 3):** Says: *"Let me check..."* → pretends to call a weather API → returns: *"Tomorrow in Chennai: 34°C, partly cloudy."*

**Discussion:** Why did the Agent give a better answer? Because it had a **tool** (the weather API). The LLM had to guess.

---

## 💬 Chat Practice (Try This Now!)

Ask the AI these three questions and label each answer:

| # | Question | Expected Label |
|---|---|---|
| 1 | "What is Python used for?" | ✅ Answerable from general knowledge |
| 2 | "What is the current price of Bitcoin?" | ⚠️ Needs a tool or retrieval |
| 3 | "Should I approve John's leave request?" | ❌ Needs clarifying context |

---

## ⚠️ What an LLM is NOT

An LLM is NOT automatically:

- ❌ A database containing your company's private records
- ❌ A search engine with guaranteed current information
- ❌ A calculator that should be trusted without double-checking
- ❌ An autonomous agent with permission to take actions
- ❌ A human who understands unstated intentions

> [!WARNING]
> **"The answer sounds professional, so it must be correct."** — This is the #1 beginner mistake! Fluent language is a model capability. Accuracy must still be checked using sources, tools, tests, or human review.

---

## Different Learner Viewpoints

- **Project manager:** What requirement is missing from the question?
- **UX designer:** What clarification would reduce user frustration?
- **DevOps engineer:** Which external service would provide current data?
- **Homemaker:** Which ingredient or instruction is missing from the recipe?
- **Developer:** Does this need context, retrieval, or a tool call?

---

## 💡 Key Takeaways

- **LLMs are pattern completers** — they predict the next best word, not the truth.
- **Confidence ≠ Correctness** — an AI can sound 100% sure and still be wrong.
- **Context is everything** — the more specific your instructions, the better the answer.
- **Agents extend LLMs** — by giving them tools (APIs, databases, search), they become much more powerful.

## Success checklist

- [ ] I can explain LLM, RAG, and agent in my own words.
- [ ] I know an LLM can sound confident and still be wrong (hallucination).
- [ ] I can identify when context, a tool, or clarification is needed.
- [ ] I can name one thing an LLM cannot safely do by itself.
