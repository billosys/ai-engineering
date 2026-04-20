---
# === CORE IDENTIFICATION ===
concept: Fulfillment Reaction
slug: fulfillment-reaction

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
section: "19.2 Version 1: Stand-alone Promise"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "onFulfilled callback"
  - "fulfillment handler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-state
  - fulfillment-value
extends: []
related:
  - rejection-reaction
  - then-method
contrasts_with:
  - rejection-reaction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a fulfillment reaction from a rejection reaction?"
---

# Quick Definition

A fulfillment reaction is the callback function passed as the first argument to `.then()`, invoked when the Promise is fulfilled, receiving the fulfillment value as its argument.

# Core Definition

From "Deep JavaScript" (Ch 19.2): "If a Promise is resolved, the provided value is passed on to the *fulfillment reactions* (first arguments of `.then()`)." In the ToyPromise implementation, fulfillment reactions are stored in `this._fulfillmentTasks` and executed asynchronously when the Promise is fulfilled.

# Prerequisites

- **Promise** — Reactions are registered on Promise objects
- **Promise state** — The fulfilled state triggers fulfillment reactions
- **Fulfillment value** — Passed as the argument to the reaction

# Key Properties

1. First argument of `.then(onFulfilled, onRejected)`
2. Receives the fulfillment value as its parameter
3. Its return value resolves the Promise returned by `.then()` (in chaining)
4. Optional -- if omitted, the fulfillment value passes through to the next `.then()`

# Construction / Recognition

## To Construct/Create:
1. Pass a function as the first argument to `.then()`

## To Identify/Recognize:
1. The first callback parameter in `.then(onFulfilled, onRejected)`

# Context & Application

Fulfillment reactions are the primary way to process successful async results. Each step in a Promise chain typically has a fulfillment reaction that transforms the value for the next step.

# Examples

**Example 1** (Ch 19):
```js
tp1.then((value) => {       // This arrow function is the fulfillment reaction
  assert.equal(value, 'abc');
});
```

# Relationships

## Builds Upon
- **Promise state** — Only invoked when the Promise is fulfilled

## Enables
- **Promise chaining** — Return values from fulfillment reactions drive the chain forward

## Contrasts With
- **Rejection reaction** — Handles the rejected state; receives the rejection value

# Common Errors

- **Error**: Assuming the fulfillment reaction is called synchronously
  **Correction**: Reactions are always scheduled asynchronously via the task queue

# Common Confusions

- **Confusion**: If a fulfillment reaction throws, the error is lost
  **Clarification**: If a fulfillment reaction throws, the Promise returned by `.then()` is rejected with that error (Version 4)

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.2, lines 8437+.

# Verification Notes

- Definition source: direct from source text and Figure 12
- Confidence rationale: Explicitly named and described in source
- Cross-reference status: verified
