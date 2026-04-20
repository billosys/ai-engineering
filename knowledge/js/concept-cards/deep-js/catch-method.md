---
# === CORE IDENTIFICATION ===
concept: ".catch() Method"
slug: catch-method

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
section: "19.4 Convenience method .catch()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Promise.prototype.catch()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - then-method
  - rejection-reaction
extends:
  - then-method
related:
  - promise-chaining
contrasts_with:
  - then-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a fulfillment reaction from a rejection reaction?"
---

# Quick Definition

The `.catch()` method is a convenience shorthand for `.then(null, rejectionReaction)`, used to register only a rejection handler.

# Core Definition

From "Deep JavaScript" (Ch 19.4): "The following two method invocations are equivalent: `.catch(rejectionReaction)` and `.then(null, rejectionReaction)`." The implementation is simply:
```js
catch(onRejected) {
  return this.then(null, onRejected);
}
```

# Prerequisites

- **Promise** — `.catch()` is a method on Promise objects
- **`.then()` method** — `.catch()` is implemented in terms of `.then()`
- **Rejection reaction** — The callback passed to `.catch()`

# Key Properties

1. Syntactic sugar for `.then(null, onRejected)`
2. Returns a new Promise (because `.then()` does)
3. If the rejection handler returns a value, the returned Promise is *fulfilled* (not rejected)

# Construction / Recognition

## To Construct/Create:
1. Call `.catch(onRejected)` on any Promise

## To Identify/Recognize:
1. A `.then()` call with only a rejection handler

# Context & Application

`.catch()` improves readability in Promise chains by making error handling visually distinct. It is commonly placed at the end of a chain to handle any rejection in the chain.

# Examples

**Example 1** (Ch 19):
```js
new ToyPromise2()
  .reject('error1')
  .catch(x => {
    assert.equal(x, 'error1');
    return 'result2';
  })
  .then(x => {
    assert.equal(x, 'result2');
  });
```

**Example 2** (Ch 19): Catching rejections from multiple steps:
```js
someAsyncFunction()
  .then(fulfillmentReaction1)
  .then(fulfillmentReaction2)
  .catch(rejectionReaction);
```

# Relationships

## Builds Upon
- **`.then()` method** — Implemented as `.then(null, onRejected)`

## Enables
- **Centralized error handling** — A single `.catch()` at end of chain handles all preceding rejections

## Contrasts With
- **`.then()` method** — `.then()` can handle both fulfillment and rejection

# Common Errors

- **Error**: Placing `.catch()` before `.then()` and expecting it to catch errors from later `.then()` calls
  **Correction**: `.catch()` only catches rejections from Promises *before* it in the chain

# Common Confusions

- **Confusion**: `.catch()` keeps the chain in a rejected state
  **Clarification**: If the `.catch()` callback returns a value (does not throw), the resulting Promise is fulfilled

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.4, lines 8437+.

# Verification Notes

- Definition source: direct from source with implementation
- Confidence rationale: Explicitly defined with equivalence shown
- Cross-reference status: verified
