---
# === CORE IDENTIFICATION ===
concept: Promise Flattening
slug: promise-flattening

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
section: "19.7 Version 3: Flattening Promises returned from .then() callbacks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Promise unwrapping"
  - "recursive thenable resolution"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-chaining
  - thenable
  - promise-resolution
extends:
  - promise-chaining
related:
  - lock-in-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Promise flattening relate to .then() chaining?"
  - "What must I understand before learning about Promise flattening?"
---

# Quick Definition

Promise flattening is the mechanism by which a Promise resolved with another Promise (or thenable) automatically adopts the state and value of that inner Promise, rather than wrapping it.

# Core Definition

From "Deep JavaScript" (Ch 19.7): "Promise-flattening is mostly about making chaining more convenient." When a Promise P is resolved with a Promise Q, P does not wrap Q -- P "becomes" Q: "State and settlement value of P are now always the same as Q's." This is implemented by having P lock in on Q: "P becomes externally unresolvable and a settlement of Q triggers a settlement of P."

# Prerequisites

- **Promise** — Flattening is a behavior of Promise resolution
- **Promise chaining** — Flattening is needed to make chaining with async callbacks work cleanly
- **Thenable** — Flattening works with any thenable, not just native Promises
- **Promise resolution** — Flattening occurs during resolution

# Key Properties

1. If `.then()` callback returns a Promise, that Promise is "flattened" into the chain
2. The next `.then()` receives the fulfillment value of the returned Promise, not the Promise itself
3. Implemented by detecting thenables and forwarding their settlements
4. Makes the Promise state model more complex (adds lock-in)

# Construction / Recognition

## To Construct/Create:
1. Return a Promise (or thenable) from a `.then()` callback

## To Identify/Recognize:
1. When a `.then()` callback returns a Promise and the next `.then()` receives the unwrapped value

# Context & Application

Without flattening, returning a Promise from a `.then()` callback would force nested `.then()` calls to unwrap it. Flattening makes chains of async operations flat and readable.

# Examples

**Example 1** (Ch 19): Without flattening (inconvenient):
```js
asyncFunc1()
.then((result1) => {
  return asyncFunc2(); // returns a Promise
})
.then((result2Promise) => {
  result2Promise
  .then((result2) => { // must manually unwrap
    assert.equal(result2, 'Result of asyncFunc2()');
  });
});
```

**Example 2** (Ch 19): With flattening (convenient):
```js
asyncFunc1()
.then((result1) => {
  return asyncFunc2(); // returns a Promise
})
.then((result2) => {
  // result2 is the fulfillment value, not the Promise
  assert.equal(result2, 'Result of asyncFunc2()');
});
```

# Relationships

## Builds Upon
- **Promise chaining** — Flattening extends chaining to handle async callbacks
- **Thenable** — Flattening detects and unwraps thenables

## Enables
- **Lock-in state** — An invisible state needed to implement flattening
- **Seamless async composition** — Multiple async operations composed in flat chains

## Related
- **Promise resolution** — Flattening occurs during the resolution process

# Common Errors

- **Error**: Expecting the returned Promise itself to be the fulfillment value
  **Correction**: Flattening automatically unwraps the Promise; the next `.then()` receives the inner value

# Common Confusions

- **Confusion**: Flattening only works with native Promises
  **Clarification**: Flattening works with any thenable (any object with a `.then()` method), enabling interoperability between different Promise implementations

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.7, lines 8437+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Central topic of Section 19.7 with implementation details
- Cross-reference status: verified against ECMAScript spec reference in text
