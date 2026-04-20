---
# === CORE IDENTIFICATION ===
concept: Rejection Value
slug: rejection-value

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
  - "rejection reason"
  - "Promise error"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-state
extends: []
related:
  - fulfillment-value
  - rejection-reaction
contrasts_with:
  - fulfillment-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Promise state?"
---

# Quick Definition

The rejection value is the error or reason stored in a Promise when it transitions from pending to rejected.

# Core Definition

From "Deep JavaScript" (Ch 19.1): "If a Promise is *rejected* with an error `e`, it becomes *rejected*. `e` is now the *rejection value* of the Promise." In the ToyPromise implementation, this value is stored in `this._promiseResult` and passed to rejection reactions (the second argument of `.then()` or the argument of `.catch()`).

# Prerequisites

- **Promise** — Rejection values are the failure outcomes of Promises
- **Promise state** — The rejected state is when a rejection value exists

# Key Properties

1. Set when `.reject(reason)` is called on a pending Promise
2. Also set when an exception is thrown inside a `.then()` callback (Version 4 of ToyPromise)
3. Passed to rejection reactions registered via `.then(null, onRejected)` or `.catch(onRejected)`
4. Propagates through the chain if no rejection handler is present

# Construction / Recognition

## To Construct/Create:
1. Call `reject(reason)` on a pending Promise
2. Throw an exception inside a `.then()` callback

## To Identify/Recognize:
1. The value passed to the `onRejected` callback in `.then(onFulfilled, onRejected)` or `.catch(onRejected)`

# Context & Application

Rejection values enable error handling in Promise chains. Without a rejection handler, rejection values propagate down the chain until caught.

# Examples

**Example 1** (Ch 19):
```js
new ToyPromise2()
  .reject('error1')
  .then(null,
    x => {
      assert.equal(x, 'error1'); // 'error1' is the rejection value
      return 'result2';
    })
  .then(x => {
    assert.equal(x, 'result2');
  });
```

# Relationships

## Builds Upon
- **Promise state** — The rejection value only exists when state is `rejected`

## Enables
- **Error propagation** — Rejection values flow through chains until handled

## Contrasts With
- **Fulfillment value** — The success counterpart stored when a Promise is fulfilled

# Common Errors

- **Error**: Assuming rejection values must be Error objects
  **Correction**: Any value can be a rejection value, though Error objects are conventional

# Common Confusions

- **Confusion**: A handled rejection (via `.catch()` or rejection reaction) keeps the chain in rejected state
  **Clarification**: When a rejection reaction returns a value (not throwing), the next Promise in the chain is *fulfilled* with that returned value

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.1, lines 8437+.

# Verification Notes

- Definition source: direct quote from source
- Confidence rationale: Explicitly defined in section 19.1
- Cross-reference status: verified
