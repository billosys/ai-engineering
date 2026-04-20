---
# === CORE IDENTIFICATION ===
concept: Lock-in State
slug: lock-in-state

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
  - "locked-in"
  - "locked-in state"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-state
  - promise-flattening
  - thenable
extends:
  - promise-state
related:
  - promise-resolution
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Promise state?"
  - "What must I understand before learning about Promise flattening?"
---

# Quick Definition

The lock-in state is an invisible pseudo-state that a Promise enters when it is resolved with a thenable, making the Promise externally unresolvable while it tracks the thenable's eventual settlement.

# Core Definition

From "Deep JavaScript" (Ch 19.7.2): "How does P become Q? By *locking in* on Q: P becomes externally unresolvable and a settlement of Q triggers a settlement of P. Lock-in is an additional invisible Promise state that makes states more complicated." Figure 14 shows that "locked-in" is reached if a Promise P is resolved with a thenable Q, after which "state and settlement value of P is always the same as those of Q."

# Prerequisites

- **Promise** — Lock-in is a state within a Promise
- **Promise state** — Lock-in extends the basic state model
- **Promise flattening** — Lock-in is the mechanism that implements flattening
- **Thenable** — Lock-in occurs when resolving with a thenable

# Key Properties

1. An invisible (internal) state, not exposed to users
2. Entered when `resolve(thenable)` is called
3. The locked-in Promise becomes externally unresolvable (further `resolve`/`reject` calls are ignored)
4. The Promise's eventual state and value mirror the thenable's state and value
5. Implemented via the `_alreadyResolved` flag in ToyPromise3

# Construction / Recognition

## To Construct/Create:
1. Resolve a Promise with another Promise or thenable

## To Identify/Recognize:
1. The Promise has been resolved but is not yet settled (still pending)
2. In the implementation: `_alreadyResolved` is `true` but `_promiseState` is still `'pending'`

# Context & Application

Lock-in is the key internal mechanism that makes Promise flattening work. It ensures that when a Promise is resolved with a thenable, the Promise's fate is entirely determined by the thenable.

# Examples

**Example 1** (Ch 19): Implementation of lock-in:
```js
resolve(value) {
  if (this._alreadyResolved) return this;
  this._alreadyResolved = true; // locks in

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
- **Promise state** — Adds a fourth pseudo-state to the model
- **Promise flattening** — Lock-in is the implementation mechanism for flattening

## Enables
- **Thenable interoperability** — Lock-in allows Promises to adopt any thenable's state

## Related
- **Promise resolution** — Lock-in is triggered during resolution

# Common Errors

- **Error**: Trying to re-resolve a locked-in Promise
  **Correction**: Once `_alreadyResolved` is set, further `resolve()` and `reject()` calls are no-ops

# Common Confusions

- **Confusion**: A locked-in Promise is settled
  **Clarification**: A locked-in Promise may still be pending if the thenable it locked onto is pending. Per the spec: "A resolved Promise may be pending, fulfilled, or rejected."

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.7.2-19.7.3, lines 8437+.

# Verification Notes

- Definition source: direct from source text and Figure 14
- Confidence rationale: Explicitly defined and diagrammed
- Cross-reference status: verified against ECMAScript spec reference in text
