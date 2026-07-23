# Practical 3.5 — Agent Framework Landscape (2025/2026) 🗺️

## Why, in simple terms

LangGraph isn't the only way to build AI agents. The ecosystem is evolving fast, and as a professional, you should know what options exist and when to use each one.

---

## 🏆 The Major Agent Frameworks

### 1. LangGraph ⭐ (What we use in this course)
- **By:** LangChain team
- **Best for:** Production agents with clear, deterministic workflows
- **Why it won:** Replaced the deprecated `AgentExecutor`. Visual graph-based control, great debugging, used by major companies
- **Think of it as:** A flowchart builder for AI

```text
Use when: You need control over every step, human approval, 
          or deterministic workflows
```

### 2. CrewAI 🔥
- **By:** Community (open source)
- **Best for:** Teams of agents working together (like a software team)
- **Think of it as:** Hiring a team — a researcher, a writer, a reviewer — each with a specific role

```text
Example: 
  Agent 1 (Researcher): Searches the web for information
  Agent 2 (Writer): Writes a blog post from the research
  Agent 3 (Reviewer): Checks the blog post for errors
```

### 3. AutoGen 🔥
- **By:** Microsoft
- **Best for:** Multi-agent conversations and enterprise collaboration
- **Think of it as:** A group chat where AI agents discuss and solve problems together

### 4. OpenAI Agents SDK 🆕
- **By:** OpenAI
- **Best for:** Simple agents using OpenAI models with handoffs between agents
- **Limitation:** Locked to OpenAI models only

### 5. Google ADK (Agent Development Kit) 🆕
- **By:** Google
- **Best for:** Agents on Google Cloud / Vertex AI / Gemini
- **Think of it as:** Google's answer to LangGraph

### 6. Cloudflare Agents SDK 🆕
- **By:** Cloudflare
- **Best for:** Serverless agents that run globally on Cloudflare Workers
- **Relevant to us:** This aligns with the Jeevisoft/Cloudflare stack we use!

### 7. Pydantic AI 🧪
- **By:** Pydantic team (same people who make our `BaseModel`)
- **Best for:** Type-safe agents with guaranteed structured output
- **Think of it as:** LangGraph but with Pydantic-level type safety

### 8. Smolagents 🧪
- **By:** HuggingFace
- **Best for:** Lightweight, code-first agents for learning and experiments

---

## 📊 Comparison Table

| Framework | Control Flow | Multi-Agent | Vendor Lock-in | Maturity | Learning Curve |
|---|---|---|---|---|---|
| **LangGraph** | Graph-based | Via subgraphs | Low (any LLM) | ⭐⭐⭐⭐⭐ | Medium |
| **CrewAI** | Role-based | ⭐ Built-in | Low (any LLM) | ⭐⭐⭐⭐ | Easy |
| **AutoGen** | Conversation | ⭐ Built-in | Low | ⭐⭐⭐⭐ | Medium |
| **OpenAI SDK** | Linear/Handoff | Via handoffs | 🔒 OpenAI only | ⭐⭐⭐ | Easy |
| **Google ADK** | Graph-based | Yes | 🔒 Google/Gemini | ⭐⭐⭐ | Medium |
| **Cloudflare** | Durable Objects | Yes | 🔒 Cloudflare | ⭐⭐ | Medium |
| **Pydantic AI** | Function-based | Limited | Low (any LLM) | ⭐⭐ | Easy |

---

## 🎯 When to Use What?

| Use Case | Best Framework | Why |
|---|---|---|
| Production workflow with human approval | **LangGraph** | Best control flow, state management |
| Team of agents (researcher → writer → reviewer) | **CrewAI** | Built for role-based collaboration |
| Enterprise multi-agent discussions | **AutoGen** | Microsoft backing, conversation patterns |
| Quick prototype with OpenAI | **OpenAI Agents SDK** | Simplest setup, but vendor locked |
| Serverless global deployment | **Cloudflare Agents SDK** | Runs on the edge, durable state |
| Learning and experimentation | **Smolagents** | Lightest weight, code-first |

---

## 🔮 Where Each Framework Appears in This Course

| Module | Framework | How |
|---|---|---|
| **Module 3** (here) | LangGraph | Build your first agent |
| **Module 4** | LangGraph | Deep dive: routing, plan-execute, state |
| **Module 9** | LangGraph + CrewAI + AutoGen | Compare frameworks on the same problem |
| **Module 10** | CrewAI or LangGraph | Multi-agent systems |
| **Module 14** | Cloudflare Agents SDK | Deploy to production |

---

## 💡 Key Takeaways

- **LangGraph is the industry standard** for production agents — that's why we use it in this course.
- **CrewAI is best for teams of agents** working together on complex tasks.
- **No framework is perfect** — each has tradeoffs in control, flexibility, and vendor lock-in.
- **Your business logic should be separate from the framework** — so you can switch later if needed.

## Success checklist

- [ ] I can name at least 4 agent frameworks and their main use case.
- [ ] I understand why this course uses LangGraph as the primary framework.
- [ ] I know the difference between graph-based and role-based agent patterns.
- [ ] I can explain vendor lock-in and why it matters.
