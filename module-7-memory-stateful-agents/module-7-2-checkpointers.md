# Practical 7.2 — LangGraph Checkpointers 💾

## Why, in simple terms

We have a `thread_id`. Now we need the physical "database" to store the memories in!

In LangGraph, databases that store state are called **Checkpointers**. 
LangGraph comes with several built-in checkpointers:
1. `MemorySaver`: Stores data in your computer's RAM. Extremely fast, requires zero setup, but deletes all memories when you restart your server. Perfect for learning!
2. `SqliteSaver` / `PostgresSaver`: Stores data in a real SQL database. Keeps memories forever, even if the server crashes. Used for Production.

For this module, we will use `MemorySaver` to keep things simple.

---

## 🛠️ Adding Memory to the Agent

In `app/main.py`, adding memory to our agent takes exactly two lines of code!

```python
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

# 1. Create the database (in RAM)
memory_saver = MemorySaver()

# 2. Pass it to the agent!
agent = create_react_agent(
    model=llm, 
    checkpointer=memory_saver  # <-- This is the magic!
)
```

## 🔄 Using the Checkpointer

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

## Success checklist

- [ ] I understand what a checkpointer is.
- [ ] I can see how `MemorySaver` is passed to the agent.
- [ ] I understand how the `config` dictionary tells the checkpointer which memory to load.
