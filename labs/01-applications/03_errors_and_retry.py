"""Day 2: Error handling — typed exceptions, retryable versus non-retryable errors."""

import random
import sys
import time
from pathlib import Path

import anthropic

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client, text_of


def call_with_retry(max_attempts: int = 5, base_delay: float = 1.0, **kwargs):
    """Manual exponential backoff with jitter. The SDK already does this (max_retries=2);
    this version exists so you can see the logic the exam tests."""
    for attempt in range(max_attempts):
        try:
            return client.with_options(max_retries=0).messages.create(**kwargs)
        except anthropic.RateLimitError as e:  # 429
            delay = float(e.response.headers.get("retry-after", base_delay * 2**attempt))
        except anthropic.APIStatusError as e:
            if e.status_code < 500:  # 400/401/403/404/413: retry never helps
                raise
            delay = base_delay * 2**attempt  # 500, 529 overloaded
        except anthropic.APIConnectionError:
            delay = base_delay * 2**attempt
        delay += random.uniform(0, 1)
        print(f"attempt {attempt + 1} failed, sleeping {delay:.1f}s")
        time.sleep(delay)
    raise RuntimeError("all retries failed")


# 1. A good request through the retry wrapper.
response = call_with_retry(
    model=MODEL, max_tokens=1024, messages=[{"role": "user", "content": "Say OK."}]
)
print("--- 1. success ---", text_of(response), "| request id:", response._request_id)

# 2. Non-retryable errors: catch the most specific class first.
bad_requests = {
    "unknown model (404)": dict(model="claude-does-not-exist", max_tokens=64, messages=[{"role": "user", "content": "hi"}]),
    "empty messages (400)": dict(model=MODEL, max_tokens=64, messages=[]),
}
for label, kwargs in bad_requests.items():
    try:
        client.messages.create(**kwargs)
    except anthropic.NotFoundError as e:
        print(f"--- {label}: NotFoundError status={e.status_code}")
    except anthropic.BadRequestError as e:
        print(f"--- {label}: BadRequestError status={e.status_code} msg={e.message[:80]}")

# EXERCISE 1: Use a wrong API key: anthropic.Anthropic(api_key="bad"). Which class and status code?
# EXERCISE 2: Why log response._request_id in production? (Support tickets and tracing.)
# EXERCISE 3: Name the status code for "overloaded". (529) Is it retryable? (Yes.)
