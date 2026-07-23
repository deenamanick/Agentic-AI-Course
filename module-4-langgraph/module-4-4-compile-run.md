# Practical 4.4 — Compile and Run the Graph 🚀

## Why, in simple terms

We have our bucket (`ResumeState`) and we have our workers (`extract_node`, `draft_summary_node`, `format_node`). 

Now we need to tell LangGraph how to connect them together into a pipeline. We do this by defining the **Edges** (the arrows between the nodes) and **compiling** the graph.

---

## 🔗 Connecting the Nodes

In `app/main.py`, the `build_graph()` function does exactly this:

```python
from langgraph.graph import StateGraph, START, END

def build_graph():
    # 1. Initialize the graph with our state bucket
    workflow = StateGraph(ResumeState)

    # 2. Add our workers (nodes) to the graph
    workflow.add_node("extract", extract_node)
    workflow.add_node("draft", draft_summary_node)
    workflow.add_node("format", format_node)

    # 3. Define the edges (the arrows!)
    # START -> extract -> draft -> format -> END
    workflow.add_edge(START, "extract")
    workflow.add_edge("extract", "draft")
    workflow.add_edge("draft", "format")
    workflow.add_edge("format", END)

    # 4. Compile it into an executable app
    return workflow.compile()
```

That's it! LangGraph now knows exactly what order to run the functions in.

---

## 🏃 Running the API

Now let's test the entire pipeline.

1. Start your API server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Send a messy brain-dump to the API using `curl`:

   ```bash
   curl -sS -X POST "http://127.0.0.1:8000/resume/build" \
     -H "Content-Type: application/json" \
     -d '{
       "raw_text": "Hey I am Sarah. I have been working as a data scientist for 4 years at Meta. I know SQL, Python, and PyTorch. Before that I was an intern at a small startup doing frontend dev with React."
     }'
   ```

3. **What happens under the hood:**
   - FastAPI receives the `raw_text` and creates the initial `ResumeState`.
   - The Graph starts.
   - **Extract Node:** Grabs `{"name": "Sarah", "skills": ["SQL", "Python", "PyTorch", "React"], ...}`
   - **Draft Node:** Writes a summary about Sarah the data scientist.
   - **Format Node:** Generates the Markdown string.
   - FastAPI returns the final Markdown to you!

---

## 🔍 See it in Langfuse

Because we added the Langfuse tracker (just like in Module 3), you can go to your Langfuse dashboard and see a perfect visual trace of your graph.

You will see exactly what data was extracted in Step 1, what summary was drafted in Step 2, and the final output in Step 3!

## Success checklist

- [ ] I understand how `add_edge` connects nodes together.
- [ ] I successfully ran the `curl` command and got a Markdown resume back.
- [ ] I can explain why this deterministic workflow is better for resume building than a free-thinking agent.
- [ ] I found the trace in my Langfuse dashboard.
