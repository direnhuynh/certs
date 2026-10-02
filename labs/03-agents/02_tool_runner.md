# Lesson 3.2 — Tool Runner and Agent Architectures

**Script:** `02_tool_runner.py` · **Domain:** Agents and Workflows · **Cost:** about $0.03 per run

## Goal

Let the SDK run the agent loop, and know which agent-building option fits which scenario.

## Tool Runner

```python
@beta_tool
def check_stock(product: str) -> str:
    """Return how many units of a product are in stock.

    Args:
        product: Product name in lower case.
    """

runner = client.beta.messages.tool_runner(model=..., max_tokens=..., tools=[check_stock], messages=[...])
for message in runner:   # one model turn per iteration; ends when no more tool calls
    ...
```

- Schema built from the **type hints**, description from the **docstring**. Write good docstrings.
- Runs the Lesson 3.1 loop for you: calls tools, appends results, repeats.
- Human approval does not need a manual loop: check inside the tool and return "User declined."
- Beta helper in the regular `anthropic` SDK.

## Four ways to build an agent

| Option | Loop run by | Hosting | Built-in tools | Choose when |
|---|---|---|---|---|
| Manual loop (Messages API) | You | You | None | Full control, unusual control flow |
| Tool Runner | SDK | You | None (your tools) | Custom-tool agent, least code |
| **Claude Agent SDK** | SDK (Claude Code harness) | You | Read/Write/Edit/Bash/Grep/Web + MCP + subagents | Coding or file-system agent on your infra |
| **Managed Agents** | Anthropic | Anthropic sandbox per session | Bash, files, code exec, MCP | Hosted, long-running, scheduled agents |

**Tool Runner ≠ Agent SDK.** Tool Runner is a loop helper for your tools. The Agent SDK is Claude Code packaged as a library.

## Workflow patterns (from "Building effective agents")

| Pattern | Shape | Example |
|---|---|---|
| Prompt chaining | A → check → B → C | Outline → validate → draft → translate |
| Routing | Classifier → specialised handler | Refund vs tech support vs sales prompts |
| Parallelization | Sectioning or voting | 3 reviewers vote on "is this code vulnerable?" |
| Orchestrator-workers | Lead splits task at run time → workers | Change N files where N is unknown in advance |
| Evaluator-optimizer | Generate → critique → revise loop | Literary translation, code with tests |
| Autonomous agent | Model plans and uses tools in a loop | Open-ended research, coding tasks |

Start simple: single call → workflow → agent. Agents cost more, are slower and harder to test.

### Should it be an agent? Check all four

- **Complexity**: steps unknown in advance?
- **Value**: worth higher cost and latency?
- **Viability**: can the model do it well?
- **Cost of error**: can mistakes be caught (tests, review, rollback)?

## Context management

| Problem | Tool |
|---|---|
| Sub-task reads lots of data | **Subagent**: fresh context, returns only a summary |
| Old tool results fill the window | **Context editing**: clear old tool results |
| Conversation near the limit | **Compaction**: server summarises earlier history |
| Facts needed across sessions | **Memory tool**: files the agent reads and writes |

## What the script does

Two tools (`check_stock`, `reorder`). The model checks stock for three products (likely in parallel), sees mouse = 0, calls `reorder("mouse", 20)`, and then summarises.

## Exam angles

- "Coding agent on our own servers with file and shell tools" → Claude Agent SDK.
- "Don't want to host the agent runtime or sandbox" → Managed Agents.
- "Steps are fixed: extract → validate → store" → prompt chaining, not an agent.
- "Run 3 independent checks and combine" → parallelization.

## Check yourself

1. Where does the Tool Runner get the tool description?
2. Difference between Tool Runner and Agent SDK?
3. Which pattern fits "unknown number of sub-tasks decided at run time"?
