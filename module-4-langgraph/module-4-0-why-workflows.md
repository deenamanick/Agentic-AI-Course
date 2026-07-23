# Practical 4.0 — Why Do We Need Workflows? (Agents vs Workflows)

## What you built so far

In **Module 3**, you built an Agent using `create_react_agent`. That agent was completely **autonomous**. You gave it tools (like a calculator), and it decided on its own:
1. Which tool to use
2. What order to use them in
3. When to stop

This is called the **ReAct (Reason + Act) loop**. It is incredibly powerful for answering open-ended questions.

## The Problem with Autonomous Agents

Imagine you are building an AI to generate professional Resumes for your users. The steps are always the same:
1. Extract their name, skills, and experience from a messy text dump.
2. Write a professional summary.
3. Format the final output as Markdown.

If you give an autonomous agent (like from Module 3) these instructions, it might decide to draft the summary *before* extracting the skills. It might skip formatting entirely. It might get distracted and search the web instead.

When you need **100% predictable, reliable results**, autonomous agents are too risky.

## The Solution: Deterministic Workflows 🚦

In **Module 4**, we are going to use LangGraph differently. Instead of letting the AI run freely, we will build a **deterministic workflow**. 

We will draw a flowchart in code. The AI *must* follow our exact steps, in our exact order. It cannot skip steps. It cannot go out of bounds.

### Visualizing the Workflow

We are building a **Resume Builder Workflow**:

```text
       START
         │
         ▼
 ┌───────────────┐
 │ 1. EXTRACT    │ ← AI reads messy input, outputs strict JSON (Name, Skills)
 └───────┬───────┘
         │
         ▼
 ┌───────────────┐
 │ 2. DRAFT      │ ← AI writes a 3-sentence professional summary
 └───────┬───────┘
         │
         ▼
 ┌───────────────┐
 │ 3. FORMAT     │ ← Python script (no AI) combines data into Markdown
 └───────┬───────┘
         │
         ▼
        END
```

## Why LangGraph?

Why use a library like LangGraph for this? Why not just write three normal Python functions?

1. **State Management:** LangGraph automatically passes data (the "State") from one node to the next.
2. **Resilience & Checkpointing:** In production, if the Draft step fails, LangGraph can pause, wait, and resume exactly where it left off without re-running the Extract step.
3. **Observability:** Tools like Langfuse can trace the exact path the graph took, showing you inputs and outputs at every single node.
4. **Human-in-the-loop (Later modules):** You can pause the graph after "Draft", ask the user "Do you like this summary?", and only proceed to "Format" if they click Yes!

## Success checklist

- [ ] I understand the difference between an autonomous agent (Module 3) and a deterministic workflow (Module 4).
- [ ] I know why we use workflows for tasks that require strict predictability (like Resume building).
- [ ] I can list the 3 nodes we are going to build for our Resume workflow.
