---
concept: Thenables
slug: thenables
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.8 Thenables (Promise-like objects)"
extraction_confidence: high
aliases:
  - Promise-like objects
  - thenable objects
prerequisites:
  - promise
  - promise-then
extends: []
related:
  - promise-resolve-reject
contrasts_with: []
answers_questions:
  - "What is a Promise?"
---

# Quick Definition

A thenable is any object with a `.then()` method, representing the minimal Promise-like interface. The Promise API transparently converts thenables to Promises for interoperability with pre-ES6 Promise libraries.

# Core Definition

"Exploring JavaScript" Ch. 43: "Because Promise-like objects only have a method .then(), they are also called thenables." The interface is: `interface PromiseLike<T> { then(...): PromiseLike<...>; }`. "This is sufficient because .catch() is actually just a convenient way of invoking .then()." Thenables are accepted by `Promise.resolve()`, `new Promise(resolve => resolve(thenable))`, and as return values from `.then()` callbacks.

# Prerequisites

- **Promise** -- thenables are the minimal Promise interface
- **Promise.then()** -- `.then()` is the only required method

# Key Properties

1. Only requires a `.then(onFulfilled, onRejected)` method
2. Designed for interoperability with pre-ES6 Promise libraries
3. `Promise.resolve(thenable)` converts to a real Promise
4. Returning a thenable from `.then()` callback resolves with it
5. `.catch()` is equivalent to `.then(undefined, onRejected)`, so `.then()` suffices

# Construction / Recognition

```js
const fulfilledThenable = {
  then(onFulfilled, onRejected) {
    onFulfilled('Success!');
  },
};

Promise.resolve(fulfilledThenable)
  .then(value => assert.equal(value, 'Success!'));
```

(Ch. 43, Section 43.8.1, lines 2363-2391)

# Context & Application

Thenables enable interoperability between different Promise implementations. Any object that duck-types as having a `.then()` method will be treated as Promise-like.

# Examples

Rejected thenable:
```js
const rejectedThenable = {
  then(onFulfilled, onRejected) {
    onRejected('Error!');
  },
};
Promise.resolve(rejectedThenable)
  .catch(reason => assert.equal(reason, 'Error!'));
```

(Ch. 43, Section 43.8.2, lines 2410-2425)

# Relationships

## Builds Upon
- **Promise** -- thenables are the duck-typed version

## Related
- **Promise.resolve()** -- converts thenables to Promises

# Common Errors

- **Error**: Accidentally creating a thenable by adding a `.then()` method to a non-Promise object
  **Correction**: Be aware that any object with `.then()` will be treated as Promise-like

# Common Confusions

- **Confusion**: Thenables are full Promises
  **Clarification**: Thenables only need `.then()`; they may lack `.catch()`, `.finally()`, etc.

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.8, lines 2308-2432.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with TypeScript interface
- Cross-reference status: verified
