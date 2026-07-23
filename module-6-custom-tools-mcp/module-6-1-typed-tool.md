# Practical 6.1 — Build a Typed Custom Tool

## Why

Tools turn model intent into real actions. A strict contract keeps guesses from becoming invalid API calls.

## What you will build

Create a currency-conversion tool with Pydantic inputs: `amount`, `source_currency`, and `target_currency`. Use a deterministic fixture before connecting a live API.

## Practice

Validate positive amounts and ISO-style currency codes. Return a small typed result. Add tests for invalid codes, negative amounts, timeouts, and upstream failure.

## Success checklist

- [ ] Inputs and outputs have explicit schemas.
- [ ] Internal exceptions are converted into safe tool errors.
- [ ] Secrets never appear in code, output, or traces.
