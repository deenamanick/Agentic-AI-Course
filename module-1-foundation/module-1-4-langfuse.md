# Practical 1.4 — Trace Requests with Langfuse

## Why

Agent systems need a request ID and trace before they become complex.

## Practice

Configure Langfuse or use the application without optional credentials. Send two requests and locate their traces. Identify model, input, output, latency, and request ID.

Do not trace secrets or unnecessary personal data.

## Success checklist

- [ ] Every response has a request ID.
- [ ] Tracing failure does not break the learning API.
- [ ] Sensitive configuration is excluded from traces.
