---
concept: Await Operator
slug: await-operator
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.1.1 The await operator makes Promises synchronous"
extraction_confidence: high
aliases:
  - await keyword
  - await expression
prerequisites:
  - async-function
  - promise
extends: []
related:
  - top-level-await
  - awaiting-is-shallow
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
---

# Quick Definition

The `await` operator pauses an async function until a Promise settles: it returns the fulfillment value if the Promise fulfills, or throws the rejection value if the Promise rejects. Non-Promise values are passed through unchanged.

# Core Definition

"Exploring JavaScript" Ch. 44: "The await operator can only be used inside async functions and async generators. Its operand is usually a Promise and leads to the following steps being performed: The current async function is paused. When and if the Promise is settled, the async function is resumed: If the Promise is fulfilled, await returns the fulfillment value. If the Promise is rejected, await throws the rejection value."

# Prerequisites

- **Async function** -- `await` can only be used inside async functions
- **Promise** -- `await` operates on Promises

# Key Properties

1. Pauses the async function (but not the overall JavaScript process)
2. Fulfilled Promise: returns the fulfillment value
3. Rejected Promise: throws the rejection value (catchable with try/catch)
4. Non-Promise values: simply passed through (but still delivered asynchronously)
5. Result is always delivered asynchronously (even for non-Promises)

# Construction / Recognition

```js
// Awaiting a fulfilled Promise
assert.equal(await Promise.resolve('fulfilled'), 'fulfilled');

// Awaiting a rejected Promise
try {
  await Promise.reject('rejected');
} catch (err) {
  assert.equal(err, 'rejected');
}

// Awaiting a non-Promise value
assert.equal(await 'non-Promise value', 'non-Promise value');
```

(Ch. 44, Section 44.2, lines 252-339)

# Context & Application

`await` is the core mechanism of async functions, enabling sequential-looking code that handles asynchronous operations. It replaces `.then()` chains with more readable linear code.

# Examples

```js
async function awaitPromise() {
  queueMicrotask(() => console.log('OTHER TASK'));
  console.log('before');
  await Promise.resolve('fulfilled');
  console.log('after');
}
// Output: before, OTHER TASK, after
```

(Ch. 44, Section 44.2.1, lines 288-304)

# Relationships

## Builds Upon
- **Async function** -- `await` requires an async function context
- **Promise** -- `await` unwraps Promises

## Related
- **Top-level await** -- `await` at module top level (ES2022)

# Common Errors

- **Error**: Using `await` outside an async function
  **Correction**: Either wrap in an async function or use top-level await in a module (ES2022)

# Common Confusions

- **Confusion**: `await` blocks the JavaScript process
  **Clarification**: `await` only pauses the current async function; other tasks continue running

# Source Reference

Chapter 44: Async functions, Sections 44.1.1, 44.2, lines 136-360.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit detailed definition with all three cases
- Cross-reference status: verified
