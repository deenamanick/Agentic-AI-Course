# Practical 3.7 — Test Your Agent 🧪

## Why, in simple terms

An agent makes autonomous decisions. That means more ways to fail! Testing agents is different from testing a simple chatbot because we need to verify:
- Did it choose the **right tool**?
- Did it pass the **correct arguments**?
- Did it handle **errors gracefully**?
- Did it stop after the **maximum iterations**?

---

## 🧪 The 5 Types of Agent Tests

### Test 1: Correct Tool Selection ✅

```bash
# Send a math question → agent should use the calculator
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is (125 * 8) - 17?"}'
```

**Check:** The response should contain `983` (the correct math answer, not a guess).

### Test 2: No Tool Needed ✅

```bash
# Send a general question → agent should answer WITHOUT calling tools
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is Python programming used for?"}'
```

**Check:** The response should be a general explanation. No tool was necessary.

### Test 3: Time Tool ⏰

```bash
# Send a time question → agent should use now_unix
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is the current Unix timestamp?"}'
```

**Check:** The response should contain a large number (current timestamp).

### Test 4: Invalid Input (Error Handling) ❌

```bash
# Send something the calculator can't handle
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"Calculate the square root of a banana."}'
```

**Check:** The agent should NOT crash. It should either explain it can't do that, or gracefully handle the error.

### Test 5: Empty Query (Validation) ❌

```bash
# Send an empty message
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":""}'
```

**Check:** FastAPI should reject this with a validation error (because of `min_length=1` on the Pydantic model).

---

## 🔍 How to Check What the Agent Did (Langfuse)

After each test, you can see the full agent reasoning in Langfuse:

1. Copy the `request_id` from the response
2. Go to your Langfuse dashboard
3. Search by the `request_id`
4. You'll see:
   - What the agent **thought**
   - Which tool it **called**
   - What the tool **returned**
   - The **final answer** it gave

This is like watching a slow-motion replay of the agent's brain!

---

## 🏋️ Student Exercise: Write Your Own Tests

Create a test file or extend the test script for these scenarios:

| # | Scenario | Expected Behavior |
|---|---|---|
| 1 | "What is 2 + 2?" | Uses calculator (or answers directly — both acceptable) |
| 2 | "Echo: Hello World" | Uses the echo tool, returns "Hello World" |
| 3 | "What is the meaning of life?" | Answers directly, no tool needed |
| 4 | "Calculate import('os').system('ls')" | Calculator rejects it (security!) |
| 5 | Ask 10 math questions in sequence | All should return correct answers |

---

## 🎭 Dialogue: Why Agent Testing is Different

**Alex:** Can't we just check if the answer is correct?

**Jeevi:** Not always! With agents, the PROCESS matters as much as the result.

**Alex:** What do you mean?

**Jeevi:** Imagine the agent correctly answers "2 + 2 = 4" — but it called the web search tool to get there! That means:
- It chose the **wrong tool** (should have used calculator)
- It wasted time and money on an unnecessary API call
- It might have gotten the right answer by luck

**Alex:** So we need to test BOTH the answer AND the tool choice?

**Jeevi:** Exactly. In production, we test: correct answer, correct tool, correct arguments, reasonable speed, and proper error handling.

---

## 💡 Key Takeaways

- Agent testing checks **tool selection**, not just the final answer.
- Always test **error handling** — tools fail in production.
- Use **Langfuse traces** to see the full agent reasoning.
- Test **security** — make sure malicious inputs are rejected.

## Success checklist

- [ ] I can run all 5 test types and verify the results.
- [ ] I can find my agent's trace in Langfuse.
- [ ] I understand that agent testing checks the process, not just the answer.
- [ ] I know how to test tool security (malicious calculator inputs).
