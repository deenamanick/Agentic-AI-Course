# Start Here — How Module 2 Extends Module 1

## What stays the same?

Module 1 created this flow:

```text
User -> FastAPI -> Groq or Ollama -> FastAPI -> User
```

Module 2 does not replace that flow. It asks a new question:

> How do our instructions change the quality and shape of the answer?

## What changes?

Module 1 used one system prompt and returned an answer.

Module 2 adds:

- Two prompt versions
- A visible `prompt_version` in every response
- A normal text endpoint
- A structured JSON endpoint
- Comparison and evaluation activities

## Everyday analogy

Module 1 built a kitchen that can receive an order and return food.

Module 2 improves the recipe:

- `v1`: broad cooking instructions
- `v2`: shorter output, headings, and clarification when requirements are unclear
- Structured endpoint: food must be placed into labeled containers

The kitchen is the same. The instructions and output contract change.

## Human roleplay

Choose four learners:

1. **User** gives a task.
2. **Prompt selector** chooses `v1` or `v2`.
3. **Model** follows that prompt.
4. **Validator** checks whether the output matches the expected format.

Repeat using an unclear request. Compare what `v1` and `v2` ask the model to do.

## Vocabulary

| Word | Simple meaning |
|---|---|
| Prompt | Instructions and input sent to a model |
| Prompt version | A named revision of instructions |
| Schema | The expected shape of data |
| Structured output | Data returned in predictable fields |
| Validation | Checking that data follows the rules |
| Evaluation | Measuring whether an output is useful and correct |

## Success checklist

- [ ] I can explain what Module 2 adds.
- [ ] I understand that the API flow remains the same.
- [ ] I can explain prompt version and schema without code.
- [ ] I know that structured output still requires validation.
