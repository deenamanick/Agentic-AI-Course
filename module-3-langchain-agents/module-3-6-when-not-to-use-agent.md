# Practical 3.6 — When NOT to Use an Agent ⚠️

## Why, in simple terms

Agents are powerful, but they're not always the right tool. Using an agent when a simple chatbot would do is like hiring a full construction crew to hang a picture frame.

---

## 📊 The Cost of Being "Agentic"

Every time the agent goes through a Think → Act → Observe cycle, it makes an API call to the LLM. Let's compare:

| Approach | API Calls | Cost | Speed | Best For |
|---|---|---|---|---|
| **Simple chatbot** (Module 2) | 1 | $ | Fast | General questions, explanations |
| **Agent with 1 tool call** | 2-3 | $$ | Medium | Math, time, simple lookups |
| **Agent with 3 tool calls** | 4-7 | $$$ | Slow | Multi-step tasks |
| **Multi-agent system** (Module 10) | 10-20+ | $$$$ | Slowest | Complex research, team tasks |

**💡 More agentic ≠ better. It means more expensive and slower.**

---

## 🚦 The Decision Flowchart

Ask yourself these questions before making something an agent:

```text
Does the user's question need a tool?
├── NO → Use a simple chatbot (Module 2's POST /chat)
│         Examples: "Explain Python", "Write a poem"
│
└── YES → Does it need MULTIPLE tools or steps?
    ├── NO → Use a single function call
    │         Examples: "What time is it?", "Calculate 17 × 23"
    │
    └── YES → Does it need AUTONOMOUS decision-making?
        ├── NO → Use a deterministic workflow (LangGraph with fixed steps)
        │         Examples: "Summarize this then translate to Spanish"
        │
        └── YES → Use a full agent with ReAct loop
                  Examples: "Research competitors and write a report"
```

---

## 🎭 Dialogue: The Overkill Problem

**Alex:** Let's make EVERYTHING an agent! Users can ask anything!

**Jeevi:** Hold on. Let me show you what happens:

**Scenario: User asks "What is Python?"**
- Chatbot: 1 API call → 200ms → $0.001 → ✅ Perfect answer
- Agent: Thinks "Do I need a tool? No." → Still 2+ API calls → 800ms → $0.003 → Same answer, 4× slower

**Alex:** Oh. So we're paying more for the same result?

**Jeevi:** Exactly. And worse — the agent might hallucinate a tool call that wasn't needed, adding delay and confusion. **Only use an agent when the task genuinely requires tools or multi-step reasoning.**

---

## ⚠️ Common Agent Failure Modes

| Failure | What Happens | How to Prevent |
|---|---|---|
| **Unnecessary tool use** | Agent calls calculator for "2+2" instead of just answering | Good system prompt: "Only use tools when necessary" |
| **Tool loops** | Agent keeps retrying a failing tool | Set `max_iterations` (we use 6) |
| **Wrong tool selection** | Agent uses calculator for a text question | Write clear tool docstrings |
| **Hallucinated tools** | Agent tries to call a tool that doesn't exist | LangGraph validates tool names |
| **Cost explosion** | Agent makes 20 API calls for a simple question | Set budget limits, monitor usage |

---

## 🔗 How This Connects to Our Code

In our `app/main.py`, look at how we configure the safety limit:

```python
# Maximum number of think-act-observe cycles before stopping
max_iterations = int(os.getenv("AGENT_MAX_ITERATIONS", "6"))
```

This means: if the agent hasn't found an answer after 6 loops, stop and return whatever it has. This prevents infinite loops and cost explosions.

---

## Quick Practice Tasks

1. For each question below, decide: **chatbot or agent?**
   - "Explain what an API is" → ?
   - "What's 17 × 23 + 5?" → ?
   - "What's the current time?" → ?
   - "Write a haiku about coding" → ?
   - "Search the web for today's top news and summarize them" → ?

2. Calculate the cost: If each API call costs $0.002 and your agent averages 4 calls per request, how much would 1,000 user requests cost?

---

## 💡 Key Takeaways

- **Not every AI application needs to be an agent.** Simple questions → chatbot. Tool-dependent questions → agent.
- **Agents cost more and are slower** because of the multi-step reasoning loop.
- **Always set guardrails:** max iterations, cost budgets, and timeout limits.
- **The best architecture is the simplest one that solves the problem.**

## Success checklist

- [ ] I can decide when to use a chatbot vs an agent.
- [ ] I know the cost and speed tradeoffs of agents.
- [ ] I can list 3 common agent failure modes and their prevention.
- [ ] I understand why `max_iterations` is a critical safety setting.
