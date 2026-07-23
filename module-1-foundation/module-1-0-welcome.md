# Start Here — You Belong in This Course

## First message to every learner

You are not expected to be a Python developer, AI engineer, or backend expert.

This course teaches one small idea at a time. Copying working code is allowed. Asking what a word means is encouraged. Errors are part of the practical, not evidence that you cannot learn.

## The same system from different viewpoints

We are building a local AI tutor.

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
Ollama asks the local AI model
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
4. **Ollama** writes an answer.
5. **Frontend** carries the answer back.

Repeat with an empty question. FastAPI should reject it before Ollama receives it.

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
