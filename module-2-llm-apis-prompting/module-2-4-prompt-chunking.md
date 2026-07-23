# Practical 2.4 — Break a Large Task into Small Prompts

## Why, in simple terms

You do not eat an elephant in one bite. Large AI tasks become easier to review when divided into visible steps.

## The chunking pattern

Instead of:

```text
Build my complete AI customer support application.
```

Use:

1. Define the user and problem.
2. List the required screens.
3. Design the request and response JSON.
4. Build one backend endpoint.
5. Build one frontend interaction.
6. Test loading, success, and failure.

## Role activity

Give each learner one role:

- Project manager defines the outcome.
- UX designer defines the user flow.
- Developer defines the API contract.
- DevOps engineer defines how services run.
- Tester defines acceptance checks.

Combine their small outputs into one plan.

## Chat practice

Ask the AI to create only the plan. Review it. Then send one step at a time and check the result before continuing.

## Lovable prompt

```text
Build a "Task Chunking Board" for beginners using React and Tailwind CSS.

Requirements:
- A field for one large goal.
- A button labeled "Break into Small Steps".
- Six editable step cards: Understand, Plan, Build, Connect, Test, Explain.
- Each card has Owner, Done When, and Notes fields.
- Add role filters for PM, UX, Developer, DevOps, Tester, and Learner.
- Show a progress bar.
- Use a friendly kanban-style classroom layout.
- Frontend only with mock AI-generated steps.
```

## Success checklist

- [ ] I can divide a large task into reviewable steps.
- [ ] Each step has a visible outcome.
- [ ] I check one step before starting the next.
- [ ] I can explain how different roles contribute.
