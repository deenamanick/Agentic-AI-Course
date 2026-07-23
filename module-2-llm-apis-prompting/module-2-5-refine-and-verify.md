# Practical 2.5 — Refine Prompts and Check AI Mistakes

## Why, in simple terms

The first answer is a draft, not a final truth. Refinement means giving specific feedback. Verification means checking claims and code.

## The three-step loop

```text
Ask -> Inspect -> Improve
```

### Ask

Give a clear first prompt.

### Inspect

Check:

- Did it answer the real question?
- Is any context missing?
- Are facts supported?
- Did it invent a package, API, or result?
- Is the explanation suitable for the learner?

### Improve

Give specific feedback:

```text
Keep the restaurant analogy.
Define "endpoint" before using it.
Remove the deployment section.
Add one example request and response.
Use no more than 200 words.
```

## Safe debugging prompt

```text
Do not rewrite everything yet.

1. Explain the error in simple language.
2. Identify the most likely line.
3. Suggest the smallest change.
4. Explain how to verify the fix.
5. State what information is missing.
```

## Three red flags

1. A package or function cannot be found in official documentation.
2. The answer asks you to expose a secret in frontend code.
3. It claims an action succeeded without evidence.

## Lovable prompt

```text
Build an "AI Answer Review Checklist" using React and Tailwind CSS.

Requirements:
- Large text area for an AI answer.
- Checklist sections: Relevance, Clarity, Evidence, Safety, and Testability.
- Red-flag buttons for Invented API, Exposed Secret, Unsupported Claim, and Too Complex.
- A feedback builder that creates a refinement prompt.
- Copy Feedback button.
- Use calm green, amber, and red status colors with accessible labels.
- Frontend only. Do not send the pasted answer anywhere.
```

## Success checklist

- [ ] I treat the first answer as a draft.
- [ ] I can give specific refinement feedback.
- [ ] I know at least three AI red flags.
- [ ] I verify important claims with evidence or tests.
