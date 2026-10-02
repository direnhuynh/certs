# Lesson 2.1 — Choosing a Model

**Script:** `01_compare_models.py` · **Domain:** Model Selection and Optimization · **Cost:** about $0.01 per run

## Goal

Pick the right model tier for a workload by trading off **quality, latency and cost**.

## The tiers

| Tier | Current ID | Price in / out per 1M tokens | Strength | Typical use |
|---|---|---|---|---|
| Opus | `claude-opus-5-5` | $4 / $20 | Deepest reasoning, long agentic tasks | Complex coding, research agents, hard analysis |
| Sonnet | `claude-sonnet-5-5` | $2 / $10 | Strong and faster | Most production apps, customer-facing assistants |
| Haiku | `claude-haiku-4-5` | $1 / $5 | Fastest, cheapest | Classification, routing, extraction, subagents, high volume |

Prices change. Check the pricing page before the exam; know the **relative** order more than exact numbers.

## Selection method

1. **Prove the task** on the most capable model. If even Opus fails, the problem is the prompt or the task, not the tier.
2. **Build an eval set** (Lesson 6.2).
3. **Step down** to Sonnet, then Haiku, while the eval score stays acceptable.
4. **Route** mixed traffic: a cheap model classifies difficulty, then sends hard cases to a bigger model (routing pattern, Lesson 3.1).
5. Re-test when you change models: prompts tuned for one model may need small changes.

## Factors

| Factor | Pushes toward |
|---|---|
| Hard reasoning, multi-step planning, code | Opus |
| Latency-sensitive (autocomplete, live chat) | Haiku or Sonnet |
| Very high volume, simple task | Haiku |
| Large context window needed | Check each model's limit (Haiku 4.5: 200K; Opus/Sonnet 5.x: 1M) |
| Vision, tools | All current tiers support them |

## Cost formula

```text
cost = input_tokens × input_price + output_tokens × output_price
```

- Output tokens cost about **5×** input tokens. Long answers and thinking are the expensive part.
- Thinking tokens are billed as output.

## What the script does

Sends the same "classify intent + write one-sentence reply" task to Haiku, Sonnet and Opus. Prints time, tokens, cost and answer for each.

## What to observe

- All three classify this easy ticket correctly → for this task, Haiku is the rational choice.
- Latency and cost rise with tier.
- Bigger models may write more (more thinking, longer reply) → output tokens dominate cost.

## Exam angles

- "10 million simple classifications per day, tight budget" → Haiku (plus batches if offline).
- "Agent fails at a complex multi-file refactor on Sonnet" → try Opus or raise effort.
- "How do you prove a cheaper model is good enough?" → run an eval set on both.

## Check yourself

1. Why start with the strongest model?
2. Which costs more per token: input or output?
3. Which model has the smallest context window in the table?
