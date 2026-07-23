# Practical 7.1 — Thread IDs 🧵

## Why, in simple terms

If the backend API is going to save memories, it needs to know *who* it is talking to! 

If Alex says *"I am stressed"*, and then Sarah connects to the API and says *"Hi"*, the AI shouldn't say *"Hi Sarah, are you still stressed?"*! 

To keep memories separated, we use **Thread IDs**.

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

When LangGraph receives this request, it:
1. Looks in its database for the box labeled `"alex-session-1"`.
2. Pulls out all the past memories and chat history from that box.
3. Gives it to the AI.
4. The AI generates a new response.
5. LangGraph saves the new response back into the `"alex-session-1"` box!

If Sarah connects with `thread_id: "sarah-session-2"`, LangGraph opens a completely empty box.

---

## 🛠️ Updating our API Request

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

## 💡 Key Takeaways

- A Thread ID is how the backend separates memories for different users or different conversations.
- The frontend must pass the same Thread ID in every request to resume an old conversation.
- If you pass a new Thread ID, the AI starts with a blank slate.

## Success checklist

- [ ] I understand why we need a Thread ID.
- [ ] I understand that if I change the Thread ID, the AI will forget me.
- [ ] I can see where `thread_id` was added to the `AgentRequest` model.
