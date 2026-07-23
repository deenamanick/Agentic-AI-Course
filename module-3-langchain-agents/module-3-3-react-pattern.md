# Practical 3.3 — The ReAct Pattern: Think → Act → Observe 🔄

## Why, in simple terms

When you ask an agent a question, it doesn't just blurt out an answer. It follows a pattern called **ReAct** (Reasoning + Acting):

1. **Think** 🧠 — "What do I need to do? Do I need a tool?"
2. **Act** 🛠️ — Call the tool (e.g., the calculator)
3. **Observe** 👀 — Read the tool's result
4. **Repeat or Answer** — If more work is needed, go back to step 1. Otherwise, give the final answer.

---

## 🎭 Human Roleplay: Act Out the ReAct Loop

### Scenario 1: Math Question

**User asks:** "What is (125 × 8) minus 17?"

| Step | Who | What They Do |
|---|---|---|
| **Think** | 🧠 Agent Brain | "This is math. I should use the calculator tool." |
| **Act** | 🧠 → 🧮 Calculator | Sends: `(125 * 8) - 17` |
| **Observe** | 🧮 → 🧠 | Returns: `983` |
| **Answer** | 🧠 → 👤 User | "The answer is 983." |

### Scenario 2: No Tool Needed

**User asks:** "What is Python used for?"

| Step | Who | What They Do |
|---|---|---|
| **Think** | 🧠 Agent Brain | "This is a general knowledge question. I don't need any tool." |
| **Answer** | 🧠 → 👤 User | "Python is used for web development, data science, AI, and automation." |

### Scenario 3: Multiple Tools Needed

**User asks:** "What's the current time, and what's 2 raised to the power of that hour?"

| Step | Who | What They Do |
|---|---|---|
| **Think** | 🧠 Agent Brain | "I need the current time first." |
| **Act** | 🧠 → ⏰ now_unix | Calls `now_unix()` |
| **Observe** | ⏰ → 🧠 | Returns: `1753257600` (which is ~14:00) |
| **Think** | 🧠 Agent Brain | "Now I need to calculate 2^14." |
| **Act** | 🧠 → 🧮 Calculator | Sends: `2 ** 14` |
| **Observe** | 🧮 → 🧠 | Returns: `16384` |
| **Answer** | 🧠 → 👤 User | "The current hour is 14, and 2^14 = 16,384." |

**💡 Notice:** The agent went through the loop TWICE — once for time, once for math. This is the power of the ReAct pattern.

---

## 🛡️ Why We Need a Maximum Iteration Limit

What happens if the agent gets confused and keeps calling tools in a loop?

```text
Think: "I need the calculator"
Act: calculator("hello")  → error
Think: "Let me try again"
Act: calculator("hello")  → error
Think: "Let me try again"
Act: calculator("hello")  → error
... forever!
```

This would burn through your API tokens and never give an answer! That's why we set:

```python
max_iterations = 6  # Stop after 6 think-act-observe cycles
```

In our code (`app/main.py`), you'll see this configured as `AGENT_MAX_ITERATIONS` in the `.env` file.

---

## 🔗 ReAct in Code (Preview)

Here's how the ReAct loop looks in our LangGraph code:

```python
# The agent graph follows the ReAct pattern:
#
# START → agent_node (Think: should I use a tool?)
#           ↓
#     ┌─── YES ───┐        ┌─── NO ───┐
#     ↓            ↓        ↓           ↓
# tool_node     (loop)   END (return final answer)
#     ↓
# agent_node (Observe result, Think again)
```

Don't worry about the code details yet — we'll build this in Practical 3.4. For now, just understand the **pattern**.

---

## 🆚 ReAct vs Module 2's One-Shot Approach

| Feature | Module 2 (One-Shot) | Module 3 (ReAct) |
|---|---|---|
| Steps | 1 (question → answer) | 1–6 (think → act → observe → repeat) |
| Tools | None | Calculator, timestamp, echo, etc. |
| Decision-making | None — AI just answers | AI decides which tools to use |
| Accuracy for math | Guesses (might be wrong) | Uses calculator (always correct) |
| Cost | Lower (1 API call) | Higher (multiple API calls per loop) |
| Speed | Faster | Slower (multiple round trips) |

> [!IMPORTANT]
> **Agents aren't always better than chatbots!** For simple questions ("What is Python?"), a one-shot answer is faster, cheaper, and just as good. Use agents only when the task genuinely needs tools or multi-step reasoning.

---

## Quick Practice Tasks

1. Act out the ReAct loop with a classmate for: "How many seconds are in 3.5 hours?"
2. Identify which tools are needed for: "Search the web for today's Bitcoin price and convert it to INR."
3. Think about: What happens if a tool returns an error? Should the agent retry or give up?

## Success checklist

- [ ] I can explain the ReAct pattern (Think → Act → Observe → Answer).
- [ ] I can trace through a multi-tool scenario step by step.
- [ ] I understand why a maximum iteration limit is necessary.
- [ ] I know when to use an agent vs a simple chatbot.
