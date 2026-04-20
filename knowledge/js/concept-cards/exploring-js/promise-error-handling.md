---
concept: Promise Error Handling
slug: promise-error-handling
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.3 Tip for error handling"
extraction_confidence: high
aliases:
  - rejection handling
  - Promise error management
prerequisites:
  - promise
  - promise-catch
  - promise-chaining
extends: []
related:
  - promise-finally
contrasts_with: []
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

Promise error handling unifies synchronous exceptions and asynchronous rejections: exceptions thrown inside `.then()` callbacks become rejections, and `.catch()` at the end of a chain handles errors from any earlier step.

# Core Definition

"Exploring JavaScript" Ch. 43 advises: "Don't mix (asynchronous) rejections and (synchronous) exceptions." Promise-based functions should "never throw exceptions" because callers only expect rejections. Solutions include wrapping sync code in `.then()` callbacks, using `new Promise()`, or using `Promise.try()`. Promises handle both "asynchronous errors (via rejections) and synchronous errors: Inside the callbacks for new Promise(), .then(), and .catch(), exceptions are converted to rejections."

# Prerequisites

- **Promise** -- error handling is fundamental to Promise usage
- **Promise.catch()** -- the primary error handling method
- **Promise chaining** -- errors propagate through chains

# Key Properties

1. Exceptions in `.then()` callbacks are automatically converted to rejections
2. `.catch()` at end of chain catches all upstream errors
3. Promise-based functions should never throw synchronous exceptions
4. `.catch()` unifies async rejections and sync exceptions (unlike callbacks)
5. Error recovery: returning a value from `.catch()` produces a fulfilled Promise

# Construction / Recognition

```js
readFile('person.json')
  .then(text => JSON.parse(text))  // sync exception becomes rejection
  .catch(err => {
    // catches both file read errors and JSON parse errors
    assert.fail(err);
  });
```

(Ch. 43, Section 43.2.1.2, lines 984-1011)

# Context & Application

Error handling is one of the main advantages of Promises over callbacks, which require separate mechanisms for sync and async errors.

# Examples

Avoiding mixed rejections and exceptions:
```js
// Don't: sync exception escapes
function asyncFunc() {
  doSomethingSync(); // might throw!
  return doSomethingAsync().then(result => { /*...*/ });
}

// Do: wrap in Promise
function asyncFunc() {
  return Promise.try(() => {
    doSomethingSync();
    return doSomethingAsync();
  }).then(result => { /*...*/ });
}
```

(Ch. 43, Section 43.3, lines 1118-1202)

# Relationships

## Builds Upon
- **Promise.catch()** -- primary mechanism
- **Promise chaining** -- errors propagate through chains

## Related
- **Promise.finally()** -- cleanup regardless of error state

# Common Errors

- **Error**: Forgetting `.catch()` at the end of a chain, causing unhandled rejections
  **Correction**: Always terminate Promise chains with `.catch()` or use try/catch with await

# Common Confusions

- **Confusion**: `.catch()` only catches asynchronous errors
  **Clarification**: It also catches synchronous exceptions thrown in preceding `.then()` callbacks

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.3, lines 1118-1202.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit tip with three solutions
- Cross-reference status: verified
