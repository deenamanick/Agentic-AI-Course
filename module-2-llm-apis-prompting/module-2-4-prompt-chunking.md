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

## Done-when rule

Every chunk needs a visible completion check.

| Chunk | Done when |
|---|---|
| Define user | One primary user and problem are written |
| Design API | Request and response JSON are agreed |
| Build endpoint | The endpoint returns a tested response |
| Connect UI | Loading, success, and failure are visible |
| Test | Acceptance checks pass |

Without “done when,” a small task can still be vague.

## Practice levels

### Understand

Arrange prepared project-step cards in a sensible order.

### Practice

Break “build an AI tutor” into no more than six chunks.

### Challenge

Identify which chunks can happen in parallel and which depend on earlier work.

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

## Common problem

**The AI writes code for every step at once.**

Ask only for a plan first. Then explicitly say: “Implement Step 1 only and stop for review.”
