---
# === CORE IDENTIFICATION ===
concept: ".then() Method"
slug: then-method

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
section: "19.2.1 Method .then()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Promise.prototype.then()"
  - ".then() handler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-state
  - fulfillment-reaction
  - rejection-reaction
extends: []
related:
  - catch-method
  - promise-chaining
contrasts_with:
  - catch-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Promise flattening relate to .then() chaining?"
  - "What distinguishes a fulfillment reaction from a rejection reaction?"
---

# Quick Definition

The `.then()` method registers fulfillment and rejection reactions on a Promise, and (from Version 2 onward) returns a new Promise enabling chaining.

# Core Definition

From "Deep JavaScript" (Ch 19.2.1): `.then()` handles two cases: "If the Promise is still pending, it queues invocations of `onFulfilled` and `onRejected`. They are to be used later, when the Promise is settled. If the Promise is already fulfilled or rejected, `onFulfilled` or `onRejected` can be invoked right away." From Version 2 onward, `.then()` returns a new Promise that is resolved with whatever value the reaction callback returns.

# Prerequisites

- **Promise** — `.then()` is a method on Promise objects
- **Promise state** — Behavior differs based on current state
- **Fulfillment reaction** — First parameter of `.then()`
- **Rejection reaction** — Second parameter of `.then()`

# Key Properties

1. Accepts two optional callbacks: `onFulfilled` and `onRejected`
2. Reactions are always executed asynchronously (added to the task queue)
3. Returns a new Promise (enabling chaining) from Version 2 onward
4. If a reaction is missing, the value/error passes through to the next `.then()`

# Construction / Recognition

## To Construct/Create:
1. Call `.then(onFulfilled, onRejected)` on any Promise

## To Identify/Recognize:
1. A method call on a Promise that registers callbacks for success and/or failure

# Context & Application

`.then()` is the primary method for consuming Promise results. Its ability to return a new Promise is what enables the entire chaining pattern, and its interaction with Promise flattening is what makes async chains readable.

# Examples

**Example 1** (Ch 19): Basic `.then()` implementation:
```js
then(onFulfilled, onRejected) {
  const fulfillmentTask = () => {
    if (typeof onFulfilled === 'function') {
      onFulfilled(this._promiseResult);
    }
  };
  const rejectionTask = () => {
    if (typeof onRejected === 'function') {
      onRejected(this._promiseResult);
    }
  };
  switch (this._promiseState) {
    case 'pending':
      this._fulfillmentTasks.push(fulfillmentTask);
      this._rejectionTasks.push(rejectionTask);
      break;
    case 'fulfilled':
      addToTaskQueue(fulfillmentTask);
      break;
    case 'rejected':
      addToTaskQueue(rejectionTask);
      break;
  }
}
```

# Relationships

## Builds Upon
- **Promise state** — Determines whether to queue or immediately schedule reactions

## Enables
- **Promise chaining** — By returning a new Promise
- **Promise flattening** — When callbacks return Promises, flattening unwraps them

## Related
- **`.catch()` method** — Shorthand for `.then(null, onRejected)`

## Contrasts With
- **`.catch()` method** — `.then()` handles both fulfillment and rejection; `.catch()` only rejection

# Common Errors

- **Error**: Forgetting that `.then()` callbacks are asynchronous even when the Promise is already settled
  **Correction**: Even settled Promises schedule reactions via `addToTaskQueue`, never synchronously

# Common Confusions

- **Confusion**: `.then()` mutates the original Promise
  **Clarification**: `.then()` returns a *new* Promise; the original is unchanged

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.2.1, lines 8437+.

# Verification Notes

- Definition source: direct from source implementation
- Confidence rationale: Complete implementation shown in source
- Cross-reference status: verified
