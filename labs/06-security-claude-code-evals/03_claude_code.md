# Lesson 6.3 — Claude Code (reading + hands-on, no script)

**Domain:** Claude Code (3.1%) · **Cost:** your Claude Code usage only

## Goal

Know the Claude Code features well enough to pick the right one in a scenario. You are using Claude Code now — try each feature in this repository.

## Feature map

| Feature | What it is | When to use |
|---|---|---|
| **`CLAUDE.md`** | Markdown memory loaded at session start | Project conventions, commands, architecture notes |
| **Settings** (`settings.json`) | Permissions, env vars, hooks, model | Team-shared config (project) or personal (user/local) |
| **Permissions** | Allow / ask / deny rules per tool and command | Stop risky commands; pre-approve safe ones |
| **Permission modes** | Default, accept edits, plan mode, bypass | Plan mode = read-only exploration before changes |
| **Hooks** | Shell commands the **harness** runs on events | Guaranteed behaviour: lint after every edit, block a command |
| **Slash commands / skills** | Reusable instructions, loaded on demand | Repeatable workflows (review, deploy, release notes) |
| **Subagents** | Separate Claude instances with own context and tools | Heavy search or review without filling main context |
| **MCP servers** | External tools and data via MCP | GitHub, databases, internal APIs |
| **Headless mode** | `claude -p "prompt"` non-interactive | CI pipelines, scripts, automation |
| **GitHub Actions** | Claude Code in CI, triggered by `@claude` | PR reviews, issue fixes |
| **Claude Agent SDK** | Claude Code harness as a library | Build your own agent product on the same engine |

## CLAUDE.md levels

| Level | Location | Shared? |
|---|---|---|
| Enterprise / managed | System-wide policy path | Whole organization |
| Project | `./CLAUDE.md` (and `.claude/` rules) | Committed to git, whole team |
| User | `~/.claude/CLAUDE.md` | Only you, all projects |
| Local / sub-directory | `CLAUDE.md` in sub-folders, local files | Loaded when relevant |

Run `/init` to generate a starter `CLAUDE.md`. Keep it short and specific; it costs context every session.

## Hooks vs CLAUDE.md — key exam distinction

| | `CLAUDE.md` instruction | Hook |
|---|---|---|
| Who acts | The model (may forget or skip) | The harness (always runs) |
| Guarantee | Guidance | **Deterministic** |
| Example | "Prefer pnpm" | Run `eslint` after every `Edit`; block `rm -rf` |

Hook events include `PreToolUse` (can block a tool call), `PostToolUse`, `UserPromptSubmit`, `SessionStart`, `Stop`, `SubagentStop`, `Notification`.

## Settings precedence (high → low)

Enterprise managed → command-line flags → local project (`.claude/settings.local.json`) → shared project (`.claude/settings.json`) → user (`~/.claude/settings.json`).

## Hands-on (15 minutes)

1. Run `/init` in this repository. Read the generated `CLAUDE.md`.
2. Add a permission rule: allow `Bash(python labs/*)` without prompts. (Ask Claude: "add a permission to allow running lab scripts".)
3. Register the MCP server from Lesson 4.1. Run `/mcp` to see it.
4. Try `claude -p "summarise STUDY_PLAN.md in 3 bullets"` in a terminal.
5. Enter plan mode (Shift+Tab) and ask for a plan to add a new lab. Notice it does not edit files.

## Exam angles

- "Every commit must pass lint, no exceptions" → hook (or CI), not `CLAUDE.md`.
- "Share project conventions with the whole team" → project `CLAUDE.md` committed to git.
- "Run Claude Code in a CI pipeline" → headless `claude -p` or GitHub Actions.
- "Explore a large codebase without polluting context" → subagent.
- "Understand the change before any file is touched" → plan mode.

## Check yourself

1. Why is a hook stronger than a `CLAUDE.md` instruction?
2. Which hook event can block a tool call before it runs?
3. Where do team-shared permissions live?
