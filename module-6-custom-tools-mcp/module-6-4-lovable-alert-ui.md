# Module 6.4: Create a Lovable Alert UI 🎨

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: The Setup (Visual Studio Code)** - Start your backend API server.
> 2. **Phase 2: The UI (Lovable AI)** - Copy the prompt below into Lovable to generate your dashboard.
> 3. **Phase 3: The Integration** - Test the full stock tool + email tool flow from the UI.

### Why (in simple terms)

A command line agent is cool, but real users want a dashboard! Let's use **Lovable** to build a modern "Stock Alert Dashboard" web app that connects to our local API. 

### What you'll learn
1. **Lovable UI**: How to generate a frontend quickly.
2. **API Integration**: How to connect a UI to a local agent backend.
3. **Full Stack Agents**: How to piece everything together into a real app.

---

## 🌊 Visual Studio Code Practice: Start your Backend

### Step 1: Start the API

1. Open your terminal in the `module-6-custom-tools-mcp` folder.
2. Make sure your `.env` has Groq configured.
3. **Make sure `MOCK_EMAILS=true` so you don't accidentally spam yourself while testing!**
4. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Leave this terminal running!

### Step 2: Verify it's working

In a **second terminal**, test the agent with curl:

```bash
curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query": "What is the price of RELIANCE.NS?"}'
```

You should get a JSON response with the stock price. If this works, your backend is ready!

---

## 🎨 Lovable AI Prompt (The Agent Dashboard)

*Copy and paste this into [Lovable.dev](https://lovable.dev) to build a professional Agent UI!*

1. Go to [Lovable.dev](https://lovable.dev) and start a new project.
2. Copy and paste the EXACT prompt below.

```text
Build a modern "AI Stock Alert Agent" using React and Tailwind CSS.

Features & Requirements:
1. Connect to my local backend:
   - Endpoint: POST http://localhost:8000/agent/chat
   - Body format: {"user_query": "..."}
   - Response format: {"answer": "...", "request_id": "..."}

2. UI Layout (Chat Interface):
   - This should look like a modern, sleek chat interface (similar to ChatGPT or Claude).
   - Bottom: A chat input bar with a "Send" button.
   - Main Area: The chat history. User messages on the right, AI responses on the left.

3. Quick Action Buttons:
   - Above the chat input, place three "Quick Prompt" buttons that populate the input when clicked:
     - "What is the price of RELIANCE.NS and TCS.BO?"
     - "Check if INFY.NS is above ₹3000. If so, email alert@example.com."
     - "What is the price of HDFCBANK.NS?"

4. Loading State:
   - When waiting for the API, show a pulsing "Agent is thinking and using tools..." indicator.

5. Styling:
   - Make it look premium, dark mode by default, with financial/stock market aesthetics (maybe subtle green/red accents).
```

---

## 🧪 Visual Studio Code Practice: Test the Full Flow

### Step 3: Test stock prices

Once Lovable builds the app:

| Step | What to do | What to expect |
| :--- | :--- | :--- |
| 1 | Click: *"What is the price of RELIANCE.NS and TCS.BO?"* | Agent calls `get_stock_price` twice and shows both prices |
| 2 | Click: *"What is the price of HDFCBANK.NS?"* | Agent calls `get_stock_price` once and shows the price |

### Step 4: Test email alerts

| Step | What to do | What to expect |
| :--- | :--- | :--- |
| 1 | Click: *"Check if INFY.NS is above ₹3000..."* | Agent checks the price first |
| 2 | Watch the uvicorn terminal | You should see `[MOCK EMAIL]` printed (not a real email!) |
| 3 | The chat response | Agent confirms the mock email was "sent" |

> [!TIP]
> If you see `[MOCK EMAIL]` in your uvicorn terminal, everything is working perfectly! The agent chained both tools together automatically.

---

## 💡 Key Takeaways

- You successfully built an agent that can interact with the real world using custom tools.
- You handled the dangers of Write Tools (emails) by using Mocking during development.
- The Lovable UI connects to the same `POST /agent/chat` endpoint you've been testing with curl.

## Checklist

- [ ] You verified the backend works with curl before starting Lovable.
- [ ] You successfully generated the UI in Lovable.
- [ ] The agent correctly fetched live Indian stock prices via the chat UI.
- [ ] The agent successfully used the email tool and you saw `[MOCK EMAIL]` in the terminal.
