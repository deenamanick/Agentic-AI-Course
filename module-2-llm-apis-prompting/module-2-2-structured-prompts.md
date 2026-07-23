# Practical 2.2 — Turn Vague Requests into Structured Prompts (The Architect's Blueprint)

## Why, in simple terms

If you just say "make something good," the AI will **guess**. If you give it a **Structured Prompt**, it's like giving an architect a **blueprint**. You get exactly what you want, no guesswork.

---

## 🏗️ The 5-Part Prompt Template

Use this structure every time for better results:

```text
1. ROLE:    Who should the AI act as?
2. TASK:    What exact result is needed?
3. CONTEXT: Who is it for and what information matters?
4. RULES:   What boundaries must it follow?
5. OUTPUT:  What format should it return?
```

---

## 🎯 Before vs After: See the Difference!

### ❌ The Vague Prompt

```text
Explain FastAPI.
```

**What the AI might return:**
> FastAPI is a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints. It provides automatic interactive documentation, data validation using Pydantic models, dependency injection, OAuth2 security, and async support with high performance comparable to NodeJS and Go...
> *(3 paragraphs of technical jargon with code the student can't read yet)*

### ✅ The Structured Prompt

```text
ROLE: You are a patient technology trainer.
TASK: Explain what FastAPI does.
CONTEXT: The learner is a project manager with no Python experience.
RULES:
- Use no more than 150 words.
- Use a restaurant analogy.
- Define API and endpoint.
- Do not include code yet.
OUTPUT: Return a short explanation and three check questions.
```

**What the AI returns:**
> Imagine a restaurant. The **kitchen** cooks food, but customers can't walk into the kitchen directly. They use a **waiter** — that's the **API** (Application Programming Interface). An **endpoint** is a specific item on the menu — like "/order-pizza."
>
> **FastAPI** is a tool that helps Python developers build these "waiters" quickly and correctly...
>
> **Check questions:**
> 1. What does API stand for?
> 2. What is an endpoint?
> 3. Why can't the customer go directly to the kitchen?

**💡 Notice the difference?** The same AI, the same model, but wildly different output quality. The only thing that changed was the **prompt**.

---

## 🎭 Guided Classroom Activity

Start with this vague prompt:

```text
Create a project plan.
```

Now ask the class these five questions:

1. 🎭 **ROLE:** Who should the AI act as? *(A senior project manager? A Scrum master?)*
2. 📋 **TASK:** What exact project is being planned? *(An AI chatbot? A mobile app?)*
3. 👥 **CONTEXT:** Who will use the plan? *(A startup CEO? A classroom instructor?)*
4. 🚧 **RULES:** What limits or requirements apply? *(Max 5 steps? Use agile? No budget discussion?)*
5. 📄 **OUTPUT:** What output format is easiest to review? *(Bullet points? A table? JSON?)*

Write the answers into the five-part template. Run **both** prompts (the vague one and the structured one) and compare how much the AI had to guess.

---

## 👥 Mixed-Background Practice

Explain the same concept (FastAPI) for different learner backgrounds:

- **A UX designer:** Focus on user experience and API response times
- **A DevOps engineer:** Focus on deployment, ports, and server configuration
- **A homemaker:** Focus on the kitchen/restaurant analogy
- **A Python developer:** Focus on decorators, type hints, and async

Notice that the **core truth stays the same** while the analogy and detail level change.

---

## Practice Levels

### Understand
Circle the Role, Task, Context, Rules, and Output in a prepared prompt.

### Practice
Rewrite one vague request using all five parts.

### Challenge
Create two versions for different learner backgrounds without changing the technical truth.

---

## 🎨 Lovable Prompt

```text
Build a "Prompt Builder for Beginners" using React and Tailwind CSS.

Layout:
- Five large fields: Role, Task, Context, Rules, and Output.
- Give a simple example under every field.
- Add learner persona buttons: Project Manager, DevOps, UX Designer, Homemaker, Developer.
- Show the generated prompt in a preview panel.
- Add Copy Prompt and Clear buttons.
- Add a "Why this helps" panel using beginner-friendly language.
- Use a warm classroom design with large text and strong contrast.
- Frontend only. Store no API keys.
```

---

## Common Problem

**The prompt becomes very long but the result is not better.**

Remove background information that does not affect the task. More text is not automatically more context. A focused 5-line structured prompt beats a 50-line essay.

## Success checklist

- [ ] I can identify all five prompt parts.
- [ ] I can dramatically improve a vague request.
- [ ] I can adapt an explanation without stereotyping the learner.
- [ ] I understand that a good prompt reduces guessing.
