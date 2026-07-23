# Practical 6.2 — Create an MCP Server

## Why

MCP exposes reusable capabilities through a standard boundary instead of embedding every tool in every agent.

## What you will build

Expose the currency converter and a read-only document lookup from a local MCP server.

## Practice

Give every tool a precise name, description, and schema. Keep business logic separate from the MCP adapter. Start the server locally and inspect the advertised tools.

Do not add a write tool yet.

## Success checklist

- [ ] The server starts with one documented command.
- [ ] Both tools are discoverable.
- [ ] Invalid arguments fail before business logic runs.
- [ ] Tool descriptions state limitations and side effects.
