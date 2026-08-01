# Module 7.3: Testing the Mental Health Companion 🧘

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: The Setup** - Start your backend API server.
> 2. **Phase 2: Visual Studio Code Practice** - Run 3 curl tests to prove the memory works.
> 3. **Phase 3: The Proof** - Verify the AI remembers you AND forgets strangers.

### Why (in simple terms)

Our API is ready. Let's test if the AI actually remembers us! We will send `curl` requests and check the responses.

### What you'll learn
1. **Memory Persistence**: Prove the AI remembers across separate requests.
2. **Memory Isolation**: Prove different Thread IDs get separate memories.
3. **The MemorySaver Limitation**: Understand what happens when you restart the server.

---

## 🌊 Visual Studio Code Practice: Running the Tests

### Step 1: Start the API

1. Open a terminal in the `module-7-memory-stateful-agents` folder.
2. Make sure your `.env` has Groq configured.
3. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

---

### Step 2: Test 1 — Tell it a secret! 🤫

We will use the `thread_id` of `"test-user-1"`.

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Hi, I have a big exam tomorrow and I am feeling incredibly anxious. Can you just remember that I have an exam?",
    "thread_id": "test-user-1"
  }'
```

**Expected:** The AI will respond with encouraging words. But did it actually save it to memory?

---

### Step 3: Test 2 — Check the Memory 🧠

Now, we send a completely new request. Notice we do **not** mention the exam! But we MUST use the same `thread_id`.

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Hi, I am back.",
    "thread_id": "test-user-1"
  }'
```

**Expected:** The AI should immediately say something like: *"Welcome back! Are you still feeling anxious about your exam tomorrow?"*

> [!TIP]
> If the AI mentions your exam without you asking — congratulations, the memory is working! 🎉

---

### Step 4: Test 3 — The Blank Slate 🆕

What happens if a **different** user connects? Change the `thread_id` to `"test-user-2"`.

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Hi, do you remember what I am stressed about?",
    "thread_id": "test-user-2"
  }'
```

**Expected:** The AI will say: *"No, I'm sorry, I don't know what you are stressed about. Please tell me!"*

Because you used a new `thread_id`, LangGraph opened an empty memory box.

---

## Summary of all 3 tests:

| Test | Thread ID | What you say | Expected AI response | What it proves |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `test-user-1` | "I have an exam tomorrow" | Encouraging words | AI receives the message |
| 2 | `test-user-1` | "Hi, I am back" | "How is your exam?" | ✅ Memory works |
| 3 | `test-user-2` | "Do you remember?" | "No, I don't know" | ✅ Memory isolation works |

> [!IMPORTANT]
> Because we are using `MemorySaver`, if you restart your `uvicorn` server, **all memories will be wiped!** This is expected — `MemorySaver` stores data in RAM only.

---

## 💡 Key Takeaways

- Sending two requests with the same `thread_id` proves memory works.
- Sending a request with a different `thread_id` proves memory isolation works.
- `MemorySaver` data is lost on server restart (this is by design for learning).

## Checklist

- [ ] You sent the first curl command and received a calming response.
- [ ] You sent the second curl command and verified the AI remembered your exam.
- [ ] You changed the `thread_id` and verified the AI treated you like a stranger.
