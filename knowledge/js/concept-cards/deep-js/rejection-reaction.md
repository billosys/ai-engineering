---
# === CORE IDENTIFICATION ===
concept: Rejection Reaction
slug: rejection-reaction

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
  - "onRejected callback"
  - "rejection handler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-state
  - rejection-value
extends: []
related:
  - fulfillment-reaction
  - then-method
  - catch-method
contrasts_with:
  - fulfillment-reaction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a fulfillment reaction from a rejection reaction?"
---

# Quick Definition

A rejection reaction is the callback function passed as the second argument to `.then()` (or the argument to `.catch()`), invoked when the Promise is rejected, receiving the rejection value as its argument.

# Core Definition

From "Deep JavaScript" (Ch 19.2): "If a Promise is rejected, the provided value is passed on to the *rejection reactions* (second arguments of `.then()`)." In the ToyPromise implementation, rejection reactions are stored in `this._rejectionTasks` and executed asynchronously when the Promise is rejected.

# Prerequisites

- **Promise** — Reactions are registered on Promise objects
- **Promise state** — The rejected state triggers rejection reactions
- **Rejection value** — Passed as the argument to the reaction

# Key Properties

1. Second argument of `.then(onFulfilled, onRejected)` or sole argument of `.catch()`
2. Receives the rejection value as its parameter
3. Its return value *resolves* (not rejects) the Promise returned by `.then()` -- the error is considered handled
4. Optional -- if omitted, the rejection propagates to the next `.then()` in the chain

# Construction / Recognition

## To Construct/Create:
1. Pass a function as the second argument to `.then()`
2. Or pass a function to `.catch()`

## To Identify/Recognize:
1. The second callback parameter in `.then(onFulfilled, onRejected)` or the `.catch()` argument

# Context & Application

Rejection reactions handle errors in Promise chains. A key design insight is that if a rejection reaction returns successfully, the chain *recovers* -- the subsequent Promise is fulfilled, not rejected.

# Examples

**Example 1** (Ch 19): Rejection reaction that recovers:
```js
new ToyPromise2()
  .reject('error1')
  .then(null,
    x => {
      assert.equal(x, 'error1');
      return 'result2'; // recovers from error
    })
  .then(x => {
    assert.equal(x, 'result2'); // chain is now fulfilled
  });
```

# Relationships

## Builds Upon
- **Promise state** — Only invoked when the Promise is rejected

## Enables
- **Error recovery** — Return values from rejection reactions resolve (fulfill) the chain

## Contrasts With
- **Fulfillment reaction** — Handles the fulfilled state; receives the fulfillment value

# Common Errors

- **Error**: Assuming a rejection reaction keeps the chain in a rejected state
  **Correction**: If the reaction returns a value, `resultPromise` is *resolved*, not rejected. As the source states: "We are assuming that `onRejected()` fixed whatever problem there was."

# Common Confusions

- **Confusion**: `.catch()` and the second argument of `.then()` behave differently
  **Clarification**: `.catch(rejectionReaction)` is exactly equivalent to `.then(null, rejectionReaction)`

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.2 and 19.6, lines 8437+.

# Verification Notes

- Definition source: direct from source text and Figure 12
- Confidence rationale: Explicitly named and described in source
- Cross-reference status: verified
