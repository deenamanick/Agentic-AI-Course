# Practical 1.2b — How the Internet Works (Frontend vs Backend)

## Why, in simple terms

Before we start building an AI application, we need to understand how the internet allows different pieces of software to talk to each other. When you use an app on your phone or visit a website, there is a lot happening behind the scenes. 

Understanding these concepts will make building your AI Agent much easier.

## The Two Main Roles: Frontend and Backend

Imagine a restaurant:
1. **The Frontend (The Dining Room):** This is what the customer sees and interacts with. It’s the menu, the tables, and the waiter. In software, the frontend is the visual interface (buttons, text, colors) that runs in your web browser (like Chrome or Safari). It is typically built using HTML, CSS, and JavaScript.
2. **The Backend (The Kitchen):** This is where the actual work gets done. The customer doesn't see the chefs cooking, they just get their food. In software, the backend is a server running code (in our case, Python) that processes data, talks to databases, and communicates with AI models.

## How do they talk? The Request-Response Cycle

The Frontend and Backend communicate using a system called **HTTP (Hypertext Transfer Protocol)**. 

1. **The Request:** The Frontend asks the Backend to do something. (e.g., "Here is a math problem, please solve it.")
2. **The Response:** The Backend processes the request and sends data back. (e.g., "The answer is 42.")

## What is an API?

API stands for **Application Programming Interface**. 

If the Frontend is the customer and the Backend is the kitchen, the **API is the waiter**. The waiter takes your order, brings it to the kitchen, and then brings your food back.

An API is simply an agreed-upon set of rules that allows two programs to talk to each other. When you build an AI backend, you are creating an API that says, "If you send me a text message, I will ask an AI model and return the response."

## How does the Frontend make a Request? (fetch)

In modern web development, the Frontend uses a JavaScript function called `fetch()` to send a request to the Backend API.

You don't need to write this code right now, but later in this module, the AI tool (Lovable) will generate code that looks like this:

```javascript
// The Frontend sending a message to our Python Backend
const response = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ user_query: "Hello AI!" })
});
```

This tells the browser: "Hey, send this JSON data to my backend at port 8000."

## Success checklist

- [ ] I understand the difference between the Frontend and the Backend.
- [ ] I know that they communicate using HTTP Requests and Responses.
- [ ] I can explain what an API does using the restaurant analogy.
