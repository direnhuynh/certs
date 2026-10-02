"""Day 7: A manual agent loop with two tools. Know every line of this for the exam."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client, text_of

# Fake data the tools read.
ORDERS = {"A100": {"status": "shipped", "carrier": "DHL", "tracking": "DHL-555"}, "A200": {"status": "processing"}}
TRACKING = {"DHL-555": "Out for delivery, expected today 17:00."}

tools = [
    {
        "name": "get_order",
        "description": "Look up an order by its ID. Returns status and, if shipped, the carrier and tracking number.",
        "input_schema": {
            "type": "object",
            "properties": {"order_id": {"type": "string", "description": "Order ID, for example A100"}},
            "required": ["order_id"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "name": "track_package",
        "description": "Get the live delivery status for a tracking number returned by get_order.",
        "input_schema": {
            "type": "object",
            "properties": {"tracking_number": {"type": "string"}},
            "required": ["tracking_number"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]


def run_tool(name: str, args: dict) -> tuple[str, bool]:
    """Return (content, is_error)."""
    if name == "get_order":
        order = ORDERS.get(args["order_id"])
        return (json.dumps(order), False) if order else (f"No order with ID {args['order_id']}.", True)
    if name == "track_package":
        status = TRACKING.get(args["tracking_number"])
        return (status, False) if status else ("Unknown tracking number.", True)
    return (f"Unknown tool {name}.", True)


messages = [{"role": "user", "content": "Where is my order A100? And what about A999?"}]

for turn in range(10):  # always cap iterations
    response = client.messages.create(model=MODEL, max_tokens=4096, tools=tools, messages=messages)
    messages.append({"role": "assistant", "content": response.content})  # full content, incl. tool_use

    if response.stop_reason in ("max_tokens", "refusal"):
        print("stopped early:", response.stop_reason)
        break
    if response.stop_reason != "tool_use":  # end_turn: done
        break

    results = []
    for block in response.content:
        if block.type == "tool_use":
            content, is_error = run_tool(block.name, block.input)
            print(f"[turn {turn}] {block.name}({block.input}) -> {content} (error={is_error})")
            results.append({"type": "tool_result", "tool_use_id": block.id, "content": content, "is_error": is_error})
    messages.append({"role": "user", "content": results})  # ALL results in ONE user message

print("\nFINAL:", text_of(response))

# EXERCISE 1: Count how many tool_use blocks arrive in one turn. That is parallel tool use.
# EXERCISE 2: Make the get_order description vague ("gets data"). Does the agent still choose correctly?
# EXERCISE 3: Note: on claude-opus-5-5, tool_choice {"type": "any"} or {"type": "tool"} returns a 400.
#             Older models accept it. Know all four values for the exam: auto, any, tool, none.
