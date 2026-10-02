"""Day 10: Weak prompt versus engineered prompt on the same task."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from common.client import MODEL, client, text_of

TICKET = """Hi, I upgraded to Pro yesterday but the export button is still greyed out.
I tried logging out and in. Also, can I get an invoice with my company VAT number? — Minh, Acme Ltd"""

weak = f"Help with this ticket: {TICKET}"

engineered = f"""<ticket>
{TICKET}
</ticket>

<instructions>
You triage support tickets for a SaaS product. A support agent reads your output, so be brief.
1. List every separate request in the ticket. Customers often bundle several requests in one ticket, and a missed request causes a second ticket.
2. For each request, give a category (billing, technical, account) and a next action.
3. If information is missing to act, say exactly what to ask the customer. Do not guess.
</instructions>

<example>
Ticket: "Password reset mail never arrives and please change my plan to yearly."
- Request: password reset email not received | technical | Check email bounce logs for the address.
- Request: switch to yearly plan | billing | Change the plan and prorate.
</example>

Answer in the same format as the example."""

for label, prompt in (("WEAK", weak), ("ENGINEERED", engineered)):
    response = client.messages.create(model=MODEL, max_tokens=1024, messages=[{"role": "user", "content": prompt}])
    print(f"===== {label} ({response.usage.output_tokens} output tokens)\n{text_of(response)}\n")

# EXERCISE 1: Remove the <example> block. How does the format change?
# EXERCISE 2: Remove the "because" reason in step 1. Does it still catch both requests?
# EXERCISE 3: Move the <ticket> block below the instructions. For long documents, which order is better?
