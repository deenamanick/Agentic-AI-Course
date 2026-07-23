# Practical 7.4 — Create a Lovable Companion UI 🎨

## Why, in simple terms

To make our Mental Health Companion truly useful, we need a web interface. 

But how does the frontend know what `thread_id` to send to the backend? If the frontend generates a new random `thread_id` every time you refresh the page, the AI will forget you!

We must tell **Lovable** to generate a `thread_id` ONCE, and save it in the browser's **LocalStorage**. This way, even if the user closes their laptop and comes back tomorrow, the browser remembers their ID and the AI remembers their mood.

---

## 🏗️ Step 1: Start your backend

1. Open your terminal in the `module-7-memory-stateful-agents` folder.
2. Make sure your `.env` has Groq configured.
3. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Leave this terminal running!

---

## 🎨 Step 2: The Lovable Prompt

1. Go to [Lovable.dev](https://lovable.dev) and start a new project.
2. Copy and paste the EXACT prompt below.

```text
Build a modern "Mental Health Companion Chat" using React and Tailwind CSS.

Features & Requirements:
1. Connect to my local backend:
   - Endpoint: POST http://localhost:8000/agent/chat
   - Body format: {"user_query": "...", "thread_id": "..."}
   - Response format: {"answer": "...", "request_id": "..."}

2. Thread ID & LocalStorage (CRITICAL):
   - When the app first loads, check LocalStorage for a 'companion_thread_id'.
   - If it doesn't exist, generate a random UUID, save it to LocalStorage, and use it.
   - Every single API request MUST include this 'thread_id' in the JSON body. This is how the AI remembers the user across sessions.

3. UI Layout (Chat Interface):
   - Make it look soothing, calming, and minimalist. Use soft pastel colors (lavender, sage green, or soft blue).
   - Bottom: A chat input bar.
   - Main Area: The chat history.
   - Include a small "Reset Memory" button in the top right corner. Clicking this should delete the 'companion_thread_id' from LocalStorage and reload the page, giving the user a blank slate.

4. Quick Prompts:
   - Add buttons above the chat bar: "I'm feeling anxious", "Can we do a breathing exercise?", "I just want to vent."
```

---

## 🧪 Step 3: Test the UI

Once Lovable builds the app:
1. Click the "I'm feeling anxious" button.
2. Talk to the AI for a bit.
3. **Refresh the page!** 
4. Type: *"Hi, do you remember what I said earlier?"*
5. The AI should remember because Lovable sent the same `thread_id` from your browser's LocalStorage!

---

## 💡 Key Takeaways

- Memory is a two-part system: The Backend must use Checkpointers (like `MemorySaver`) to store the data, and the Frontend must use `LocalStorage` (or user accounts) to remember the `thread_id`.

## Success checklist

- [ ] I successfully generated the UI in Lovable.
- [ ] I can refresh the browser page, send a new message, and confirm the AI still remembers my mood.
- [ ] I understand how LocalStorage on the frontend pairs with MemorySaver on the backend.
