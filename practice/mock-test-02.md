# CCDV-F Mock Test 2

- 53 questions · 120 minutes · one correct answer per question
- Domain mix follows the exam blueprint weights
- Write your letter after **Answer:**, for example `**Answer:** B`
- When done, ask Claude: "review practice/mock-test-02.md"
- Pass target: 39/53 (≈73%). Ready-for-exam target: 43/53 (≈80%).

Start time: ______  End time: ______

---

### Q1

A finance app must extract line items from photos of paper receipts. What is the simplest approach?

- **A.** Run external OCR first, because Claude cannot read images
- **B.** Convert the photo to a PDF first, because images are not accepted
- **C.** Upload the photo and refer to it only by its filename in text
- **D.** Send the photo as an image block, with instructions on what to extract

**Answer:** 

### Q2

What does the official Python SDK do by default when a request fails with 429, 5xx or a connection error?

- **A.** It retries every 4xx error, including 400
- **B.** It never retries, so you must write a retry loop
- **C.** It retries automatically with exponential backoff (2 retries by default)
- **D.** It retries forever until the request succeeds

**Answer:** 

### Q3

A database tool returns 5,000 rows on every call and fills the context. What is the best fix?

- **A.** Call the tool less often by raising the temperature
- **B.** Move the rows into the system prompt
- **C.** Raise `max_tokens`
- **D.** Make the tool return concise, filtered results, with pagination or limits

**Answer:** 

### Q4

On multi-step math word problems, accuracy is low even with a good prompt. Which change is most likely to help?

- **A.** Lower `max_tokens` so answers stay focused
- **B.** Add stop sequences after each step
- **C.** Switch to a smaller, faster model
- **D.** Turn on extended (adaptive) thinking, or raise the effort

**Answer:** 

### Q5

A service asks for 20,000-token reports with a non-streaming SDK call. Some requests fail with timeouts before the report is finished. What is the best fix?

- **A.** Set the temperature to 0 so the model writes faster
- **B.** Stream the request and collect the result with the SDK's final-message helper
- **C.** Split the report into 10 calls of 2,000 tokens and join the results
- **D.** Raise the SDK `max_retries` to 10 so timeouts are retried

**Answer:** 

### Q6

You want plain prose paragraphs without markdown. Which instruction tends to work best?

- **A.** "Do NOT use markdown!!!"
- **B.** "No bullets. No headers. No lists. No bold."
- **C.** "Avoid formatting if possible."
- **D.** "Write your response as flowing prose paragraphs."

**Answer:** 

### Q7

How does your code know that a Message Batch has finished processing?

- **A.** `request_counts.processing` is greater than 0
- **B.** Each request shows a `completed` status in `results()`
- **C.** The batch object returns HTTP 204
- **D.** `processing_status` is `"ended"`

**Answer:** 

### Q8

An FAQ bot gives good answers at `high` effort, but it is slow and expensive. What should you try?

- **A.** Lower the effort (or use a smaller model) and confirm with an eval that quality holds
- **B.** Turn on more thinking
- **C.** Raise `max_tokens`
- **D.** Raise the effort to `max`

**Answer:** 

### Q9

Which example shows the parallelization pattern with voting?

- **A.** Write a draft, critique it, then revise it
- **B.** Run the same "is this code vulnerable?" check three times and take the majority answer
- **C.** Classify a ticket, then send it to the matching prompt
- **D.** Extract data, then validate it, then store it

**Answer:** 

### Q10

Requests switch between two different tool lists in random order, and the cache hit rate is poor. What is the fix?

- **A.** Lower `max_tokens`
- **B.** Add cache breakpoints after every tool
- **C.** Keep one stable tool list with the same order and content on every request
- **D.** Use the 1-hour TTL

**Answer:** 

### Q11

How do you send a PDF to Claude for analysis?

- **A.** As a `tool_result` block with the file path
- **B.** As one `image` block per page; PDFs are not accepted directly
- **C.** As a raw byte string inside the system prompt
- **D.** As a `document` content block (base64, URL or Files API `file_id`)

**Answer:** 

### Q12

You want typed, validated Python objects (for example `Invoice(total: float, items: list[Item])`) extracted from text. What is the most robust approach?

- **A.** Ask for JSON and fix errors with a second call
- **B.** Use regular expressions on the free-text answer
- **C.** `client.messages.parse()` with a Pydantic model (structured output)
- **D.** Ask for YAML and parse it with a YAML library

**Answer:** 

### Q13

A team wants every developer's Claude Code sessions to follow the same project conventions. Where should the conventions go?

- **A.** In a project `CLAUDE.md` committed to the repository
- **B.** In each developer's `~/.claude/CLAUDE.md`
- **C.** In a message posted to the team chat
- **D.** In an environment variable

**Answer:** 

### Q14

A team wants cited answers from documents and also wants the final answer in a strict JSON schema, in the same request. What happens?

- **A.** It works only on Haiku
- **B.** It works if every tool sets `strict: true`
- **C.** The two features are incompatible in one request. Choose one, or split the work into two calls
- **D.** It works after adding a beta header

**Answer:** 

### Q15

A manager wants to move the real-time customer chat to the Batches API to save 50%. What is the correct response?

- **A.** Use Batches with one request per batch to keep latency low
- **B.** Batches have no latency guarantee, so they do not fit real-time chat. Use caching or a smaller model instead
- **C.** Use Batches with streaming turned on
- **D.** Use Batches and poll the batch every 100 ms

**Answer:** 

### Q16

How does the Anthropic web search tool work?

- **A.** It requires an MCP server
- **B.** It is available only inside Claude Code
- **C.** Your code must implement the search and return a `tool_result`
- **D.** It runs on Anthropic's servers and returns results in the same response

**Answer:** 

### Q17

A 300-token system prompt has `cache_control`, but `cache_creation_input_tokens` is always 0. Why?

- **A.** Caching needs a separate beta header on every model
- **B.** Caching works only inside the Batches API
- **C.** The TTL expired before the request
- **D.** The prefix is shorter than the model's minimum cacheable length

**Answer:** 

### Q18

What does a tool schema need when `strict: true` is set?

- **A.** No description
- **B.** At least 10 parameters
- **C.** Only string-typed parameters
- **D.** `additionalProperties: false` and a `required` list

**Answer:** 

### Q19

You changed a production prompt. How do you make sure quality did not regress?

- **A.** Read three outputs and check that they look fine
- **B.** Ask the model whether the new prompt is better
- **C.** Ship it and monitor complaints
- **D.** Run the automated eval set before and after the change, and compare the scores

**Answer:** 

### Q20

You need a coding agent with built-in file reading, editing and bash tools, running on your own servers. Which option fits best?

- **A.** The Claude Agent SDK
- **B.** The Message Batches API
- **C.** The SDK Tool Runner with no tools
- **D.** The Files API

**Answer:** 

### Q21

`max_tokens` is set to 4,000, and the answer is 300 tokens long. How many output tokens are you billed for?

- **A.** About 300, the tokens actually generated
- **B.** 4,000, the reserved amount
- **C.** 2,000, half of the reservation
- **D.** 4,300, the reservation plus the generated tokens

**Answer:** 

### Q22

An assistant must remember user preferences across separate sessions. What is the right approach?

- **A.** Rely on the API to remember earlier sessions
- **B.** A memory tool or external storage that the agent reads and writes
- **C.** Use a bigger context window
- **D.** Put the preferences in an assistant prefill

**Answer:** 

### Q23

How does a `tool_result` block identify which tool call it answers?

- **A.** By its position in the content list
- **B.** By `tool_use_id`, which must equal the `id` of the matching `tool_use` block
- **C.** By the message ID of the response
- **D.** By the tool's `name`

**Answer:** 

### Q24

How do Claude's input and output token prices compare?

- **A.** Output tokens are free when streaming
- **B.** Input tokens cost more than output tokens
- **C.** Input and output cost the same
- **D.** Output tokens cost more per token (about 5× the input price)

**Answer:** 

### Q25

What is the maximum number of cache breakpoints in one request?

- **A.** There is no limit
- **B.** 1
- **C.** 10
- **D.** 4

**Answer:** 

### Q26

In MCP, which party decides when a tool is called?

- **A.** The model
- **B.** The MCP server's administrator
- **C.** The end user, by clicking a button
- **D.** The application, which attaches it automatically

**Answer:** 

### Q27

Which set of few-shot examples works best?

- **A.** No examples, only a detailed description of the format
- **B.** One example repeated three times
- **C.** 50 nearly identical examples
- **D.** 3–5 varied examples that cover typical and edge cases

**Answer:** 

### Q28

Which statement about system prompts is correct?

- **A.** System prompts are not sent to the model
- **B.** System prompts are encrypted and cannot be revealed
- **C.** Never place secrets in the system prompt; assume users can extract it
- **D.** Secrets are safe in the system prompt if marked confidential

**Answer:** 

### Q29

What does `tool_choice: {"type": "none"}` do?

- **A.** It removes the tool definitions from billing
- **B.** It lets the model call tools without schemas
- **C.** It forces the model to call at least one tool
- **D.** It prevents the model from calling any tool in that request

**Answer:** 

### Q30

A chat product resends the full history every turn, so input cost grows with each message. Which optimization fits best?

- **A.** Send every turn through the Batches API
- **B.** Lower `max_tokens` on each turn
- **C.** Prompt caching, with a breakpoint at the end of the latest conversation turn
- **D.** Remove the system prompt to save tokens

**Answer:** 

### Q31

Traffic mixes many easy questions with a few hard ones. What is a cost-effective design?

- **A.** Use a cheap model to classify difficulty, then route the hard questions to a stronger model
- **B.** Send everything to Haiku
- **C.** Split traffic between the models at random
- **D.** Send everything to Opus

**Answer:** 

### Q32

Which statement about MCP architecture is correct?

- **A.** MCP replaces the Messages API
- **B.** A host application runs MCP clients, and each client connects to one MCP server
- **C.** One MCP server must run inside each model
- **D.** MCP servers call the Claude API directly to run tools

**Answer:** 

### Q33

A response returns `stop_reason: "tool_use"`. What does this mean for your code?

- **A.** The conversation has ended and must start again
- **B.** The tool already ran on Anthropic's servers and its result is in the response
- **C.** The tool definition has a schema error that must be fixed
- **D.** Claude is asking for a client tool call. Run the tool and send back a `tool_result`

**Answer:** 

### Q34

You want to screen user inputs for jailbreak attempts before they reach the main model, cheaply. What fits best?

- **A.** A regex blocklist only
- **B.** The largest model at maximum effort for screening
- **C.** A longer main system prompt
- **D.** A fast, small model (such as Haiku) that classifies each input against your policy

**Answer:** 

### Q35

A request uses `stop_sequences: ["</answer>", "</error>"]`. The response has `stop_reason: "stop_sequence"`. How do you find out which sequence matched?

- **A.** Read the `message_start` event
- **B.** Read `usage.stop_reason_detail`
- **C.** Read the `stop_sequence` field of the response
- **D.** Read the `type` of the last content block

**Answer:** 

### Q36

An agent can execute code that the model writes. Which control is most important?

- **A.** Ask the model to only write safe code
- **B.** Run the code as root for reliability
- **C.** Turn off logging to protect privacy
- **D.** Run the code in a sandbox with restricted network and filesystem access

**Answer:** 

### Q37

Does streaming a response reduce its cost?

- **A.** No. You are billed for the same tokens; streaming only shortens the time to the first token
- **B.** Yes. Streaming lowers the input token count
- **C.** Yes. Streamed output tokens cost 50% less
- **D.** Yes. Streaming removes the output token charge

**Answer:** 

### Q38

An assistant turn contains `text` and `tool_use` blocks. When you continue the conversation, what do you append as the assistant message?

- **A.** Only the `tool_use` blocks
- **B.** Only the text blocks, joined into one string
- **C.** The full `response.content` list, unchanged
- **D.** Nothing, because the server stores the assistant turn

**Answer:** 

### Q39

An agent can issue refunds. The business requires human sign-off for every refund. What is the best design?

- **A.** Tell the model in the prompt to be careful with refunds
- **B.** Gate the refund tool in code: ask for human approval first, and return "declined" if it is not approved
- **C.** Set the temperature to 0 for refund requests
- **D.** Remove the system prompt from refund conversations

**Answer:** 

### Q40

When should you choose an autonomous agent over a fixed workflow?

- **A.** When the steps cannot be predicted and the model must decide them as it goes
- **B.** When you need the lowest possible latency
- **C.** When cost is the only concern
- **D.** When the steps are fixed and known in advance

**Answer:** 

### Q41

Several results in a batch have the type `expired`. What does this mean?

- **A.** The results were deleted after the retention period
- **B.** The requests were not processed within the 24-hour limit and should be resubmitted
- **C.** The batch was canceled by a user
- **D.** The requests were invalid and must be fixed

**Answer:** 

### Q42

A knowledge base has 10,000 documents. How should you give the relevant knowledge to Claude for each question?

- **A.** List the document titles in the system prompt
- **B.** Retrieve only the relevant chunks (RAG) and include those
- **C.** Include all 10,000 documents in every request
- **D.** Ask Claude to recall the documents from training data

**Answer:** 

### Q43

For question answering over a long document, which technique improves accuracy?

- **A.** Remove all XML tags from the document
- **B.** Ask the model to first extract the relevant quotes in `<quotes>` tags, then answer from those quotes
- **C.** Repeat the question at the start and the end
- **D.** Ask for the answer first, then the quotes

**Answer:** 

### Q44

Answers for an internal engineering audience are too generic. What should you add to the prompt?

- **A.** A shorter prompt
- **B.** Context: who the audience is, the purpose of the output and what success looks like
- **C.** A higher temperature
- **D.** A switch to Haiku

**Answer:** 

### Q45

What is indirect prompt injection?

- **A.** Malicious instructions hidden in content the model processes, such as documents, web pages or tool outputs
- **B.** An attacker stealing your API key
- **C.** Too many tokens in a prompt
- **D.** A user typing "ignore your instructions" in the chat

**Answer:** 

### Q46

A team does not want to host the agent loop or a tool sandbox, and needs long-running sessions. Which option fits best?

- **A.** The Message Batches API
- **B.** Managed Agents
- **C.** The Claude Agent SDK on a laptop
- **D.** A manual agent loop on the Messages API

**Answer:** 

### Q47

Where should persona and rules go when they must apply to every turn of a conversation?

- **A.** In the top-level `system` parameter
- **B.** In the first assistant message
- **C.** In the `metadata` field
- **D.** In `stop_sequences`

**Answer:** 

### Q48

A new deployment fails on every call with HTTP 401. What should you do?

- **A.** Check the API key configuration. A retry will not help
- **B.** Switch to streaming requests
- **C.** Ask for a higher rate limit tier
- **D.** Retry with exponential backoff

**Answer:** 

### Q49

A request with `model: "claude-opus-latest-v2"` returns HTTP 404 `not_found_error`. What is the most likely cause?

- **A.** The region does not support streaming
- **B.** `max_tokens` is too high for this model
- **C.** The model ID is not valid. Use an exact model ID from the docs or the Models API
- **D.** The service has a short outage, so retry later

**Answer:** 

### Q50

Which set of dimensions do Claude API rate limits use?

- **A.** Requests per minute, input tokens per minute and output tokens per minute
- **B.** Only monthly spend in dollars
- **C.** Only the number of concurrent connections
- **D.** Only total requests per day

**Answer:** 

### Q51

You need to analyze a 600,000-token document with Haiku 4.5. What happens, and what should you do?

- **A.** It does not fit Haiku's 200K window. Chunk the document or use a model with a 1M-token window
- **B.** Use the Batches API to get around the limit
- **C.** Haiku silently truncates the input, so it is fine
- **D.** Use streaming to get around the limit

**Answer:** 

### Q52

One large prompt that must research, outline, draft and edit gives poor results. What should you do?

- **A.** Raise `max_tokens`
- **B.** Repeat the instructions three times
- **C.** Write all the instructions in capital letters
- **D.** Split the work into a chain of prompts, one per stage

**Answer:** 

### Q53

A long agent conversation is close to the context limit, and its answers are getting worse. What helps?

- **A.** Send the history twice
- **B.** Raise `max_tokens`
- **C.** Raise the temperature
- **D.** Compaction or context editing, to summarize history or clear old tool results

**Answer:** 
