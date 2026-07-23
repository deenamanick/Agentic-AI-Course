# Practical 4.1 — Defining the Graph State 🪣

## Why, in simple terms

A LangGraph workflow is basically a bucket brigade. 
- Node 1 does some work, drops it in the bucket, and passes the bucket to Node 2.
- Node 2 looks in the bucket, does more work, drops it in, and passes it to Node 3.

In LangGraph, this "bucket" is called the **State**. Before we can build our nodes, we have to define exactly what shape our bucket is, so every node knows what data to expect.

---

## 🏗️ The `ResumeState`

In `app/main.py`, we define our state using Python's `TypedDict`. This is just a dictionary where we guarantee the types of the values.

```python
from typing import TypedDict, Optional

class ResumeState(TypedDict):
    # 1. Input from the user
    raw_text: str           # e.g., "Hi I'm Alex, I worked at Google..."
    
    # 2. Output from the Extract Node
    name: Optional[str]     # e.g., "Alex"
    skills: list[str]       # e.g., ["Python", "Cloud Architecture"]
    experience: list[str]   # e.g., ["Software Engineer at Google (2 yrs)"]
    
    # 3. Output from the Draft Node
    summary: Optional[str]  # e.g., "Alex is a seasoned engineer..."
    
    # 4. Output from the Format Node
    final_resume: str       # The beautifully formatted Markdown
```

### How the State changes over time:

**At START:**
Everything is empty except `raw_text`.
```json
{
  "raw_text": "Hi I'm Alex...",
  "name": null,
  "skills": [],
  "experience": [],
  "summary": null,
  "final_resume": ""
}
```

**After Node 1 (Extract):**
Node 1 fills in the extracted data.
```json
{
  "raw_text": "Hi I'm Alex...",
  "name": "Alex",
  "skills": ["Python"],
  "experience": ["Google"],
  "summary": null,
  "final_resume": ""
}
```

**After Node 2 (Draft):**
Node 2 reads `skills` and fills in `summary`.
```json
{
  "raw_text": "Hi I'm Alex...",
  "name": "Alex",
  "skills": ["Python"],
  "experience": ["Google"],
  "summary": "Alex is an engineer...",
  "final_resume": ""
}
```

**After Node 3 (Format):**
Node 3 reads everything and fills in `final_resume`.

---

## 🎭 Dialogue: Overwriting vs Appending

**Alex:** If Node 2 updates the state, does it overwrite what Node 1 did?

**Jeevi:** By default, yes! If Node 2 returns `{"summary": "new text"}`, LangGraph updates the `summary` key in the state dictionary. 

**Alex:** What if I want to keep a running list of messages, like a chat history? I wouldn't want to overwrite it!

**Jeevi:** Great point. LangGraph has a special feature called `Annotated` for that. If you want a list to append instead of overwrite, you define it like this: `messages: Annotated[list, operator.add]`. But for our Resume Builder, overwriting specific keys is exactly what we want!

---

## 💡 Key Takeaways

- The **State** is the shared memory passed between nodes in the graph.
- Every node takes the State as input, and returns an updated State.
- Defining a clear `TypedDict` for your state makes your graph predictable and easy to debug.

## Success checklist

- [ ] I understand that the State is the shared data passed between nodes.
- [ ] I can trace how the `ResumeState` fills up as it moves from Node 1 to Node 3.
- [ ] I know how to define a State using `TypedDict` in Python.
