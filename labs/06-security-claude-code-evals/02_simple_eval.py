"""Day 11: A tiny eval — code-graded checks, then an LLM judge with a rubric."""

import sys
from pathlib import Path

from pydantic import BaseModel

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import HAIKU, MODEL, client, text_of

SYSTEM = "Classify the support message. Answer with exactly one word: billing, technical, sales, or other."

# Test set: real-looking inputs plus edge cases, each with the expected label.
CASES = [
    ("I was charged twice this month.", "billing"),
    ("The app freezes when I upload a PDF.", "technical"),
    ("Do you offer discounts for 500 seats?", "sales"),
    ("What is the weather like?", "other"),
    ("My card was declined and now the dashboard shows error 500.", "billing"),  # ambiguous on purpose
]


def run_eval(model: str) -> float:
    passed = 0
    for text, expected in CASES:
        response = client.messages.create(
            model=model, max_tokens=1024, system=SYSTEM, messages=[{"role": "user", "content": text}]
        )
        answer = text_of(response).strip().lower()
        ok = answer == expected  # code-based grading: exact match
        passed += ok
        print(f"  {'PASS' if ok else 'FAIL'}  expected={expected:9} got={answer:9} | {text}")
    return passed / len(CASES)


for model in (HAIKU, MODEL):
    print(f"=== {model}")
    print(f"accuracy: {run_eval(model):.0%}\n")


# Model-based grading: for open-ended output where exact match is impossible.
class Grade(BaseModel):
    score: int  # 1-5
    reason: str


reply = "Sorry about the double charge. I refunded the extra payment; it shows in 3–5 business days."
grade = client.messages.parse(
    model=MODEL,
    max_tokens=1024,
    output_format=Grade,
    messages=[{
        "role": "user",
        "content": (
            "Grade this support reply from 1 to 5.\n"
            "Rubric: 5 = apologises, states the concrete action taken, gives a timeline. "
            "Subtract 1 for each missing element. Subtract 2 for any promise the agent cannot verify.\n\n"
            f"<reply>{reply}</reply>"
        ),
    }],
).parsed_output
print("LLM judge:", grade)

# EXERCISE 1: Add 5 more edge cases. Does Haiku still match the bigger model?
# EXERCISE 2: Why use a rubric with concrete criteria instead of "rate quality 1-5"? (Consistency.)
