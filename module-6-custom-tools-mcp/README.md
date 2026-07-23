# Module 6 — Custom Tools & External APIs

## What you will build

So far, your agents have been trapped inside a box, only able to read and write text. In this module, you give your agent the ability to **interact with the real world**.

We are building the **Indian Stock Market Alert Agent**. 

You will build two powerful custom tools:
1. `get_stock_price`: Uses `yfinance` to fetch live prices from the NSE and BSE. (This is a **Read Tool**).
2. `send_email_alert`: Uses `smtplib` to physically send an email to a user's inbox. (This is a **Write Tool**).

---

## What's in this folder

- `app/main.py`
  - `POST /agent/chat`
  - A ReAct agent equipped with the two custom tools.
  - Implements **Tool Safety** by using `MOCK_EMAILS` to prevent spamming during testing.
- `.env.example`
  - Configuration for Groq, SMTP (Email/Password), and MOCK settings.
- `requirements.txt`
  - Note the addition of `yfinance`!

## Practicals

0. [External APIs & The Real World](module-6-0-external-apis.md)
1. [Building the Stock Price Tool](module-6-1-stock-tool.md)
2. [Building the Email Tool](module-6-2-email-tool.md)
3. [Tool Safety (Crucial!)](module-6-3-tool-safety.md)
4. [Create a Lovable Alert UI](module-6-4-lovable-alert-ui.md)

---

## Prerequisites

- Python 3.10+
- A Groq account and API key
- (Optional) A Gmail account if you want to test sending *real* emails (Requires generating an App Password).

---

## Setup

From this folder (`module-6-custom-tools-mcp/`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in your `GROQ_API_KEY` in `.env`.

> **IMPORTANT:** Ensure `MOCK_EMAILS=true` is set in your `.env` file when you start testing!

---

## Run

### Start the API server

```bash
uvicorn app.main:app --reload
```

---

## Test Locally

Send a prompt asking the agent to check an Indian stock and send an email:

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "Check the price of RELIANCE.NS. If it is over ₹2000, send an email to boss@example.com saying we should sell."
  }'
```

Watch the terminal running `uvicorn` carefully! You will see the agent call the `get_stock_price` tool, and then you will see the `[MOCK EMAIL]` output printed to the terminal instead of an actual email being sent.

---

## Checkpoint (Module 6)

- [ ] I can explain what a custom tool is in LangChain.
- [ ] I understand why the **docstring** of a Python function is critical for the AI to use the tool correctly.
- [ ] I understand the danger of **Write Tools** (like sending emails) compared to **Read Tools**.
- [ ] I successfully tested my agent and saw the Mock Email printed in my terminal.
