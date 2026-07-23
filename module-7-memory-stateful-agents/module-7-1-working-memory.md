# Practical 7.1 — Working and Conversation Memory

## Why

Sending an entire conversation forever increases cost and eventually exceeds the context window.

## What you will build

Add a bounded message window and a rolling summary to the existing chat API.

## Practice

Compare full history, the last `N` messages, and summary-plus-recent-messages. Measure answer quality and input tokens over a 20-turn conversation.

## Success checklist

- [ ] Memory is separated by session and user.
- [ ] The context has a hard size limit.
- [ ] Summaries are labeled as model-generated.
- [ ] Token savings are reported.
