---
# === CORE IDENTIFICATION ===
concept: Resolving vs Fulfilling a Promise
slug: resolving-vs-fulfilling

# === CLASSIFICATION ===
category: async-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.1.4.2 What is the difference between resolving and fulfilling a Promise?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - resolve vs fulfill
  - Promise resolution

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-states
extends: []
related:
  - promise-constructor
  - promise-chaining
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What concepts are prerequisite to understanding Promises?"
---

# Quick Definition

Fulfilling a Promise means setting it to the "fulfilled" state with a non-Promise value. Resolving a Promise means determining its fate: if resolved with a non-Promise value, it is fulfilled; if resolved with another Promise, it adopts that Promise's state.

# Core Definition

"Exploring JavaScript" Ch. 43 explains: "A Promise can only be fulfilled with a non-Promise value. In contrast, we can resolve a Promise with either a non-Promise value or a Promise." If `resolve(x)` is called: "If x is a non-Promise value then p is fulfilled with x. If x is a Promise, then p adopts the state of x (which basically results in x replacing p)." Therefore, "resolving only determines the fate of a Promise; it may or may not fulfill it."

# Prerequisites

- **Promise** -- resolving/fulfilling are operations on Promises
- **Promise states** -- understanding pending/fulfilled/rejected

# Key Properties

1. `resolve(nonPromise)` fulfills the Promise with that value
2. `resolve(promise)` makes the Promise adopt the other Promise's state
3. Resolving never nests Promises (unwraps them)
4. `reject()` always rejects, regardless of argument type
5. This behavior is critical for Promise chaining to work correctly

# Construction / Recognition

```js
// Resolving with a non-Promise value -> fulfillment
new Promise((resolve) => resolve(42))
  .then(v => console.log(v)); // 42

// Resolving with a Promise -> adopts state
new Promise((resolve) => resolve(Promise.reject('err')))
  .catch(e => console.log(e)); // 'err'
```

# Context & Application

This distinction is essential for understanding Promise chaining, `return` in `.then()` callbacks, and `return` in async functions. It explains why returning a Promise from `.then()` does not create nested Promises.

# Examples

From the source:
- If `x` is a non-Promise value: `p` is fulfilled with `x`
- If `x` is a Promise: "p adopts the state of x"
  - While x is pending, p is pending
  - If and when x is fulfilled, p is fulfilled
  - If and when x is rejected, p is rejected

(Ch. 43, Section 43.1.4.2, lines 273-289)

# Relationships

## Builds Upon
- **Promise** -- resolve/fulfill are operations on Promises
- **Promise states** -- resolve determines which state the Promise enters

## Enables
- **Promise chaining** -- chaining works because `.then()` resolves (not just fulfills) its return Promise

# Common Errors

- **Error**: Assuming `resolve()` always fulfills
  **Correction**: `resolve(rejectedPromise)` results in a rejected Promise

# Common Confusions

- **Confusion**: "Resolved" means "fulfilled"
  **Clarification**: Resolved means the Promise's fate is determined; it may be fulfilled, rejected, or still pending (if resolved with a pending Promise)

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.4.2, lines 273-289.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit detailed explanation
- Cross-reference status: verified
