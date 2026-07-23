# Practical 3.3 — Build and Run the Agent Executor

## Build

Run `POST /agent/chat` and inspect how the model, prompt, tools, and executor connect. Add request ID, maximum iterations, timeout behavior, and useful trace metadata.

## Success checklist

- [ ] The executor has explicit limits.
- [ ] Tool outputs are treated as untrusted data.
- [ ] The API response does not expose hidden reasoning.
- [ ] Each execution can be traced by request ID.
