# Module 6: Custom Tools & External APIs

This module is about giving your AI agent the ability to **interact with the real world**. So far your agents could only read and write text. Here you will:

- Understand what External APIs are and why agents need them
- Build a **Stock Price Tool** (Read Tool — safe)
- Build an **Email Alert Tool** (Write Tool — dangerous!)
- Learn about **Tool Safety** (mocking, human-in-the-loop)
- Connect it all to a beautiful Lovable UI

### What's in this folder

- `app/main.py` — A single file containing **both tools** + the FastAPI agent. Everything lives here.
- `.env.example` — Configuration for Groq, SMTP, and mock email settings.
- `requirements.txt` — Python dependencies (includes `yfinance`).

### Practicals

- `module-6-0-external-apis.md` — External APIs & The Real World (concepts only)
- `module-6-1-stock-tool.md` — Building the Stock Price Tool (lines 33-57 of main.py)
- `module-6-2-email-tool.md` — Building the Email Tool (lines 59-104 of main.py)
- `module-6-3-tool-safety.md` — Tool Safety: Read vs Write tools (lines 75-81 of main.py)
- `module-6-4-lovable-alert-ui.md` — Create a Lovable Alert UI (full-stack integration)

### Recommended order

1. External APIs (concepts)
2. Stock Tool (first tool — Read, safe)
3. Email Tool (second tool — Write, dangerous)
4. Tool Safety (understanding mocks)
5. Lovable UI (full-stack integration)

---

## Prerequisites

- Python 3.10+
- A Groq account and API key
- (Optional) A Gmail account if you want to test sending *real* emails (requires an App Password).

---

## Setup

> **👨‍🎓 Student Guide: Follow these steps in order!**

From this folder (`module-6-custom-tools-mcp/`):

```bash
# Step 1: Create a virtual environment
python3 -m venv .venv

# Step 2: Activate it
source .venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Copy the env template & fill in your keys
cp .env.example .env
```

Fill in your `GROQ_API_KEY` in `.env`.

> [!IMPORTANT]
> Ensure `MOCK_EMAILS=true` is set in your `.env` file when you start testing! This prevents the agent from sending real emails.

---

## Run

### Start the API server

```bash
uvicorn app.main:app --reload
```

---

## Quick Test (1 curl command)

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Check the price of RELIANCE.NS. If it is over ₹2000, send an email to boss@example.com saying we should sell."
  }'
```

Watch the terminal running `uvicorn` carefully! You will see:
1. The agent call the `get_stock_price` tool → returns the price
2. The `[MOCK EMAIL]` output printed to the terminal (not a real email!)

---

## Checklist

- [ ] You can explain what a custom tool is in LangChain.
- [ ] You understand why the **docstring** of a Python function is critical for the AI to use the tool correctly.
- [ ] You understand the danger of **Write Tools** (like sending emails) compared to **Read Tools**.
- [ ] You successfully tested your agent and saw the Mock Email printed in your terminal.
