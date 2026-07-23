# Practical 2.4 — Break a Large Task into Small Prompts (How to Eat an Elephant 🐘)

## Why, in simple terms

If you ask the AI to "build a whole Amazon clone" in one go, it will get confused, skip parts, and make mistakes. **Chunking** is the art of breaking a big project into tiny, bite-sized tasks. It's how you "eat an elephant" — **one bite at a time**.

---

## 🍴 The 3-Bite Rule

Instead of:

```text
❌ "Build my complete AI customer support application."
```

Do this instead:

```text
🍴 Bite 1: "Define the user and what they need."
   ✅ Check: Can I explain it to a friend?

🍴 Bite 2: "Design the API request and response JSON."
   ✅ Check: Does the JSON shape look right on paper?

🍴 Bite 3: "Build the POST /chat endpoint."
   ✅ Check: Does curl return a response?

🍴 Bite 4: "Connect the React UI to the endpoint."
   ✅ Check: Does the answer appear on screen?

🍴 Bite 5: "Test loading, success, and failure states."
   ✅ Check: What happens when the API is down?

🍴 Bite 6: "Add error messages and retry logic."
   ✅ Check: Is the error message helpful to a human?
```

**💡 Why this works:** By testing after every single bite, you know **exactly** when a bug was introduced. If you do everything at once and something breaks, you have no idea where the problem is!

---

## 🎭 Role Activity (Classroom Exercise)

Give each learner one role. Each person writes **only their small output**:

| Role | Their "Bite" | Done When |
|---|---|---|
| 🎯 Project Manager | Define the outcome | One primary user and problem are written |
| 🎨 UX Designer | Define the user flow | Screen flow is drawn on paper |
| 💻 Developer | Define the API contract | Request and response JSON are agreed |
| ⚙️ DevOps Engineer | Define how services run | Ports, commands, and .env are documented |
| 🧪 Tester | Define acceptance checks | Pass/fail criteria exist for each feature |

Now combine their small outputs into one plan. Notice how **five small pieces** became a complete project plan — without anyone being overwhelmed!

---

## 💬 Chat Practice: The Incremental Build

### 🍴 Bite 1: Just the Plan
Ask the AI:
```text
"I want to build an AI tutor that helps students learn Python.
Don't write any code yet. Just give me a plan with 5 steps."
```
*(Wait. Read the plan. Is it reasonable?)*

### 🍴 Bite 2: One Endpoint Only
Ask the AI:
```text
"Great plan. Now implement Step 1 ONLY: Build a POST /ask endpoint
that accepts a question and returns a hardcoded answer.
Stop after this step."
```
*(Wait. Run it. Does curl work?)*

### 🍴 Bite 3: Connect to AI
Ask the AI:
```text
"Step 1 works. Now implement Step 2: Replace the hardcoded answer
with a call to Groq using LangChain. Keep everything else the same."
```
*(Wait. Run it. Does the AI answer?)*

> [!TIP]
> Always say **"Stop after this step"** or **"Implement Step X ONLY."** Otherwise, the AI will try to do everything at once and will likely break things.

---

## 🔗 How This Connects to Our Code

Look at our `app/main.py` — it was built using chunking! Notice how the code is organized into independent sections:

```python
# ─── PROMPT VERSIONS ─────────
# Bite 1: Define the system prompts

# ─── REQUEST & RESPONSE SHAPES ─────────
# Bite 2: Define the data contracts

# ─── MODEL PROVIDER SELECTION ─────────
# Bite 3: Build the AI connection

# ─── ENDPOINT 1: Normal Chat ─────────
# Bite 4: Handle text responses

# ─── ENDPOINT 2: Structured Chat ─────────
# Bite 5: Handle JSON responses
```

Each section is an independent "bite" that was built and tested separately.

---

## Practice Levels

### Understand
Arrange prepared project-step cards in a sensible order.

### Practice
Break "build an AI tutor" into no more than six chunks, each with a "Done when" check.

### Challenge
Identify which chunks can happen in parallel and which depend on earlier work.

---

## 🎨 Lovable Prompt

```text
Build a "Task Chunking Board" for beginners using React and Tailwind CSS.

Requirements:
- A field for one large goal.
- A button labeled "Break into Small Steps".
- Six editable step cards: Understand, Plan, Build, Connect, Test, Explain.
- Each card has Owner, Done When, and Notes fields.
- Add role filters for PM, UX, Developer, DevOps, Tester, and Learner.
- Show a progress bar.
- Use a friendly kanban-style classroom layout.
- Frontend only with mock AI-generated steps.
```

---

## Common Problem

**The AI writes code for every step at once.**

Ask only for a plan first. Then explicitly say: *"Implement Step 1 only and stop for review."*

## Success checklist

- [ ] I can divide a large task into reviewable steps.
- [ ] Each step has a visible "Done when" outcome.
- [ ] I check one step before starting the next.
- [ ] I can explain how different roles contribute to the plan.
