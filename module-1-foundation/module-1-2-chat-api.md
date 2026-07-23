# Practical 1.2 — Understand and Run the Chat API

## Build

Read `app/main.py` and identify request validation, model construction, messages, tracing, and response construction. Start the API with Uvicorn and call `POST /chat`.

## Practice

Send valid JSON, missing fields, an empty query, and malformed JSON. Record the HTTP status and response shape.

## Success checklist

- [ ] The API returns an answer and request ID.
- [ ] Invalid payloads are rejected.
- [ ] You can draw the request-to-model data flow.
