# Module 6 — Custom Tools and Model Context Protocol

## Goal

Build reusable tools that agents can discover and call safely.

## Topics

- Typed tool contracts with Pydantic
- Local functions, REST APIs, databases, search, and document tools
- MCP servers, clients, resources, prompts, and tool discovery
- Authentication and secret handling
- Timeouts, retries, rate limits, and idempotency
- Tool allowlists and user-scoped authorization
- Safe errors that do not leak credentials or internals

## Practicals

1. [Build a typed custom tool](module-6-1-typed-tool.md)
2. [Create an MCP server](module-6-2-mcp-server.md)
3. [Connect an agent to MCP](module-6-3-mcp-client.md)
4. [Secure, test, and approval-gate tools](module-6-4-safe-tools.md)

## Deliverable

An MCP server with at least two read-only tools, one approval-gated write tool, schemas, tests, and a client example.

## Completion criteria

- Secrets never appear in responses or traces.
- Tool arguments are validated before execution.
- Repeated idempotency keys cannot repeat a write.
