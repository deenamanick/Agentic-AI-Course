# Module 6.3: Tool Safety (Crucial!) 🛑

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Understand the Danger** - Read about Read vs Write tools and infinite loops.
> 2. **Phase 2: The Solution** - Learn the 3 main ways to make Write Tools safe.
> 3. **Phase 3: Visual Studio Code Practice** - Open `app/main.py` and study the mock logic in Tool 2 (lines 91-96).

### Why (in simple terms)

You have given an autonomous AI Agent access to your email account. 

Imagine this scenario: The user prompts: *"Check the price of RELIANCE.NS. If it is under ₹3000, send an email to my boss."*

What happens if the AI hallucinates? What if it gets stuck in an infinite loop and sends 10,000 emails to your boss in one minute? **Your account will be banned, and you will be in huge trouble.**

### What you'll learn
1. **Read vs Write Tools**: How to classify tool safety.
2. **Infinite Loops**: The real-world danger of autonomous agents.
3. **Safety Mechanisms**: How to protect your systems.

---

## 🛡️ The Danger of "Write" Tools

In the AI world, we classify tools into two categories:

| Tool Type | Examples | If the AI loops it... | Danger Level |
| :--- | :--- | :--- | :--- |
| **Read Tools** (safe) | `get_stock_price`, Web Search, Read PDF | You waste some API credits. No harm done. | 🟢 Low |
| **Write Tools** (dangerous!) | `send_email_alert`, Delete File, Post to Twitter, Transfer Money | Real-world damage! Banned accounts, lost data, lost money. | 🔴 Critical |

**CRITICAL RULE:** You must NEVER give an autonomous agent access to a Write Tool without a safety mechanism.

---

## 🚦 Safety Mechanisms

How do we make Write Tools safe?

### 1. Human-in-the-Loop (Approval Gates)
The most common and safest method. When the AI wants to use the `send_email_alert` tool, it must pause execution. It sends a popup to the user: *"I am about to send this email to your boss. Click Approve or Reject."* The AI cannot proceed until the human clicks Approve.

*(LangGraph makes this easy with `interrupt_before`, which we will learn in later modules.)*

### 2. Idempotency Keys
For system-to-system tools (like "Charge Credit Card"), you pass a unique ID (like a UUID) with the request. If the AI hallucinates and calls the tool 5 times in a row with the same UUID, your payment server knows to only process it once.

### 3. Read-Only Fallbacks (Mocking)
If you are building a learning project, the easiest safety mechanism is just... not sending the email! You modify your tool to print the email to the terminal instead of actually sending it.

**This is what we do in this module!**

---

## 🌊 Visual Studio Code Practice: How Our Mock Works

> [!IMPORTANT]
> Open `app/main.py` and look inside Tool 2 (`send_email_alert`). The mock logic is the **very first thing** inside the function.

### Step 1: Find the mock logic in the code

Look for these lines in `app/main.py`:

```python
    # ── SAFETY MECHANISM: MOCK MODE (module-6-3-tool-safety.md) ──────
    is_mock = os.getenv("MOCK_EMAILS", "true").lower() == "true"
    
    if is_mock:
        print(f"\n[MOCK EMAIL] To: {to_email}\nSubject: {subject}\nBody: {body}\n")
        return f"Successfully sent MOCK email alert to {to_email}. (MOCK_EMAILS=true)"
```

### Step 2: Understand how it works

| What happens | When `MOCK_EMAILS=true` | When `MOCK_EMAILS=false` |
| :--- | :--- | :--- |
| Email sent? | ❌ No real email | ✅ Real email sent |
| What you see | `[MOCK EMAIL]` printed in terminal | Email arrives in inbox |
| Safe for testing? | ✅ Yes — no spam | ⚠️ Use carefully |

### Step 3: Check your `.env` file

Open your `.env` file and make sure this line exists:

```bash
MOCK_EMAILS=true
```

> [!CAUTION]
> Only set `MOCK_EMAILS=false` when you have tested everything and are 100% ready to send real emails. Always start with `true`!

---

## 💡 Key Takeaways

- **Read Tools** are generally safe. **Write Tools** are highly dangerous.
- An AI can hallucinate or loop, causing real-world damage with Write Tools.
- Always use Human-in-the-Loop or Mocking when developing agents with Write Tools!
- Our `MOCK_EMAILS=true` flag in `.env` is a simple but effective safety mechanism.

## Checklist

- [ ] You know the difference between a Read Tool and a Write Tool.
- [ ] You understand the danger of infinite loops with Write Tools.
- [ ] You understand what Human-in-the-Loop (Approval Gating) means.
- [ ] You found the mock logic inside `app/main.py` and verified `MOCK_EMAILS=true` is in your `.env`.
