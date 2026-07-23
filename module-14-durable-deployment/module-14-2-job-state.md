# Practical 14.2 — Model Durable State and Ownership

## Build

Model `queued`, `running`, `waiting_for_approval`, `succeeded`, `failed`, and `cancelled` states in D1 or a local equivalent. Store owner, progress, attempts, timestamps, and result metadata.

## Success checklist

- [ ] Invalid transitions are rejected.
- [ ] Ownership is checked for reads and writes.
- [ ] Large artifacts are referenced rather than loaded into state.
