# Lesson 1.4 — Message Batches API

**Script:** `04_batch.py` · **Domain:** Applications and Integration · **Cost:** under $0.01 per run · **Time:** usually a few minutes

## Goal

Know when the Batches API is the right answer and how its lifecycle works.

## Key facts (memorise)

| Fact | Value |
|---|---|
| Price | **50% of standard** input and output price |
| Latency | Asynchronous. Most batches finish within 1 hour. Maximum **24 hours**, then unfinished requests **expire** |
| Size | Up to **100,000 requests** or **256 MB** per batch |
| Results kept | **29 days** |
| Features | Every Messages API feature works (tools, vision, caching, system prompts) |
| Result order | **Any order** — match by `custom_id` |

## Lifecycle

```text
batches.create(requests=[{custom_id, params}, ...])
        │   processing_status = "in_progress"
        ▼
batches.retrieve(id)   ← poll until processing_status == "ended"
        │
        ▼
batches.results(id)    ← stream results, one per request
        each result.result.type ∈ succeeded | errored | canceled | expired
```

- `custom_id` is your key (for example a database row ID). Must be unique in the batch.
- `request_counts` shows `processing`, `succeeded`, `errored`, `canceled`, `expired`.
- `batches.cancel(id)` stops a batch; unfinished requests become `canceled`.

## Handling results

| type | Action |
|---|---|
| `succeeded` | Read `result.message` (a normal Message) |
| `errored` | `invalid_request` → fix and resubmit. Server error → resubmit as is |
| `expired` | Did not finish in 24 h → resubmit |
| `canceled` | You cancelled → resubmit if still needed |

## When to use

Use batches when **nobody waits** for the answer:
- Nightly classification or tagging of large datasets
- Running evals across hundreds of test cases
- Bulk summarisation, content moderation backlog, data extraction

Do **not** use for: chat, anything a user waits on, anything with a latency requirement.

Combine with prompt caching for more savings when requests share a long prefix.

## What the script does

1. Creates a batch of 3 sentiment-classification requests with `custom_id` = review ID.
2. Polls every 20 s until `processing_status == "ended"`.
3. Reads results and joins each one back to its review text by `custom_id`.

## Exam angles

- "Classify 2 million records overnight at lowest cost" → Batches API.
- "Real-time support chat, reduce cost" → **not** batches (latency). Use caching or a smaller model.
- "Results don't line up with inputs" → you matched by position; match by `custom_id`.

## Check yourself

1. Maximum processing time before expiry?
2. Why can't you trust result order?
3. Can you use tools and images inside a batch request? (Yes.)
