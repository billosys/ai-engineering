---
concept: Promise-Based Functions Start Synchronously
slug: promise-sync-start-async-settle
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.4 Promise-based functions start synchronously, settle asynchronously"
extraction_confidence: high
aliases:
  - sync start async settle
prerequisites:
  - promise
  - event-loop
extends: []
related:
  - async-function-start-sync-settle-async
  - promise-concurrency
contrasts_with: []
answers_questions:
  - "What concepts are prerequisite to understanding Promises?"
---

# Quick Definition

Promise-based functions start executing synchronously in the current task but their Promises are always settled asynchronously in a later task, ensuring predictable behavior and avoiding race conditions.

# Core Definition

"Exploring JavaScript" Ch. 43: "Their execution starts right away, synchronously (in the current task). But the Promise they return is guaranteed to be settled asynchronously (in a later task) -- if ever." Benefits: "Starting synchronously helps avoid race conditions... Chaining Promises won't starve other tasks... Promise-based functions always return results asynchronously; we can be sure that there is never a synchronous return."

# Prerequisites

- **Promise** -- this describes Promise execution behavior
- **Event loop** -- asynchronous settlement occurs in later event loop iterations

# Key Properties

1. `new Promise()` executor callback runs synchronously
2. Promise settlement notification always arrives asynchronously
3. Avoids race conditions (predictable start order)
4. Prevents task starvation (breaks between settlements)
5. Predictable: results are always async, never sync

# Construction / Recognition

```js
console.log('START');
asyncFunc().then(() => console.log('.then()'));
console.log('END');
// Output: START, asyncFunc, new Promise(), END, .then()
```

(Ch. 43, Section 43.4, lines 1216-1242)

# Context & Application

This guarantee is fundamental to the predictability of Promise-based code and explains execution ordering.

# Examples

See construction example above. (Ch. 43, Section 43.4, lines 1216-1242)

# Relationships

## Builds Upon
- **Promise** -- fundamental behavioral property
- **Event loop** -- settlement occurs in later iterations

## Related
- **Async function start sync settle async** -- same property for async functions

# Common Errors

- **Error**: Expecting `.then()` callback to run before code after the function call
  **Correction**: `.then()` callbacks always run after the current task completes

# Common Confusions

- **Confusion**: The entire Promise-based function runs asynchronously
  **Clarification**: The function body (including `new Promise()` executor) runs synchronously; only settlement is async

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.4, lines 1205-1274.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with benefits listed
- Cross-reference status: verified against Ch. 44.5
