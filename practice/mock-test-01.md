# CCDV-F Mock Test 1

- 53 questions · 120 minutes · one correct answer per question
- Domain mix follows the exam blueprint weights
- Write your letter after **Answer:**, for example `**Answer:** B`
- When done, ask Claude: "review practice/mock-test-01.md"
- Pass target: 39/53 (≈73%). Ready-for-exam target: 43/53 (≈80%).

Start time: ______  End time: ______

---

### Q1

A route performs simple intent classification at 20 million requests per day, with a latency target under 500 ms. Which model choice fits best?

- **A.** Opus with maximum effort
- **B.** Sonnet with extended thinking at high effort
- **C.** Haiku
- **D.** Opus through the Batches API

**Answer:** 

### Q2

Where should you put a role such as "You are a senior tax accountant reviewing filings"?

- **A.** In an assistant prefill
- **B.** In a tool description
- **C.** In the last user message
- **D.** In the system prompt

**Answer:** 

### Q3

The same 30 MB PDF is used in many requests across different user sessions. The team wants to stop re-sending the base64 data every time. What should they use?

- **A.** Split the PDF into images
- **B.** The Message Batches API
- **C.** Upload the PDF once with the Files API and reference it by `file_id`
- **D.** Prompt caching alone

**Answer:** 

### Q4

An agent got stuck and ran 200 iterations, which cost a lot. Which safeguard matters most?

- **A.** Removing the system prompt
- **B.** More tools
- **C.** A hard cap on iterations and spend, with a clear stop condition
- **D.** A higher temperature

**Answer:** 

### Q5

Your app consumes a streaming response. Which event carries the final `stop_reason` and the output token count?

- **A.** `message_delta`
- **B.** `ping`
- **C.** `content_block_stop`
- **D.** `message_start`

**Answer:** 

### Q6

A request returns HTTP 429. How should the client decide how long to wait before retrying?

- **A.** Retry at once with a different API key
- **B.** Always wait exactly 1 second
- **C.** Use the `retry-after` response header
- **D.** Halve `max_tokens` and retry at once

**Answer:** 

### Q7

Which MCP primitive provides reusable templates that the user picks, often shown as slash commands?

- **A.** Tools
- **B.** Roots
- **C.** Resources
- **D.** Prompts

**Answer:** 

### Q8

A company wants one Jira integration that works in Claude Code, Claude Desktop and its own app. What should it build?

- **A.** A fine-tuned model
- **B.** A long system prompt describing Jira
- **C.** An MCP server
- **D.** A copy of the tool definitions in each app

**Answer:** 

### Q9

An agent has 150 tools. Requests are slow, input token counts are huge, and tool selection is poor. What helps most?

- **A.** Split the work into 150 single-tool agents
- **B.** Tool search, with most tools marked `defer_loading: true`
- **C.** Put every tool definition in the system prompt
- **D.** Set `strict: true` on every tool

**Answer:** 

### Q10

A request uses a server-side tool (web search). The response returns `stop_reason: "pause_turn"`. What should the client do?

- **A.** Treat the response as the final answer
- **B.** Raise `max_tokens` and resend the original request without the response
- **C.** Remove the server tool and retry
- **D.** Send the returned content back in a follow-up request so Claude can continue the turn

**Answer:** 

### Q11

A customer-facing chat app shows a blank screen for about 20 seconds, then the full answer appears at once. Users think the app is frozen. What is the best fix?

- **A.** Send the requests through the Message Batches API
- **B.** Increase `max_tokens` so the model finishes faster
- **C.** Stream the response so text appears as it is generated
- **D.** Retry the request whenever it takes longer than 5 seconds

**Answer:** 

### Q12

After adding a new request parameter, every call fails with HTTP 400 `invalid_request_error`. The client retries each call 5 times with backoff. What is the right assessment?

- **A.** Wait for the `retry-after` header, then retry
- **B.** Retrying is correct because 400 errors are temporary
- **C.** Move to another region and retry
- **D.** Do not retry. A 400 means the request itself is malformed and must be fixed

**Answer:** 

### Q13

A streaming request returns HTTP 200, then fails halfway through generation. What must the client handle?

- **A.** An HTTP 500 status on the same connection
- **B.** An `error` event inside the stream (for example `overloaded_error`)
- **C.** Nothing, because HTTP 200 guarantees the stream will complete
- **D.** A `retry-after` value inside `message_stop`

**Answer:** 

### Q14

An email-summarizer agent has a `send_email` tool. After reading a crafted email, it forwarded the mailbox to an attacker. Which control is most effective?

- **A.** Least privilege: remove the send capability, or require human approval before sending
- **B.** A larger model
- **C.** A stronger system prompt alone
- **D.** Temperature 0

**Answer:** 

### Q15

A team hosts a shared MCP server on a remote host. Which transport should clients use?

- **A.** Streamable HTTP
- **B.** Named pipes
- **C.** stdio
- **D.** WebRTC

**Answer:** 

### Q16

Prompt caching is enabled, but `cache_read_input_tokens` is always 0. The system prompt begins with `Current time: {now}`. What is the problem?

- **A.** The cache TTL is too short
- **B.** The timestamp changes the prefix on every request. Move it after the cache breakpoint
- **C.** This model does not support caching
- **D.** More breakpoints are needed

**Answer:** 

### Q17

A research agent's context fills with large raw search results, and its answer quality drops. What is the best fix?

- **A.** Put all the search results in the system prompt
- **B.** Run the main agent at a higher temperature
- **C.** Raise `max_tokens`
- **D.** Delegate the searches to subagents that return only short summaries

**Answer:** 

### Q18

A pipeline extracts fields from an invoice, validates them, then writes them to an ERP system. The steps never change. Which design fits best?

- **A.** Parallel voting
- **B.** Orchestrator-workers
- **C.** Prompt chaining (a workflow) with validation between the steps
- **D.** An autonomous agent with all three tools

**Answer:** 

### Q19

A web app lets users upload a screenshot of an error dialog and ask what went wrong. How should the app send the screenshot?

- **A.** As an `image` content block (base64 or URL) in the user message, together with the text question
- **B.** Run OCR first, because Claude cannot read images
- **C.** Return it in a `tool_result` block
- **D.** Attach it to the system prompt as raw bytes

**Answer:** 

### Q20

A user tells a chatbot their name in the first message. Two messages later, the bot says it does not know the user's name. The app sends only the newest user message in each request. What is the cause?

- **A.** The model's context window is full
- **B.** Prompt caching is disabled
- **C.** The system prompt is too long
- **D.** The Messages API is stateless, so the app must resend the conversation history in every request

**Answer:** 

### Q21

A marketing translation is generated, critiqued against style criteria, and revised until it meets the bar. Which pattern is this?

- **A.** Routing
- **B.** Sectioning
- **C.** Prompt chaining
- **D.** Evaluator-optimizer

**Answer:** 

### Q22

Which MCP primitive exposes read-only data that the application attaches as context?

- **A.** Prompts
- **B.** Tools
- **C.** Sampling
- **D.** Resources

**Answer:** 

### Q23

A downstream service parses Claude's output as JSON. About 2% of responses fail to parse. Which change most reliably removes these failures?

- **A.** Add "RESPOND ONLY IN VALID JSON" in capital letters
- **B.** Use structured output with a JSON schema (`output_config.format`)
- **C.** Add two JSON examples to the prompt
- **D.** Ask the model to double-check its JSON

**Answer:** 

### Q24

A task must change an unknown number of files. A lead model decides at run time which subtasks to create and delegates them. Which pattern is this?

- **A.** Routing
- **B.** Prompt chaining
- **C.** Orchestrator-workers
- **D.** Voting

**Answer:** 

### Q25

A developer processes Message Batches results by assuming result #1 belongs to input #1. Some labels end up on the wrong products. What is the fix?

- **A.** Sort the results by creation time
- **B.** Match each result to its input with `custom_id`
- **C.** Poll the batch status more often
- **D.** Submit only one request per batch

**Answer:** 

### Q26

Requests that share a long prompt arrive about every 15 minutes, and the cache keeps missing. What should you change?

- **A.** Move the shared prompt to the end
- **B.** Add more cache breakpoints
- **C.** Use the Batches API
- **D.** Use the 1-hour cache TTL

**Answer:** 

### Q27

Anthropic support asks for details about one failed production request. What should your logs contain to identify it?

- **A.** Only the model name
- **B.** Only the local timestamp
- **C.** The request ID (`request-id` header, `_request_id` in the Python SDK)
- **D.** The full API key

**Answer:** 

### Q28

Roughly how much does a cache read cost, compared with normal input tokens?

- **A.** Cache reads are free
- **B.** About 2×
- **C.** About 0.1×
- **D.** About 1.25×

**Answer:** 

### Q29

While summarizing a customer email, the model sometimes follows instructions written inside the email. Which prompt change helps most?

- **A.** Wrap the email in XML tags and state that the content inside them is data to summarize
- **B.** Use two system prompts
- **C.** Write the instructions in capital letters
- **D.** Make the prompt shorter

**Answer:** 

### Q30

A support system first classifies each ticket, then sends it to a specialized prompt for billing, technical or sales issues. Which pattern is this?

- **A.** Parallelization
- **B.** Routing
- **C.** Evaluator-optimizer
- **D.** Orchestrator-workers

**Answer:** 

### Q31

Every customer-support request includes the same 80-page product manual, followed by the customer's question. Input costs are high. What is the best optimization?

- **A.** Summarize the manual again on every request
- **B.** Switch to the smallest model without testing
- **C.** Prompt caching, with the manual in the cached prefix and the question after the breakpoint
- **D.** Send each request through the Batches API

**Answer:** 

### Q32

A text-to-speech app has the instruction "NEVER use ellipses", and the model still uses them sometimes. Which revision works best?

- **A.** Explain the reason: the speech engine cannot pronounce ellipses, so never use them
- **B.** Remove the rule and post-process the text
- **C.** Repeat the rule five times
- **D.** Move the rule to the end in capital letters

**Answer:** 

### Q33

In an agent, Claude sometimes passes the string "five" to a tool parameter that expects an integer, and the tool crashes. What prevents this most reliably?

- **A.** Set `tool_choice` to `none`
- **B.** Mention the type in the tool description
- **C.** Retry the call whenever validation fails
- **D.** Set `strict: true` on the tool definition, with a complete JSON schema

**Answer:** 

### Q34

A tool fails because the record does not exist. What is the best way to report this to Claude?

- **A.** Return a `tool_result` with `is_error: true` and a clear message
- **B.** Raise an exception and end the conversation
- **C.** Call the tool again until it works
- **D.** Leave that tool result out and continue

**Answer:** 

### Q35

A support bot invents details about company policy. Which combination best reduces this?

- **A.** Add general knowledge to the system prompt
- **B.** Add few-shot examples of confident answers
- **C.** Answer only from the provided documents, allow "I don't know", and quote the supporting text
- **D.** Raise the effort

**Answer:** 

### Q36

In one turn, Claude returns two `tool_use` blocks. How should your code return the results?

- **A.** Put the results in an assistant message
- **B.** Put both `tool_result` blocks in a single user message
- **C.** Send two separate user messages, one per result
- **D.** Return only the first result and drop the second

**Answer:** 

### Q37

A report generator sometimes returns answers that stop in the middle of a sentence. Which `stop_reason` will the response most likely show?

- **A.** `pause_turn`
- **B.** `stop_sequence`
- **C.** `max_tokens`
- **D.** `end_turn`

**Answer:** 

### Q38

A team needs a linter to run after every file edit Claude Code makes, with no exceptions. What should it use?

- **A.** A subagent
- **B.** An instruction in `CLAUDE.md`
- **C.** A `PostToolUse` hook
- **D.** A reminder in each prompt

**Answer:** 

### Q39

A response comes back with `stop_reason: "refusal"`. How should the application handle it?

- **A.** Retry the same input until it succeeds
- **B.** Handle it gracefully: show a safe message, and log the refusal category
- **C.** Ignore it and display the content
- **D.** Switch to raw HTTP calls

**Answer:** 

### Q40

Claude often calls `search_orders` when `get_order` was the right tool. What should you fix first?

- **A.** Set `tool_choice` to `none`
- **B.** Add more tools
- **C.** Raise `max_tokens`
- **D.** Rewrite the tool names and descriptions to say when to use each tool, and when not to

**Answer:** 

### Q41

How are extended thinking tokens billed?

- **A.** As output tokens
- **B.** They are free
- **C.** Only when the thinking is displayed
- **D.** As input tokens

**Answer:** 

### Q42

The output format changes from call to call: sometimes bullets, sometimes prose. Which change gives the most consistent format?

- **A.** Raise the temperature
- **B.** Switch to Haiku
- **C.** Add 3–5 examples of the exact format in `<example>` tags
- **D.** Raise `max_tokens`

**Answer:** 

### Q43

An agent that migrates code across several repositories keeps failing on a mid-tier model. What should you try first?

- **A.** The most capable model (Opus), with higher effort
- **B.** Haiku, to make more attempts per minute
- **C.** Lower `max_tokens`
- **D.** A shorter system prompt

**Answer:** 

### Q44

Answers on a route are good on Opus. You want to move it to Sonnet to save cost. What is the most reliable way to decide?

- **A.** Run the same eval set on both models and compare the scores
- **B.** Check a public benchmark leaderboard
- **C.** Switch now and wait for user complaints
- **D.** Ask Sonnet to rate its own answers

**Answer:** 

### Q45

A legal team needs answers about contracts with exact, verifiable references to the passages that support each claim. Which feature fits best?

- **A.** Put the contracts in the system prompt
- **B.** Raise the effort to `max`
- **C.** Enable citations on the document content blocks
- **D.** Use structured output with a `quote` field

**Answer:** 

### Q46

A team estimates Claude token counts with OpenAI's `tiktoken`, and its cost forecasts do not match the bills. What should they do?

- **A.** Use the `count_tokens` endpoint
- **B.** Multiply the tiktoken counts by 1.3
- **C.** Use `max_tokens` as the estimate
- **D.** Divide the character count by 4

**Answer:** 

### Q47

A user asks a question about a 150-page contract, and the answers miss details. Which prompt layout is best?

- **A.** Summarize the contract first and send only the summary
- **B.** Put the contract at the top in XML tags, and the question and instructions at the end
- **C.** Put the question first and the contract after it
- **D.** Put half of the contract in the system prompt and half in the user message

**Answer:** 

### Q48

During peak hours, a production app gets occasional HTTP 529 (overloaded) errors. What should the client do?

- **A.** Create a new API key for each request
- **B.** Switch every request to the Batches API
- **C.** Lower `max_tokens` to 256
- **D.** Retry with exponential backoff and jitter

**Answer:** 

### Q49

Which statement about `response.content` in the Messages API is correct?

- **A.** It always contains exactly one text block
- **B.** It is a list of typed blocks (for example `thinking`, `text`, `tool_use`). Check each block's `type` before reading it
- **C.** It contains only tool calls when tools are defined
- **D.** It is always a single string

**Answer:** 

### Q50

You need to grade 5,000 generated summaries for faithfulness to their source documents. Which approach fits best?

- **A.** An LLM judge with a specific rubric, spot-checked against human grades
- **B.** Exact string match against reference summaries
- **C.** A human reads all 5,000
- **D.** Word count limits

**Answer:** 

### Q51

A React single-page app calls the Claude API directly from the browser, with the API key in the JavaScript bundle. What should the team do?

- **A.** Obfuscate the key in the bundle
- **B.** Put the key in the system prompt
- **C.** Rotate the key every week but keep it in the bundle
- **D.** Move the API calls to a backend and keep the key in server-side secret storage

**Answer:** 

### Q52

Every night, a team must classify 400,000 product descriptions. Results are needed the next morning. The goal is the lowest cost. Which approach fits best?

- **A.** Submit the requests through the Message Batches API
- **B.** Stream all requests in parallel with 50 workers
- **C.** Send synchronous requests one at a time to avoid rate limits
- **D.** Use extended thinking at maximum effort

**Answer:** 

### Q53

Which statement about a web-browsing agent is correct?

- **A.** A strong system prompt alone prevents injection
- **B.** Web content is safe when it is served over HTTPS
- **C.** Prompt injection can only come from the user
- **D.** Content from fetched pages is untrusted and can contain prompt-injection instructions

**Answer:** 
