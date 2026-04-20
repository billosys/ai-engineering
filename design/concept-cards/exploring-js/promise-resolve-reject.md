---
# === CORE IDENTIFICATION ===
concept: Promise.resolve() and Promise.reject()
slug: promise-resolve-reject

# === CLASSIFICATION ===
category: async-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.1.5 Creating resolved and rejected Promises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Promise.resolve
  - Promise.reject
  - Promise factory methods

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-states
extends: []
related:
  - resolving-vs-fulfilling
  - promise-constructor
  - promise-combinator-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

`Promise.resolve(x)` creates a Promise fulfilled with `x` (or returns `x` unchanged if it is already a Promise), while `Promise.reject(err)` creates a Promise rejected with `err`. Both are static factory methods for creating settled Promises.

# Core Definition

"Exploring JavaScript" Ch. 43 explains: "If x is a non-Promise value then Promise.resolve(x) creates a Promise that is fulfilled with that value." "If the argument is already a Promise, it is returned unchanged." "`Promise.reject(err)` accepts a value err (that is normally not a Promise) and returns a Promise that is rejected with it." These are "primitive functions" in the combinator pattern.

# Prerequisites

- **Promise** -- these are static methods on the Promise class
- **Promise states** -- they create Promises in specific states

# Key Properties

1. `Promise.resolve(nonPromise)` creates a fulfilled Promise (ES6)
2. `Promise.resolve(promise)` returns the same Promise unchanged
3. `Promise.reject(value)` creates a rejected Promise (ES6)
4. Useful for converting values to Promises and starting Promise chains
5. Classified as "primitive functions" in the Promise combinator pattern

# Construction / Recognition

```js
Promise.resolve(123)
  .then(x => assert.equal(x, 123));

const abcPromise = Promise.resolve('abc');
assert.equal(Promise.resolve(abcPromise), abcPromise); // same object

Promise.reject(new Error('My error!'))
  .catch(err => assert.equal(err.message, 'My error!'));
```

(Ch. 43, Section 43.1.5, lines 291-324)

# Context & Application

Used to normalize values to Promises, start Promise chains, return early results from Promise-based functions, and test Promise-based code.

# Examples

```js
function convertToNumber(stringOrNumber) {
  if (typeof stringOrNumber === 'number') {
    return Promise.resolve(stringOrNumber);
  } else if (typeof stringOrNumber === 'string') {
    return stringToNumberAsync(stringOrNumber);
  } else {
    return Promise.reject(new TypeError());
  }
}
```

(Ch. 43, Section 43.1.5, lines 338-347)

# Relationships

## Builds Upon
- **Promise** -- static factory methods on Promise

## Enables
- **Promise chaining** -- `Promise.resolve()` can start a chain
- **Promise combinator functions** -- listed as "primitives" alongside combinators

# Common Errors

- **Error**: Passing a rejected Promise to `Promise.resolve()` expecting it to become fulfilled
  **Correction**: `Promise.resolve()` returns the same Promise unchanged, including its rejected state

# Common Confusions

- **Confusion**: `Promise.reject()` unwraps Promises like `Promise.resolve()` does
  **Clarification**: `Promise.reject()` always creates a new rejected Promise; it does not unwrap its argument

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.5, lines 291-347.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definitions with examples
- Cross-reference status: verified
