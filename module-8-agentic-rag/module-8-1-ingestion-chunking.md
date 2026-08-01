# Module 8.1: Ingest and Chunk Documents 📄

> **👨‍🎓 Student Guide: How to follow this Lab**
> 1. **Phase 1: Understand the Goal** - Learn why we need to split documents into small chunks.
> 2. **Phase 2: Visual Studio Code Practice** - Build an ingestion pipeline that loads PDFs, chunks them, and stores metadata.
> 3. **Phase 3: The Brain** - Compare chunking strategies and test for idempotency.

### Why (in simple terms)

Before your AI can search through a document, you need to prepare it. You can't just throw a 200-page PDF at an LLM — it won't fit in the context window!

Instead, we **split** the document into small, searchable pieces called **chunks**. Each chunk gets stored with metadata (page number, source file, section title) so we can trace every answer back to its source.

### What you'll learn
1. **Document Loading**: How to read PDFs with Python.
2. **Chunking Strategies**: Fixed-size vs section-aware chunking.
3. **Metadata**: Why every chunk needs a page number and source.
4. **Idempotency**: Why re-ingesting the same document shouldn't create duplicates.

---

## 📦 What is Chunking?

| Concept | What it means | Simple analogy |
| :--- | :--- | :--- |
| **Document** | A full PDF, Word doc, or text file | A whole textbook |
| **Chunk** | A small piece of the document (200-500 words) | A single index card |
| **Metadata** | Information attached to each chunk (page, source, section) | The label on the back of the card |
| **Embedding** | A numerical representation of the chunk for search | GPS coordinates for the card |

---

## 🌊 Visual Studio Code Practice: Building the Ingestion Pipeline

### Step 1: Understand the two chunking strategies

| Strategy | How it works | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **Fixed-size chunking** | Split every N characters (e.g., 500 chars) | Simple, predictable | May cut sentences in half |
| **Section-aware chunking** | Split by headers, paragraphs, or logical sections | Preserves meaning | More complex to implement |

### Step 2: What metadata to store with each chunk

Every chunk should carry this metadata so you can trace it back later:

| Metadata field | Example | Why you need it |
| :--- | :--- | :--- |
| `document_id` | `"company-policy-v2"` | Identify which document it came from |
| `page` | `5` | Cite the exact page in the response |
| `section` | `"Vacation Policy"` | Help the user find it in the original document |
| `chunk_index` | `3` | Know the order of chunks within a page |
| `checksum` | `"a1b2c3d4..."` | Detect duplicates — if the checksum matches, skip re-ingestion |
| `source_title` | `"HR Policy Manual"` | Display a human-friendly name in citations |

### Step 3: Handle edge cases

| Edge case | What to do |
| :--- | :--- |
| Empty page | Skip it — don't create a chunk for a blank page |
| Unreadable page (scanned image) | Log a warning and skip, or use OCR if available |
| Re-ingesting the same document | Check the checksum — if it matches, don't create duplicates |

---

## 🎭 Dialogue: Why Chunks Matter

**Alex:** Why can't we just give the entire PDF to the AI?

**Jeevi:** Two reasons! First, most LLMs have a context window limit (say, 8,000 tokens). A 200-page PDF could be 100,000 tokens — it won't fit! Second, even if it did fit, the AI would get confused by too much irrelevant information. Small, focused chunks are much easier for the AI to use.

**Alex:** And the metadata lets us create citations?

**Jeevi:** Exactly! When the AI uses a chunk to answer, we can say "This answer is based on page 5, section 'Vacation Policy' of the HR Policy Manual." Without metadata, we'd have no idea where the answer came from.

---

## Quick Practice Tasks
- **Try both strategies**: Chunk a small PDF with fixed-size (500 chars) and section-aware chunking. Compare the results.
- **Inspect chunks manually**: Read a few chunks and check — does the chunk make sense on its own? Or was a sentence cut in half?
- **Test idempotency**: Run the ingestion twice on the same document. Verify no duplicates were created.

---

## 💡 Key Takeaways

- Retrieval quality begins with clean text, useful chunks, and traceable metadata.
- Fixed-size chunking is simple but may break sentences. Section-aware chunking preserves meaning.
- Every chunk must carry metadata (page, source, section) for citations to work.
- Idempotency (no duplicates on re-ingestion) is critical for production systems.

## Checklist

- [ ] You understand why documents must be chunked before searching.
- [ ] You can explain the difference between fixed-size and section-aware chunking.
- [ ] Every chunk maps back to a page and source.
- [ ] Duplicate ingestion is idempotent (no duplicates created).
- [ ] Empty and unreadable pages are handled.
