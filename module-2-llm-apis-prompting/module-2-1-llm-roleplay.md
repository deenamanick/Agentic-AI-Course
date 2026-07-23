# Practical 2.1 — Meet the LLM Through Roleplay

## Why, in simple terms

An LLM predicts a useful continuation from the instructions and text it receives. It does not automatically know your private goal, current company data, or whether its answer is true.

## Human prediction game

Ask learners to complete:

- “Twinkle, twinkle, little…”
- “The capital of France is…”
- “For this customer, the correct refund is…”

The first two have familiar patterns. The third lacks company policy and customer details. This demonstrates why context matters.

## LLM, RAG, and agent

| Concept | Everyday comparison |
|---|---|
| LLM | A knowledgeable person answering from learned experience |
| RAG | The person first opens the correct reference book |
| Agent | The person decides which book or tool to use and performs steps |

## Roleplay

Use three learners:

1. **User:** asks for tomorrow’s weather.
2. **LLM:** can answer only from memory and must admit it lacks live data.
3. **Agent:** decides to call a weather tool before answering.

Discuss why confident wording is not proof of current information.

## Chat practice

Ask the model:

1. A general knowledge question
2. A current or private-data question
3. A question with missing context

Label each answer:

- likely answerable from general knowledge
- needs a tool or retrieval
- needs a clarifying question

## Success checklist

- [ ] I can explain LLM, RAG, and agent in my own words.
- [ ] I know an LLM can sound confident and still be wrong.
- [ ] I can identify when context, a tool, or clarification is needed.
