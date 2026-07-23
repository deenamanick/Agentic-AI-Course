# Practical 7.4 — Build a Stateful Tutor

## Why

A tutor is a useful memory project because progress should persist while answers remain grounded in the current lesson.

## What you will build

Build a tutor that remembers learning goals, completed topics, quiz results, and common mistakes across sessions.

## Practice

Start two users and prove their state stays isolated. Let one user correct a preference and delete a memory. Generate the next lesson using only approved memories.

## Success checklist

- [ ] The tutor personalizes without inventing learner history.
- [ ] Progress survives a new session.
- [ ] Users can correct and forget information.
- [ ] An automated isolation test prevents memory leakage.
