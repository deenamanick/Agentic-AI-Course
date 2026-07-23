# Practical 2.11 — Create a Lovable Prompt Lab UI

## Why

Terminal tests are important, but a visual comparison helps mixed-background learners see prompt behavior, JSON structure, loading, and errors.

## Copy this prompt into Lovable

```text
Build a beginner-friendly "Prompt Version Lab" using React, Vite, and Tailwind CSS.

Purpose:
The UI compares normal and structured responses from a FastAPI prompting lab.

Layout:
- Header: "Jeevi Prompt Version Lab".
- Subtitle: "See how instructions change AI answers".
- Large user-query text area.
- Two mode buttons: Normal Answer and Structured Answer.
- Send Request button.
- A response panel with clear loading, success, and error states.
- Show prompt_version and request_id in small labeled fields.
- In Normal mode, display answer as readable text.
- In Structured mode, display summary and each step as a numbered card.
- Add five suggested prompts: clear, unclear, planning, beginner explanation, and unsupported information.
- Add a small scorecard for Relevant, Clear, Follows Format, Clarifies, and Honest.
- Add Clear and Copy Response buttons.

API contract:

Normal mode:
- POST http://127.0.0.1:8000/chat
- Body: { "user_query": "student text" }
- Response: {
    "answer": "text",
    "request_id": "ID",
    "prompt_version": "v1 or v2"
  }

Structured mode:
- POST http://127.0.0.1:8000/chat/structured
- Body: { "user_query": "student text" }
- Response: {
    "summary": "text",
    "steps": ["step"],
    "request_id": "ID",
    "prompt_version": "v1 or v2"
  }

Code rules:
- Put API functions in src/services/promptLabApi.js.
- Read the backend URL from VITE_API_BASE_URL.
- Never place GROQ_API_KEY or any provider secret in frontend code.
- Prevent duplicate submissions while loading.
- Show friendly messages for HTTP 401, 422, 429, 500, and 502.
- Use accessible labels, keyboard navigation, and strong contrast.
- Frontend only. Do not create a backend or serverless function.
```

## Connect the exported UI

Create `.env` in the frontend:

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

The API service can use:

```javascript
const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

async function postPrompt(path, userQuery) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_query: userQuery,
    }),
  });

  if (!response.ok) {
    const error = new Error(`Request failed: ${response.status}`);
    error.status = response.status;
    throw error;
  }

  return response.json();
}

export function sendNormalPrompt(userQuery) {
  return postPrompt("/chat", userQuery);
}

export function sendStructuredPrompt(userQuery) {
  return postPrompt("/chat/structured", userQuery);
}
```

## Run the complete lab

Terminal 1:

```bash
uvicorn app.main:app --reload
```

Terminal 2, inside the frontend:

```bash
npm install
npm run dev
```

## Compare prompt versions visually

1. Set `PROMPT_VERSION=v1` in the backend `.env`.
2. Restart Uvicorn.
3. Send all suggested prompts and record scores.
4. Set `PROMPT_VERSION=v2`.
5. Restart Uvicorn.
6. Send the same prompts.
7. Compare results rather than relying on memory.

## Error messages learners should understand

| Status | Friendly UI meaning |
|---|---|
| `401` | The backend model-provider key needs attention |
| `422` | The submitted query is missing or invalid |
| `429` | The provider rate limit was reached; wait and retry |
| `500` | The backend had an unexpected problem |
| `502` | The model did not return the required structured format |

## Practice levels

### Understand

Identify the user query, endpoint, response, prompt version, and request ID on screen.

### Practice

Compare `v1` and `v2` using the same five prompts.

### Challenge

Store comparison results locally and export a Markdown report without storing API keys or sensitive prompts.

## Success checklist

- [ ] Both endpoint modes work.
- [ ] Normal and structured responses render differently.
- [ ] Prompt version and request ID are visible.
- [ ] Errors are explained in beginner-friendly language.
- [ ] No provider key appears in frontend code.
