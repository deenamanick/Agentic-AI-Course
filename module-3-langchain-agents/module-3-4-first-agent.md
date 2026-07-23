# Practical 3.4 — Build Your First Tool-Using Agent (with LangGraph) 🚀

## Why, in simple terms

This is where everything comes together! We'll build a real agent that can:
- Read a user's question
- **Decide** if it needs a tool
- **Call** the tool
- **Return** the final answer

We're using **LangGraph** (not the older, deprecated `AgentExecutor`). LangGraph is the industry standard for building production agents in 2025/2026.

---

## 🏗️ What is LangGraph?

LangGraph lets you build agents as **graphs** — a series of connected steps (nodes) with clear paths between them (edges).

```text
        START
          │
    ┌─────▼─────┐
    │ agent_node │ ← The brain: reads the question, decides what to do
    └─────┬─────┘
          │
    Should I use ──── NO ──── END (return final answer)
    a tool?
          │
         YES
          │
    ┌─────▼─────┐
    │ tool_node  │ ← Calls the tool (calculator, timestamp, etc.)
    └─────┬─────┘
          │
    ┌─────▼─────┐
    │ agent_node │ ← Reads the tool result, decides: more tools or answer?
    └─────┬─────┘
          │
         ...repeat until done
```

**💡 Why LangGraph instead of AgentExecutor?**
- `AgentExecutor` (the old way) is officially **deprecated** by the LangChain team
- LangGraph gives you **clear, visual control** over each step
- It's what real companies use in production

---

## 🔗 The Complete Code (Walkthrough)

### Step 1: Imports and Setup

```python
from langgraph.prebuilt import create_react_agent  # LangGraph's ReAct agent
from langchain_core.tools import tool               # Tool decorator
from langchain_groq import ChatGroq                  # Groq Cloud (default)
from langchain_ollama import ChatOllama              # Ollama (optional)
```

### Step 2: Define Your Tools

```python
@tool
def calculator(expression: str) -> str:
    """Evaluate a simple arithmetic expression, e.g. '(17 * 23) + 5'."""
    return _safe_eval_arithmetic(expression)

@tool
def now_unix() -> str:
    """Return the current Unix timestamp in seconds."""
    return str(int(time.time()))
```

### Step 3: Create the Agent Graph

```python
# This one line creates a complete ReAct agent with LangGraph!
agent = create_react_agent(
    model=llm,           # The AI brain (Groq or Ollama)
    tools=[calculator, now_unix, echo],  # The tools it can use
)
```

### Step 4: Run the Agent

```python
result = await agent.ainvoke(
    {"messages": [("user", req.user_query)]},
    config={...}  # Langfuse tracking
)
```

**That's it!** LangGraph handles the entire Think → Act → Observe loop for you.

---

## 🧪 Try It Yourself

### Start the server:

```bash
# Terminal 1: Start the API
uvicorn app.main:app --reload
```

### Test with math (should use calculator):

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"Compute (125 * 8) - 17."}'
```

Expected: The agent calls the calculator tool and returns `983`.

### Test with time (should use now_unix):

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is the current Unix timestamp?"}'
```

### Test without tools (should answer directly):

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is Python used for?"}'
```

Expected: The agent answers directly without calling any tool.

---

## 🎭 Dialogue: LangGraph vs the Old Way

**Alex:** I saw some tutorials using `AgentExecutor`. Is that different?

**Jeevi:** `AgentExecutor` is the **old** way of building agents in LangChain. It's been officially deprecated — meaning the LangChain team themselves say "don't use it anymore, use LangGraph instead."

**Alex:** Why did they change?

**Jeevi:** `AgentExecutor` was a black box — hard to debug, hard to customize, hard to add human approval steps. LangGraph makes every step visible as a **node in a graph**, so you can see exactly what's happening and control each step.

**Alex:** So we're learning the modern way?

**Jeevi:** Exactly. LangGraph is what companies like Uber, Elastic, and LinkedIn use in production.

---

## 🏋️ Student Exercise: Add a New Tool

Add a `word_count` tool:

```python
@tool
def word_count(text: str) -> str:
    """Count the number of words in the given text."""
    count = len(text.split())
    return f"{count} words"
```

1. Add it to the tools list in `build_agent()`
2. Restart the server
3. Test: `curl ... '{"user_query":"How many words are in: The quick brown fox jumps over the lazy dog"}'`
4. Check: Did the agent use the `word_count` tool?

## Success checklist

- [ ] I can run `POST /agent/chat` and get a response.
- [ ] The agent uses the calculator for math questions.
- [ ] The agent answers general questions without calling tools.
- [ ] I understand why we use LangGraph instead of the deprecated `AgentExecutor`.
- [ ] I can add a new tool to the agent.
