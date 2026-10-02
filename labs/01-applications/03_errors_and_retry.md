# Lesson 1.3 — Errors and Retry

**Script:** `03_errors_and_retry.py` · **Domain:** Applications and Integration · **Cost:** under $0.01 per run (failed requests are not billed)

## Goal

Classify every API error as **retryable** or **not retryable**, and know the SDK's built-in retry behaviour.

## HTTP status codes

| Code | SDK class (Python) | Meaning | Retry? |
|---|---|---|---|
| 400 | `BadRequestError` | Invalid request (bad params, empty messages, prefill on new models) | No — fix the request |
| 401 | `AuthenticationError` | Bad or missing API key | No |
| 403 | `PermissionDeniedError` | Key lacks permission | No |
| 404 | `NotFoundError` | Wrong model ID or endpoint | No |
| 413 | `APIStatusError` | Request too large | No — shrink it |
| 429 | `RateLimitError` | Rate limit hit | **Yes** — wait `retry-after` seconds |
| 500 | `InternalServerError` | Server error | **Yes** |
| 529 | `APIStatusError` (overloaded) | API temporarily overloaded | **Yes** |
| — | `APIConnectionError` / `APITimeoutError` | Network problem / timeout | **Yes** |

Rule: **4xx except 429 = your fault, do not retry. 429, 5xx, network = retry with backoff.**

## Exponential backoff with jitter

```text
delay = base × 2^attempt + random(0, 1)
attempt 0 → ~1s, 1 → ~2s, 2 → ~4s, 3 → ~8s ...
```

- **Exponential**: back off harder each time so you do not hammer a struggling server.
- **Jitter**: random spread so many clients do not retry at the same instant.
- **`retry-after` header** on 429: the server tells you how long to wait. Use it.
- **Cap** the number of attempts and the maximum delay.

## SDK behaviour (built in)

- Retries connection errors, 408, 409, 429 and ≥500 automatically, **2 times by default**, with exponential backoff.
- Change it: `anthropic.Anthropic(max_retries=5)` or per call `client.with_options(max_retries=0)`.
- Default timeout: 10 minutes. Change with `timeout=`.
- Catch exceptions **most specific first**: `NotFoundError` → `RateLimitError` → `APIStatusError` → `APIConnectionError`.

## Rate limits (concept)

Limits are per organization and model: requests per minute (RPM), input tokens per minute (ITPM), output tokens per minute (OTPM). Response headers show remaining capacity (`anthropic-ratelimit-*`). Prompt cache reads count less against input limits on current models, so caching also helps throughput.

## Debugging

Log `response._request_id` (from the `request-id` header). Anthropic support needs it to trace a request.

## What the script does

1. `call_with_retry()` — manual backoff loop (SDK retries turned off with `max_retries=0` so you see the logic). Makes one good call.
2. Sends two bad requests and catches the exact exception class:
   - unknown model → `NotFoundError` (404)
   - empty `messages` → `BadRequestError` (400)

## Exam angles

- "Intermittent 529 errors at peak hours" → retry with exponential backoff and jitter. Not "switch endpoints", not "increase max_tokens".
- "Batch job gets 429s" → respect `retry-after`, reduce concurrency, or use the Batches API.
- "App retries a 400 forever" → bug; 400 is not retryable.

## Check yourself

1. Which status means "overloaded"? Retry it?
2. Why add jitter?
3. How many times does the Python SDK retry by default?
