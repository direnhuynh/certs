# Lesson 1.5 — Structured Output

**Script:** `05_structured_output.py` · **Domain:** Applications and Integration · **Cost:** about $0.02 per run

## Goal

Get machine-readable output that is **guaranteed** to match a schema, and know the alternatives.

## Options, weakest to strongest

| Approach | Guarantee | When |
|---|---|---|
| "Answer in JSON" in the prompt | None — usually works, sometimes breaks | Quick prototypes |
| Examples of the JSON in the prompt | Better consistency, still no guarantee | Format steering |
| Assistant prefill `{` | Old technique; **rejected on newest models** | Legacy material only |
| **Structured output** (`output_config.format`) | Response is valid JSON matching your schema | Any code that parses the output |
| **Strict tool use** (`strict: true` on a tool) | Tool `input` matches the tool's schema | Agents and tool calls |

## Structured output

```python
# Python SDK + Pydantic: schema built and result validated for you
response = client.messages.parse(model=..., max_tokens=..., messages=..., output_format=Lead)
lead = response.parsed_output          # a Lead instance

# Raw JSON schema on the API
client.messages.create(..., output_config={"format": {"type": "json_schema", "schema": {...}}})
# → first text block is valid JSON
```

Schema rules:
- Objects need `additionalProperties: false` and a `required` list.
- Use `enum` for fixed choices (for example `"low" | "medium" | "high"`).
- Keep schemas simple; very complex schemas can be rejected.

Note: the older `output_format` **request field** on `messages.create()` is deprecated. The current field is `output_config.format`. (`output_format=` on the Python `parse()` helper is the SDK helper's own argument.)

## Strict tool use

```python
{"name": "book_flight", "strict": True, "input_schema": {..., "additionalProperties": False}}
```

Guarantees the tool arguments are schema-valid. Use it in agents where your code executes the tool.

## Limits to remember

- Structured output is **not compatible with citations** (400 error).
- A schema guarantees **shape**, not **truth**. The model can still put a wrong value in a valid field. Validate business rules in code.
- If `stop_reason` is `max_tokens`, the JSON may be incomplete. Check `stop_reason` first.

## What the script does

1. `messages.parse()` with a Pydantic `Lead` model extracts name, email, plan, seats, interests and demo flag from an email.
2. `messages.create()` with a raw JSON schema returns `{"urgency": ..., "summary": ...}`, which the script loads with `json.loads`.

## Exam angles

- "Downstream parser fails 2% of the time on malformed JSON" → structured output.
- "Agent passes wrong-type arguments to a function" → `strict: true` on the tool.
- "Need cited answers **and** a JSON schema" → incompatible in one call; choose one or use two calls.

## Check yourself

1. Which field holds the schema in the raw API?
2. Does a valid schema guarantee correct facts?
3. Which schema keyword stops extra keys?
