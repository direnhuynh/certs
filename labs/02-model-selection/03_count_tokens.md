# Lesson 2.3 — Token Counting

**Script:** `03_count_tokens.py` · **Domain:** Model Selection and Optimization · **Cost:** free (`count_tokens` is not billed)

## Goal

Measure input size **before** sending: estimate cost, stay inside the context window, and enforce budgets.

## The endpoint

```python
count = client.messages.count_tokens(
    model="claude-opus-5-5",
    system="...",          # optional
    tools=[...],           # optional — tool definitions count as input
    messages=[...],
)
count.input_tokens
```

- Accepts the same fields as `messages.create()` (system, tools, images, documents).
- Free to call, but has its own rate limit.
- Result is an estimate; actual usage can differ slightly.

## Why it matters

| Need | Use |
|---|---|
| Reject or trim an input that will not fit the context window | Count first, then truncate or chunk |
| Show a cost estimate before running | `input_tokens × price` |
| Decide whether a prefix is long enough to cache | Compare with the minimum cacheable length |
| Track per-user spend | Count and store |

## Tokens are not words

- Roughly 1 token ≈ 3–4 English characters, but it varies by language and content (code, Vietnamese, JSON).
- **Different model generations can use different tokenizers.** The same text can produce different counts on different models.
- **Never** use OpenAI's `tiktoken` to estimate Claude tokens. Use `count_tokens`.

## Hidden input tokens

These all count as input:
- System prompt
- Tool definitions (name, description, schema) and the built-in tool-use system prompt
- Images and PDF pages
- Every previous turn of the conversation (the API is stateless)

## Context window

- Opus 5.5 and Sonnet 5.5: 1M tokens. Haiku 4.5: 200K tokens.
- The window holds **input + output**. A huge input leaves less room for the answer.
- Use the Models API (`client.models.retrieve(id)`) to read `max_input_tokens` and `max_tokens` live.

## What the script does

Counts the tokens of `STUDY_PLAN.md` wrapped in a summarise request, for Opus and Haiku, and prints an input cost estimate for each.

## What to observe

The two counts may differ — different tokenizers.

## Exam angles

- "Estimate the cost of a request before sending it" → `count_tokens`.
- "App fails with context-length errors on big documents" → count, then chunk or summarise.
- "Team estimates tokens with tiktoken and bills are off" → use `count_tokens`.

## Check yourself

1. Do tool definitions cost tokens?
2. Is `count_tokens` billed?
3. Why can the same text give different counts on two models?
