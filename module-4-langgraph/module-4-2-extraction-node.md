# Practical 4.2 — Node 1: Structured Extraction 🗂️

## Why, in simple terms

Our user is going to give us a messy paragraph like:
*"Hey there, my name is Alex. I worked at Google from 2021 to 2023 as a backend dev where I used Python and Docker. Before that I was at a startup using React. Oh, I also know SQL."*

We cannot feed this directly into a resume template! We need to extract the exact pieces of data (Name, Skills, Experience) into a clean, predictable JSON format.

In LangChain, this is called **Structured Output**.

---

## 🛠️ The Extraction Schema

First, we define exactly what we want the LLM to extract using Pydantic. This is the "mold" we force the AI to fill.

```python
from pydantic import BaseModel, Field

class ExtractedResumeData(BaseModel):
    name: str = Field(description="The person's full name, if provided.")
    skills: list[str] = Field(description="A list of technical and soft skills.")
    experience: list[str] = Field(description="A list of past work experience, jobs, or roles.")
```

## 🧠 Node 1: `extract_node`

A node in LangGraph is just a regular Python function that takes the `State` as input, and returns a dictionary with the keys it wants to update in the state.

```python
async def extract_node(state: ResumeState) -> dict:
    """
    Node 1: Reads the raw user text and extracts structured JSON data.
    """
    # 1. Get the raw text from the state bucket
    raw_text = state["raw_text"]
    
    # 2. Get our LLM (Groq)
    llm = build_llm()
    
    # 3. Force the LLM to return data matching our Pydantic schema
    # with_structured_output is a superpower!
    extractor = llm.with_structured_output(ExtractedResumeData)
    
    # 4. Prompt the AI
    prompt = f"Extract the name, skills, and experience from this text:\n\n{raw_text}"
    
    # 5. Invoke the AI
    result = await extractor.ainvoke(prompt)
    
    # 6. Return the extracted data to update the State bucket!
    return {
        "name": result.name,
        "skills": result.skills,
        "experience": result.experience
    }
```

---

## 🎭 Dialogue: Forcing the Output

**Alex:** Wait, how do you *guarantee* the AI returns a list for skills? What if it just returns a paragraph saying "Their skills include..."?

**Jeevi:** That's the magic of `.with_structured_output(ExtractedResumeData)`. When you use this with a modern model like Groq (Llama 3) or OpenAI, the model is physically constrained at the API level to return valid JSON that perfectly matches your Pydantic schema.

**Alex:** So I don't have to write "PLEASE format your response as JSON" in my prompt anymore?

**Jeevi:** Exactly! You just pass the schema, and the framework handles the rest. This makes Node 1 incredibly robust.

---

## 💡 Key Takeaways

- A Node is just a Python function that takes `state` and returns a dict to update the state.
- `with_structured_output` forces the LLM to return exact JSON matching a Pydantic model.
- Node 1 turns messy human text into clean data so the rest of the workflow can run predictably.

## Success checklist

- [ ] I understand how Pydantic is used to define the extraction schema.
- [ ] I know how to use `with_structured_output` on an LLM.
- [ ] I understand how `extract_node` updates the state with the extracted data.
