"""Day 5: Count tokens before you send — estimate cost and check context limits."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import HAIKU, MODEL, client

text = Path(__file__).resolve().parents[2].joinpath("STUDY_PLAN.md").read_text()
messages = [{"role": "user", "content": f"Summarize this plan:\n\n{text}"}]

for model, price_in in ((MODEL, 4.00), (HAIKU, 1.00)):
    count = client.messages.count_tokens(model=model, messages=messages)
    print(f"{model}: {count.input_tokens} input tokens  ≈ ${count.input_tokens * price_in / 1_000_000:.5f}")

# Different model families can use different tokenizers, so counts can differ for the same text.
# Never estimate Claude tokens with tiktoken; use count_tokens.

# EXERCISE: Add a tools=[...] list to count_tokens. Do tool definitions cost input tokens? (Yes.)
