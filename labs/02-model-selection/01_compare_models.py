"""Day 5: Same task on three tiers — compare latency, tokens and cost."""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import HAIKU, OPUS, SONNET, client, text_of

# USD per 1M tokens (input, output). Check https://platform.claude.com/docs for current prices.
PRICES = {OPUS: (4.00, 20.00), SONNET: (2.00, 10.00), HAIKU: (1.00, 5.00)}

task = (
    "A customer writes: 'I was charged twice for my March invoice, order #4471.' "
    "Classify the intent as one of: billing, technical, sales, other. Then write a one-sentence reply."
)

for model in (HAIKU, SONNET, OPUS):
    start = time.perf_counter()
    response = client.messages.create(
        model=model, max_tokens=2048, messages=[{"role": "user", "content": task}]
    )
    seconds = time.perf_counter() - start
    price_in, price_out = PRICES[model]
    cost = (response.usage.input_tokens * price_in + response.usage.output_tokens * price_out) / 1_000_000
    print(f"=== {model}  {seconds:.1f}s  in={response.usage.input_tokens} out={response.usage.output_tokens}  ${cost:.5f}")
    print(text_of(response).strip(), "\n")

# EXERCISE 1: Replace the task with a hard logic puzzle. Where does Haiku start to fail?
# EXERCISE 2: For 10 million of these tickets per day, compute the daily cost per model.
