# Practical 1.4 — Build Your First FastAPI Application

## Why, in simple terms

FastAPI turns Python functions into web API endpoints.

Before connecting AI, build the smallest possible API.

## Step 1: Create a learning file

Create `simple_api.py`:

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="My First API")


class GreetingRequest(BaseModel):
    name: str


class GreetingResponse(BaseModel):
    message: str


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "API is working"}


@app.post("/greet", response_model=GreetingResponse)
def greet(request: GreetingRequest) -> GreetingResponse:
    return GreetingResponse(message=f"Hello, {request.name}!")
```

## Step 2: Understand the code

- `FastAPI()` creates the application.
- `BaseModel` describes valid JSON.
- `@app.get("/")` connects a URL to a function.
- `@app.post("/greet")` creates a POST endpoint.
- `response_model` checks the returned JSON.

The `@` line is called a **decorator**. For now, remember: it connects the function below it to an API route.

## Step 3: Run it

```bash
uvicorn simple_api:app --reload
```

- `simple_api` is the filename without `.py`.
- `app` is the FastAPI variable.
- `--reload` restarts the server after code changes.

Open:

```text
http://127.0.0.1:8000/docs
```

Test `GET /` and `POST /greet`.

## Practice tasks

1. Add an `age` integer to `GreetingRequest`.
2. Include the age in the response.
3. Send text instead of a number and inspect the validation error.
4. Add `GET /health` that returns `{"status": "ok"}`.

## Success checklist

- [ ] I can explain an endpoint.
- [ ] I can run Uvicorn.
- [ ] I can test an endpoint in `/docs`.
- [ ] I understand that Pydantic validates JSON.

## Lovable practice prompt

```text
Build a beginner-friendly "API Learning Dashboard" using React and Tailwind CSS.

Requirements:
- Show two API cards: GET /health and POST /greet.
- Each card explains the HTTP method in one simple sentence.
- Add a name input for POST /greet.
- Add a "Send Request" button.
- Show request JSON on the left and response JSON on the right.
- Show status code using green for success and red for error.
- Use a clean classroom theme with large readable text.
- Frontend only. Use mock responses for now.
```
