"""Day 3: Structured output — guaranteed-valid JSON."""

import json
import sys
from pathlib import Path

from pydantic import BaseModel

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client, text_of

email = (
    "Hi team, this is Jane Doe (jane@acme.io). We want the Enterprise plan for 40 seats. "
    "We care about SSO and audit logs. Can someone book a demo next week?"
)


# 1. Pydantic + messages.parse(): the SDK builds the schema and validates the result.
class Lead(BaseModel):
    name: str
    email: str
    plan: str
    seats: int
    interests: list[str]
    demo_requested: bool


response = client.messages.parse(
    model=MODEL,
    max_tokens=1024,
    messages=[{"role": "user", "content": f"Extract the sales lead:\n\n{email}"}],
    output_format=Lead,
)
lead = response.parsed_output
print("--- 1. parsed ---")
print(lead)

# 2. Raw JSON schema through output_config.format.
schema = {
    "type": "object",
    "properties": {
        "urgency": {"type": "string", "enum": ["low", "medium", "high"]},
        "summary": {"type": "string"},
    },
    "required": ["urgency", "summary"],
    "additionalProperties": False,
}
response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    messages=[{"role": "user", "content": f"Triage this email:\n\n{email}"}],
    output_config={"format": {"type": "json_schema", "schema": schema}},
)
print("\n--- 2. raw schema ---")
print(json.loads(text_of(response)))

# EXERCISE 1: Add a field `company: str` to Lead. Run again.
# EXERCISE 2: Compare: structured output versus "please answer in JSON" in the prompt.
#             Which one guarantees valid JSON? Which one is the exam's answer for "parser keeps failing"?
