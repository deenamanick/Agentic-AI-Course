# Practical 6.3 — Tool Safety (Crucial!) 🛑

## Why, in simple terms

You have given an autonomous AI Agent access to your email account. 

Imagine this scenario: The user prompts: *"Check the price of RELIANCE.NS. If it is under ₹3000, send an email to my boss."*

What happens if the AI hallucinates? What if it gets stuck in an infinite loop and sends 10,000 emails to your boss in one minute? **Your account will be banned, and you will be in huge trouble.**

---

## 🛡️ The Danger of "Write" Tools

In the AI world, we classify tools into two categories:
1. **Read Tools:** Safe. (e.g., `get_stock_price`, Web Search, Read PDF). If the AI loops a Read Tool, you just waste some API credits. No harm done.
2. **Write Tools:** Dangerous! (e.g., `send_email_alert`, Delete File, Post to Twitter, Transfer Money). If the AI loops a Write Tool, it causes real-world damage.

**CRITICAL RULE:** You must NEVER give an autonomous agent access to a Write Tool without a safety mechanism.

---

## 🚦 Safety Mechanisms

How do we make Write Tools safe?

### 1. Human-in-the-Loop (Approval Gates)
The most common and safest method. When the AI wants to use the `send_email_alert` tool, it must pause execution. It sends a popup to the user: *"I am about to send this email to your boss. Click Approve or Reject."* The AI cannot proceed until the human clicks Approve.

*(LangGraph makes this easy with `interrupt_before`, which we will learn in later modules).*

### 2. Idempotency Keys
For system-to-system tools (like "Charge Credit Card"), you pass a unique ID (like a UUID) with the request. If the AI hallucinates and calls the tool 5 times in a row with the same UUID, your payment server knows to only process it once.

### 3. Read-Only Fallbacks
If you are building a learning project, the easiest safety mechanism is just... not sending the email! You can modify your tool to just print the email to the terminal instead of actually sending it.

For our code in `app/main.py`, we have added a `MOCK_EMAILS=true` environment variable. When this is set to true, the `send_email_alert` tool will just return a success string without actually firing off the email. This keeps you safe while developing!

---

## 💡 Key Takeaways

- **Read Tools** are generally safe. **Write Tools** are highly dangerous.
- An AI can hallucinate or loop, causing real-world damage with Write Tools.
- Always use Human-in-the-Loop or Mocking when developing agents with Write Tools!

## Success checklist

- [ ] I know the difference between a Read Tool and a Write Tool.
- [ ] I understand the danger of infinite loops with Write Tools.
- [ ] I understand what Human-in-the-Loop (Approval Gating) means.
