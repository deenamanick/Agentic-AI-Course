# Practical 2.3 — Separate System and User Prompts

## Why, in simple terms

Think of a restaurant:

- The restaurant policy is the **system prompt**.
- The customer’s order is the **user prompt**.

The customer can choose food, but cannot rewrite the restaurant’s safety policy.

## Human roleplay

One learner is the tutor and receives a private role card:

> Explain concepts using simple words and one example. Never pretend to know information you do not have.

Another learner asks three questions. Discuss which instructions remain stable and which content changes.

## Connect to code

Find these in `app/main.py`:

```python
SystemMessage(content=SYSTEM_PROMPT)
HumanMessage(content=req.user_query)
```

Test the same user request under two safe system roles. Then try a user message that asks to ignore the system role.

The application selects the system prompt here:

```python
SystemMessage(
    content=get_system_prompt(prompt_version)
)
```

The learner’s input stays separate:

```python
HumanMessage(content=req.user_query)
```

## Understand

- System prompt = application behavior and boundaries
- User prompt = the current request
- Neither prompt alone guarantees security; permissions must also be enforced in code

## Practice levels

### Understand

Sort prepared instruction cards into “system behavior” and “current user task.”

### Practice

Change the teaching style in `SYSTEM_PROMPT_V2` and compare one response.

### Challenge

Create a safe role for a beginner tutor that asks for clarification rather than inventing missing details.

## Common problem

**The user asks the model to ignore all previous instructions.**

Do not rely on the prompt as the only security control. Tool permissions, authentication, validation, and approval belong in application code.

## Success checklist

- [ ] I can explain system and user prompts using an analogy.
- [ ] User data remains separate from system policy.
- [ ] Prompt inputs are visible and testable.
- [ ] Untrusted text is never inserted as system instructions.
