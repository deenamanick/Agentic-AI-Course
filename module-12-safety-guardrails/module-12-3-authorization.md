# Practical 12.3 — Authorization and Least Privilege

## Build

Require authenticated user context for every resource tool and verify ownership inside the backend. Separate read and write capabilities.

Test guessed IDs, another user’s ID, missing identity, and a model-requested override.

## Success checklist

- [ ] Authorization is server-side.
- [ ] Denied requests reveal no resource details.
- [ ] Tools receive only the permissions they need.
