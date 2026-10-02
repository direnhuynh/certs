# CCDV-F Study Workspace

Two-week preparation for **Claude Certified Developer – Foundations (CCDV-F)**.

- Exam: 53 questions, 120 minutes, Pearson VUE, US$125, pass at 720/1000 (scaled).
- Eligibility: Claude Partner Network organizations only. Register with your company email at the [Anthropic Partner Academy](https://anthropic-partners.skilljar.com/page/partner-certifications).
- Download the official exam guide there and check the domain weights in `STUDY_PLAN.md` against it.

## Layout

| Path | Content |
|---|---|
| `STUDY_PLAN.md` | Day-by-day plan with a progress checklist |
| `common/client.py` | Shared Anthropic client and model constants |
| `labs/01-applications/` | Messages API, streaming, errors, batches, structured output (33.1%) |
| `labs/02-model-selection/` | Model choice, prompt caching, token counting, effort (16.8%) |
| `labs/03-agents/` | Workflow patterns, manual agent loop, tool runner (14.7%) |
| `labs/04-tools-mcp/` | Tool schema design, MCP server (10.6%) |
| `labs/05-prompt-context/` | Prompt and context engineering exercises (11.0%) |
| `labs/06-security-claude-code-evals/` | Prompt injection, evals, Claude Code (13.8% combined) |
| `notes/cheatsheet.md` | Facts to know cold on exam day |
| `notes/mistakes.md` | Log of every practice question you got wrong |
| `practice/` | 5 mock tests (53 questions each), encoded answer keys, score tracker |

## Setup

```bash
sudo apt install python3.12-venv   # Ubuntu/Debian: needed once, provides venv + pip
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo 'ANTHROPIC_API_KEY=sk-ant-...' > .env   # put your real key here; .env is git-ignored
```

Get an API key at https://platform.claude.com. Every lab calls the real API and costs a small amount of money.
Most labs cost under US$0.05 per run.

Run a lab from the repository root:

```bash
python labs/01-applications/01_basic_message.py
```

## Lessons

Every script has a lesson file with the same name: `01_basic_message.md` explains `01_basic_message.py`.
Each lesson has: goal, concepts, what the script does, expected output, exam angles, and self-check questions.

| Domain | Lessons |
|---|---|
| 1 Applications | 1.1 Messages API · 1.2 Streaming · 1.3 Errors and retry · 1.4 Batches · 1.5 Structured output |
| 2 Model selection | 2.1 Choosing a model · 2.2 Prompt caching · 2.3 Token counting · 2.4 Effort and thinking |
| 3 Agents | 3.1 Manual agent loop · 3.2 Tool Runner and architectures |
| 4 Tools and MCP | 4.1 Tool design and MCP server |
| 5 Prompting | 5.1 Prompt and context engineering |
| 6–8 Security, Claude Code, Evals | 6.1 Prompt injection · 6.2 Evals · 6.3 Claude Code (no script) |

## How to study each day

1. Read the lesson `.md` file.
2. Run the matching `.py` script. Compare the output with "Expected output" in the lesson.
3. Do the `EXERCISE` comments in the script, then answer "Check yourself" in the lesson.
4. Answer 10 practice questions for the domain. Log each miss in `notes/mistakes.md`.
5. Tick the day in `STUDY_PLAN.md`.
