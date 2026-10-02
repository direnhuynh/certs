# Lesson 1.1 — Messages API Basics

**Script:** `01_basic_message.py` · **Domain:** Applications and Integration · **Cost:** about $0.02 per run

## Goal

Understand the request and response shape of `POST /v1/messages`. Every other feature (tools, thinking, structured output) is a parameter on this same endpoint.

## Concepts

### Request

```python
client.messages.create(
    model="claude-opus-5-5",          # required: exact model ID
    max_tokens=1024,                  # required: hard cap on OUTPUT tokens
    system="You are ...",             # optional: role, rules, context
    messages=[                        # required: conversation, starts with "user"
        {"role": "user", "content": "..."},
    ],
    stop_sequences=["END"],           # optional: stop when this text appears
)
```

- `max_tokens` caps output only. It does not change the price per token.
- `system` is separate from `messages`. Put the role, rules and stable context there.
- `content` can be a string or a **list of blocks** (`text`, `image`, `document`, `tool_result`, ...).

### Response

```text
Message
├── id, model, role="assistant"
├── content: [ThinkingBlock?, TextBlock, ToolUseBlock?, ...]
├── stop_reason: "end_turn" | "max_tokens" | "stop_sequence" | "tool_use" | "pause_turn" | "refusal"
├── stop_sequence: the matched string, or None
└── usage: input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens
```

- `content` is a **list**. Never assume `content[0].text` exists. A thinking block or tool call can come first.
- `usage` is your bill. Log it.

### stop_reason — know all six

| Value | Meaning | Your code should |
|---|---|---|
| `end_turn` | Natural finish | Use the answer |
| `max_tokens` | Hit the cap mid-answer | Raise `max_tokens`, or send the partial answer back and ask to continue |
| `stop_sequence` | Hit one of your `stop_sequences` | Read `stop_sequence` to see which one |
| `tool_use` | Model wants a tool | Run the tool, send `tool_result` (Lesson 3.1) |
| `pause_turn` | A long server-tool turn paused | Send the content back to resume |
| `refusal` | Safety decline | Show a safe message; read `stop_details` |

### The API is stateless

The server remembers nothing between calls. For a chat, you keep the history and send it **every time**:

```text
call 1: [user]
call 2: [user, assistant, user]
call 3: [user, assistant, user, assistant, user]
```

Consequences:
- Input tokens grow with each turn. Long chats get expensive → prompt caching (Lesson 2.2), compaction (Lesson 3.x).
- Append the full assistant `content` list, not only the text. Tool and thinking blocks must survive.

### Prefill (old technique)

Older models let you put a partial `assistant` message last to force the start of the answer (for example `{`). The newest models reject this with a 400. Use structured output (Lesson 1.5) instead. Exam material may still mention prefill — know both.

## What the script does

1. Single request with a system prompt. Prints text, usage, and the list of block types.
2. Two-turn chat. Turn 2 asks "What is my project called?". The model only knows the answer because you resent turn 1.
3. `max_tokens=20` on a long essay → `stop_reason=max_tokens`.
4. `stop_sequences=["4"]` while counting 1–10 → output stops before `4`, `stop_reason=stop_sequence`.

## Expected output

- Step 1 block types: often `['thinking', 'text']` on Opus 5.5, because it always thinks. The thinking text is empty by default.
- Step 3: `stop_reason=max_tokens` and `output_tokens=20`.
- Step 4: text like `'1\n2\n3\n'`, `stop_sequence: 4`.

## Exam angles

- "Response is cut off mid-sentence" → `stop_reason` is `max_tokens`; raise the limit or continue.
- "Chatbot forgets earlier messages" → you are not resending history.
- "Code crashes reading `content[0].text`" → iterate blocks and check `type`.

## Check yourself

1. Which field tells you why generation stopped?
2. Does `max_tokens=100` make a request cheaper if the answer is only 30 tokens? (No — you pay for tokens actually produced.)
3. Why must you append `response.content` and not just the text string?
