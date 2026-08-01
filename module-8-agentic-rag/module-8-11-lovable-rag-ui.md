# Practical 8.5 — Lovable UI for Agentic RAG

## Why

Now that you have a powerful Corrective RAG backend powered by LangGraph, you need a way for users to interact with it. Instead of just testing via terminal/curl, we'll build a beautiful UI using **Lovable**.

## What you will build

A modern React frontend that connects to your `POST /agent/chat` endpoint. It will display the AI's response, the confidence score, and the exact source document it used for the answer.

## Practice: Generate the UI with Lovable

### 1. The Lovable Prompt

Copy the prompt below and paste it into Lovable to generate your UI:

```text
Build a "Smart HR Support Bot" UI.

Frontend Requirements:
- A modern chat interface with the title "Company Policy Assistant".
- When I ask a question, show a "Searching Handbook..." loading animation.
- Display the AI response in a clear chat bubble.
- Under the response, show a "Source Used" tag: (e.g., "Answered using: Vacation Policy").
- Show a "Confidence Score" bar or badge (e.g., "85% match").
- If the AI refuses to answer (due to low confidence), display it in a warning color (like amber or orange).
- Add a "Company Handbooks" sidebar showing a list of topics the bot knows about.
- Use a "Professional Enterprise" theme (slate greys, deep blues, clean typography).

Integration Specs (Mock for Lovable):
- Expecting a POST http://localhost:8000/agent/chat endpoint.
- Request body: { "user_query": "..." }
- Response structure: { "answer": "...", "source_used": "...", "confidence": 0.85, "request_id": "uuid" }

Note: You are building the FRONTEND only. The backend RAG logic and Vector DB are already running locally.
```

### 2. Connect your Backend

Once Lovable generates the code:
1. Export the project to Visual Studio Code.
2. Start your backend API in the `module-8-agentic-rag` folder:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
3. Start the Lovable frontend:
   ```bash
   npm run dev
   ```

## Success checklist

- [ ] You successfully generated the RAG Chat UI in Lovable.
- [ ] The UI sends requests to your local Python API at `http://localhost:8000/agent/chat`.
- [ ] The UI properly displays the `source_used` and `confidence` score returned by LangGraph.
- [ ] You tested an unanswerable question and saw the AI refuse gracefully in the UI.
