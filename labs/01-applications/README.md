# Domain 1 — Applications and Integration (33.1%)

The biggest domain. Questions give you a production scenario and ask for the right API feature or pattern.

## Lessons (read the `.md`, then run the `.py`)

| # | Lesson | Script | Topic |
|---|---|---|---|
| 1.1 | [01_basic_message.md](01_basic_message.md) | `01_basic_message.py` | Request/response shape, `stop_reason`, stateless multi-turn |
| 1.2 | [02_streaming.md](02_streaming.md) | `02_streaming.py` | When to stream, SSE event order |
| 1.3 | [03_errors_and_retry.md](03_errors_and_retry.md) | `03_errors_and_retry.py` | Status codes, retryable errors, backoff |
| 1.4 | [04_batch.md](04_batch.md) | `04_batch.py` | Batches API: 50% off, async, `custom_id` |
| 1.5 | [05_structured_output.md](05_structured_output.md) | `05_structured_output.py` | Guaranteed JSON, strict tools |

## Also read in the docs (no script)

- Vision: image input (base64 or URL).
- PDF input as `document` blocks.
- Files API: upload once, reuse by `file_id`.
- Citations: `citations: {enabled: true}` on documents (not compatible with structured output).

## Domain summary

- "Users wait on long answers" → streaming.
- "Large offline job, lowest cost" → Batches API.
- "Parser fails on malformed JSON" → structured output.
- "Intermittent 429/529" → retry with backoff.
