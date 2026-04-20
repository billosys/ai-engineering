---
# === CORE IDENTIFICATION ===
concept: Promise Chaining
slug: promise-chaining

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
section: "19.3 Version 2: Chaining .then() calls"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ".then() chaining"
  - "Promise chain"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - then-method
  - fulfillment-reaction
  - rejection-reaction
extends:
  - then-method
related:
  - promise-flattening
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Promise flattening relate to .then() chaining?"
---

# Quick Definition

Promise chaining is the pattern where `.then()` returns a new Promise resolved with the return value of the reaction callback, enabling sequential composition of async operations.

# Core Definition

From "Deep JavaScript" (Ch 19.3): "A value that we return from a fulfillment reaction or a rejection reaction can be handled by a fulfilment reaction in a following `.then()` call." The implementation works by having `.then()` create and return a `resultPromise`. The fulfillment or rejection task resolves `resultPromise` with whatever the callback returns, or passes through the value/error if the callback is missing.

# Prerequisites

- **Promise** — Chaining is built on Promise objects
- **`.then()` method** — Chaining requires `.then()` to return a new Promise
- **Fulfillment reaction** — Return values from reactions drive the chain
- **Rejection reaction** — Rejection reactions can "fix" errors and return fulfillment values

# Key Properties

1. `.then()` returns a new Promise (`resultPromise`)
2. If `onFulfilled` returns a value, `resultPromise` is resolved with it
3. If `onRejected` returns a value, `resultPromise` is *resolved* (not rejected) -- the error is considered handled
4. If a reaction is missing, the value/error passes through unchanged

# Construction / Recognition

## To Construct/Create:
1. Call `.then()` on a Promise and return a value from the callback
2. Chain additional `.then()` calls on the returned Promise

## To Identify/Recognize:
1. Multiple `.then()` calls connected in sequence: `promise.then(...).then(...).then(...)`

# Context & Application

Chaining avoids nested callbacks ("callback hell") by enabling flat, sequential async code. With flattening (Version 3), chaining becomes even more powerful because returned Promises are automatically unwrapped.

# Examples

**Example 1** (Ch 19): Chaining fulfillment values:
```js
new ToyPromise2()
  .resolve('result1')
  .then(x => {
    assert.equal(x, 'result1');
    return 'result2';
  })
  .then(x => {
    assert.equal(x, 'result2');
  });
```

**Example 2** (Ch 19): Rejection handled, then fulfilled:
```js
new ToyPromise2()
  .reject('error1')
  .then(null,
    x => {
      assert.equal(x, 'error1');
      return 'result2';
    })
  .then(x => {
    assert.equal(x, 'result2');
  });
```

# Relationships

## Builds Upon
- **`.then()` method** — Chaining requires `.then()` to return a Promise

## Enables
- **Promise flattening** — Makes chaining with async callbacks seamless
- **Sequential async composition** — Complex async workflows as flat chains

## Related
- **`.catch()` method** — Can be used in chains for error handling

# Common Errors

- **Error**: Forgetting to return a value from a `.then()` callback
  **Correction**: If nothing is returned, the next `.then()` receives `undefined` as its fulfillment value

# Common Confusions

- **Confusion**: A rejection handler keeps the chain rejected
  **Clarification**: If `onRejected` returns a value (without throwing), `resultPromise` is *resolved*, not rejected. The error is considered handled.

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.3, lines 8437+.

# Verification Notes

- Definition source: direct from source implementation
- Confidence rationale: Full implementation shown in ToyPromise2
- Cross-reference status: verified
