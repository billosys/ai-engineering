---
# === CORE IDENTIFICATION ===
concept: Promise States
slug: promise-states

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
section: "43.1.4 The three basic states of Promises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Promise lifecycle
  - "pending/fulfilled/rejected"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
extends: []
related:
  - resolving-vs-fulfilling
  - promise-then
  - promise-catch
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Promise?"
  - "What concepts are prerequisite to understanding Promises?"
---

# Quick Definition

A Promise has three states: pending (initial, no result yet), fulfilled (operation succeeded with a value), or rejected (operation failed with an error). Once fulfilled or rejected, a Promise is called "settled" and its state never changes again.

# Core Definition

"Exploring JavaScript" Ch. 43 describes three states: "A Promise is initially in the state 'pending'. It can later transition to either the state 'fulfilled' or the state 'rejected' (but it may never do so). If a Promise is in a final (non-pending) state, it is called settled." The first value received permanently settles the Promise; subsequent values are ignored.

# Prerequisites

- **Promise** -- states are a fundamental property of Promises

# Key Properties

1. **Pending**: initial state, no result yet
2. **Fulfilled**: operation succeeded, Promise holds a fulfillment value
3. **Rejected**: operation failed, Promise holds a rejection reason (usually an Error)
4. **Settled**: either fulfilled or rejected -- a final state
5. A Promise can only transition once from pending to settled
6. Some Promises are never settled (e.g., `new Promise(() => {})`)

# Construction / Recognition

```js
// A Promise that is never settled
new Promise(() => {})

// A fulfilled Promise
Promise.resolve('value')

// A rejected Promise
Promise.reject(new Error('reason'))
```

(Ch. 43, Section 43.1.4, lines 241-271)

# Context & Application

Understanding Promise states is essential for debugging async code, understanding `.then()` vs `.catch()` behavior, and using Promise combinators correctly.

# Examples

From the source:
```js
// Never-settled Promise
new Promise(() => {}) // stays pending forever
```

(Ch. 43, Section 43.1.4.1, lines 265-271)

# Relationships

## Builds Upon
- **Promise** -- states are the core lifecycle of a Promise

## Enables
- **Promise.then()** -- triggered by fulfillment
- **Promise.catch()** -- triggered by rejection
- **Promise combinator functions** -- behavior depends on input Promise states

## Related
- **Resolving vs fulfilling** -- resolving determines fate; fulfilling is one outcome

# Common Errors

- **Error**: Expecting a Promise to change state after being settled
  **Correction**: A settled Promise's state and value are permanent

# Common Confusions

- **Confusion**: "Resolved" and "fulfilled" mean the same thing
  **Clarification**: Resolving may lead to fulfillment or rejection (if resolved with a rejected Promise); fulfilling specifically means success

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.4, lines 241-289.

# Verification Notes

- Definition source: direct from source text with figure reference
- Confidence rationale: explicit definition with state diagram
- Cross-reference status: verified
