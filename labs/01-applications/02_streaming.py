"""Day 2: Streaming — text deltas, raw SSE events, final message."""

import sys from collections
import Counter from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client, print_usage

prompt = [{"role": "user", "content": "Explain HTTP keep-alive in 5 short bullet points."}]

# 1. High-level helper: print text as it arrives, then read the full message.
print("--- 1. text_stream ---")
with client.messages.stream(model=MODEL, max_tokens=2048, messages=prompt) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final = stream.get_final_message()
print()
print_usage(final)

# 2. Raw events: see the SSE event order the exam asks about.
print("\n--- 2. event types in order ---")
seen = []
counts = Counter()
with client.messages.stream(model=MODEL, max_tokens=2048, messages=prompt) as stream:
    for event in stream:
        counts[event.type] += 1
        if not seen or seen[-1] != event.type:
            seen.append(event.type)
print(" -> ".join(seen))
print(dict(counts))

# EXERCISE 1: Which event carries the final stop_reason and output token count? (Look at message_delta.)
# EXERCISE 2: Add thinking={"type": "adaptive", "display": "summarized"} to call 2.
#             Which new delta type appears? (thinking_delta)
# EXERCISE 3: When must you stream? Write your answer in notes/cheatsheet.md.
