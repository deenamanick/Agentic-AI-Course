# Practical 2.5 — Refine Prompts and Check AI Mistakes (The Iterative Sculptor 🎨)

## Why, in simple terms

Your first prompt is rarely perfect. **Prompt Refinement** is like **sculpting with clay**. You start with a rough block (the first prompt), see what's missing, and then "shave off" the mistakes with a second and third prompt until it's exactly what you want.

---

## 🔄 The ACK-CRITIQUE-DIRECT Loop

When the AI gives you something that's "not quite right," **don't start over**. Use this 3-step technique:

### Step 1: ACKNOWLEDGE ✅
Tell the AI what it got RIGHT. This prevents it from throwing away the good parts.

### Step 2: CRITIQUE 🔍
Point out the SPECIFIC problem. Not "it's bad" — tell it exactly what's wrong.

### Step 3: DIRECT 🎯
Give the AI the exact change you want.

**Example:**

```text
❌ Bad refinement: "Make it better."

✅ Good refinement using ACK-CRITIQUE-DIRECT:

"ACKNOWLEDGE: The restaurant analogy is great and the length is good.
 CRITIQUE: But you used the word 'endpoint' without defining it first,
           and the third check question is too vague.
 DIRECT: Define 'endpoint' in the first sentence where you use it.
         Change the third question to: 'What happens when a customer
         orders something not on the menu?'"
```

---

## 🎭 Dialogue: The Sculpting Process

**Alex (PM):** The AI's explanation of FastAPI is okay, but it's too long and too technical.

**Jeevi:** Don't start over! Let's sculpt it. Watch:

*Round 1 — The Rough Block:*
```text
"Explain FastAPI for a beginner."
```
*[AI returns 3 paragraphs with code examples]*

**Jeevi:** ACK: The content is correct. CRITIQUE: Too long, has code. DIRECT: Keep the restaurant analogy, remove all code, max 100 words.

*Round 2 — First Refinement:*
*[AI returns a shorter, simpler version]*

**Jeevi:** ACK: Length is perfect! CRITIQUE: Still doesn't define "API." DIRECT: Add one sentence defining API in the first line.

*Round 3 — Final Polish:*
*[AI returns the perfect explanation]*

**Alex:** That took 3 tries, but each one got better!

**Jeevi:** Exactly. Three focused refinements beat starting from scratch every time.

---

## 🔍 The Ask → Inspect → Improve Loop

```text
 ┌──────────┐
 │   ASK    │ ── Give a clear first prompt
 └────┬─────┘
      │
 ┌────▼─────┐
 │ INSPECT  │ ── Check the result carefully
 └────┬─────┘
      │
 ┌────▼─────┐
 │ IMPROVE  │ ── Give specific ACK-CRITIQUE-DIRECT feedback
 └────┬─────┘
      │
      └──── Repeat until satisfied
```

### When Inspecting, Check:

- ✅ Did it answer the **real** question?
- ✅ Is any context missing?
- ✅ Are facts supported or invented?
- ✅ Did it make up a package, API, or result? (See Practical 2.1b)
- ✅ Is the explanation suitable for the learner's level?

---

## 🛡️ Safe Debugging Prompt

When your code has a bug, use this prompt instead of "fix it":

```text
Do not rewrite everything yet.

1. Explain the error in simple language.
2. Identify the most likely line.
3. Suggest the smallest change that fixes it.
4. Explain how to verify the fix worked.
5. State what information you're missing (if any).
```

**💡 Why this works:** It forces the AI to think step-by-step instead of randomly rewriting your entire file.

---

## 🚩 Three Red Flags (Quick Review from 2.1b)

1. A package or function cannot be found in official documentation.
2. The answer asks you to expose a secret (API key) in frontend code.
3. It claims an action succeeded without evidence.

---

## 📊 The Evidence Ladder

Use stronger checks for higher-risk claims:

1. Read the answer carefully.
2. Run the code or command.
3. Check the API response or test result.
4. Consult official documentation.
5. Ask a qualified human for high-impact decisions.

An AI answer is not evidence that an external action happened.

---

## 🔗 How This Connects to Our Code

In `app/main.py`, the structured endpoint is an example of us **refining** the AI's behavior:

```python
# We REFINE the prompt by adding strict output instructions
SystemMessage(
    content=(
        get_system_prompt(prompt_version)
        + " "
        + "Return ONLY valid JSON with keys: summary (string) and steps (array of strings)."
    )
)
```

This is the "DIRECT" step of ACK-CRITIQUE-DIRECT, but done in code. We're telling the AI exactly what format we want.

---

## Practice Levels

### Understand
Find two unclear claims in a prepared AI answer.

### Practice
Write one refinement prompt using the ACK-CRITIQUE-DIRECT technique.

### Challenge
Verify a technical claim against official documentation and record the link and date.

---

## 🎨 Lovable Prompt

```text
Build an "AI Answer Review Checklist" using React and Tailwind CSS.

Requirements:
- Large text area for an AI answer.
- Checklist sections: Relevance, Clarity, Evidence, Safety, and Testability.
- Red-flag buttons for Invented API, Exposed Secret, Unsupported Claim, and Too Complex.
- A feedback builder that creates an ACK-CRITIQUE-DIRECT prompt.
- Copy Feedback button.
- Use calm green, amber, and red status colors with accessible labels.
- Frontend only. Do not send the pasted answer anywhere.
```

---

## Common Problem

**The AI repeatedly rewrites everything.**

Request the smallest change and state which parts must remain unchanged. Use the ACK step to protect the good parts.

## Success checklist

- [ ] I treat the first answer as a draft, not a final truth.
- [ ] I can give specific refinement feedback using ACK-CRITIQUE-DIRECT.
- [ ] I know at least three AI red flags.
- [ ] I verify important claims with evidence or tests.
