---
# === CORE IDENTIFICATION ===
concept: Promise State
slug: promise-state

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
  - "Promise lifecycle"
  - "Promise settlement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
extends: []
related:
  - fulfillment-value
  - rejection-value
  - lock-in-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Promise state?"
  - "What must I understand before learning about Promise flattening?"
---

# Quick Definition

A Promise state is one of three conditions a Promise can be in: pending (initial), fulfilled (resolved with a value), or rejected (settled with an error).

# Core Definition

As described in "Deep JavaScript" (Ch 19.1): "A Promise is initially *pending*. If a Promise is *resolved* with a value `v`, it becomes *fulfilled*. `v` is now the *fulfillment value* of the Promise. If a Promise is *rejected* with an error `e`, it becomes *rejected*. `e` is now the *rejection value* of the Promise."

The simplified model has three states. With Promise flattening, an additional invisible pseudo-state "locked-in" is introduced.

# Prerequisites

- **Promise** — States describe the lifecycle of a Promise object

# Key Properties

1. `pending` — initial state, neither fulfilled nor rejected
2. `fulfilled` — the operation completed successfully with a fulfillment value
3. `rejected` — the operation failed with a rejection reason
4. Once a Promise moves from `pending` to `fulfilled` or `rejected`, it is *settled* and cannot change state again

# Construction / Recognition

## To Construct/Create:
1. Every new Promise starts in the `pending` state
2. Calling `resolve(value)` transitions to `fulfilled`
3. Calling `reject(error)` transitions to `rejected`

## To Identify/Recognize:
1. In the ToyPromise implementation, state is tracked via `this._promiseState` (string: `'pending'`, `'fulfilled'`, `'rejected'`)

# Context & Application

Promise states determine how `.then()` behaves: if pending, reactions are queued; if already settled, reactions are immediately enqueued to the task queue. Understanding states is essential before learning about flattening, which introduces the additional locked-in pseudo-state.

# Examples

**Example 1** (Ch 19): State transitions in ToyPromise implementation:
```js
resolve(value) {
  if (this._promiseState !== 'pending') return this;
  this._promiseState = 'fulfilled';
  this._promiseResult = value;
  this._clearAndEnqueueTasks(this._fulfillmentTasks);
  return this;
}
```

# Relationships

## Builds Upon
- **Promise** — States are the internal lifecycle mechanism of Promises

## Enables
- **Promise chaining** — State determines whether reactions execute immediately or are queued
- **Lock-in state** — Flattening adds an invisible pseudo-state between pending and settled

## Related
- **Fulfillment value** — The value associated with the fulfilled state
- **Rejection value** — The value associated with the rejected state

## Contrasts With
- **Lock-in state** — An additional invisible state introduced by Promise flattening

# Common Errors

- **Error**: Thinking a Promise can transition from fulfilled back to pending or to rejected
  **Correction**: State transitions are one-way; once settled, a Promise stays settled

# Common Confusions

- **Confusion**: "Resolved" means the same as "fulfilled"
  **Clarification**: Per the ECMAScript spec: "An unresolved Promise is always in the pending state. A resolved Promise may be pending, fulfilled, or rejected." Resolving with another Promise can leave a Promise pending or cause rejection.

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.1, lines 8437+.

# Verification Notes

- Definition source: direct quote from source
- Confidence rationale: Explicitly defined with diagram (Figure 11) in the source
- Cross-reference status: verified against ECMAScript spec quote in section 19.7.2
