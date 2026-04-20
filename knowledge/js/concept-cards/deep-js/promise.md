---
# === CORE IDENTIFICATION ===
concept: Promise
slug: promise

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Promise object"
  - "JS Promise"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - promise-state
  - thenable
  - promise-chaining
  - revealing-constructor-pattern
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a Promise from scratch?"
  - "What is a Promise state?"
---

# Quick Definition

A Promise is an object that represents the eventual result of an asynchronous operation, holding either a fulfillment value or a rejection reason.

# Core Definition

In "Deep JavaScript," Rauschmayer approaches Promises by building a toy implementation (`ToyPromise`) from scratch. A Promise can be created, resolved or rejected (only once), and reactions (callbacks) can be registered via `.then()`. The implementation reveals that a Promise maintains internal state (`pending`, `fulfilled`, or `rejected`), a result value, and queues of fulfillment and rejection tasks.

# Prerequisites

- **Callbacks** — Promises wrap callback-based async patterns
- **Event loop** — Promise reactions are executed asynchronously via the task queue

# Key Properties

1. A Promise is initially in the `pending` state
2. A Promise can only be settled (fulfilled or rejected) once
3. Reactions registered via `.then()` work correctly regardless of whether the Promise has already settled
4. Promises always settle asynchronously -- reactions are added to the task queue, never executed synchronously

# Construction / Recognition

## To Construct/Create:
1. Use `new Promise((resolve, reject) => { ... })` (revealing constructor pattern)
2. Or in the toy implementation: create a `ToyPromise` and call `.resolve(value)` or `.reject(reason)`

## To Identify/Recognize:
1. An object with a `.then()` method that accepts fulfillment and rejection callbacks
2. Has internal state tracking (pending/fulfilled/rejected)

# Context & Application

Promises are the foundation of modern asynchronous JavaScript programming. They enable chaining, error propagation, and serve as the basis for `async`/`await` syntax.

# Examples

**Example 1** (Ch 19): Resolve before `.then()`:
```js
const tp1 = new ToyPromise1();
tp1.resolve('abc');
tp1.then((value) => {
  assert.equal(value, 'abc');
});
```

**Example 2** (Ch 19): `.then()` before resolve:
```js
const tp2 = new ToyPromise1();
tp2.then((value) => {
  assert.equal(value, 'def');
});
tp2.resolve('def');
```

# Relationships

## Builds Upon
- **Event loop / task queue** — Promises schedule reactions asynchronously

## Enables
- **Promise chaining** — `.then()` returns a Promise enabling sequential async operations
- **Promise flattening** — Nested Promises are automatically unwrapped
- **async/await** — Syntactic sugar built on top of Promises

## Related
- **Thenable** — Any object with a `.then()` method; Promises interoperate with thenables

## Contrasts With
- **Callback pattern** — Promises provide a standardized, composable alternative to raw callbacks

# Common Errors

- **Error**: Assuming `.then()` callbacks execute synchronously
  **Correction**: Promise reactions are always executed asynchronously, even if the Promise is already settled

- **Error**: Trying to resolve or reject a Promise more than once
  **Correction**: Only the first resolution/rejection takes effect; subsequent calls are ignored

# Common Confusions

- **Confusion**: Resolving a Promise always fulfills it
  **Clarification**: Resolving with a rejected Promise or a pending Promise does not fulfill -- resolving may reject or leave the Promise pending

# Source Reference

Chapter 19: Exploring Promises by implementing them, Sections 19.1-19.9, lines 8437+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Promise is the central concept of Chapter 19, extensively defined and implemented
- Cross-reference status: verified against ToyPromise implementation
