# Practical 1.3 — How Web APIs, HTTP, and JSON Work

## Why, in simple terms

The chat screen and AI backend are two different programs. They communicate using an API.

Think of a restaurant:

- Frontend = customer
- API request = order
- Backend = kitchen
- API response = completed dish

## Data flow

```text
Chat UI
   |
   | POST /chat with JSON
   v
FastAPI backend
   |
   | sends messages
   v
Ollama model
   |
   | returns an answer
   v
FastAPI returns JSON to the UI
```

## Important words

| Term | Simple meaning |
|---|---|
| URL | Address of an API |
| Endpoint | One API path, such as `/chat` |
| Request | Data sent to the backend |
| Response | Data returned by the backend |
| JSON | A common text format for data |
| Header | Extra information about the request |
| Status code | Number describing the result |

## HTTP methods

- `GET`: read something
- `POST`: create something or start an action
- `PUT` or `PATCH`: update something
- `DELETE`: remove something

Our chat uses `POST` because it sends a new question for processing.

## Request JSON

```json
{
  "user_query": "Explain AI agents simply."
}
```

## Response JSON

```json
{
  "answer": "An AI agent can choose and perform actions...",
  "request_id": "a-unique-id"
}
```

## Status codes to know

- `200`: success
- `201`: created
- `202`: accepted for background processing
- `400`: bad request
- `401`: login required
- `403`: not allowed
- `404`: not found
- `422`: FastAPI validation failed
- `500`: backend error

## Quick browser practice

After starting FastAPI, open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically creates an interactive API page.

## Success checklist

- [ ] I can explain request and response.
- [ ] I know why `/chat` uses `POST`.
- [ ] I can recognize JSON.
- [ ] I know what `200`, `422`, and `500` mean.
