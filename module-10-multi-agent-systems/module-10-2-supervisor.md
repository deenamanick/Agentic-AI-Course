# Practical 10.2 — Build a Supervisor Workflow

## Build

Create a supervisor that assigns bounded tasks, tracks progress, and finalizes results. The supervisor may delegate only to registered roles and must stop after a fixed number of handoffs.

## Test

Include unavailable agents, invalid handoffs, repeated delegation, and incomplete results.

## Success checklist

- [ ] Delegation depth is bounded.
- [ ] Agent failures remain visible.
- [ ] The supervisor cannot approve consequential actions.
