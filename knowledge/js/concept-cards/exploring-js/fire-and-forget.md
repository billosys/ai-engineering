---
concept: Fire and Forget Pattern
slug: fire-and-forget
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.6.1 We don't need await if we 'fire and forget'"
extraction_confidence: high
aliases:
  - fire and forget await
prerequisites:
  - async-function
  - await-operator
extends: []
related:
  - await-concurrency
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
---

# Quick Definition

"Fire and forget" means calling an async function without `await` when you don't need the result, allowing the operation to run in the background while execution continues. Only `await` the final operation you need to wait for.

# Core Definition

"Exploring JavaScript" Ch. 44: "await is not required when working with a Promise-based function; we only need it if we want to pause and wait until the returned Promise is settled. If we only want to start an asynchronous operation, then we don't need it." Starting without `await` prevents race conditions because "each invocation of .write() starts synchronously."

# Prerequisites

- **Async function** -- pattern used in async functions
- **Await operator** -- understanding when to omit it

# Key Properties

1. Call async function without `await` to start it without waiting
2. Only `await` when you need the result or need to wait for completion
3. Starting synchronously prevents race conditions even without `await`
4. Useful for operations where order matters but waiting doesn't

# Construction / Recognition

```js
async function asyncFunc() {
  const writer = openFile('someFile.txt');
  writer.write('hello'); // don't wait
  writer.write('world'); // don't wait
  await writer.close();  // wait for file to close
}
```

(Ch. 44, Section 44.6.1, lines 646-651)

# Context & Application

Useful for logging, writing to streams, or sending notifications where you don't need to wait for each individual operation to complete.

# Examples

See construction example above. (Ch. 44, Section 44.6.1, lines 646-656)

# Relationships

## Builds Upon
- **Async function** -- used within async functions
- **Await operator** -- selectively omitted

## Related
- **Await concurrency** -- related concurrency pattern

# Common Errors

- **Error**: Never awaiting fire-and-forget operations, missing errors
  **Correction**: Consider adding error handlers even for fire-and-forget operations

# Common Confusions

- **Confusion**: Fire-and-forget means the operation might not complete
  **Clarification**: The operation still runs; you just don't wait for it in the current function

# Source Reference

Chapter 44: Async functions, Section 44.6.1, lines 637-656.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with example
- Cross-reference status: verified
