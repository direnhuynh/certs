# Lesson 2.4 — Effort and Extended Thinking

**Script:** `04_effort.py` · **Domain:** Model Selection and Optimization · **Cost:** about $0.05–0.15 per run

## Goal

Control how much the model reasons, and trade quality against tokens and latency.

## Extended thinking

The model reasons in `thinking` blocks before its final answer. Better results on maths, logic, coding, planning.

| Generation | Configuration |
|---|---|
| **Current models** | `thinking: {"type": "adaptive"}` — the model decides how much to think |
| Older models (and older exam material) | `thinking: {"type": "enabled", "budget_tokens": N}` — fixed budget, N ≥ 1024 and < `max_tokens` |

- `budget_tokens` is **removed** on the newest models (400 error). Adaptive replaces it.
- Opus 5.5 always thinks; you cannot disable it. Lower the effort instead.
- `display: "summarized"` returns a readable summary of the reasoning. Default on new models is `"omitted"` (empty thinking text). Raw chain of thought is never returned.
- Thinking tokens are **billed as output tokens** whatever the display setting.
- In multi-turn and tool loops, send thinking blocks back unchanged.

## Effort

```python
output_config={"effort": "low" | "medium" | "high" | "xhigh" | "max"}
```

| Effort | Behaviour | Use for |
|---|---|---|
| `low` | Little thinking, short answers, fewer tool calls | Chat, classification, simple subagents, high volume |
| `medium` | Balanced (default on Opus 5.5) | General tasks |
| `high` | Thorough (default on most other models) | Important reasoning |
| `xhigh` | Very thorough | Agentic coding, long tasks |
| `max` | Everything | Correctness matters more than cost |

Effort is the first quality-vs-cost lever **after** free wins like caching. Often the newest model at lower effort beats an older model at high effort.

## Thinking vs latency

More thinking → better answers on hard problems, but slower and pricier. For latency-sensitive routes, use low effort or a smaller model. Stream if users wait (thinking can take a while before the first text token).

## What the script does

Runs a logic puzzle at `low`, `medium` and `high` effort with adaptive thinking and summarised display. Prints time, output tokens, thinking-summary length and the first part of the answer.

## What to observe

- Output tokens and time rise with effort.
- On an easy puzzle, all three may be correct → the higher cost buys nothing. That is the point: measure before raising effort.

## Exam angles

- "Complex reasoning answers are shallow" → enable thinking / raise effort.
- "Responses are too slow and costly for simple FAQ" → lower effort or smaller model.
- "Code sets `budget_tokens` and gets a 400 on a new model" → switch to adaptive + effort.
- "Are thinking tokens free?" → No, billed as output.

## Check yourself

1. Which parameter replaces `budget_tokens` on current models?
2. How are thinking tokens billed?
3. Which effort would you choose for a 10M-request classification route?
