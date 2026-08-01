# Module 7.2: LangGraph Checkpointers 💾

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Understand the Goal** - Learn what a Checkpointer is and why we need one.
> 2. **Phase 2: Visual Studio Code Practice** - Add `MemorySaver` to your agent in just 2 lines.
> 3. **Phase 3: The Brain** - See how the `config` dictionary connects the Thread ID to the Checkpointer.

### Why (in simple terms)

We have a `thread_id`. Now we need the physical "database" to store the memories in!

In LangGraph, databases that store state are called **Checkpointers**. 

### What you'll learn
1. **Checkpointers**: The LangGraph concept for storing agent state.
2. **MemorySaver**: An in-memory checkpointer perfect for learning.
3. **The config dict**: How to connect Thread IDs to the checkpointer at runtime.

---

## 📦 Checkpointer Options

LangGraph comes with several built-in checkpointers:

| Checkpointer | Where it stores data | Survives restart? | Best for |
| :--- | :--- | :--- | :--- |
| `MemorySaver` | Your computer's RAM | ❌ No — data is lost | Learning & local testing |
| `SqliteSaver` | A SQLite file on disk | ✅ Yes | Small production apps |
| `PostgresSaver` | A PostgreSQL database | ✅ Yes | Large production apps |

For this module, we will use `MemorySaver` to keep things simple.

---

## 🌊 Visual Studio Code Practice: Adding Memory to the Agent

### Step 1: Create the Checkpointer

In `app/main.py`, adding memory to our agent takes exactly **two lines of code!**

```python
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

# LINE 1: Create the database (in RAM)
memory_saver = MemorySaver()

# LINE 2: Pass it to the agent!
agent = create_react_agent(
    model=llm, 
    checkpointer=memory_saver  # <-- This is the magic!
)
```

### Step 2: Use the Checkpointer in the API

When we call the agent via the API, we pass the `thread_id` inside a special `config` dictionary. 

LangGraph automatically intercepts this, looks inside `memory_saver` for that `thread_id`, loads the past messages, runs the LLM, and saves the new messages back to `memory_saver`!

```python
# The config dictionary tells LangGraph which memory box to open
config = {"configurable": {"thread_id": req.thread_id}}

# Run the agent! It will automatically load history and save new history.
result = await agent.ainvoke(
    {"messages": [HumanMessage(content=req.user_query)]},
    config=config
)
```

### How it all fits together:

| What | Where in the code | What it does |
| :--- | :--- | :--- |
| `MemorySaver()` | Top of `main.py` (line 43) | Creates the in-memory database |
| `checkpointer=memory_saver` | Inside `create_react_agent()` (line 53) | Tells the agent to use this database |
| `config = {"configurable": {"thread_id": ...}}` | Inside the `/agent/chat` endpoint (line 95-96) | Tells the agent which user's memory to load |

---

## 🎭 Dialogue: Is it really that easy?

**Alex:** Wait, that's it? I don't have to write code to append messages to a list? I don't have to write SQL queries to `INSERT INTO chat_history`?

**Jeevi:** Exactly! That is the primary reason developers use LangGraph. State management is incredibly tedious to write from scratch. LangGraph's checkpointers handle reading, appending, and writing state automatically just by passing `checkpointer=memory_saver`.

**Alex:** And if I want to deploy this to production, I just swap `MemorySaver()` for `PostgresSaver()`?

**Jeevi:** Yes! You change line 1 to connect to your PostgreSQL database, and LangGraph will automatically create the tables and save memories there instead. The rest of your code stays exactly the same.

---

## 💡 Key Takeaways

- LangGraph databases are called **Checkpointers**.
- `MemorySaver` is an in-memory checkpointer perfect for local testing.
- You must pass the `thread_id` inside a `config` dictionary when calling `.ainvoke()`.

## Checklist

- [ ] You understand what a Checkpointer is.
- [ ] You can see how `MemorySaver` is passed to the agent in [main.py](file:///home/deena/Pictures/whizlabs/Agentic-AI-Course/module-7-memory-stateful-agents/app/main.py#L43-L54).
- [ ] You understand how the `config` dictionary tells the checkpointer which memory to load.
