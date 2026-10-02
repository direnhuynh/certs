# Lesson 4.1 — Tool Design and MCP Servers

**Script:** `01_mcp_server.py` · **Domain:** Tools and MCPs · **Cost:** $0 for the server (using it inside Claude Code counts against your Claude Code usage)

## Goal

Design tools the model uses correctly, and expose them through the Model Context Protocol (MCP) so any MCP host can use them.

## Part 1 — Tool design

### Good description checklist

- What the tool does, **when** to use it, and when **not** to.
- What it returns (format, units).
- Limits and side effects ("sends a real email", "read-only").
- Meaning of each parameter, with an example value.

```text
Bad:  "get_data — gets data"
Good: "search_orders — Search the customer's orders by status or date range. Read-only.
       Returns up to 20 orders as JSON (id, status, total_usd). Use get_order for one known ID."
```

### Schema checklist

- Precise types, `enum` for fixed choices, `required` list, `additionalProperties: false`.
- `strict: true` → tool input guaranteed to match the schema.
- Validate inputs in code anyway (paths, amounts, permissions) — schema ≠ security.

### Tool set design

- A few well-separated tools beat many overlapping ones. Overlap confuses selection.
- Return concise, relevant results. Huge tool outputs fill context and cost tokens.
- Return actionable error messages with `is_error: true`.
- Many tools (dozens+)? Use **tool search** with `defer_loading: true` so definitions load on demand.

### Client tools vs server tools

| Type | Runs where | Examples |
|---|---|---|
| Client tools | Your code | Your functions, DB queries, internal APIs |
| Anthropic-defined client tools | Your code, schema built in | `bash`, text editor, computer use, memory |
| Server tools | Anthropic's infrastructure | Web search, web fetch, code execution, tool search |

Server tool results arrive in the same response; no loop on your side. A long server-tool turn can end with `stop_reason: "pause_turn"`.

## Part 2 — MCP

MCP is an open standard to connect AI applications to tools and data — "USB-C for AI integrations". Build an integration once; use it in Claude Code, Claude Desktop, claude.ai and your own apps.

### Architecture

```text
HOST (Claude Code, Claude Desktop, your app)
 ├── MCP client ──── MCP server A (GitHub)
 ├── MCP client ──── MCP server B (database)
 └── MCP client ──── MCP server C (your study-notes server)
```

One client per server connection. Messages use JSON-RPC 2.0.

### Server primitives — who controls them

| Primitive | Controlled by | Purpose | In the script |
|---|---|---|---|
| **Tools** | Model | Actions with side effects or lookups | `add_note` |
| **Resources** | Application | Read-only data the app attaches as context | `notes://all` |
| **Prompts** | User | Reusable templates the user chooses (often slash commands) | `quiz_me` |

### Transports

| Transport | Use |
|---|---|
| **stdio** | Local server started as a subprocess (this lab) |
| **Streamable HTTP** | Remote server over HTTP; supports auth (OAuth) |
| SSE | Older remote transport, being replaced by Streamable HTTP |

### Using MCP from the Messages API

The MCP connector lets the API call a **remote** MCP server directly: pass `mcp_servers=[{type: "url", url, name}]` **and** a tool entry `{type: "mcp_toolset", mcp_server_name: name}` (beta header). Only remote servers, not stdio.

### Security

- Only install MCP servers you trust; they run with your permissions.
- Tool output from MCP servers is untrusted data (prompt injection risk, Lesson 6.1).
- Scope credentials narrowly.

## What the script does

A `FastMCP` server named `study-notes` over stdio with one tool, one resource and one prompt. Notes are stored in `notes/mcp-notes.md`.

## Run it

```bash
source .venv/bin/activate
# Inspect with the MCP Inspector (needs Node.js)
npx @modelcontextprotocol/inspector python labs/04-tools-mcp/01_mcp_server.py

# Register in Claude Code
claude mcp add study-notes -- "$(pwd)/.venv/bin/python" "$(pwd)/labs/04-tools-mcp/01_mcp_server.py"
claude mcp list
```

Then in Claude Code: "Use study-notes to add a note: caching is a prefix match."

## Exam angles

- "Model keeps picking the wrong tool" → rewrite tool descriptions, remove overlap.
- "Same integration needed in Claude Code, Desktop and our app" → MCP server.
- "Expose read-only docs for the app to attach" → MCP resource.
- "Local server vs remote team server" → stdio vs Streamable HTTP.
- "100+ tools slow and confuse the agent" → tool search with deferred loading.

## Check yourself

1. Name the three MCP primitives and who controls each.
2. Which transport for a server running on a remote host?
3. Does `strict: true` make a tool safe to run without input checks?
