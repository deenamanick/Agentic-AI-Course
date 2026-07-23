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

## Understand

- System prompt = application behavior and boundaries
- User prompt = the current request
- Neither prompt alone guarantees security; permissions must also be enforced in code

## Success checklist

- [ ] I can explain system and user prompts using an analogy.
- [ ] User data remains separate from system policy.
- [ ] Prompt inputs are visible and testable.
- [ ] Untrusted text is never inserted as system instructions.
