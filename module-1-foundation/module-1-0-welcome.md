# Start Here — You Belong in This Course

## First message to every learner

You are not expected to be a Python developer, AI engineer, or backend expert.

This course teaches one small idea at a time. Copying working code is allowed. Asking what a word means is encouraged. Errors are part of the practical, not evidence that you cannot learn.

## What is Agentic AI? (Real-World Use Cases)

Unlike a traditional ChatGPT interface (where you ask a question and it just returns text), **Agentic AI** refers to systems that can plan, use tools, interact with external systems, and autonomously execute multi-step workflows to achieve a goal. 

As you progress through this course, you will build the foundations to create agents like:
- **Software Engineering Assistants:** Agents that can read a codebase, identify bugs, write code, run tests, and open pull requests autonomously.
- **Autonomous Customer Support:** Agents that don't just answer questions, but take action (e.g., verifying identity, hitting a billing API, and processing a refund).
- **Data Analysis Automation:** Agents that scrape the web for competitor pricing, run a Python script to format it, and email a summarized report to the team.
- **IT Operations (Auto-Remediation):** Agents that receive server failure alerts, SSH into the server, kill the rogue process, and write a post-mortem report.
- **Personal Assistants:** Agents that manage your daily life by reading emails, drafting replies, and scheduling calendar events automatically.

## The same system from different viewpoints

We are building an AI tutor. Groq is the default classroom provider, so students do not need a local GPU. Ollama remains an optional local path.

| Learner background | Familiar way to understand it |
|---|---|
| Project manager | A request moves through defined stages and returns an outcome |
| DevOps engineer | Services communicate over ports and produce observable requests |
| UX designer | A user action needs loading, success, and error experiences |
| Homemaker | A recipe accepts ingredients, follows steps, and produces a result |
| Teacher | A student asks, the tutor interprets, and an answer returns |
| Developer | A typed client-server request flows through an LLM adapter |

No viewpoint is the “correct” one. They describe the same system at different levels.

## The complete picture before code

```text
Student types a question
        |
        v
Chat screen sends the question
        |
        v
FastAPI checks the request
        |
        v
Groq or Ollama asks a Llama model
        |
        v
FastAPI returns the answer
        |
        v
Chat screen displays it
```

## Human roleplay

Choose five people:

1. **Student** writes a question on paper.
2. **Frontend** carries the question.
3. **FastAPI** checks that a question exists.
4. **Model provider** writes an answer.
5. **Frontend** carries the answer back.

Repeat with an empty question. FastAPI should reject it before the model provider receives it.

## Words to become comfortable with

- **Frontend:** what a user sees
- **Backend:** code that processes requests
- **API:** an agreed way for programs to communicate
- **Model:** software that generates the AI response
- **Prompt:** instructions and input given to the model
- **Trace:** a record of what happened

You only need recognition now. Later practicals make each word concrete.

## Personal learning goal

Complete this sentence:

> By the end of Module 1, I want to confidently explain ________.

Examples:

- how a chat screen reaches an AI model
- what Python does in an AI application
- why an API is needed
- how to test a backend

## Success checklist

- [ ] I can describe the complete flow without technical detail.
- [ ] I know this course does not assume a developer background.
- [ ] I have written one personal learning goal.
- [ ] I am comfortable asking for a simpler explanation.
