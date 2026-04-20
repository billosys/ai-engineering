---
concept: Promise Chaining
slug: promise-chaining
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.1.8 Chaining method calls"
extraction_confidence: high
aliases:
  - Promise chain
  - ".then() chaining"
prerequisites:
  - promise-then
  - promise-catch
extends: []
related:
  - promise
  - promise-error-handling
contrasts_with: []
answers_questions:
  - "How do I create and consume a Promise?"
  - "How do callbacks, Promises, and async/await relate as async patterns?"
---

# Quick Definition

Promise chaining is the technique of calling `.then()` and `.catch()` in sequence, where each returns a new Promise, enabling sequential composition of asynchronous operations.

# Core Definition

"Exploring JavaScript" Ch. 43 explains: ".then() and .catch() always returning Promises enables us to create arbitrary long chains of method calls." In a chain, "return in line A returns the result of the last .then()." The text notes that ".then() is the asynchronous version of the synchronous semicolon."

# Prerequisites

- **Promise.then()** -- each link in the chain is a `.then()` call
- **Promise.catch()** -- error handling in chains

# Key Properties

1. Each `.then()` and `.catch()` returns a new Promise
2. Chains execute sequential async steps without nesting
3. A `.catch()` at the end handles errors from any step
4. Returning a Promise from a callback "flattens" -- no nested Promises

# Construction / Recognition

```js
function myAsyncFunc() {
  return asyncFunc1()
    .then((result1) => {
      return asyncFunc2(); // returns a Promise
    })
    .then((result2) => {
      return result2 ?? '(Empty)'; // returns a value
    })
    .then((result3) => {
      return asyncFunc4(); // returns a Promise
    });
}
```

(Ch. 43, Section 43.1.8, lines 468-483)

# Context & Application

Chaining is the fundamental composition mechanism for Promises. It replaces deeply nested callbacks ("callback hell") with flat, readable sequences.

# Examples

Chaining with mixed error handling:
```js
asyncFunc1()
  .then(result1 => asyncFunc2())
  .then(result2 => { /* ... */ })
  .catch(error => {
    // handles errors from asyncFunc1(), asyncFunc2(), and callbacks
  });
```

(Ch. 43, Section 43.1.8, lines 498-515)

# Relationships

## Builds Upon
- **Promise.then()** -- each chain link
- **Promise.catch()** -- chain error handling

## Enables
- **Async function** -- async/await provides cleaner syntax for chains

# Common Errors

- **Error**: Losing the tail -- assigning `promise.then(...)` but returning the original promise
  **Correction**: Return the result of `.then()`, not the original Promise

- **Error**: Unnecessary nesting -- putting `.then()` inside another `.then()` callback
  **Correction**: Return the inner Promise and chain at the same level

# Common Confusions

- **Confusion**: Each `.then()` modifies the original Promise
  **Clarification**: Each `.then()` creates and returns a new Promise; the original is unchanged

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.8, lines 461-515.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section on chaining with common mistakes
- Cross-reference status: verified
