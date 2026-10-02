# Lesson 3.1 — Tool Use and the Manual Agent Loop

**Script:** `01_manual_agent_loop.py` · **Domain:** Agents and Workflows · **Cost:** about $0.03 per run

## Goal

Understand the tool-use protocol line by line. Every agent framework (Tool Runner, Agent SDK, Managed Agents) runs this loop underneath.

## The protocol

```text
YOU  → messages + tools
API  → assistant content: [text?, tool_use{id, name, input}, tool_use{...}]   stop_reason="tool_use"
YOU  → run each tool in your code
YOU  → user content: [tool_result{tool_use_id, content, is_error?}, ...]      (ALL results, ONE message)
API  → more tool_use ... or final text                                         stop_reason="end_turn"
```

The model **never runs code itself** for client tools. It only asks; your code executes.

## Tool definition

```python
{
  "name": "get_order",
  "description": "Look up an order by its ID. Returns status and, if shipped, carrier and tracking number.",
  "input_schema": {"type": "object", "properties": {...}, "required": [...], "additionalProperties": False},
  "strict": True,
}
```

The **description** is what the model reads to decide. Detailed descriptions are the #1 fix for wrong tool choice.

## Loop rules (high exam value)

1. Loop while `stop_reason == "tool_use"`. Stop on `end_turn`.
2. Append the **full** assistant `content` (including `tool_use` blocks) to history.
3. Each `tool_result.tool_use_id` must match a `tool_use.id` from the previous turn.
4. Return **all** results for a turn in **one** user message. Splitting them trains the model to stop parallel calls.
5. On failure, return `is_error: true` with a helpful message ("No order with ID A999"). Never drop the result.
6. Check `max_tokens` (tool input may be cut off) and `refusal` **before** running tools.
7. **Cap iterations** (and cost) so a confused agent cannot loop forever.

## Parallel tool use

One assistant turn can contain several `tool_use` blocks (for example, look up two orders at once). Run them (concurrently if possible), then return all results together. Disable with `disable_parallel_tool_use: true` if order matters.

## tool_choice

| Value | Effect |
|---|---|
| `auto` (default) | Model decides whether to call a tool |
| `any` | Must call some tool |
| `tool` + `name` | Must call that tool |
| `none` | Must not call tools |

Newest models (Opus 5.5, Sonnet 5.5) reject `any` and `tool` with a 400. Use `auto` + a clear instruction + `strict: true`. Exam material may still test forced tool choice — know what it does.

## What the script does

Customer asks about orders A100 and A999. Two tools: `get_order` and `track_package`.
- Turn 1: model calls `get_order` for both (parallel). A999 returns `is_error=True`.
- Turn 2: model calls `track_package("DHL-555")`.
- Turn 3: final answer: A100 out for delivery, A999 not found.

## Exam angles

- "Model calls the wrong tool" → improve names and descriptions.
- "API error: tool_result without matching tool_use" → you dropped or mis-ordered history.
- "Agent stopped making parallel calls" → you sent results in separate messages.
- "Tool throws an exception" → return `is_error: true` with a clear message; let the model recover.

## Check yourself

1. Who executes a client tool — the model or your code?
2. Where do tool results go — `assistant` or `user` message?
3. What prevents an infinite loop?
