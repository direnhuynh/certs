# Domain 3 — Agents and Workflows (14.7%)

Also read Anthropic's post "Building effective agents" — many questions come from it.

## Lessons (read the `.md`, then run the `.py`)

| # | Lesson | Script | Topic |
|---|---|---|---|
| 3.1 | [01_manual_agent_loop.md](01_manual_agent_loop.md) | `01_manual_agent_loop.py` | Tool-use protocol, loop rules, parallel tools, `tool_choice` |
| 3.2 | [02_tool_runner.md](02_tool_runner.md) | `02_tool_runner.py` | Tool Runner, Agent SDK vs Managed Agents, workflow patterns, context management |

## Domain summary

- Simplest first: single call → workflow → agent.
- Steps known in advance → workflow. Steps decided at run time → agent.
- Loop on `tool_use`, return all results in one message, cap iterations.
- Long tasks → subagents, context editing, compaction, memory.
