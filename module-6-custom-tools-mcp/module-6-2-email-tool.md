# Practical 6.2 — Building the Email Tool 📧

## Why, in simple terms

Our agent can now fetch stock prices. But if the price drops drastically, we want the agent to alert us! We need to build a tool that can physically send an email to a user.

To do this, we use Python's built-in `smtplib`. This allows Python to log in to an email server (like Gmail) and send a message.

---

## 🔐 Handling Passwords Safely

**CRITICAL RULE:** Never hardcode passwords in your Python files! If you upload your code to GitHub with a password in it, hackers will steal it immediately.

Instead, we use `.env` files. We store the email and password in the `.env` file, and read them securely using `os.getenv()`.

> [!CAUTION]
> If you are using Gmail, you cannot use your normal login password. You must generate an **"App Password"** in your Google Account Security settings.

---

## 🛠️ The Code: `send_email_alert`

Here is our second custom tool. Notice again how clear the docstring is.

```python
import os
import smtplib
from email.mime.text import MIMEText
from langchain_core.tools import tool

@tool
def send_email_alert(to_email: str, subject: str, body: str) -> str:
    """
    Sends an email alert to a specified email address.
    ONLY use this tool if the user explicitly asks you to send an email or alert them.
    
    Args:
        to_email: The email address to send the alert to.
        subject: The subject line of the email.
        body: The main message of the email.
        
    Returns:
        A success string or an error message.
    """
    # 1. Read secrets safely from the .env file
    sender_email = os.getenv("SMTP_EMAIL")
    sender_password = os.getenv("SMTP_PASSWORD")
    
    if not sender_email or not sender_password:
        return "Error: SMTP credentials not configured in the server."

    try:
        # 2. Format the email
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to_email

        # 3. Connect to Gmail's SMTP server and send!
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            
        return f"Successfully sent email alert to {to_email}."
        
    except Exception as e:
        return f"Failed to send email: {str(e)}"
```

---

## 🎭 Dialogue: The Agent's Decision Making

**Alex:** Okay, so I have two tools now: `get_stock_price` and `send_email_alert`. How does the AI know when to use which one?

**Jeevi:** By reading your prompt! If you say *"What is the price of Tata Motors?"*, the AI reads the tool descriptions and thinks: *"I need price data. I will use `get_stock_price`. I do not need to send an email."* 

**Alex:** And if I say *"Email me the price of Tata Motors"*?

**Jeevi:** The AI thinks: *"Step 1: I need the price. I will use `get_stock_price`. Step 2: I have the price. Now I need to email it. I will use `send_email_alert`."* It automatically chains them together!

---

## 💡 Key Takeaways

- You must handle API keys and Passwords using `.env` files. Never hardcode them!
- Python's `smtplib` makes sending emails incredibly easy.
- You can give an agent multiple tools, and it will figure out how to chain them together to solve complex requests.

## Success checklist

- [ ] I understand why I must use an `.env` file for passwords.
- [ ] I understand how the agent chains multiple tools together.
