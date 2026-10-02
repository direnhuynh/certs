"""Day 1: Messages API basics — request shape, content blocks, stop_reason, multi-turn."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client, print_usage, text_of

# 1. Single request with a system prompt.
response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    system="You are a concise senior Python engineer.",
    messages=[{"role": "user", "content": "In two sentences: what is a Python generator?"}],
)
print("--- 1. single request ---")
print(text_of(response))
print_usage(response)
print("block types:", [block.type for block in response.content])

# 2. Multi-turn. The API keeps no state: send the whole history each time.
history = [{"role": "user", "content": "My project is called Pelican. Reply with OK."}]
response = client.messages.create(model=MODEL, max_tokens=1024, messages=history)
history.append({"role": "assistant", "content": response.content})  # append full content blocks, not only the text
history.append({"role": "user", "content": "What is my project called?"})
response = client.messages.create(model=MODEL, max_tokens=1024, messages=history)
print("\n--- 2. multi-turn ---")
print(text_of(response))

# 3. Force stop_reason == "max_tokens".
response = client.messages.create(
    model=MODEL,
    max_tokens=20,
    messages=[{"role": "user", "content": "Write a 300-word essay about databases."}],
)
print("\n--- 3. truncated ---")
print_usage(response)  # expect stop_reason=max_tokens

# 4. stop_sequences.
response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    stop_sequences=["4"],
    messages=[{"role": "user", "content": "Count from 1 to 10, one number per line. Output only the numbers."}],
)
print("\n--- 4. stop sequence ---")
print(repr(text_of(response)))
print("stop_reason:", response.stop_reason, "| stop_sequence:", response.stop_sequence)

# EXERCISE 1: In request 1, set max_tokens=5. Which stop_reason do you get?
# EXERCISE 2: Remove the assistant turn in step 2 so two "user" messages are adjacent. Does the API accept it?
# EXERCISE 3: Add a final {"role": "assistant", "content": "Sure:"} prefill to step 1.
#             Current models reject prefill with a 400. What replaces prefill? (Answer: structured output or system prompt.)
