# Practical 5.3 — Compile and Test the Job Analyzer 🚀

## Why, in simple terms

Writing the code is only half the battle. We need to run it and *observe* the reflection pattern in action to see if the Critic actually improves the final result!

---

## 🏃 Running the API

1. Open a terminal in the `module-5-agent-design-patterns` folder.
2. Start your API server:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Send a terribly formatted CV to the API using `curl`:

   ```bash
   curl -sS -X POST "http://127.0.0.1:8000/analyzer/score" \
     -H "Content-Type: application/json" \
     -d '{
       "raw_cv": "hi my name alex i do coding i know python n sum html. i worked at google for 2 weeks den quit.",
       "job_title": "Senior Staff Software Engineer"
     }'
   ```

4. Wait about 4-6 seconds. (Remember, this takes longer because it is making **three separate LLM calls** under the hood!).

---

## 🔍 The Most Important Step: Check Langfuse

When you get the response back, copy the `request_id` and open your **Langfuse Dashboard**.

You MUST look at the trace for this request. If you click on the trace, you will see the three steps:

1. **`analyzer` call:** Look at what the AI generated first. It might be a very generic, polite review.
2. **`critique` call:** Look at what the Senior HR Manager AI wrote! It will likely be brutal: *"The reviewer failed to point out the terrible grammar. The reviewer gave them an 80/100 which is way too high for a Senior role."*
3. **`refine` call:** Look at the final output. It should be drastically improved, incorporating all the harsh feedback.

**💡 This is the magic of the Reflection Pattern.** You will physically see the quality improve between Step 1 and Step 3.

---

## 🏋️ Student Exercise: Change the Persona

In `app/main.py`, find the `critique_node`. Change the persona from a "Harsh Senior HR Manager" to a "Comedian who roasts resumes".

```python
# Change this:
"You are a harsh Senior HR Manager..."

# To this:
"You are a stand-up comedian. Roast this CV analysis..."
```

Restart your server, run the `curl` command again, and check Langfuse. How did the final output change? 

*Because Node 3 (Refine) is forced to listen to Node 2 (Critique), the final output will likely become a roast!*

## Success checklist

- [ ] I successfully ran the `curl` command and got a scored CV back.
- [ ] I opened Langfuse and looked at the `critique` node's output.
- [ ] I can physically see the difference between the `draft_review` and the `final_review`.
- [ ] I tried changing the critic's persona.
