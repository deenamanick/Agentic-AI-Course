# Agentic AI Engineer Course (Jeevi Academy)

This repo contains the curriculum + coding exercises.

## Teaching philosophy

This is a beginner-first course for mixed-background learners, including project managers, DevOps engineers, UX designers, developers, teachers, homemakers, students, and career-switchers.

- Start with an everyday analogy and visible result.
- Teach understanding before syntax.
- Use roleplay to explain system flows.
- Copy, run, change, and safely break small examples.
- Separate required foundation work from optional challenges.
- Never assume previous Python, FastAPI, or AI experience.

Instructors should use the [Beginner Teaching Guide](BEGINNER-TEACHING-GUIDE.md).

## Outcomes

- Build an AI backend using hosted Llama models through Groq without requiring a student GPU.
- Optionally switch the same backend to local Ollama inference.
- Build structured, tool-using agents with LangChain and LangGraph.
- Expose reusable tools through Model Context Protocol (MCP).
- Add memory, Agentic RAG, citations, and multi-agent coordination.
- Evaluate agent quality, safety, cost, latency, and execution trajectories.
- Add tracing and production observability with Langfuse.
- Deploy durable agent jobs using the HTTP `202 Accepted` pattern.

## Teaching roadmap

- Start with FastAPI `POST /chat` using Groq, with Ollama as an optional local provider.
- Add prompts + structured outputs.
- Add tools (LangChain) and graphs (LangGraph).
- Progress from deterministic workflows to bounded multi-agent systems.
- Finish with evaluation, security, observability, and durable deployment.

## Modules

| Module | Topic | Primary outcome |
|---|---|---|
| 1 | [AI and Agentic AI foundations](module-1-foundation/) | Build a Groq-first FastAPI chat backend with optional Ollama |
| 2 | [LLM APIs and prompting](module-2-llm-apis-prompting/) | Version prompts and return validated structured output |
| 3 | [LangChain agents](module-3-langchain-agents/) | Build a ReAct agent with typed tools |
| 4 | [LangGraph workflows](module-4-langgraph/) | Build a deterministic, stateful agent graph |
| 5 | [Agent design patterns](module-5-agent-design-patterns/) | Choose the right autonomy level and workflow pattern |
| 6 | [Custom tools and MCP](module-6-custom-tools-mcp/) | Build safe reusable tools and expose an MCP server |
| 7 | [Memory and stateful agents](module-7-memory-stateful-agents/) | Implement short-term, long-term, entity, and episodic memory |
| 8 | [Agentic RAG](module-8-agentic-rag/) | Build grounded retrieval with reranking and citations |
| 9 | [Agent framework comparison](module-9-agent-frameworks/) | Compare LangGraph, CrewAI, and AutoGen on one problem |
| 10 | [Multi-agent systems](module-10-multi-agent-systems/) | Coordinate specialized agents with bounded delegation |
| 11 | [Evaluation and testing](module-11-evaluation-testing/) | Measure quality, trajectory correctness, cost, and latency |
| 12 | [Safety and human approval](module-12-safety-guardrails/) | Defend tools and data with policy and approval gates |
| 13 | [Observability and optimization](module-13-observability-optimization/) | Trace, diagnose, and optimize agent executions |
| 14 | [Durable deployment](module-14-durable-deployment/) | Run long-lived jobs with retries and recovery |
| 15 | [Production capstone](module-15-production-capstone/) | Ship and defend a production-ready agent system |

## Course-wide engineering standard

Every module from Module 5 onward should include:

- A runnable happy path and at least three failure-path tests.
- Typed inputs and outputs with explicit validation.
- Timeouts, bounded retries, and a maximum agent-step budget.
- Trace metadata containing a request ID, prompt version, and model name.
- A short threat model when external data or tools are involved.
- A measurable acceptance criterion rather than visual inspection alone.

## Suggested delivery

- **Foundation:** Modules 1–4
- **Agent engineering:** Modules 5–10
- **Production engineering:** Modules 11–14
- **Capstone:** Module 15
