---
concept: Promise.withResolvers()
slug: promise-with-resolvers
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.1.11 Promise.withResolvers()"
extraction_confidence: high
aliases:
  - withResolvers
prerequisites:
  - promise
  - promise-constructor
extends:
  - promise-constructor
related:
  - promise-resolve-reject
contrasts_with: []
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

`Promise.withResolvers()` is a static factory method (ES2024) that creates a Promise and returns an object containing the Promise along with its `resolve` and `reject` functions, allowing settlement from outside the constructor callback.

# Core Definition

"Exploring JavaScript" Ch. 43: "The most common way of creating and resolving a Promise is via the Promise constructor." However, "sometimes we want to use [resolve and reject] outside of it. That's when the following static factory method is useful: `const { promise, resolve, reject } = Promise.withResolvers();`" Introduced in ES2024.

# Prerequisites

- **Promise** -- this creates Promise instances
- **Promise constructor** -- `withResolvers` is an alternative to the constructor

# Key Properties

1. Introduced in ES2024
2. Returns `{ promise, resolve, reject }`
3. `resolve` and `reject` can be used outside the constructor callback
4. Named "withResolvers" because the spec calls `resolve` and `reject` "resolving functions"

# Construction / Recognition

```js
const { promise, resolve, reject } = Promise.withResolvers();
resolve('fulfilled');
assert.equal(await promise, 'fulfilled');
```

(Ch. 43, Section 43.1.11, lines 770-794)

# Context & Application

Useful when the code that creates the Promise is different from the code that settles it, such as in queue implementations or deferred patterns.

# Examples

One-element queue using `withResolvers`:
```js
class OneElementQueue {
  #promise = null;
  #resolve = null;
  constructor() {
    const { promise, resolve } = Promise.withResolvers();
    this.#promise = promise;
    this.#resolve = resolve;
  }
  get() { return this.#promise; }
  put(value) { this.#resolve(value); }
}
```

(Ch. 43, Section 43.1.11.2, lines 846-881)

# Relationships

## Builds Upon
- **Promise constructor** -- alternative to `new Promise()`

## Related
- **Promise.resolve()/Promise.reject()** -- other factory methods

# Common Errors

- **Error**: Calling `resolve` or `reject` multiple times expecting multiple settlements
  **Correction**: Only the first call has effect; subsequent calls are ignored

# Common Confusions

- **Confusion**: `withResolvers` is needed for all Promise creation
  **Clarification**: Only needed when resolve/reject must be accessible outside the constructor callback; `new Promise()` suffices for most cases

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.11, lines 751-881.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with implementation
- Cross-reference status: verified
