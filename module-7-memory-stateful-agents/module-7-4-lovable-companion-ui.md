# Module 7.4: Create a Lovable Companion UI 🎨

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: The Setup (Visual Studio Code)** - Make sure your backend is running.
> 2. **Phase 2: The UI (Lovable AI)** - Copy the prompt below into Lovable to generate your frontend.
> 3. **Phase 3: The Integration** - Test the memory by chatting, refreshing the page, and chatting again.

### Why (in simple terms)

To make our Mental Health Companion truly useful, we need a web interface. 

But how does the frontend know what `thread_id` to send to the backend? If the frontend generates a new random `thread_id` every time you refresh the page, the AI will forget you!

We must tell **Lovable** to generate a `thread_id` ONCE, and save it in the browser's **LocalStorage**. This way, even if the user closes their laptop and comes back tomorrow, the browser remembers their ID and the AI remembers their mood.

### What you'll learn
1. **Lovable UI**: How to generate a mental health chat interface.
2. **LocalStorage**: How the frontend remembers the Thread ID across browser refreshes.
3. **Full Stack Memory**: How backend Checkpointers + frontend LocalStorage work together.

---

## 🌊 Visual Studio Code Practice: Start your Backend

### Step 1: Start the API

1. Open your terminal in the `module-7-memory-stateful-agents` folder.
2. Make sure your `.env` has Groq configured.
3. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Leave this terminal running!

---

## 🎨 Lovable AI Prompt (The Companion Chat)

*Copy and paste this into [Lovable.dev](https://lovable.dev) to build a calming companion UI!*

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

## 🧪 Visual Studio Code Practice: Test the UI

### Step 2: Test Memory Persistence

Once Lovable builds the app:

| Step | What to do | What to expect |
| :--- | :--- | :--- |
| 1 | Click the **"I'm feeling anxious"** button | The AI responds with empathy |
| 2 | Chat for a bit about your stress | Normal conversation |
| 3 | **Refresh the page!** (Ctrl+R / Cmd+R) | Chat history may clear, but `thread_id` stays in LocalStorage |
| 4 | Type: *"Hi, do you remember what I said earlier?"* | ✅ The AI should remember because the same `thread_id` was sent! |

### Step 3: Test the Reset Button

| Step | What to do | What to expect |
| :--- | :--- | :--- |
| 1 | Click the **"Reset Memory"** button in the top-right corner | Page reloads, new `thread_id` is generated |
| 2 | Type: *"Do you remember me?"* | ❌ The AI has no memory — brand new `thread_id`! |

---

## 🔗 How Frontend + Backend Memory Work Together

| Layer | Technology | What it stores | Why |
| :--- | :--- | :--- | :--- |
| **Frontend** | Browser LocalStorage | The `thread_id` (a UUID) | So the same ID is sent on every request |
| **Backend** | LangGraph MemorySaver | The full conversation history | So the AI can recall past messages |

> [!IMPORTANT]
> Memory is a **two-part system**. If either part breaks, the AI forgets:
> - If the frontend loses the `thread_id` → new ID → empty memory box → AI forgets
> - If the backend restarts (with MemorySaver) → RAM is cleared → AI forgets

---

## 💡 Key Takeaways

- Memory is a two-part system: The Backend uses Checkpointers to store the data, and the Frontend uses LocalStorage to remember the `thread_id`.
- The "Reset Memory" button works by simply deleting the `thread_id` from LocalStorage.

## Checklist

- [ ] You successfully generated the UI in Lovable.
- [ ] You can refresh the browser page, send a new message, and confirm the AI still remembers your mood.
- [ ] You understand how LocalStorage on the frontend pairs with MemorySaver on the backend.
