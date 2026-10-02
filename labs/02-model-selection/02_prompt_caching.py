"""Day 6: Prompt caching — watch cache_creation and cache_read tokens change."""

import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client, print_usage

# A large stable document. It must exceed the model's minimum cacheable length.
POLICY = "\n".join(
    f"Rule {i}: Refunds for order type {i % 7} are allowed within {10 + i % 20} days if the item is unused "
    f"and the customer provides receipt number format R-{i:05d}."
    for i in range(600)
)


def ask(question: str, system_prefix: str = ""):
    return client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": system_prefix + "You answer questions about this refund policy:\n\n" + POLICY,
                "cache_control": {"type": "ephemeral"},  # cache everything up to here
            }
        ],
        messages=[{"role": "user", "content": question}],  # volatile part comes after the breakpoint
    )


print("--- 1. first call: expect cache_write > 0 ---")
print_usage(ask("What is the refund window for rule 12?"))

print("--- 2. same prefix, different question: expect cache_read > 0 ---")
print_usage(ask("What receipt format does rule 99 need?"))

print("--- 3. timestamp at the start of the system prompt: cache miss again ---")
print_usage(ask("What is rule 5?", system_prefix=f"Current time: {datetime.now().isoformat()}\n"))

# EXERCISE 1: Move the timestamp into the user message instead. Does call 3 hit the cache now?
# EXERCISE 2: Reduce POLICY to range(5). Why does cache_write become 0? (Below minimum length.)
# EXERCISE 3: Add "ttl": "1h" to cache_control. When is the 1-hour TTL worth its higher write price?
