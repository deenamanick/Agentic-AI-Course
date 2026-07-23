# Practical 2.2 — Turn Vague Requests into Structured Prompts

## Why, in simple terms

“Make something good” forces the AI to guess. A structured prompt is like a clear project brief.

## The five-part prompt

```text
ROLE: Who should the AI act as?
TASK: What exact result is needed?
CONTEXT: Who is it for and what information matters?
RULES: What boundaries must it follow?
OUTPUT: What format should it return?
```

## From vague to clear

Vague:

```text
Explain FastAPI.
```

Structured:

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

## Mixed-background practice

Explain the same concept for:

- A UX designer
- A DevOps engineer
- A homemaker
- A Python developer

Notice that the core truth stays the same while analogy and detail change.

## Guided classroom activity

Start with:

```text
Create a project plan.
```

Ask the class five questions:

1. Who should the AI act as?
2. What exact project is being planned?
3. Who will use the plan?
4. What limits or requirements apply?
5. What output format is easiest to review?

Write the answers into the five-part template. Run both prompts and compare how much the AI had to guess.

## Practice levels

### Understand

Circle Role, Task, Context, Rules, and Output in a prepared prompt.

### Practice

Rewrite one vague request using all five parts.

### Challenge

Create two versions for different learner backgrounds without changing the technical truth.

## Lovable prompt

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

## Success checklist

- [ ] I can identify all five prompt parts.
- [ ] I can improve a vague request.
- [ ] I can adapt an explanation without stereotyping the learner.
- [ ] I understand that a good prompt reduces guessing.

## Common problem

**The prompt becomes very long but the result is not better.**

Remove background information that does not affect the task. More text is not automatically more context.
