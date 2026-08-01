# Module 6.4: Create a Lovable Alert UI 🎨

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: The Setup** - Start your local backend API.
> 2. **Phase 2: The UI (Lovable AI)** - Use the provided prompt in Lovable to generate your dashboard.
> 3. **Phase 3: The Integration** - Connect your Lovable UI to your local AI Agent.

### Why (in simple terms)

A command line agent is cool, but real users want a dashboard! Let's use **Lovable** to build a modern "Stock Alert Dashboard" web app that connects to our local API. 

### What you'll learn
1. **Lovable UI**: How to generate a frontend quickly.
2. **API Integration**: How to connect a UI to a local agent backend.
3. **Full Stack Agents**: How to piece everything together into a real app.

---

## 🌊 Visual Studio Code Practice: Backend & Testing

### Step 1: Start your backend

1. Open your terminal in the `module-6-custom-tools-mcp` folder.
2. Make sure your `.env` has Groq configured. **Make sure `MOCK_EMAILS=true` so you don't accidentally spam yourself while testing!**
3. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Leave this terminal running!

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

## 🧪 Step 3: Test the UI

Once Lovable builds the app:
1. Click the quick prompt: *"What is the price of RELIANCE.NS and TCS.BO?"*
2. The agent will "think", call the `get_stock_price` tool twice, and return the answer in the chat!
3. Click the email alert prompt. Watch the agent check the price and (mock) send an email!

---

## 💡 Key Takeaways

- You successfully built an agent that can interact with the real world using custom tools.
- You handled the dangers of Write Tools (emails) by using Mocking during development.

## Checklist

- [ ] You successfully generated the UI in Lovable.
- [ ] The agent correctly fetched live Indian stock prices via the chat UI.
- [ ] The agent successfully used the email tool when requested.
