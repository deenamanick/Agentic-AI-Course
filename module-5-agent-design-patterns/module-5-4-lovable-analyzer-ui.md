# Practical 5.4 — Create a Lovable Analyzer UI 🎨

## Why, in simple terms

A command line API is hard for non-technical users to use. Let's use **Lovable** to build a modern "Job Analyzer" web app that connects to our local API. 

Because our Reflection Pattern takes about 4-6 seconds to run, we MUST include a very clear loading state in the UI so the user doesn't think the app is broken!

---

## 🏗️ Step 1: Start your backend

1. Open your terminal in the `module-5-agent-design-patterns` folder.
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
Build a modern "AI Job CV Analyzer" using React and Tailwind CSS.

Features & Requirements:
1. Connect to my local backend:
   - Endpoint: POST http://localhost:8000/analyzer/score
   - Body format: {"raw_cv": "...", "job_title": "..."}
   - Response format: {"final_review": "...", "request_id": "..."}

2. UI Layout (Split Screen):
   - Left Side (Input): 
     - A text input for "Target Job Title" (e.g. Senior Data Engineer).
     - A large textarea where the user can paste their CV.
     - A prominent "Analyze CV" button.
   - Right Side (Output): 
     - A clean, modern panel. Use `react-markdown` to render the `final_review` received from the API.

3. Loading State (CRITICAL):
   - When the user clicks "Analyze CV", show a multi-step loading animation on the Right Side.
   - It should say:
     - "Step 1: Drafting initial review..." (show for 2 seconds)
     - "Step 2: Senior HR Manager critiquing draft..." (show for 2 seconds)
     - "Step 3: Refining final output..." 
   - Note: The API does all of this on the backend and takes about 6 seconds. The frontend animation is just a visual placebo to keep the user entertained while they wait.

4. Styling:
   - Make it look like a premium SaaS tool (think Vercel or Stripe aesthetics).
   - Use nice drop shadows and a clean typography hierarchy.
```

---

## 🧪 Step 3: Test the UI

Once Lovable builds the app:
1. Type a fake Job Title.
2. Paste a terrible CV.
3. Click "Analyze CV" and watch your 3-step placebo loading animation!
4. Read the final output. Does it look like a harsh HR Manager reviewed it?

---

## 💡 Key Takeaways

- Complex Agent patterns (like Reflection) take longer to execute than standard LLM calls.
- As a full-stack engineer, you must handle this latency gracefully on the frontend using multi-step loading animations to keep the user engaged.

## Success checklist

- [ ] I successfully generated the UI in Lovable.
- [ ] I saw the multi-step loading animation while waiting for the 6-second API call.
- [ ] The UI successfully displays the Markdown review from the local Python agent.
