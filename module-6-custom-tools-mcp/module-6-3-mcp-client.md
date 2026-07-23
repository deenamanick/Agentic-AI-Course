# Practical 6.3 — Connect an Agent to MCP

## Why

Discovery is useful only when an agent selects and calls the correct remote tool.

## What you will build

Connect a LangChain or LangGraph agent to the MCP server from Practical 6.2.

## Practice

Test requests that require currency conversion, document lookup, neither tool, and an unavailable MCP server. Trace the selected tool, validated arguments, duration, and result status.

## Success checklist

- [ ] The agent discovers tools at startup or per session.
- [ ] Irrelevant questions do not trigger a tool.
- [ ] Server failure returns a controlled fallback.
- [ ] A timeout prevents the request from hanging.
