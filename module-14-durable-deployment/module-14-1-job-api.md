# Practical 14.1 — Design the Asynchronous Job API

## Build

Design:

- `POST /jobs`
- `GET /jobs/:id`
- `POST /jobs/:id/cancel`

Long work returns `202 Accepted` with job ID, status URL, and retry guidance.

## Success checklist

- [ ] Submission does not wait for completion.
- [ ] Schemas and status codes are documented.
- [ ] Every operation requires authentication.
