"""Day 3: Message Batches API — 50% cheaper, asynchronous, results keyed by custom_id."""

import sys
import time
from pathlib import Path

from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client, text_of

reviews = {
    "review-1": "The app crashes every time I open settings.",
    "review-2": "Love the new dark mode, great work!",
    "review-3": "It is okay. Nothing special.",
}

batch = client.messages.batches.create(
    requests=[
        Request(
            custom_id=review_id,
            params=MessageCreateParamsNonStreaming(
                model=MODEL,
                max_tokens=1024,
                system="Classify the review sentiment. Answer with one word: positive, negative, or neutral.",
                messages=[{"role": "user", "content": text}],
            ),
        )
        for review_id, text in reviews.items()
    ]
)
print("batch id:", batch.id, "| status:", batch.processing_status)

# Poll. A small batch usually ends within minutes; the limit is 24 hours.
while True:
    batch = client.messages.batches.retrieve(batch.id)
    if batch.processing_status == "ended":
        break
    print("status:", batch.processing_status, "| processing:", batch.request_counts.processing)
    time.sleep(20)

print("counts:", batch.request_counts)

# Results arrive in ANY order. Always match by custom_id.
for result in client.messages.batches.results(batch.id):
    if result.result.type == "succeeded":
        print(result.custom_id, "->", text_of(result.result.message).strip(), "| text:", reviews[result.custom_id])
    else:
        print(result.custom_id, "->", result.result.type)  # errored / canceled / expired

# EXERCISE 1: Which result types are safe to resubmit? (expired, errored with a server error)
# EXERCISE 2: A user needs the answer in under 2 seconds. Batch or not? (Not — batch has no latency guarantee.)
