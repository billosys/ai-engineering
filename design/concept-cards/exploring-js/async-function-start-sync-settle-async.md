---
concept: Async Functions Start Synchronously, Settle Asynchronously
slug: async-function-start-sync-settle-async
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.5 Async functions start synchronously, settle asynchronously"
extraction_confidence: high
aliases:
  - async function execution model
prerequisites:
  - async-function
  - promise
extends: []
related:
  - promise-concurrency
  - async-function-return-semantics
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
  - "What distinguishes synchronous from asynchronous code execution?"
---

# Quick Definition

Async functions begin executing synchronously until the first `await` or `return`/`throw`, then pause and return a Promise. The Promise is always settled asynchronously, never in the same task.

# Core Definition

"Exploring JavaScript" Ch. 44 describes the execution model: "The Promise resultPromise for the result is created when the async function is started. Then the body is executed." A permanent exit (return/throw) settles resultPromise; a temporary exit (await) pauses the function. "Promise resultPromise is returned after the first (permanent or temporary) exit." Settlement notification is always asynchronous.

# Prerequisites

- **Async function** -- this is the execution model of async functions
- **Promise** -- result is always a Promise

# Key Properties

1. Execution starts synchronously (current task)
2. At first `await`: function pauses, returns resultPromise
3. At `return`: resolves resultPromise, execution leaves permanently
4. At `throw`: rejects resultPromise, execution leaves permanently
5. Settlement notification always happens asynchronously (next microtask)
6. Starting synchronously helps avoid race conditions

# Construction / Recognition

```js
async function asyncFunc() {
  console.log('asyncFunc() starts'); // synchronous
  return 'abc';
}
asyncFunc().then(x => console.log(`Resolved: ${x}`)); // async
console.log('Task ends'); // synchronous
// Output: asyncFunc() starts, Task ends, Resolved: abc
```

(Ch. 44, Section 44.5, lines 617-634)

# Context & Application

Understanding this execution model is essential for predicting the order of operations and avoiding race conditions.

# Examples

See construction example above. (Ch. 44, Section 44.5, lines 617-634)

# Relationships

## Builds Upon
- **Async function** -- this is its execution model
- **Promise** -- settlement is always asynchronous

## Related
- **Promise concurrency** -- starting synchronously enables concurrent patterns

# Common Errors

- **Error**: Assuming async functions execute entirely asynchronously
  **Correction**: Code before the first `await` runs synchronously in the current task

# Common Confusions

- **Confusion**: The result Promise is available only after the function completes
  **Clarification**: The Promise is returned immediately at the first pause point or exit

# Source Reference

Chapter 44: Async functions, Section 44.5, lines 588-634.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit detailed section with execution steps
- Cross-reference status: verified against Ch. 43.4
