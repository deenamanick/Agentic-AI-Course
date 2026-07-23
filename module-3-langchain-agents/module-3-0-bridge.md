# Start Here — How Module 3 Extends Module 2

## What you built so far

In **Module 1**, you built the "Kitchen" — a FastAPI server that takes a question and returns an AI answer.

In **Module 2**, you improved the "Recipe" — you learned to write better prompts, structure outputs as JSON, and refine AI answers.

But here's the limitation: **your AI can only talk. It can't DO anything.**

## The key question Module 3 answers

> Can the AI decide to use a tool — like a calculator, a database, or a web search — on its own?

## Everyday analogy

Imagine you hired a brilliant assistant:

- **Module 1–2 assistant:** You ask "What's 17 × 23?" and they answer "It's approximately 391." *(They guessed! Might be wrong!)*
- **Module 3 assistant:** You ask "What's 17 × 23?" and they say "Let me grab my calculator..." → uses the calculator → "It's exactly 391." ✅

The difference? The Module 3 assistant has **tools** and knows **when to use them**.

## What changes in the code?

| Module 2 | Module 3 |
|---|---|
| `POST /chat` → LLM answers directly | `POST /agent/chat` → LLM can CHOOSE to call tools first |
| One shot: question → answer | Loop: think → act → observe → answer |
| `SystemMessage` + `HumanMessage` | `SystemMessage` + `HumanMessage` + **Tools** |
| LangChain `ainvoke()` | LangGraph **graph execution** |

## What stays the same?

- FastAPI is still the web server
- Groq or Ollama is still the AI provider
- Langfuse still tracks every request
- Pydantic still validates the data

## 🎭 Human Roleplay

Choose four learners:

1. **User:** Asks "What's 125 × 8 minus 17?"
2. **Agent (Brain):** Reads the question. Thinks: "This needs math. I should use the calculator tool."
3. **Calculator Tool:** Receives `(125 * 8) - 17`, computes `983`, returns the number.
4. **Agent (Brain):** Reads the calculator's answer. Says: "The answer is 983."

Now repeat with: "What is Cloudflare Workers?"
- The Agent should think: "This is a general knowledge question. I don't need a tool." → Answers directly.

## Vocabulary

| Word | Simple Meaning |
|---|---|
| Tool | A Python function the AI can choose to call |
| Agent | An AI that can decide which tools to use |
| ReAct | A pattern: **Re**ason about what to do, then **Act** |
| LangGraph | A framework for building agents with clear, predictable steps |

## Success checklist

- [ ] I can explain the difference between a chatbot (Module 2) and an agent (Module 3).
- [ ] I understand that an agent can choose to use tools.
- [ ] I know the code structure stays mostly the same (FastAPI + Groq/Ollama).
- [ ] I can act out the agent flow with the human roleplay.
