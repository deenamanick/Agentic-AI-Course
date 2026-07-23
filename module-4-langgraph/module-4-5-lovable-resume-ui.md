# Practical 4.5 — Create a Lovable Resume UI 🎨

## Why, in simple terms

A Markdown string in a terminal is cool, but real users need a beautiful interface! Let's use **Lovable** to build a modern React UI that talks to our new Resume Builder endpoint.

This UI will allow users to type in their messy brain-dump, and it will render the Markdown response into a beautiful, printable resume.

---

## 🏗️ Step 1: Start your backend

Make sure your FastAPI server is running with the correct settings.

1. Open your terminal in the `module-4-langgraph` folder.
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
Build a modern "AI Resume Builder" using React and Tailwind CSS.

Features & Requirements:
1. Connect to my local backend:
   - Endpoint: POST http://localhost:8000/resume/build
   - Body format: {"raw_text": "..."}
   - Response format: {"markdown_resume": "..."}

2. UI Layout (Split Screen):
   - Left Side (Input): A large textarea where the user can dump their messy work history, skills, and background. Include a prominent "Build Resume" button.
   - Right Side (Output): A clean, white, paper-like preview area. It should use `react-markdown` to render the `markdown_resume` received from the API.

3. Loading State:
   - When the user clicks "Build Resume", show a modern skeleton loader or spinner on the Right Side with text saying "Extracting data & drafting summary...". 
   - LangGraph workflows take a few seconds, so the loading state must be obvious.

4. Print Functionality:
   - Add a "Download PDF" or "Print" button above the Right Side output area. When clicked, it should trigger the browser's native print dialog (just printing the resume preview area).
```

---

## 🧪 Step 3: Test the UI

Once Lovable builds the app:
1. Type a messy paragraph about yourself in the left box.
2. Click "Build Resume".
3. Watch as the AI workflow extracts your data, writes a professional summary, and formats it.
4. Click the Print button to save it as a PDF!

---

## 💡 Key Takeaways

- You built a complex, deterministic AI pipeline in Python, and easily connected it to a modern React frontend.
- By having the Python API return **Markdown**, the frontend can easily render it, style it, and print it. This is a very common architecture pattern!

## Success checklist

- [ ] I successfully generated the UI in Lovable.
- [ ] I can type my experience and see a formatted resume generated on the screen.
- [ ] I understand why returning Markdown from the API is easier than generating a raw PDF file on the server.
