# Module 8.8: Corrective RAG (Agentic Workflow) 🔄

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Normal vs Agentic RAG** - Understand the difference.
> 2. **Phase 2: Visual Studio Code Practice** - See the Corrective flow in action.

---

### Step 1 — Normal RAG vs Agentic RAG

So far, we have discussed **Normal RAG**. It has a very simple workflow:

```text
Normal RAG:
Search once 
  ↓ 
Answer
```
But what if the search results were bad? What if the user asked a confusing question? Normal RAG will just use the bad search results and hallucinate an answer.

Because you are building **Agentic AI**, we can make the system much smarter. 

```text
Agentic RAG (Corrective):
Search 
  ↓ 
Not good? 
  ↓ 
Search again (Rewrite the query)
  ↓ 
Still not good? 
  ↓ 
Say "I don't have enough evidence."
```

Instead of blindly answering, the Agent **grades** the evidence. If the evidence is weak, it tries again. If it's still weak, it refuses to answer. This is called **Corrective RAG (CRAG)**.

---

## 🌊 Visual Studio Code Practice

> **👨‍💻 Code Mapping:** Open `app/main.py` and look at **Line 79**. 

This is where our LangGraph workflow is defined. Look at the `grade_evidence_node`.

```python
def grade_evidence_node(state: GraphState):
    print("-> GRADE EVIDENCE")
    score = state.get("score", 0.0)
    # If the score is higher than 0.5, we grade it as "good"
    grade = "good" if score >= 0.5 else "bad"
    return {"grade": grade}
```

Then, look at `decide_to_generate`:
```python
def decide_to_generate(state: GraphState):
    if state["grade"] == "good":
        return "generate"     # Evidence is good, answer the question!
    else:
        if state.get("retries", 0) < 1:
            return "rewrite"  # Evidence is bad, try searching again!
        else:
            return "refusal"  # We already tried. Refuse to answer.
```

### 🚦 Stop Conditions (Critical!)
Notice the `retries < 1` logic. You MUST limit retries. If the agent rewrites the query and retrieves forever, you'll waste API credits and get stuck in an infinite loop. 

---

## 💡 Key Takeaways

- Normal RAG blindly trusts its first search result.
- Corrective RAG (Agentic RAG) grades the evidence. If it's bad, it retries. If it's still bad, it refuses.
- You must always have a stop condition (like a max retry count) to prevent infinite loops.

## Checklist

- [ ] You can explain the difference between Normal RAG and Agentic RAG.
- [ ] You understand why the agent must be able to refuse to answer.
- [ ] You found the routing logic in `app/main.py` and understand how it prevents infinite loops.
