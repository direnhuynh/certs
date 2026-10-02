# Lesson 2.2 — Prompt Caching

**Script:** `02_prompt_caching.py` · **Domain:** Model Selection and Optimization · **Cost:** about $0.25 per run (the most expensive lab)

## Goal

Cut cost and latency for requests that repeat a large prefix, and diagnose cache misses. This is one of the most tested topics.

## How it works

The API stores the processed prefix of your prompt. A later request with the **exact same prefix** reads it from the cache instead of processing it again.

```text
Render order:   tools  →  system  →  messages
                └──────── cached prefix ────────┘ ← cache_control breakpoint
                                                   └─ uncached tail (new question)
```

- **Prefix match, byte for byte.** Change one character early in the prompt and everything after it misses.
- Mark the end of the cached part with `cache_control: {"type": "ephemeral"}` on a block. Or use top-level `cache_control` to cache automatically up to the last cacheable block.
- Up to **4 breakpoints** per request.
- **Minimum length**: the prefix must exceed a model-dependent minimum (roughly 512–4096 tokens). Shorter prefixes silently do not cache.

## Pricing (relative to base input price)

| Token type | Price |
|---|---|
| Cache write, 5-minute TTL | about 1.25× |
| Cache write, 1-hour TTL | about 2× |
| Cache read | about 0.1× |
| Normal input | 1× |

- **TTL**: 5 minutes default, or `"ttl": "1h"`. Each hit **refreshes** the TTL.
- The cache pays off from the **second** request. One write + one read already beats two full-price requests.
- Use the 1-hour TTL when requests arrive less often than every 5 minutes but more often than hourly.

## Reading usage

```text
input_tokens                  ← uncached part (full price)
cache_creation_input_tokens   ← written to cache this request
cache_read_input_tokens       ← served from cache
```

## Silent cache killers

| Cause | Fix |
|---|---|
| Timestamp or date in the system prompt | Move it after the breakpoint (into the user message) |
| Request ID / UUID / user name early in prompt | Move it to the end |
| `json.dumps()` without `sort_keys=True` | Sort keys so output is identical |
| Tool list changes order or content | Keep a fixed, sorted tool list |
| Switching model | Caches are per model |
| Prefix below minimum length | Cache a larger stable block |

## Good layout

```text
[tools — fixed]  [system — fixed rules + big document]  ← breakpoint
[conversation history]                                  ← breakpoint (for chats)
[new user question]
```

## What the script does

Uses a ~23K-token refund policy as the system prompt with a breakpoint.
1. First question → **cache write** (`cache_write` about 23K).
2. Different question, same prefix → **cache read** (`cache_read` about 23K, low cost).
3. Adds a timestamp at the **start** of the system prompt → prefix changed → **new cache write**.

## Exam angles

- "Every request includes the same 100-page manual; costs are high" → prompt caching.
- "Caching enabled but `cache_read_input_tokens` is always 0" → something in the prefix changes each call.
- "Requests every 20 minutes, cache keeps expiring" → 1-hour TTL.
- "Multi-turn chat costs grow each turn" → breakpoint on the latest conversation turn.

## Check yourself

1. What is the render order of the prefix?
2. Why did call 3 miss?
3. Approximate price of a cache read vs normal input?
