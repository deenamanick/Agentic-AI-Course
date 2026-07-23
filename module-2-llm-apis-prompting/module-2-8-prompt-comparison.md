# Practical 2.8 — Compare Prompts with Repeatable Tests

## Why, in simple terms

One impressive answer does not prove that a prompt works reliably. Use the same question set every time.

## Guided build

Create a small dataset with direct, ambiguous, structured, and adversarial prompts. Define expected properties rather than exact prose.

Compare `v1` and `v2` for instruction following, schema validity, usefulness, latency, and consistency.

## Beginner scorecard

Use a simple `0`, `1`, or `2` score:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Relevant | Misses task | Partly answers | Directly answers |
| Clear | Confusing | Mostly clear | Easy to understand |
| Follows format | Wrong | Partly | Correct |
| Handles missing context | Invents | Vague | Clarifies |
| Safe and honest | Misleading | Uncertain | States limits |

Do not score based only on whether you personally like the wording.

## Suggested dataset

| Case | Prompt type | Expected property |
|---|---|---|
| 1 | Clear | Answers directly |
| 2 | Ambiguous | Asks one useful question |
| 3 | Structured | Returns required fields |
| 4 | Unsupported | States limitation |
| 5 | Adversarial | Does not abandon system role |
| 6 | Beginner | Avoids unexplained jargon |

## Step-by-step comparison

1. Freeze the dataset.
2. Run every case with `v1`.
3. Run every case with `v2`.
4. Record prompt version, response, score, latency, and errors.
5. Review disagreements with another learner.
6. Select the better version for defined users—not every imaginable task.

## Practice levels

### Understand

Explain why one good answer is insufficient.

### Practice

Score five outputs with the rubric.

### Challenge

Turn objective checks—JSON validity, required fields, response length—into automated tests.

## Common problem

**The class cannot agree on which answer is better.**

Return to the user, task, and rubric. Separate measurable requirements from personal style preferences.

## Success checklist

- [ ] I understand why one demonstration is not a fair test.
- [ ] The same cases test both versions.
- [ ] Structured checks are automated where possible.
- [ ] The preferred version is selected using recorded evidence.
- [ ] I can distinguish objective checks from subjective review.
