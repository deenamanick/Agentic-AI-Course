# Practical 1.1 — Python Basics for AI Agents

## Why, in simple terms

Python is the language used by our backend. You do not need to learn every Python feature. You need enough Python to read data, create functions, and understand the AI API code.

Think of Python as instructions written from top to bottom:

```python
student_name = "Anu"
course = "Agentic AI"

print(student_name)
print(course)
```

## Concepts to learn first

| Concept | Simple meaning | Example |
|---|---|---|
| Variable | A named box that stores a value | `name = "Anu"` |
| String | Text | `"Hello"` |
| Integer | Whole number | `10` |
| Float | Decimal number | `0.7` |
| Boolean | True or false | `is_ready = True` |
| List | An ordered group of values | `tools = ["search", "calculator"]` |
| Dictionary | Values stored using names or keys | `user = {"name": "Anu"}` |
| `if` | Make a decision | `if is_ready:` |
| `for` | Repeat an action | `for tool in tools:` |

## What you will build

Create a file named `python_basics.py`:

```python
student = {
    "name": "Anu",
    "topic": "AI Agents",
    "completed_lessons": 1,
}

agent_tools = ["calculator", "search", "memory"]

print(f"Welcome, {student['name']}!")
print(f"Today you are learning {student['topic']}.")

for tool in agent_tools:
    print(f"Agent tool: {tool}")

if student["completed_lessons"] > 0:
    print("Great start!")
else:
    print("Let us begin!")
```

Run it:

```bash
python3 python_basics.py
```

## Practice tasks

1. Change the student name.
2. Add a `weather` tool.
3. Change `completed_lessons` to `0`.
4. Add a boolean named `ollama_running`.
5. Print a different message when Ollama is not running.

## Errors are useful

Remove one quotation mark and run the program. Python will show a `SyntaxError`. Restore the quotation mark and run it again.

## Success checklist

- [ ] I can create a variable.
- [ ] I know the difference between a list and dictionary.
- [ ] I can use `if` and `for`.
- [ ] I can run a Python file from the terminal.

## Common problems

**`python3: command not found`**

Install Python 3 and restart the terminal.

**`SyntaxError`**

Check quotation marks, brackets, colons, and indentation near the reported line.
