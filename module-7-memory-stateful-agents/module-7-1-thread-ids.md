# Module 7.1: Thread IDs 🧵

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: The Problem** - Understand why we need to separate memories for different users.
> 2. **Phase 2: The Solution** - Learn what a Thread ID is and how it works.
> 3. **Phase 3: Visual Studio Code Practice** - See the code that adds `thread_id` to your API.

### Why (in simple terms)

If the backend API is going to save memories, it needs to know *who* it is talking to! 

If Alex says *"I am stressed"*, and then Sarah connects to the API and says *"Hi"*, the AI shouldn't say *"Hi Sarah, are you still stressed?"*! 

To keep memories separated, we use **Thread IDs**.

### What you'll learn
1. **Thread IDs**: A unique string that labels each user's memory box.
2. **Memory Separation**: How LangGraph keeps conversations isolated.
3. **API Design**: How to require a `thread_id` in your request body.

---

## 🪡 What is a Thread ID?

A Thread ID is just a unique string of text (like `"user-alex-123"` or a random UUID). 

Every time the frontend makes a request to our API, it must include a `thread_id` in the JSON body. 

```json
{
  "user_query": "I am feeling stressed today.",
  "thread_id": "alex-session-1"
}
```

### How the locker room works (step by step):

| Step | What happens |
| :--- | :--- |
| 1 | Frontend sends a request with `thread_id: "alex-session-1"` |
| 2 | LangGraph looks in its database for the box labeled `"alex-session-1"` |
| 3 | Pulls out all the past memories and chat history from that box |
| 4 | Gives them to the AI along with the new message |
| 5 | The AI generates a response |
| 6 | LangGraph saves the new response back into the `"alex-session-1"` box |

If Sarah connects with `thread_id: "sarah-session-2"`, LangGraph opens a completely empty box.

---

## 🌊 Visual Studio Code Practice: Adding `thread_id` to your API

### Step 1: Update the Request Model

In `app/main.py`, notice how we updated our Pydantic `BaseModel` to require a `thread_id`:

```python
class AgentRequest(BaseModel):
    user_query: str
    thread_id: str = Field(..., description="Unique ID for the conversation thread.")
```

Now, the frontend (like our Lovable UI) is responsible for generating a random Thread ID and sending it with every single chat message.

---

## 🎭 Dialogue: The Locker Room Analogy

**Alex:** So the `thread_id` is like a locker number in a gym?

**Jeevi:** Exactly! Imagine the backend has a huge locker room. Each locker has a label — `"alex-session-1"`, `"sarah-session-2"`, etc. When you send a message, you hand the attendant your locker number. They open your locker, pull out all your old notes, show them to the AI, and then put the new note back in!

**Alex:** And if I forget my locker number and make a new one?

**Jeevi:** Then the attendant opens a completely empty locker. The AI has never seen you before! That's why the frontend must save the `thread_id` and reuse it every time.

---

## Quick Practice Tasks
- **Change the Thread ID:** Send two curl requests with different `thread_id` values and confirm the AI treats them as separate users.
- **Same Thread ID:** Send two curl requests with the same `thread_id` and confirm the AI remembers the first message.

---

## 💡 Key Takeaways

- A Thread ID is how the backend separates memories for different users or different conversations.
- The frontend must pass the same Thread ID in every request to resume an old conversation.
- If you pass a new Thread ID, the AI starts with a blank slate.

## Checklist

- [ ] You understand why we need a Thread ID.
- [ ] You understand that if you change the Thread ID, the AI will forget you.
- [ ] You can see where `thread_id` was added to the `AgentRequest` model in [main.py](file:///home/deena/Pictures/whizlabs/Agentic-AI-Course/module-7-memory-stateful-agents/app/main.py#L23-L25).
