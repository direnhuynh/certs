# CCDV-F Cheat Sheet

Read this the night before the exam. Add a line every time a practice question surprises you.

## Decision rules

| Scenario says | Answer |
|---|---|
| Long output, user waits, blank screen | Streaming |
| Large offline job, lowest cost | Message Batches API (50% off, up to 24 h) |
| Same large context in every request | Prompt caching |
| Cache read tokens always 0 | Something in the prefix changes (timestamp, UUID, tool order) |
| JSON parser fails on model output | Structured output (`output_config.format`) or `strict: true` tools |
| 429 / 529 / 5xx | Retry with exponential backoff + jitter, honour `retry-after` |
| 400 / 401 / 403 / 404 | Fix the request; do not retry |
| Simple, high-volume, latency-sensitive | Haiku |
| Hardest reasoning or long agentic coding | Opus |
| Steps are known in advance | Workflow, not agent |
| Model chooses wrong tool | Better tool names and descriptions |
| Integration reused across apps | MCP server |
| Read-only data the app attaches | MCP resource |
| Instruction inside a web page or tool result | Prompt injection: treat as data, least privilege, human approval |
| Must always run on every edit in Claude Code | Hook, not CLAUDE.md |
| "Is the cheaper model good enough?" | Run an eval set |
| Context fills up in a long agent run | Subagents, context editing, compaction |

## Numbers

- Batches: 50% price, ≤100,000 requests or 256 MB, ≤24 h, results kept 29 days.
- Cache: write ≈1.25× input (5 min TTL), read ≈0.1× input, TTL 5 min or 1 h, ≤4 breakpoints, order `tools → system → messages`.
- SDK default: 2 retries, 10 minute timeout.

## stop_reason

`end_turn` · `max_tokens` · `stop_sequence` · `tool_use` · `pause_turn` · `refusal`

## Streaming events

`message_start` → `content_block_start` → `content_block_delta` … → `content_block_stop` → `message_delta` (stop_reason, usage) → `message_stop`. Also `ping` and `error`.

## Old versus new API (exam material may use either)

| Older form | Current form |
|---|---|
| `thinking: {type: "enabled", budget_tokens: N}` | `thinking: {type: "adaptive"}` + `output_config.effort` |
| Assistant prefill to force format | Structured output / system prompt |
| `tool_choice: any` / `tool` to force a call | Still valid on older models; newest models need `auto` + instruction |
| `output_format` request field | `output_config.format` |

## My own notes

- 
