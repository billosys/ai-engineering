---
# === CORE IDENTIFICATION ===
concept: Fulfillment Value
slug: fulfillment-value

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
section: "19.1 Refresher: states of Promises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Promise result"
  - "resolved value"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-state
extends: []
related:
  - rejection-value
  - fulfillment-reaction
contrasts_with:
  - rejection-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Promise state?"
---

# Quick Definition

The fulfillment value is the result value stored in a Promise when it transitions from pending to fulfilled.

# Core Definition

From "Deep JavaScript" (Ch 19.1): "If a Promise is *resolved* with a value `v`, it becomes *fulfilled*. `v` is now the *fulfillment value* of the Promise." In the ToyPromise implementation, this value is stored in `this._promiseResult` and passed to fulfillment reactions registered via `.then()`.

# Prerequisites

- **Promise** — Fulfillment values are the successful outcomes of Promises
- **Promise state** — The fulfilled state is when a fulfillment value exists

# Key Properties

1. Set when `.resolve(value)` is called on a pending Promise
2. Stored internally and passed to fulfillment reactions (first argument of `.then()`)
3. Immutable once set -- the Promise cannot be re-resolved

# Construction / Recognition

## To Construct/Create:
1. Call `resolve(value)` on a pending Promise

## To Identify/Recognize:
1. The value passed to the `onFulfilled` callback in `.then(onFulfilled, onRejected)`

# Context & Application

The fulfillment value is the "success result" of an asynchronous operation. It flows through Promise chains via `.then()` callbacks.

# Examples

**Example 1** (Ch 19):
```js
const tp1 = new ToyPromise1();
tp1.resolve('abc');
tp1.then((value) => {
  assert.equal(value, 'abc'); // 'abc' is the fulfillment value
});
```

# Relationships

## Builds Upon
- **Promise state** — The fulfillment value only exists when state is `fulfilled`

## Enables
- **Promise chaining** — Fulfillment values flow through `.then()` chains

## Contrasts With
- **Rejection value** — The error counterpart stored when a Promise is rejected

# Common Errors

- **Error**: Expecting the fulfillment value to be the Promise returned by `.then()` callback when that callback returns a Promise
  **Correction**: With flattening, the fulfillment value of the returned Promise is extracted, not the Promise itself

# Common Confusions

- **Confusion**: The fulfillment value and the argument to `resolve()` are always the same
  **Clarification**: If `resolve()` receives a thenable, Promise flattening means the fulfillment value is the thenable's eventual result, not the thenable itself

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.1, lines 8437+.

# Verification Notes

- Definition source: direct quote from source
- Confidence rationale: Explicitly defined in section 19.1
- Cross-reference status: verified
