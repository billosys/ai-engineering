---
# === CORE IDENTIFICATION ===
concept: Promise Resolution
slug: promise-resolution

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
section: "19.7.2 Flattening makes Promise states more complicated"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "resolving a Promise"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-state
extends: []
related:
  - promise-flattening
  - thenable
  - lock-in-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Promise state?"
  - "How do I implement a Promise from scratch?"
---

# Quick Definition

Promise resolution is the act of settling or locking in a Promise by calling `resolve(value)`, which may fulfill, reject, or lock the Promise onto another thenable depending on the value provided.

# Core Definition

From "Deep JavaScript" (Ch 19.7.2): "The concept of *resolving* has also become more complicated. Resolving a Promise now only means that it can't be settled directly, anymore: Resolving may reject a Promise: We can resolve a Promise with a rejected Promise. Resolving may not even settle a Promise: We can resolve a Promise with another one that is always pending."

The ECMAScript specification states: "An unresolved Promise is always in the pending state. A resolved Promise may be pending, fulfilled, or rejected."

# Prerequisites

- **Promise** — Resolution is an operation on Promises
- **Promise state** — Resolution changes the state or locks it in

# Key Properties

1. A resolved Promise cannot be directly settled again
2. Resolving with a non-thenable value fulfills the Promise
3. Resolving with a thenable locks in the Promise on that thenable
4. Resolving with a rejected Promise causes rejection
5. Resolving with a forever-pending Promise leaves the Promise pending

# Construction / Recognition

## To Construct/Create:
1. Call `resolve(value)` on a pending Promise

## To Identify/Recognize:
1. The `resolve()` method or the first callback parameter of the Promise constructor

# Context & Application

Resolution is a subtler concept than it appears. In simple cases, resolving equals fulfilling. But with flattening, resolving is the entry point to a more complex state machine that handles thenables.

# Examples

**Example 1** (Ch 19): Resolution with flattening:
```js
resolve(value) {
  if (this._alreadyResolved) return this;
  this._alreadyResolved = true;

  if (isThenable(value)) {
    // Forward fulfillments and rejections from `value` to `this`.
    value.then(
      (result) => this._doFulfill(result),
      (error) => this._doReject(error));
  } else {
    this._doFulfill(value);
  }
  return this;
}
```

# Relationships

## Builds Upon
- **Promise state** — Resolution transitions or locks state

## Enables
- **Promise flattening** — Resolution handles thenable unwrapping
- **Lock-in state** — Resolution with a thenable causes lock-in

## Related
- **Thenable** — Resolution behavior depends on whether the value is a thenable

# Common Errors

- **Error**: Calling `resolve()` multiple times expecting multiple state transitions
  **Correction**: Only the first call to `resolve()` or `reject()` takes effect

# Common Confusions

- **Confusion**: "Resolving" and "fulfilling" are synonymous
  **Clarification**: Resolving with a thenable may result in rejection or indefinite pending; resolving only guarantees that the Promise cannot be directly settled again

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.7.2-19.7.3, lines 8437+.

# Verification Notes

- Definition source: direct from source with ECMAScript spec quote
- Confidence rationale: Explicitly discussed as a nuanced concept
- Cross-reference status: verified against spec quote in text
