---
# === CORE IDENTIFICATION ===
concept: Promise Reaction Passthrough
slug: promise-reaction-passthrough

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
section: "19.5 Omitting reactions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "reaction omission"
  - "value/error passthrough"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-chaining
  - fulfillment-reaction
  - rejection-reaction
extends:
  - promise-chaining
related:
  - catch-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Promise flattening relate to .then() chaining?"
---

# Quick Definition

Promise reaction passthrough is the behavior where omitting a fulfillment or rejection reaction in `.then()` causes the value or error to pass through unchanged to the next Promise in the chain.

# Core Definition

From "Deep JavaScript" (Ch 19.5-19.6): "The new version also forwards fulfillments if we omit a fulfillment reaction and it forwards rejections if we omit a rejection reaction." In the implementation: "If `onFulfilled` is missing, we use the fulfillment value of the current Promise to resolve `resultPromise`." Similarly, "If `onRejected` is missing, we use the rejection value of the current Promise to reject `resultPromise`."

# Prerequisites

- **Promise** — Passthrough occurs on Promise objects
- **Promise chaining** — Passthrough is a chaining behavior
- **Fulfillment reaction** — Understanding what it means for one to be absent
- **Rejection reaction** — Understanding what it means for one to be absent

# Key Properties

1. Missing `onFulfilled`: fulfillment value passes through to next `.then()`
2. Missing `onRejected`: rejection value propagates to next `.then()` or `.catch()`
3. Enables error handling at the end of a chain
4. Enables skipping `.catch()` when the Promise fulfills

# Construction / Recognition

## To Construct/Create:
1. Call `.then(onFulfilled)` without a rejection handler (error passes through)
2. Call `.catch(onRejected)` which is `.then(null, onRejected)` (fulfillment passes through)

## To Identify/Recognize:
1. A `.then()` call with only one callback (the other is `null`/`undefined`)

# Context & Application

Passthrough enables the common pattern of multiple `.then()` calls followed by a single `.catch()` at the end: rejections skip unfulfilled `.then()` handlers and reach the `.catch()`.

# Examples

**Example 1** (Ch 19): Rejection passthrough:
```js
someAsyncFunction()
  .then(fulfillmentReaction1)
  .then(fulfillmentReaction2)
  .catch(rejectionReaction);
// rejectionReaction handles rejections from all three
```

**Example 2** (Ch 19): Fulfillment passthrough:
```js
someAsyncFunction()
  .catch(rejectionReaction)
  .then(fulfillmentReaction);
// If someAsyncFunction() fulfills, .catch() is skipped
```

# Relationships

## Builds Upon
- **Promise chaining** — Passthrough is a specific chaining behavior

## Enables
- **Centralized error handling** — Errors propagate to a final `.catch()`
- **Error recovery** — `.catch()` can fix errors without blocking subsequent fulfillment handlers

# Common Errors

- **Error**: Assuming a missing `onRejected` silently swallows the rejection
  **Correction**: The rejection passes through to the next handler in the chain

# Common Confusions

- **Confusion**: `.catch()` blocks fulfillment values from reaching subsequent `.then()` calls
  **Clarification**: If the Promise is fulfilled, `.catch()` is skipped entirely (fulfillment passes through)

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.5-19.6, lines 8437+.

# Verification Notes

- Definition source: direct from source text and implementation
- Confidence rationale: Explicitly described with examples
- Cross-reference status: verified
