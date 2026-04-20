---
concept: Promise.try()
slug: promise-try
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.1.9 Promise.try()"
extraction_confidence: high
aliases: []
prerequisites:
  - promise
  - promise-chaining
extends: []
related:
  - promise-resolve-reject
contrasts_with: []
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

`Promise.try(cb)` (ES2025) starts a Promise chain by calling `cb`, converting any thrown exceptions into rejected Promises and any returned values into resolved Promises, providing safe handling of mixed sync/async code at the start of a chain.

# Core Definition

"Exploring JavaScript" Ch. 43: "Where the Promise method .then(cb) continues a Promise chain, Promise.try(cb) starts a Promise chain -- while treating the callback cb similarly: It calls cb. If cb throws an exception, Promise.try() returns a rejection with that exception. If cb returns a value, Promise.try() resolves that value into a Promise." Introduced in ES2025.

# Prerequisites

- **Promise** -- `Promise.try()` creates Promises
- **Promise chaining** -- starts a chain

# Key Properties

1. Introduced in ES2025
2. Starts a Promise chain (vs. `.then()` which continues one)
3. Catches synchronous exceptions and converts them to rejections
4. Only needed for direct Promise code; async functions handle this natively

# Construction / Recognition

```js
function computeAsync() {
  return Promise.try(() => {
    const value = syncFuncMightThrow();
    return asyncFunc(value);
  });
}
```

(Ch. 43, Section 43.1.9, lines 544-549)

# Context & Application

Used when starting a Promise chain with code that mixes synchronous and asynchronous operations. Not needed if using async functions, which already handle this case.

# Examples

From the source, an alternative without `Promise.try()`:
```js
function countPlusOneAsync() {
  return Promise.resolve().then(
    () => countSyncOrAsync()
  ).then(result => result + 1);
}
```

The downside of this alternative is that it "executes the code... on the next tick (and not immediately)."

(Ch. 43, Section 43.1.9.3, lines 579-601)

# Relationships

## Builds Upon
- **Promise** -- static method on Promise
- **Promise chaining** -- starts a chain

## Related
- **Promise.resolve()/Promise.reject()** -- alternative approaches to starting chains

# Common Errors

- **Error**: Using `Promise.try()` when an async function would suffice
  **Correction**: Prefer async functions which naturally handle mixed sync/async code

# Common Confusions

- **Confusion**: `Promise.try()` is needed whenever creating Promises
  **Clarification**: Only needed at the start of a chain with mixed sync/async code when not using async functions

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.9, lines 517-601.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with use case
- Cross-reference status: verified
