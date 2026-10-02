"""Day 8: The SDK Tool Runner runs the agent loop for you (beta helper)."""

import sys
from pathlib import Path

from anthropic import beta_tool

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client

INVENTORY = {"keyboard": 12, "mouse": 0, "monitor": 3}


@beta_tool
def check_stock(product: str) -> str:
    """Return how many units of a product are in stock.

    Args:
        product: Product name in lower case, for example keyboard.
    """
    if product not in INVENTORY:
        return f"Unknown product {product}. Known products: {', '.join(INVENTORY)}."
    return f"{INVENTORY[product]} units of {product} in stock."


@beta_tool
def reorder(product: str, quantity: int) -> str:
    """Place a supplier reorder for a product that is out of stock.

    Args:
        product: Product name in lower case.
        quantity: Units to order, between 1 and 100.
    """
    return f"Reorder placed: {quantity} x {product}."


# The schema is generated from the function signature and docstring.
runner = client.beta.messages.tool_runner(
    model=MODEL,
    max_tokens=4096,
    tools=[check_stock, reorder],
    messages=[{"role": "user", "content": "Check stock for keyboard, mouse and monitor. Reorder 20 of anything at zero."}],
)

for message in runner:  # one iteration per model turn; stops when Claude is done
    for block in message.content:
        if block.type == "tool_use":
            print("tool call:", block.name, block.input)
        elif block.type == "text":
            print("text:", block.text)

# EXERCISE 1: Add a human approval step: in reorder(), ask input("approve? y/n") and return
#             "User declined." when the answer is n. Watch how Claude reacts.
# EXERCISE 2: Tool Runner versus Claude Agent SDK — write the difference in notes/cheatsheet.md.
