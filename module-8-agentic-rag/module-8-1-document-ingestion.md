# Module 8.1: Document Ingestion 📄

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Understand the Goal** - Learn what happens before we can search a document.
> 2. **Phase 2: Visual Studio Code Practice** - Look at how we load our knowledge base.

---

### Step 1 — Getting the Documents Ready

Before your AI can search through a PDF, Word document, or company wiki, we have to pull the text out of it. 

This process is called **Document Ingestion**.

If you were building a massive production system, this step involves:
1. Connecting to an AWS bucket or Google Drive.
2. Downloading the PDF.
3. Using a tool (like PyPDF or unstructured.io) to extract the text.
4. Cleaning out the messy headers, footers, and page numbers.

### Step 2 — Metadata (The Secret to Trust)

When you pull text out of a document, you must also attach **Metadata** to it. 

Metadata is just "data about the data". 

Imagine someone rips a page out of a book and hands it to you. You read it, but you have no idea what book it came from or what page number it is. 

If we don't attach metadata during ingestion, the AI will answer questions but won't be able to tell the user *where* it got the answer!

**Good Metadata looks like this:**
- `source_file`: "HR_Policy_2025.pdf"
- `page_number`: 12
- `author`: "Human Resources"

---

## 🌊 Visual Studio Code Practice

For this module, we want to focus entirely on the **RAG logic** (searching and answering) without getting bogged down in the messy code of parsing complex PDFs. 

So, we are going to use a **Hardcoded Knowledge Base** in Python.

> **👨‍💻 Code Mapping:** Open `app/main.py` and look at **Line 17**. 

You will see our simulated Document Ingestion:

```python
knowledge_base = [
    "Vacation Policy: Employees get 20 days of paid time off per year.",
    "Work Hours: Standard hours are 9:00 AM to 5:00 PM, Monday to Friday.",
    "Remote Work: Employees can work from home up to 2 days per week.",
    "Dress Code: Business casual is required from Monday to Thursday. Friday is casual.",
    "Health Benefits: Full health insurance is provided after 3 months of employment."
]
```

By storing these as simple strings in a list, we skip the messy PDF parsing and jump straight into teaching the AI how to search!

---

## 💡 Key Takeaways

- Document Ingestion is the process of extracting text from files like PDFs.
- Metadata (source file, page number) must be saved alongside the text so the AI can provide citations later.
- We are using a hardcoded knowledge base in this module to keep the focus on the AI logic.

## Checklist

- [ ] You understand what Document Ingestion is.
- [ ] You can explain why metadata is critical for building trustworthy AI.
- [ ] You found the `knowledge_base` list in `app/main.py`.
