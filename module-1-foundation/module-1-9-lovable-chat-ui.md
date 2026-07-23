# Practical 1.9 — Create a Lovable Chat UI and Connect It

## Why, in simple terms

The backend works (we already configured FastAPI to call Groq or Ollama in Practical 1.6), but normal users need a visual interface. Lovable can generate the React interface. Visual Studio Code is where you connect it to the real FastAPI endpoint.

> [!NOTE]
> This practical focuses entirely on the Frontend (React). The backend code that calls Groq or Ollama was already completed in previous steps and doesn't need to be rewritten here.

## Part 1: Copy this prompt into Lovable

```text
Build a beginner-friendly "Local AI Tutor" chat interface using React, Vite, and Tailwind CSS.

Purpose:
The UI will connect to a FastAPI backend endpoint at POST http://127.0.0.1:8000/chat.

Layout:
- A centered chat application with a maximum width of 900px.
- Header title: "Jeevi AI Tutor".
- Subtitle: "Powered by FastAPI and Llama".
- Main message area with separate user and assistant message cards.
- User messages aligned right with an indigo background.
- Assistant messages aligned left with a light neutral background.
- Bottom input area with a multiline text box and Send button.

Behavior:
- Disable Send when the input is empty.
- Show "AI is thinking..." while waiting.
- Pressing Enter sends; Shift+Enter creates a new line.
- Display a friendly error card if the API request fails.
- Display the returned request_id in small text under each assistant answer.
- Add a Clear Chat button.

API contract:
- Request method: POST
- URL: http://127.0.0.1:8000/chat
- Request header: Content-Type: application/json
- Request body: { "user_query": "the student's message" }
- Response: { "answer": "AI response", "request_id": "unique ID" }

Code requirements:
- Put API calls in src/services/chatApi.js.
- Read the backend URL from VITE_API_BASE_URL.
- Do not hardcode secrets in frontend code.
- Use accessible labels and keyboard navigation.
- Frontend only. Do not create a backend or serverless function.
```

## Part 2: Export and open in Visual Studio Code

Open the exported project and install dependencies:

```bash
npm install
```

Create `.env`:

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Part 3: API connection

The service should look similar to:

```javascript
const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export async function sendChatMessage(userQuery) {
  const response = await fetch(`${API_BASE_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_query: userQuery,
    }),
  });

  if (!response.ok) {
    throw new Error(`Chat request failed with status ${response.status}`);
  }

  return response.json();
}
```

## Part 4: Understand CORS

The frontend and backend normally use different development ports. The browser may block the request until FastAPI allows the frontend origin.

This course backend already enables CORS using `FRONTEND_ORIGIN` from `.env`. Its configuration is equivalent to:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)
```

Avoid `allow_origins=["*"]` in a production application.

## Part 5: Run the complete project

Terminal 1:

```bash
ollama serve
```

Terminal 2:

```bash
uvicorn app.main:app --reload
```

Terminal 3, inside the frontend:

```bash
npm run dev
```

## Full data flow

```text
Lovable React UI
   -> fetch()
   -> FastAPI POST /chat (Your backend from Practical 1.6)
   -> ChatGroq or ChatOllama
   -> Llama model
   -> ChatResponse JSON
   -> message displayed in React
```

## Practice tasks

1. Show request IDs in the UI.
2. Add a Retry button after an error.
3. Prevent duplicate submissions while waiting.
4. Add three suggested beginner questions.
5. Test with FastAPI stopped and display a friendly message.

## Success checklist

- [ ] The UI sends the correct request JSON.
- [ ] The AI answer appears in the chat.
- [ ] Loading and error states work.
- [ ] No secrets are stored in frontend code.
- [ ] I can explain the UI-to-model-provider data flow.
