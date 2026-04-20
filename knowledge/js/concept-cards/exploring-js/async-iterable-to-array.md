---
concept: Converting Async Iterable to Array
slug: async-iterable-to-array
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Asynchronous iteration"
chapter_number: 45
pdf_page: null
section: "45.2.3 Example: converting an async iterable to an Array"
extraction_confidence: high
aliases:
  - asyncIterableToArray
prerequisites:
  - async-iteration-protocol
  - for-await-of
extends: []
related:
  - async-generator
contrasts_with: []
answers_questions:
  - "How do synchronous and asynchronous iteration protocols differ?"
---

# Quick Definition

An async iterable can be collected into an Array using `for-await-of` inside an async function that pushes values to a result array, since there is no built-in async equivalent of `Array.from()` or spread syntax.

# Core Definition

"Exploring JavaScript" Ch. 45 provides the pattern: "async function asyncIterableToArray(asyncIterable) { const result = []; for await (const value of asyncIterable) { result.push(value); } return result; }" Note: "We can't use an async generator in this case: We get our input via for-await-of and return an Array wrapped in a Promise."

# Prerequisites

- **Async iteration protocol** -- consumes async iterables
- **for-await-of** -- used to iterate

# Key Properties

1. No built-in way to spread an async iterable
2. Must use `for-await-of` to collect values manually
3. Returns a Promise for an Array (since the function is async)
4. Cannot use an async generator for this task

# Construction / Recognition

```js
async function asyncIterableToArray(asyncIterable) {
  const result = [];
  for await (const value of asyncIterable) {
    result.push(value);
  }
  return result;
}
```

(Ch. 45, Section 45.2.3, lines 367-373)

# Context & Application

Common utility when working with async iterables and needing to process all values at once rather than streaming.

# Examples

```js
async function* createAsyncIterable() { yield 'a'; yield 'b'; }
assert.deepEqual(
  await asyncIterableToArray(createAsyncIterable()),
  ['a', 'b']
);
```

(Ch. 45, Section 45.2.3, lines 384-393)

# Relationships

## Builds Upon
- **Async iteration protocol** -- consumes the protocol
- **for-await-of** -- iteration mechanism

## Related
- **Async generator** -- often produces the async iterable being collected

# Common Errors

- **Error**: Trying to use spread syntax with an async iterable
  **Correction**: Spread doesn't work with async iterables; use the manual collection pattern

# Common Confusions

- **Confusion**: `Array.from()` works with async iterables
  **Clarification**: `Array.from()` only works with sync iterables; use a custom helper for async

# Source Reference

Chapter 45: Asynchronous iteration, Section 45.2.3, lines 359-397.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit helper function with explanation
- Cross-reference status: verified
