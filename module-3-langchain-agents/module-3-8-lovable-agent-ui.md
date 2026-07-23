# Practical 3.8 — Create a Lovable Agent UI

## Why, in simple terms

Testing an API with `curl` or Postman is great for developers, but real users need a visual interface. Let's use **Lovable** to build a modern React UI that talks to our new Agent endpoint!

Unlike a simple chat UI, an "Agent" UI should look like it's doing work. We want to show loading states that say "Agent is thinking..." because agent queries take longer (due to the Think → Act → Observe loop).

---

## 🏗️ Step 1: Start your backend

Make sure your FastAPI server is running with the correct settings.

1. Open your terminal in the `module-3-langchain-agents` folder.
2. Make sure your `.env` has Groq configured (or Ollama if you prefer).
3. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Leave this terminal running!

---

## 🎨 Step 2: The Lovable Prompt

1. Go to [Lovable.dev](https://lovable.dev) and start a new project.
2. Copy and paste the EXACT prompt below.

> [!TIP]
> **Pro Tip:** In Lovable, you can paste this into the main chat box to generate the whole app in one go!

```text
Build a modern "AI Agent Interface" using React and Tailwind CSS.

Features & Requirements:
1. Connect to my local backend:
   - Endpoint: POST http://localhost:8000/agent/chat
   - Body format: {"user_query": "..."}
   - Response format: {"answer": "...", "request_id": "..."}

2. UI Layout:
   - A clean, dark-mode terminal aesthetic (slate-900 background).
   - A header that says "Jeevisoft Autonomous Agent".
   - A main chat area showing the conversation history.
   - User messages should align right (blue bubbles).
   - Agent messages should align left (gray bubbles with a robot 🤖 icon).
   - A prominent input bar at the bottom.

3. Agent UX (Crucial!):
   - When the user submits, immediately show their message.
   - Show a "Thinking..." indicator that looks like a console loader (e.g. `[  Processing  ]`) while waiting for the fetch response.
   - Agents take longer to reply than simple chatbots because they use tools, so the loading state must be very obvious.

4. Example Prompts:
   - Add three clickable suggestion chips above the input bar:
     a) "Calculate (125 * 8) - 17"
     b) "What is the current Unix timestamp?"
     c) "What is Python?"
   - Clicking a chip should immediately send that query.
```

---

## 🧪 Step 3: Test the UI

Once Lovable builds the app, test the three suggestions! 

Notice the speed difference:
- "What is Python?" will be fast (No tools needed).
- The Math and Time questions will take slightly longer (Agent uses the `calculator` or `now_unix` tools).

---

## 💡 Key Takeaways

- Building UIs for **Agents** requires better loading states because the multi-step reasoning loop takes time.
- Because we added `CORSMiddleware` to our FastAPI `app/main.py`, a web app like Lovable can talk directly to our local Python server.

## Success checklist

- [ ] I successfully generated the UI in Lovable.
- [ ] I can see the "Thinking..." state when sending a request.
- [ ] The UI successfully displays answers from the local Python agent.
