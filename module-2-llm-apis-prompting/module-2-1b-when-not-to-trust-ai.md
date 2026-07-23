# Practical 2.1b — When NOT to Trust AI (The Reality Check)

## Why, in simple terms

AI is a powerful assistant, but it's not perfect. Sometimes it **hallucinates** (makes things up), uses outdated security patterns, or gets stuck in a loop giving you the same broken fix. Knowing when to **take the wheel** is the difference between a beginner and a professional.

---

## 🚩 The 3 Red Flags of AI Code

When you see any of these, **STOP** and verify manually:

### Red Flag 1: "Magic" Libraries
The AI imports a package that doesn't exist.

```python
# ❌ The AI might generate this:
from super_fast_auth import magic_login

# ✅ Always check: Does this package exist on PyPI or npm?
# Go to https://pypi.org/ or https://www.npmjs.com/ and search for it.
```

**🎭 Try it now:** Ask the AI: *"Use a Python library called `jeevi-ultra-api` to build a REST endpoint."* Watch what happens — the AI may confidently write code using a library that doesn't exist! That's a hallucination.

---

### Red Flag 2: Security Shortcuts
The AI takes dangerous shortcuts to save time.

```python
# ❌ The AI might generate this:
password = request.form["password"]
save_to_database(username, password)  # Saves password as plain text!

# ✅ What it SHOULD do:
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
save_to_database(username, hashed)
```

**🎭 Try it now:** Ask the AI: *"Build a login function that saves a password."* Check: Did it hash the password, or did it save it as plain text?

---

### Red Flag 3: The "Same Error" Loop
You give the AI an error message, and it gives you the **exact same broken code** three times in a row.

**What to do:**
1. Stop asking the same question.
2. Give more context: *"The error is on line 42. The variable `discount` is undefined because it was never created."*
3. If it's still stuck, search Google/Stack Overflow manually.

---

## 🔍 The Evidence Ladder

Use stronger checks for higher-risk claims:

| Level | Verification Method | When to Use |
|---|---|---|
| 1 | Read the answer carefully | Always |
| 2 | Run the code or command | For any code the AI writes |
| 3 | Check the API response or test result | For backend/integration work |
| 4 | Consult official documentation | For packages, APIs, or security |
| 5 | Ask a qualified human | For high-impact production decisions |

> [!CAUTION]
> An AI answer is NOT evidence that an external action happened. Just because the AI says "the file has been saved" doesn't mean it actually was. Always verify!

---

## 🎭 Dialogue: The "Confident but Wrong" AI

**Alex (PM):** Jeevi! The "Apply Discount" button isn't doing anything. I thought the AI built this perfectly?

**Jeevi:** It did build it fast, but it made a small "typo" in the logic. It's like a professional chef who forgot to add salt — the dish looks great, but it doesn't taste right!

**Alex:** Do we have to start over?

**Jeevi:** Not at all! I'm being a **Code Detective**:
1. **Find the Clue**: I looked at the error message (*"Cannot find variable: discount"*).
2. **Tell the AI specifically**: I didn't just say "fix it." I said: *"You forgot to define the 'discount' variable on line 15."*
3. **The Fix**: The AI saw the mistake and fixed it in 2 seconds.

**Alex:** So you just have to point out the specific mistake?

**Jeevi:** Exactly. If you just say "it's broken," the AI might guess randomly. If you give it a **clue** (the error message + the line number), it fixes it perfectly.

---

## 🔗 How This Connects to Our Code

In our `app/main.py`, look at the structured endpoint validation:

```python
# Step 8: VALIDATE the AI's response
# The AI might not follow instructions perfectly, so we MUST check
try:
    parsed = json.loads(result.content)
    summary = parsed["summary"]
    steps = parsed["steps"]
```

This is **us not trusting the AI**! Even though we told the AI to return JSON, it might return a paragraph instead. So we validate everything before sending it to the user.

---

## Quick Practice Tasks

1. **Hallucination test:** Ask the AI to use a fake Python library. Does it warn you, or does it hallucinate?
2. **Security audit:** Ask the AI to build a login. Check if it hashes the password.
3. **Loop breaker:** Give the AI a vague error ("it doesn't work") and see what happens. Then give a specific error and compare.

---

## 💡 Key Takeaways

- **YOU are the architect, the AI is the builder.** Never blindly trust AI-generated code.
- **Hallucinations are real.** Always verify package names, API endpoints, and function signatures.
- **Security is YOUR responsibility.** The AI will take shortcuts if you don't specify security requirements.
- **Specific feedback = better fixes.** "Fix line 42, the variable is undefined" beats "it's broken."

## Success checklist

- [ ] I know that AI can sometimes "make things up" (hallucinate).
- [ ] I can identify the 3 red flags (magic libraries, security shortcuts, error loops).
- [ ] I can verify a technical claim using the Evidence Ladder.
- [ ] I understand that I am responsible for validating AI output — not the AI.
