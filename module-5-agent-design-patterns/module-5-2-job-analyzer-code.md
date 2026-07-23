# Practical 5.2 — Coding the Job Analyzer 👨‍💻

## Why, in simple terms

We know the theory of the Reflection Pattern. Now let's look at how we build it in `app/main.py`.

Just like in Module 4, we define a `TypedDict` for our State. But this time, notice how the State holds the *draft* review, the *critique*, and the *final* review!

---

## 🪣 The State Bucket

```python
class JobAnalyzerState(TypedDict):
    raw_cv: str            # The messy CV from the user
    job_title: str         # The role they are applying for
    
    draft_review: str      # Output of Node 1
    critique: str          # Output of Node 2
    final_review: str      # Output of Node 3
    
    llm: BaseChatModel
    langfuse_handler: CallbackHandler
```

---

## 📝 Node 1: `analyzer_node`

This node takes the `raw_cv` and writes the first draft.

```python
async def analyzer_node(state: JobAnalyzerState) -> dict:
    """Node 1: Draft the initial CV review."""
    llm = state["llm"]
    
    prompt = f"""
    You are an expert recruiter. Analyze this CV for a {state['job_title']} role.
    Provide strengths, weaknesses, and a score out of 100.
    
    CV:
    {state['raw_cv']}
    """
    
    result = await llm.ainvoke(prompt)
    return {"draft_review": result.content}
```

---

## 🧐 Node 2: `critique_node` (The Magic Happens Here)

This is the most important node. It acts as a totally different persona: a Harsh Senior Manager. It reads the draft from Node 1, and tries to find flaws.

```python
async def critique_node(state: JobAnalyzerState) -> dict:
    """Node 2: Critique the draft review."""
    llm = state["llm"]
    
    prompt = f"""
    You are a harsh Senior HR Manager. Review the CV analysis below.
    Find 3 specific things the reviewer missed or could improve. 
    Did they include a score? Did they check for typos in the CV?
    Be extremely critical. Do NOT rewrite the review, just list the flaws.
    
    Draft Review:
    {state['draft_review']}
    """
    
    result = await llm.ainvoke(prompt)
    return {"critique": result.content}
```

---

## 🛠️ Node 3: `refine_node`

The original persona comes back. It reads its own draft, and reads the harsh critique. Then it rewrites the draft to fix all the mistakes!

```python
async def refine_node(state: JobAnalyzerState) -> dict:
    """Node 3: Refine the review based on the critique."""
    llm = state["llm"]
    
    prompt = f"""
    You are an expert recruiter. You wrote a draft CV review, but your manager critiqued it.
    Rewrite the final review, fixing all the issues raised by your manager.
    
    Your Draft:
    {state['draft_review']}
    
    Manager's Critique:
    {state['critique']}
    """
    
    result = await llm.ainvoke(prompt)
    return {"final_review": result.content}
```

---

## 🔗 Connecting the Graph

In `build_graph()`, we connect them in a straight line (our 1-cycle Reflection pattern).

```python
workflow.add_edge(START, "analyzer")
workflow.add_edge("analyzer", "critique")
workflow.add_edge("critique", "refine")
workflow.add_edge("refine", END)
```

## Success checklist

- [ ] I can explain what the `critique_node` does differently from the `analyzer_node`.
- [ ] I understand how the `refine_node` uses BOTH the draft and the critique to create the final output.
- [ ] I can see how LangGraph forces the data to flow predictably through these 3 steps.
