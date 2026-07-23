# Practical 6.0 — External APIs & The Real World 🌍

## Why, in simple terms

So far, our AI Agents have been trapped in a box.
- The **Calculator Agent** (Module 3) could only do math.
- The **Resume Builder** (Module 4) could only read text and output text.
- The **Job Analyzer** (Module 5) could only read text and output text.

What if we want our Agent to actually *do* something in the real world? What if we want it to check the live price of a stock on the Indian Stock Market, and then send a real email to your inbox?

To do this, we give the Agent **Custom Tools** that connect to **External APIs**.

---

## 🔌 What is an External API?

An API (Application Programming Interface) is how two computer programs talk to each other. 
When you check the weather on your phone, your phone is calling a Weather API.

For our **Indian Stock Market Alert Agent**, we are going to build two custom tools that talk to the outside world:

1. **`get_stock_price` Tool:** This tool will use a famous Python library called `yfinance` (Yahoo Finance). It reaches out to the internet, asks Yahoo for the live price of a stock (like `RELIANCE.NS` for Reliance on the NSE), and returns the number.
2. **`send_email_alert` Tool:** This tool will use Python's built-in `smtplib`. It reaches out to an email server (like Gmail), logs in with an App Password, and physically sends an email to an inbox.

### How the Agent uses them:

When you type:
> *"Check the price of TCS.BO on the BSE. If it is over ₹4000, send an email to alex@example.com saying 'SELL NOW!'."*

The Agent will:
1. "Think": I need to find the price of TCS.BO. I will use the `get_stock_price` tool.
2. "Act": Calls `get_stock_price("TCS.BO")` -> Gets back `4100`.
3. "Think": 4100 is greater than 4000. I need to send an email. I will use the `send_email_alert` tool.
4. "Act": Calls `send_email_alert("alex@example.com", "SELL NOW!")`.
5. "Think": I have completed the task.

---

## 💡 Key Takeaways

- To make an AI useful, it needs to interact with the real world.
- We do this by writing normal Python code (to fetch data or send messages) and wrapping it in an `@tool` decorator so the AI can use it.
- In this module, we will build a real Stock Tracker that can send emails!

## Success checklist

- [ ] I understand why an AI needs Custom Tools to interact with the real world.
- [ ] I know what an API is.
- [ ] I understand the 2 tools we are going to build for our Stock Alert Agent.
