# Practical 4.3 — Nodes 2 & 3: Generation & Formatting ✍️

## Why, in simple terms

Now that Node 1 has filled our `ResumeState` bucket with clean data (Name, Skills, Experience), we need to actually write the resume!

- **Node 2 (Draft):** Uses the AI to write a professional summary.
- **Node 3 (Format):** Uses pure Python (no AI) to assemble everything into a Markdown document.

---

## 🧠 Node 2: `draft_summary_node`

This node looks inside the state, grabs the skills and experience, and asks the LLM to write a 3-sentence summary.

```python
async def draft_summary_node(state: ResumeState) -> dict:
    """
    Node 2: Drafts a professional summary based on the extracted data.
    """
    llm = build_llm()
    
    name = state.get("name", "User")
    skills = ", ".join(state.get("skills", []))
    exp = ", ".join(state.get("experience", []))
    
    prompt = f"""
    Write a 3-sentence professional resume summary for {name}.
    They have these skills: {skills}.
    They have this experience: {exp}.
    Make it sound highly professional and impactful. Do not use the word "I".
    """
    
    # Notice we use standard ainvoke here, not structured output, 
    # because we just want a string of text!
    response = await llm.ainvoke(prompt)
    
    # Return the summary to update the State bucket
    return {"summary": response.content}
```

---

## 💻 Node 3: `format_node`

Does every step in a LangGraph workflow need AI? **No!**
If a step can be done with standard Python logic, you should ALWAYS use standard Python. It is faster, 100% reliable, and free.

Our `format_node` just takes the data and the summary from the state, and formats a Markdown string.

```python
def format_node(state: ResumeState) -> dict:
    """
    Node 3: Combines all state data into a final formatted Markdown resume.
    Notice this function is NOT async and does NOT call the LLM!
    """
    name = state.get("name", "Unknown Name")
    summary = state.get("summary", "No summary provided.")
    skills = state.get("skills", [])
    experience = state.get("experience", [])
    
    # Create the markdown string
    md = f"# {name.upper()}\n\n"
    
    md += "## PROFESSIONAL SUMMARY\n"
    md += f"{summary}\n\n"
    
    md += "## SKILLS\n"
    for skill in skills:
        md += f"- {skill}\n"
    md += "\n"
    
    md += "## EXPERIENCE\n"
    for exp in experience:
        md += f"- {exp}\n"
        
    # Return the final resume to update the state!
    return {"final_resume": md}
```

---

## 🎭 Dialogue: When to use AI vs Code

**Alex:** Wait, Node 3 doesn't use the LLM at all?

**Jeevi:** Exactly! Once you have the structured data and the written summary, you don't need an AI to assemble a Markdown file. Python string formatting (`f""`) is perfect for this.

**Alex:** But I could have just asked the LLM to format it as Markdown in Node 2?

**Jeevi:** You could, but LLMs are unpredictable. Sometimes they might wrap it in ` ```markdown `, sometimes they might add conversational text like *"Here is your resume!"*. By doing the final formatting in pure Python, we guarantee it looks exactly the same every single time.

---

## 💡 Key Takeaways

- A Node does not have to be an AI call. It can be pure Python logic.
- Standard generation (Node 2) uses `.ainvoke()`, while extraction (Node 1) used `.with_structured_output()`.
- Always use standard code (not AI) for tasks that require 100% predictability, like formatting data into templates.

## Success checklist

- [ ] I understand how Node 2 reads the data extracted by Node 1.
- [ ] I understand why Node 3 is pure Python instead of an LLM call.
- [ ] I can trace how the `ResumeState` is fully populated by the end of Node 3.
