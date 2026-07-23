# Practical 2.12 — AI-Assisted Debugging and Refactoring

## Why, in simple terms

AI can help you fix bugs (debugging) and clean up messy code (refactoring). But you need to know **how to guide it** — otherwise it'll guess randomly or rewrite your entire file.

---

## Part 1: Debugging with AI 🔍 (Be a Detective, Not a Bystander)

### The Wrong Way

```text
❌ "My code is broken. Fix it."
```

The AI will guess. It might "fix" something that wasn't broken and introduce new bugs.

### The Right Way (The Detective Prompt)

```text
✅ "I'm getting this error when I call POST /chat/structured:

   Error: json.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

   The error happens in app/main.py at line 195:
   parsed = json.loads(result.content)

   The AI model returned this instead of JSON:
   'Here is a summary: The serverless architecture...'

   Can you explain why this happened and suggest the smallest fix?"
```

### 🎭 The Detective Formula

Always give the AI these 4 clues:

| Clue | Example |
|---|---|
| 📝 **The exact error message** | `json.JSONDecodeError: Expecting value...` |
| 📍 **Where it happens** | `app/main.py, line 195` |
| 📦 **What you expected** | Valid JSON with `summary` and `steps` |
| ❌ **What actually happened** | The AI returned a paragraph instead of JSON |

---

### 🔗 Real Example from Our Code

In our `app/main.py`, this is the section that can fail:

```python
# Step 8: VALIDATE the AI's response
try:
    parsed = json.loads(result.content)        # Can fail here!
    summary = parsed["summary"]                # Or here!
    steps = parsed["steps"]                    # Or here!
    if not isinstance(summary, str) or not isinstance(steps, list):
        raise ValueError("Invalid JSON shape")  # Or here!
except (json.JSONDecodeError, KeyError, TypeError, ValueError):
    raise HTTPException(
        status_code=502,
        detail="Model did not return the required structured response.",
    )
```

**Common bugs and how to debug them:**

| What Happened | The Clue | The Fix |
|---|---|---|
| AI returned a paragraph before the JSON | `json.JSONDecodeError` | Add "Return ONLY JSON, no text before or after" to the prompt |
| AI returned JSON but missing `steps` | `KeyError: 'steps'` | Make the schema example clearer in the prompt |
| AI returned `steps` as a single string | `ValueError: Invalid JSON shape` | Add "steps must be an array" to the prompt |

---

## Part 2: Refactoring with AI 🧹 (Tidy Up, One Drawer at a Time)

### What is Refactoring?

Refactoring means making code **cleaner and easier to read** without changing what it does. It's like organizing a messy desk — everything still works, but now you can find things.

### The Wrong Way

```text
❌ "Clean up my entire codebase."
```

The AI will rewrite everything and probably break things.

### The Right Way (One Drawer at a Time)

```text
✅ "In app/main.py, the chat() and chat_structured() functions have
   a lot of duplicated code in the Langfuse metadata section.
   Can you:
   1. Extract the common metadata into a helper function.
   2. Keep the existing behavior exactly the same.
   3. Show me the helper function first, then how to use it."
```

---

### 🎭 Dialogue: Making Messy Code "Pretty"

**Alex (PM):** The code works, but our new developer says it's hard to read.

**Jeevi:** She's right. When we were rushing, we just threw everything into one big pile. Now I'm going to **Tidy Up** (Refactor).

**Alex:** Will "tidying up" break the button again?

**Jeevi:** Not if I do it **one drawer at a time** (Chunking).
- I'm not cleaning the whole house at once.
- I'm asking the AI to "Take this one section and make it look professional and easy to read."
- I check the button after every small change to make sure it still works.

**Alex:** So it's like moving from a messy pile of clothes to a neatly organized closet?

**Jeevi:** Precisely! The code does the exact same thing, but now any other human can read it and understand it.

---

### 🔗 Real Refactoring Example from Our Code

Look at the duplicated Langfuse metadata in our `app/main.py`:

**Before (duplicated in both endpoints):**
```python
"metadata": {
    "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
    "environment": os.getenv("APP_ENV", "Development"),
    "request_id": request_id,
    "prompt_version": prompt_version,
    "langfuse_session_id": request_id,
    "langfuse_tags": [...],
},
```

**After (extracted into a helper):**
```python
def build_trace_metadata(request_id: str, prompt_version: str) -> dict:
    """Build common Langfuse metadata for all endpoints."""
    return {
        "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
        "environment": os.getenv("APP_ENV", "Development"),
        "request_id": request_id,
        "prompt_version": prompt_version,
        "langfuse_session_id": request_id,
        "langfuse_tags": [
            f"Project:{os.getenv('APP_PROJECT', 'Jeevi-Academy')}",
            f"Environment:{os.getenv('APP_ENV', 'Development')}",
            f"PromptVersion:{prompt_version}",
        ],
    }
```

**💡 Why this is better:** If we add a third endpoint later, we don't have to copy-paste the metadata block again. One change in the helper fixes all endpoints.

---

## Quick Practice Tasks

1. **Debug practice:** Intentionally break the structured endpoint (remove `"Return ONLY valid JSON"` from the prompt) and use the Detective Formula to fix it.
2. **Refactor practice:** Ask the AI to rename variables in one function from short names (`req`, `llm`) to descriptive names (`chat_request`, `language_model`).
3. **Safety check:** After each refactoring step, run `bash scripts/test_chat.sh` to verify nothing broke.

---

## 💡 Key Takeaways

- **Debugging:** Be a **Detective**. Give the AI clues (error message, line number, expected vs actual).
- **Refactoring:** Be a **Tidier**. Clean one section at a time, test after each change.
- **One step at a time:** Never fix or clean everything at once. Small steps = zero crashes.
- **Always test after changes:** Run your test script after every modification.

## Success checklist

- [ ] I can provide the AI with specific error details (not just "it's broken").
- [ ] I can identify duplicated code and ask the AI to extract it into a helper.
- [ ] I test after every small change to catch regressions immediately.
- [ ] I understand the difference between debugging (fixing) and refactoring (cleaning).
