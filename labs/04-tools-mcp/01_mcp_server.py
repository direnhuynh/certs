"""Day 9: A small MCP server (stdio transport) that stores study notes.

Shows all three MCP primitives: a tool, a resource and a prompt.
"""

from pathlib import Path

from mcp.server.fastmcp import FastMCP

NOTES_FILE = Path(__file__).resolve().parents[2] / "notes" / "mcp-notes.md"

mcp = FastMCP("study-notes")


@mcp.tool()
def add_note(topic: str, note: str) -> str:
    """Save a short study note under a topic, for example topic='caching'."""
    NOTES_FILE.parent.mkdir(exist_ok=True)
    with NOTES_FILE.open("a") as f:
        f.write(f"- **{topic}**: {note}\n")
    return f"Saved note under {topic}."


@mcp.resource("notes://all")
def all_notes() -> str:
    """All saved study notes as Markdown."""
    return NOTES_FILE.read_text() if NOTES_FILE.exists() else "No notes yet."


@mcp.prompt()
def quiz_me(topic: str) -> str:
    """Ask Claude to quiz you on a CCDV-F topic."""
    return (
        f"Give me 3 CCDV-F style scenario questions about {topic}. "
        "Four options each. Wait for my answers before you explain."
    )


if __name__ == "__main__":
    mcp.run()  # stdio transport by default
