# Practical 3.2 — What Are Tools? (The Librarian's Phone 📞)

## Why, in simple terms

Remember from Module 2.1? We said an LLM is like "a brilliant librarian who hasn't left the library in 2 years." An **agent tool** is the phone we give the librarian so they can call for current information.

A tool is simply a **Python function** that the AI can decide to call.

---

## 🛠️ Your First Three Tools

Here are the tools we'll use in our agent. They are just normal Python functions with a special decorator:

### Tool 1: Calculator 🧮

```python
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluate a simple arithmetic expression, e.g. '(17 * 23) + 5'."""
    try:
        result = _safe_eval_arithmetic(expression)
        return str(result)
    except Exception as e:
        return f"error: {e}"
```

**What the AI sees:** *"There's a tool called `calculator` that can evaluate math expressions."*
**When the AI uses it:** When the user asks a math question.

### Tool 2: Unix Timestamp ⏰

```python
@tool
def now_unix() -> str:
    """Return the current Unix timestamp in seconds."""
    return str(int(time.time()))
```

**What the AI sees:** *"There's a tool called `now_unix` that returns the current time."*
**When the AI uses it:** When the user asks what time it is.

### Tool 3: Echo 🔊

```python
@tool
def echo(text: str) -> str:
    """Echo back the given text."""
    return text
```

**What the AI sees:** *"There's a tool called `echo` that repeats text back."*
**When the AI uses it:** When the user asks to echo something (useful for testing).

---

## 🤔 Why These Specific Three Tools?

You might be wondering: *Why only these three? Why not a web search or a database tool?*

We chose these three because they perfectly demonstrate the **three main reasons** we use agents, without requiring any external API keys or complex setups:

1. **Calculator:** LLMs are famously bad at math. This tool proves the agent can solve problems the LLM's brain cannot solve on its own.
2. **Time (`now_unix`):** LLMs have no concept of "now" (their training data is frozen in the past). This proves the agent can fetch real-time data that the LLM lacks.
3. **Echo:** This is a pure debugging tool. It helps you prove the tool-calling connection is working before you build complex logic.

We keep it to just three simple tools so you can focus 100% on **learning how the agent loop works**, without getting distracted by broken API keys or network errors. Once you understand the loop, adding a web search tool is easy!

---

## 🎭 Dialogue: Why Are Descriptions So Important?

**Alex:** These are just regular Python functions. What makes them "tools"?

**Jeevi:** Two things:
1. The `@tool` decorator tells LangChain "the AI is allowed to call this function."
2. The **docstring** (the text in triple quotes) is what the AI reads to decide WHEN to use it.

**Alex:** Wait, the AI reads the docstring?!

**Jeevi:** Yes! If you write a bad docstring like `"""Does stuff."""`, the AI won't know when to use it. If you write `"""Evaluate a simple arithmetic expression, e.g. '(17 * 23) + 5'."""`, the AI knows exactly when this tool is useful.

**Alex:** So the docstring is basically a prompt for the tool?

**Jeevi:** Exactly! 🎯 The tool's docstring is as important as the system prompt.

---

## 🔒 Tool Safety: The Calculator Example

Our calculator doesn't just run `eval(expression)` — that would be **extremely dangerous**! A user could send:

```python
# ❌ DANGEROUS: eval() can execute ANY Python code
eval("__import__('os').system('rm -rf /')")  # This could DELETE your files!
```

Instead, we use `_safe_eval_arithmetic()` which:
1. Parses the expression into an AST (Abstract Syntax Tree)
2. Only allows math operations (+, -, ×, ÷, powers)
3. Blocks function calls, variable access, and imports
4. Then evaluates the safe expression

```python
# ✅ SAFE: Only allows arithmetic
_safe_eval_arithmetic("(17 * 23) + 5")  # Returns "396"
_safe_eval_arithmetic("import os")       # Raises ValueError!
```

> [!CAUTION]
> **Never use `eval()` directly with user input.** Always validate and restrict what can be executed. This is a real-world security lesson.

---

## 🏗️ How to Build Your Own Tool (Exercise)

Want to add a new tool? Follow this pattern:

```python
@tool
def word_count(text: str) -> str:
    """Count the number of words in the given text."""
    count = len(text.split())
    return f"{count} words"
```

**Three rules for every tool:**
1. **Clear name** — `word_count` not `wc` or `do_thing`
2. **Clear docstring** — The AI uses this to decide when to call it
3. **Safe execution** — Validate inputs, handle errors, never expose secrets

---

## Quick Practice Tasks

1. Write a `to_upper(text: str) -> str` tool that converts text to uppercase.
2. Write a `reverse_text(text: str) -> str` tool that reverses a string.
3. For each tool, write a docstring that would help the AI know when to use it.
4. Think: what would happen if your tool's docstring was empty?

---

## 💡 Key Takeaways

- A **tool** is just a Python function with the `@tool` decorator.
- The **docstring** is the AI's instruction manual for when to use the tool.
- **Security matters** — always validate inputs (never use raw `eval()`).
- Tools should do **one thing well** and return a clear result.

## Success checklist

- [ ] I can explain what a tool is using the librarian analogy.
- [ ] I understand why the docstring is critical for tool selection.
- [ ] I know why `eval()` is dangerous and how `_safe_eval_arithmetic` is safer.
- [ ] I can write a simple tool with a clear name, docstring, and safe execution.
