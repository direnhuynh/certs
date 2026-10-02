# Domain 2 — Model Selection and Optimization (16.8%)

Questions ask you to balance quality, latency and cost.

## Lessons (read the `.md`, then run the `.py`)

| # | Lesson | Script | Topic |
|---|---|---|---|
| 2.1 | [01_compare_models.md](01_compare_models.md) | `01_compare_models.py` | Opus vs Sonnet vs Haiku, selection method |
| 2.2 | [02_prompt_caching.md](02_prompt_caching.md) | `02_prompt_caching.py` | Prefix caching, pricing, cache killers |
| 2.3 | [03_count_tokens.md](03_count_tokens.md) | `03_count_tokens.py` | Count before sending, context windows |
| 2.4 | [04_effort.md](04_effort.md) | `04_effort.py` | Adaptive thinking, effort levels |

## Domain summary — cost levers in order

1. Prompt caching (free win for repeated prefixes).
2. Batches API (50% off when nobody waits).
3. Right-size output and context (only relevant content).
4. Effort level.
5. Smaller model — prove it with an eval first.
