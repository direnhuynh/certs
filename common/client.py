"""Shared client and model constants for every lab."""

import anthropic
from dotenv import load_dotenv

load_dotenv()

# Model IDs. Use these exact strings; never add a date suffix.
OPUS = "claude-opus-5-5"      # Default. Hardest reasoning and agentic work. $4 / $20 per 1M tokens.
SONNET = "claude-sonnet-5-5"  # Balanced speed and capability. $2 / $10 per 1M tokens.
HAIKU = "claude-haiku-4-5"    # Fast, cheap, high volume. $1 / $5 per 1M tokens. 200K context.

MODEL = OPUS

# Reads ANTHROPIC_API_KEY from the environment (.env is loaded above).
client = anthropic.Anthropic()


def text_of(message) -> str:
    """Join every text block of a response. Responses can also hold thinking and tool_use blocks."""
    return "".join(block.text for block in message.content if block.type == "text")


def print_usage(message) -> None:
    u = message.usage
    print(
        f"[usage] input={u.input_tokens} output={u.output_tokens} "
        f"cache_write={u.cache_creation_input_tokens} cache_read={u.cache_read_input_tokens} "
        f"stop_reason={message.stop_reason}"
    )
