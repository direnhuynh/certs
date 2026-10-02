# Lesson 5.1 — Prompt and Context Engineering

**Script:** `01_prompt_techniques.py` · **Domain:** Prompt and Context Engineering · **Cost:** about $0.02 per run

## Goal

Write prompts that give consistent, correct output, and manage context as a limited budget.

## Core techniques

### 1. Clear and direct

Treat the model like a skilled new colleague with **no context**. Say:
- The task and its purpose (who reads the output, why).
- The exact output format.
- What success looks like.
- **Why** a rule exists. The model generalises from reasons ("Customers bundle requests, and a missed one causes a second ticket").

### 2. Examples (few-shot)

- 3–5 examples, varied, covering edge cases.
- Wrap in `<example>` tags.
- Examples steer format strongly — make sure they show exactly what you want.

### 3. XML tags for structure

```text
<document> ... </document>
<instructions> ... </instructions>
<example> ... </example>
```

- Separates data from instructions. Reduces confusion and injection risk.
- Refer to tags by name ("Using the document in <document> tags ...").
- No special tag names are required; be consistent.

### 4. Role (system prompt)

"You are a senior security auditor" sets domain, vocabulary and tone. Put the role and stable rules in `system`.

### 5. Let it think

Hard reasoning → enable adaptive thinking or raise effort (Lesson 2.4). Without thinking, ask for reasoning in `<thinking>` tags then the answer in `<answer>` tags.

### 6. Chain prompts

Split a complex job into steps with separate calls (extract → analyse → write). Each step is simpler, testable and debuggable.

### 7. Control format

- Machine-read output → structured output (Lesson 1.5).
- Tell the model what to do, not only what not to do ("Write in flowing paragraphs" beats "Don't use bullet points").
- Prefill is removed on newest models.

## Long context

- Put long documents **at the top**, the instructions and question **at the bottom**. Measurably better answers.
- Wrap each document with metadata:

```text
<documents>
  <document index="1"><source>contract.pdf</source><document_content>...</document_content></document>
</documents>
```

- Ask for relevant **quotes first**, then the answer from the quotes.

## Reduce hallucination

- Allow "I don't know" explicitly.
- Ground: "Answer only from the provided documents."
- Require quotes or use the citations feature.
- Lower the stakes of guessing: ask for a confidence level or to flag missing information.

## Context engineering

Context is a finite budget. More text ≠ better.
- Include only relevant information (retrieval / RAG instead of dumping everything).
- Keep stable content first for caching (Lesson 2.2).
- Clear stale tool results; summarise long histories (compaction).
- Use subagents to keep heavy reading out of the main context.

## What the script does

Same support ticket, two prompts:
- **WEAK**: "Help with this ticket: ..."
- **ENGINEERED**: ticket in `<ticket>` tags, numbered instructions with reasons, one `<example>`, explicit format.

Compare: does the weak prompt catch **both** requests (export button + VAT invoice)? Is its format predictable?

## Exam angles

- "Output format varies between calls" → examples + explicit format (or structured output).
- "Model mixes up instructions and document content" → XML tags.
- "Answers on a 200-page document miss details" → document at top, question at bottom, quote first.
- "Model invents policy details" → ground in documents, allow "I don't know", citations.

## Check yourself

1. Where should a long document go relative to the question?
2. Why explain the reason behind an instruction?
3. Name two techniques to reduce hallucination.
