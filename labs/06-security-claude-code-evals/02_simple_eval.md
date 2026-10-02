# Lesson 6.2 — Evals, Testing and Debugging

**Script:** `02_simple_eval.py` · **Domain:** Eval, Testing, and Debugging · **Cost:** about $0.02 per run

## Goal

Measure quality with numbers, so model, prompt and cost decisions are based on evidence.

## Why evals

Prompts and models change. Without an eval you cannot answer:
- Did my prompt change help or hurt?
- Is Haiku good enough to replace Opus here?
- Did the new model version break anything?

## Building an eval

1. **Define success criteria** — specific and measurable. "Classify intent with ≥95% accuracy" not "works well".
2. **Collect test cases** — real traffic samples + edge cases + known past failures. Include an expected answer or a rubric.
3. **Choose grading** (prefer the top of the list):

| Method | Speed / cost | Best for | Example |
|---|---|---|---|
| **Code-based** | Fast, cheap, exact | Labels, JSON validity, regex, numbers | `answer == "billing"` |
| **Model-based (LLM judge)** | Medium | Open-ended text: tone, helpfulness, faithfulness | Rubric scored 1–5 |
| **Human** | Slow, expensive | Final checks, calibrating the judge | Expert review |

4. **Run automatically** after every change. Track the score over time.

## LLM-as-judge tips

- Give a **concrete rubric** with criteria and points, not "rate quality 1–5".
- Ask for reasoning, then the score; use structured output for the score.
- Use a capable judge model; check it against human grades on a sample.
- Judge one dimension at a time when possible.

## Testing practice

- Volume beats perfection: many automated cases > few hand-checked ones.
- Hold out a test set; don't tune prompts on the exact cases you report.
- Test edge cases: empty input, very long input, other languages, adversarial input.
- Regression tests: every bug you fix becomes a test case.

## Debugging checklist

| Symptom | Look at |
|---|---|
| Output cut off | `stop_reason == "max_tokens"` |
| Strange errors | HTTP status + error type; log `request_id` |
| Costs higher than expected | `usage` (input, output, cache read/write); thinking tokens |
| Cache not working | `cache_read_input_tokens` = 0 → prefix changes |
| Agent misbehaves | Full transcript: tool calls, inputs, results, ordering |
| Inconsistent quality | Run the eval; compare prompts or models side by side |

The Claude Console (Workbench) helps prototype prompts, compare outputs and generate test cases.

## What the script does

1. **Code-graded** classification eval: 5 cases (one deliberately ambiguous) on Haiku and Opus. Prints PASS/FAIL and accuracy.
2. **Model-graded**: an LLM judge scores a support reply against a 3-criterion rubric using structured output (`Grade` model).

## What to observe

- Both models likely pass the clear cases; the ambiguous case shows where labels need a clear definition — often a **test-set** problem, not a model problem.
- The judge returns a score **and** a reason, so you can audit it.

## Exam angles

- "Prove the cheaper model is acceptable" → eval set on both models.
- "Grade 10,000 summaries for faithfulness" → LLM judge with rubric (maybe via Batches API).
- "Check that output is valid JSON with field X" → code-based grading.
- "Prompt change shipped and quality dropped unnoticed" → automated eval in CI.

## Check yourself

1. Which grading method should you prefer when possible?
2. What makes a good LLM-judge rubric?
3. Which response field shows a truncated answer?
