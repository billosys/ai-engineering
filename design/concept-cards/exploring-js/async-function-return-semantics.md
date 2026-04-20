---
concept: Async Function Return Semantics
slug: async-function-return-semantics
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.4 return in async functions"
extraction_confidence: high
aliases:
  - return in async functions
  - async return behavior
prerequisites:
  - async-function
  - resolving-vs-fulfilling
extends: []
related:
  - return-await
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
---

# Quick Definition

The result of an async function is always a Promise: returning a non-Promise value fulfills it, returning a Promise resolves with it (adopting its state), throwing an exception rejects it, and implicit return resolves with `undefined`.

# Core Definition

"Exploring JavaScript" Ch. 44: "If we call an async function, the result is always a Promise -- even if the async function throws an exception." Returning a non-Promise value fulfills the result Promise. Returning a Promise `q` "resolves the result Promise p of the async function: p adopts the state of q (q basically replaces p). Resolving never nests Promises."

# Prerequisites

- **Async function** -- these are return semantics of async functions
- **Resolving vs fulfilling** -- the distinction matters for return behavior

# Key Properties

1. `return value` resolves the result Promise with value
2. `return promise` resolves the result Promise with the returned Promise (no nesting)
3. `throw error` rejects the result Promise
4. Implicit return (no return statement) resolves with `undefined`
5. Async functions start synchronously, settle asynchronously

# Construction / Recognition

```js
async function asyncFunc() { return 123; }
asyncFunc().then(result => assert.equal(result, 123));

async function asyncFunc() { throw new Error('Problem!'); }
asyncFunc().catch(err => assert.deepEqual(err, new Error('Problem!')));

async function asyncFunc1() { return Promise.resolve('fulfilled'); }
// Result Promise adopts fulfilled state
```

(Ch. 44, Section 44.4, lines 501-579)

# Context & Application

Understanding return semantics is essential for correctly composing async functions and avoiding subtle bugs with `return` vs `return await`.

# Examples

Async function starts sync, settles async:
```js
async function asyncFunc() {
  console.log('asyncFunc() starts');
  return 'abc';
}
asyncFunc().then(x => console.log(`Resolved: ${x}`));
console.log('Task ends');
// Output: asyncFunc() starts, Task ends, Resolved: abc
```

(Ch. 44, Section 44.5, lines 617-634)

# Relationships

## Builds Upon
- **Async function** -- return semantics are specific to async functions
- **Resolving vs fulfilling** -- `return` resolves, does not always fulfill

## Related
- **Return await pattern** -- `return await` vs plain `return`

# Common Errors

- **Error**: Returning a rejected Promise without `await` in a try/catch block
  **Correction**: Use `return await` inside try/catch to properly catch rejections

# Common Confusions

- **Confusion**: Returning a Promise from async function creates a nested Promise
  **Clarification**: Resolving never nests; the returned Promise's state is adopted

# Source Reference

Chapter 44: Async functions, Sections 44.4, 44.5, lines 501-634.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit detailed section
- Cross-reference status: verified
