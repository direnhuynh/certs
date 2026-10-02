# Lesson 1.2 — Streaming

**Script:** `02_streaming.py` · **Domain:** Applications and Integration · **Cost:** about $0.02 per run

## Goal

Know when to stream, how the SDK helper works, and the order of Server-Sent Events (SSE).

## Why stream

| Without streaming | With streaming |
|---|---|
| User sees nothing until the full answer is ready | Text appears token by token |
| Long outputs can hit HTTP timeouts | Connection stays active; no timeout problem |
| Simple code | Slightly more code |

Stream when: chat UI, long output, large `max_tokens` (the SDKs require streaming for very large values), long thinking.
Do not need to stream: short background jobs, batch jobs.

Streaming does **not** change price or total generation time. It changes **time to first token** (perceived latency).

## Two ways in Python

```python
# 1. Helper (recommended): accumulates state for you
with client.messages.stream(model=..., max_tokens=..., messages=...) as stream:
    for text in stream.text_stream:
        print(text, end="")
    final = stream.get_final_message()   # full Message, same as messages.create()

# 2. Raw events: lower memory, you assemble everything
for event in client.messages.create(..., stream=True):
    ...
```

## SSE event order

```text
message_start                      ← Message with empty content, initial usage
  content_block_start  (index 0)   ← block type: text / thinking / tool_use
    content_block_delta  ×N        ← text_delta / thinking_delta / input_json_delta
  content_block_stop
  content_block_start  (index 1)
    ...
  content_block_stop
message_delta                      ← stop_reason + final output_tokens
message_stop
```

- `ping` events can appear anywhere (keep-alive). Ignore them.
- An `error` event can appear mid-stream (for example `overloaded_error`). Your code must handle it even after HTTP 200.
- Delta types: `text_delta` (text), `thinking_delta` (thinking), `input_json_delta` (partial tool input JSON), `signature_delta` (thinking signature).

## What the script does

1. Uses `text_stream` to print text live, then `get_final_message()` to print usage.
2. Iterates raw events and prints the **sequence** of distinct event types and their counts.

## Expected output

Step 2 prints something like:

```text
message_start -> content_block_start -> content_block_delta -> content_block_stop -> content_block_start -> content_block_delta -> content_block_stop -> message_delta -> message_stop
```

Two content blocks appear when the model also emits a thinking block.

## Exam angles

- "Users complain the app feels frozen during long answers" → streaming.
- "Where do you read the stop reason in a stream?" → `message_delta`.
- "Request with very large `max_tokens` times out" → stream it.
- "Stream fails halfway with overloaded error" → handle the `error` event; retry.

## Check yourself

1. Does streaming reduce cost? (No.)
2. Which event carries the final `output_tokens`?
3. What delta type carries tool input while it is generated?
