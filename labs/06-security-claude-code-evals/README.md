# Domains 6–8 — Security and Safety (8.1%), Claude Code (3.1%), Eval/Testing/Debugging (2.6%)

## Lessons (read the `.md`, then run the `.py`)

| # | Lesson | Script | Topic |
|---|---|---|---|
| 6.1 | [01_prompt_injection.md](01_prompt_injection.md) | `01_prompt_injection.py` | Direct and indirect injection, defence in depth, secrets, refusals |
| 6.2 | [02_simple_eval.md](02_simple_eval.md) | `02_simple_eval.py` | Success criteria, code vs LLM grading, debugging checklist |
| 6.3 | [03_claude_code.md](03_claude_code.md) | — (hands-on in Claude Code) | CLAUDE.md, hooks, permissions, subagents, headless mode |

## Domain summary

- Assume the model can be fooled; limit what a fooled model can do.
- Deterministic behaviour in Claude Code → hooks, not CLAUDE.md.
- Decisions about prompts and models → backed by an eval.
