# Practical 7.3 — Testing the Mental Health Companion 🧘

## Why, in simple terms

Our API is ready. Let's test if the AI actually remembers us! We will send two `curl` requests. The first to state our mood, and the second to see if it remembers.

---

## 🏃 Running the API

1. Open a terminal in the `module-7-memory-stateful-agents` folder.
2. Make sure your `.env` has Groq configured.
3. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🧠 Test 1: Tell it a secret!

We will use the `thread_id` of `"test-user-1"`.

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Hi, I have a big exam tomorrow and I am feeling incredibly anxious. Can you just remember that I have an exam?",
    "thread_id": "test-user-1"
  }'
```

The AI will likely respond with some encouraging words. But did it actually save it to memory?

## 🧠 Test 2: Checking the Memory

Now, we send a completely new request. Notice we do not mention the exam! But we MUST use the same `thread_id`.

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Hi, I am back.",
    "thread_id": "test-user-1"
  }'
```

**Look at the response!** The AI should immediately say something like: *"Welcome back! Are you still feeling anxious about your exam tomorrow?"*

---

## 💥 Test 3: The Blank Slate

What happens if a different user connects? Change the `thread_id` to `"test-user-2"`.

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Hi, do you remember what I am stressed about?",
    "thread_id": "test-user-2"
  }'
```

The AI will say: *"No, I'm sorry, I don't know what you are stressed about. Please tell me!"*

Because you used a new `thread_id`, LangGraph opened an empty memory box.

*(Note: Because we are using `MemorySaver`, if you restart your `uvicorn` server, all memories will be wiped!)*

## Success checklist

- [ ] I sent the first curl command to state my mood.
- [ ] I sent the second curl command and verified the AI remembered my exam.
- [ ] I changed the `thread_id` and verified the AI treated me like a stranger.
