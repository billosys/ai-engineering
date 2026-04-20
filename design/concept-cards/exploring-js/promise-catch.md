---
# === CORE IDENTIFICATION ===
concept: Promise.prototype.catch()
slug: promise-catch

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
section: "43.1.7 .catch() and its callback"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ".catch()"
  - catch method

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-then
extends: []
related:
  - promise-chaining
  - promise-error-handling
contrasts_with:
  - promise-then

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

`.catch()` registers a callback for the rejection value of a Promise. It is equivalent to `.then(undefined, onRejected)` and, like `.then()`, returns a new Promise whose state depends on the callback's behavior.

# Core Definition

"Exploring JavaScript" Ch. 43 states: "The difference between .then() and .catch() is that the latter is triggered by rejections, not fulfillments. However, both methods turn the actions of their callbacks into Promises in the same manner." A `.catch()` callback returning a value produces a fulfilled Promise, enabling error recovery.

# Prerequisites

- **Promise** -- `.catch()` is a Promise instance method
- **Promise.then()** -- `.catch()` is essentially `.then(undefined, onRejected)`

# Key Properties

1. Triggered by rejections, not fulfillments
2. Equivalent to `.then(undefined, onRejected)`
3. Returns a new Promise (enabling chaining)
4. Callback returning a value -> returned Promise is fulfilled (error recovery)
5. Callback throwing -> returned Promise is rejected
6. Can handle both async rejections and sync exceptions from earlier `.then()` callbacks

# Construction / Recognition

```js
Promise.reject(new Error('oops'))
  .catch((e) => {
    return 'default value'; // error recovery
  })
  .then((str) => {
    assert.equal(str, 'default value');
  });
```

(Ch. 43, Section 43.1.7, lines 438-459)

# Context & Application

`.catch()` is the standard way to handle errors in Promise chains. It can catch both async rejections and synchronous exceptions thrown in `.then()` callbacks, unifying error handling.

# Examples

From the source:
```js
const err = new Error();
Promise.reject(err)
  .catch((e) => {
    assert.equal(e, err);
    return 'default value'; // recovery
  })
  .then((str) => {
    assert.equal(str, 'default value');
  });
```

(Ch. 43, Section 43.1.7, lines 446-459)

# Relationships

## Builds Upon
- **Promise** -- `.catch()` is a Promise instance method
- **Promise.then()** -- `.catch()` is a specialized form of `.then()`

## Enables
- **Promise error handling** -- primary error handling mechanism in Promise chains

## Contrasts With
- **Promise.then()** -- `.then()` handles fulfillments; `.catch()` handles rejections

# Common Errors

- **Error**: Placing `.catch()` only at the start of a chain, missing later rejections
  **Correction**: Place `.catch()` at the end to catch all rejections in the chain

# Common Confusions

- **Confusion**: `.catch()` terminates the Promise chain
  **Clarification**: `.catch()` returns a new Promise; the chain can continue after it

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.7, lines 438-459.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition
- Cross-reference status: verified
