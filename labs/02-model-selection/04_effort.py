"""Day 6: Effort and adaptive thinking — trade quality for tokens and latency."""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client, text_of

puzzle = (
    "Three boxes are labeled apples, oranges, and mixed. Every label is wrong. "
    "You may take one fruit from one box. Which box do you pick from, and how do you fix all labels?"
)

for effort in ("low", "medium", "high"):
    start = time.perf_counter()
    response = client.messages.create(
        model=MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive", "display": "summarized"},  # Claude decides how much to think
        output_config={"effort": effort},
        messages=[{"role": "user", "content": puzzle}],
    )
    seconds = time.perf_counter() - start
    thinking = "".join(b.thinking for b in response.content if b.type == "thinking")
    print(f"=== effort={effort}  {seconds:.1f}s  output_tokens={response.usage.output_tokens}")
    print("thinking summary chars:", len(thinking))
    print(text_of(response).strip()[:300], "\n")

# Facts:
# - Current models use thinking={"type": "adaptive"}. The older {"type": "enabled", "budget_tokens": N}
#   form is removed on the newest models. Older exam material may still mention budget_tokens.
# - Thinking tokens are billed as output tokens.
# - On claude-opus-5-5, thinking cannot be disabled and the default effort is "medium".
# EXERCISE: Which effort would you pick for a high-volume chat route? For an agentic coding task?
