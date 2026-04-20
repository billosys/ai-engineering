---
# === CORE IDENTIFICATION ===
concept: Exception Handling in Promises
slug: promise-exception-handling

# === CLASSIFICATION ===
category: async-programming
subcategory: promises
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exploring Promises by implementing them"
chapter_number: 19
section: "19.8 Version 4: Exceptions thrown in reaction callbacks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Promise error conversion"
  - "try/catch in Promises"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - then-method
  - rejection-value
  - promise-chaining
extends:
  - promise-chaining
related:
  - catch-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a Promise from scratch?"
---

# Quick Definition

Exception handling in Promises converts exceptions thrown inside `.then()` reaction callbacks into rejections of the Promise returned by `.then()`.

# Core Definition

From "Deep JavaScript" (Ch 19.8): "As our final feature, we'd like our Promises to handle exceptions in user code as rejections." The implementation wraps reaction execution in try/catch via `_runReactionSafely()`:
```js
_runReactionSafely(resultPromise, reaction) {
  try {
    const returned = reaction(this._promiseResult);
    resultPromise.resolve(returned);
  } catch (e) {
    resultPromise.reject(e);
  }
}
```

# Prerequisites

- **Promise** — Exception handling is a feature of Promise objects
- **`.then()` method** — Exceptions are caught in `.then()` callbacks
- **Rejection value** — The caught exception becomes the rejection value
- **Promise chaining** — Exception-to-rejection conversion works through chains

# Key Properties

1. Exceptions in fulfillment or rejection reactions are caught automatically
2. The caught exception becomes the rejection value of the Promise returned by `.then()`
3. This prevents uncaught exceptions from crashing the program
4. Enables `.catch()` at the end of a chain to handle all errors, including thrown exceptions

# Construction / Recognition

## To Construct/Create:
1. Throw an exception inside a `.then()` callback

## To Identify/Recognize:
1. A `.catch()` handler receiving an error that was thrown (not explicitly rejected) in a previous `.then()`

# Context & Application

This feature unifies error handling: whether an async operation explicitly rejects or a synchronous computation throws, both result in a rejected Promise that can be caught with `.catch()`.

# Examples

**Example 1** (Ch 19):
```js
new ToyPromise4()
  .resolve('a')
  .then((value) => {
    assert.equal(value, 'a');
    throw 'b'; // triggers a rejection
  })
  .catch((error) => {
    assert.equal(error, 'b');
  })
```

# Relationships

## Builds Upon
- **Promise chaining** — Exceptions in reactions affect the chained Promise

## Enables
- **Unified error handling** — Both thrown exceptions and explicit rejections are handled the same way

## Related
- **`.catch()` method** — The primary way to handle exceptions converted to rejections

# Common Errors

- **Error**: Expecting thrown exceptions to propagate as uncaught errors
  **Correction**: Inside `.then()` callbacks, exceptions are caught and converted to rejections

# Common Confusions

- **Confusion**: Throwing in a rejection handler re-rejects with the original error
  **Clarification**: Throwing in a rejection handler rejects the *next* Promise in the chain with the *newly thrown* value

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.8, lines 8437+.

# Verification Notes

- Definition source: direct from source implementation
- Confidence rationale: Complete implementation shown
- Cross-reference status: verified
