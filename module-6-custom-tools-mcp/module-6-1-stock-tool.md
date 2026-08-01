# Module 6.1: Building the Stock Price Tool 📈

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Understand the Goal** - Read why we need a tool to fetch stock prices.
> 2. **Phase 2: Visual Studio Code Practice** - Open `app/main.py` and study Tool 1 (lines 37-68).
> 3. **Phase 3: The Brain** - Learn how the docstring instructs the AI to use the tool correctly.

### Why (in simple terms)

We need our AI to be able to check the live price of any stock on the Indian Stock Market (NSE or BSE). 

To do this, we will write a standard Python function using the `yfinance` library, and then wrap it in LangChain's `@tool` decorator so the AI knows how to use it!

### What you'll learn
1. **Tool Creation**: How to use the `@tool` decorator.
2. **yfinance**: How to fetch live stock data for free.
3. **Docstrings**: Why they are critical for AI tool usage.

---

## 🌊 Visual Studio Code Practice: Understanding the `get_stock_price` Tool

> [!IMPORTANT]
> All the code for this module lives in **one file**: `app/main.py`. You do NOT create a separate file. Open `app/main.py` and look for the section labeled **TOOL 1**.

### Step 1: Open the code

Open `app/main.py` in Visual Studio Code and find this section:

```
# =====================================================================
# TOOL 1: GET STOCK PRICE  (Read Tool — SAFE)
# Covered in: module-6-1-stock-tool.md
# =====================================================================
```

### Step 2: Study the tool

Here is what the tool does, line by line:

```python
import yfinance as yf
from langchain_core.tools import tool

@tool
def get_stock_price(ticker: str) -> str:
    """
    Fetches the current stock price for a given ticker symbol.
    For Indian stocks on the NSE, append '.NS' (e.g., 'RELIANCE.NS').
    For Indian stocks on the BSE, append '.BO' (e.g., 'TCS.BO').
    
    Args:
        ticker: The stock ticker symbol.
        
    Returns:
        A string containing the current price or an error message.
    """
    try:
        # Step 1: Fetch the data from Yahoo Finance
        stock = yf.Ticker(ticker)
        
        # Step 2: Get the current price (or previous close if market is closed)
        todays_data = stock.history(period='1d')
        if todays_data.empty:
            return f"Error: Could not find data for {ticker}. Did you forget .NS or .BO?"
            
        price = todays_data['Close'].iloc[0]
        
        # Step 3: Return a clean string to the AI
        return f"The current price of {ticker} is ₹{price:.2f}"
        
    except Exception as e:
        return f"Error fetching price for {ticker}: {str(e)}"
```

### What each part does:

| Line | What it does | Why it matters |
| :--- | :--- | :--- |
| `@tool` | Tells LangChain "this is a tool the AI can use" | Without this, the AI can't call the function |
| `def get_stock_price(ticker: str) -> str:` | A normal Python function that takes a ticker string | The type hint `str` tells the AI what argument to pass |
| The **docstring** (triple quotes) | Instructions for the AI on *when* and *how* to use the tool | The AI reads this to decide the correct arguments |
| `yf.Ticker(ticker)` | Connects to Yahoo Finance and fetches the stock data | This is the "external API" call |
| `return f"The current price..."` | Returns a clean string | The AI reads this string and uses it in its response |

---

## 🎭 Dialogue: The Power of Docstrings

**Alex:** Why do we need to tell the AI to append `.NS` or `.BO` in the docstring? Shouldn't it just know?

**Jeevi:** The AI knows general knowledge, but it doesn't know exactly how the Yahoo Finance API works! If a user asks *"Check the price of Reliance"*, the AI might try to pass the string `"Reliance"` to the tool. Yahoo Finance will crash because it needs the exact ticker `"RELIANCE.NS"`. 

**Alex:** Ah! So the docstring is literally instructions for the AI on how to format the arguments?

**Jeevi:** Exactly! By writing good docstrings, the AI will automatically fix the user's input before calling your Python function.

---

## 💡 Key Takeaways

- A custom tool is just a Python function wrapped in the `@tool` decorator.
- The `yfinance` library is an amazing, free way to get stock data without needing API keys.
- **The Docstring is the Prompt for the Tool.** You must write clear instructions in the docstring so the AI knows how to pass arguments correctly.

## Checklist

- [ ] You found Tool 1 in `app/main.py`.
- [ ] You understand how the `@tool` decorator works.
- [ ] You understand why we use `yfinance`.
- [ ] You can explain why the docstring inside the tool is critical for the AI's success.
