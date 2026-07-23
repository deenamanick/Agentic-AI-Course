# Practical 6.1 — Building the Stock Price Tool 📈

## Why, in simple terms

We need our AI to be able to check the live price of any stock on the Indian Stock Market (NSE or BSE). 

To do this, we will write a standard Python function using the `yfinance` library, and then wrap it in LangChain's `@tool` decorator so the AI knows how to use it!

---

## 🛠️ The Code: `get_stock_price`

In `app/main.py`, we define our custom tool. Notice the **docstring** inside the function! This is incredibly important. The AI reads this docstring to understand *when* and *how* to use the tool.

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
        # 1. Fetch the data from Yahoo Finance
        stock = yf.Ticker(ticker)
        
        # 2. Get the current price (or previous close if market is closed)
        todays_data = stock.history(period='1d')
        if todays_data.empty:
            return f"Error: Could not find data for ticker {ticker}. Make sure to use .NS or .BO for Indian stocks."
            
        price = todays_data['Close'].iloc[0]
        
        # 3. Return a clean string to the AI
        return f"The current price of {ticker} is ₹{price:.2f}"
        
    except Exception as e:
        return f"Error fetching price for {ticker}: {str(e)}"
```

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

## Success checklist

- [ ] I understand how the `@tool` decorator works.
- [ ] I understand why we use `yfinance`.
- [ ] I can explain why the docstring inside the tool is critical for the AI's success.
