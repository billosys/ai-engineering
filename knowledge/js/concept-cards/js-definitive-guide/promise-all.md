---
concept: Promise.all()
slug: promise-all
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 377
section: "13.2.5 Promises in Parallel"
extraction_confidence: high
aliases: []
prerequisites:
  - promise-object
extends: []
related:
  - promise-all-settled
  - promise-race
  - promise-any
contrasts_with:
  - promise-race
  - promise-all-settled
answers_questions:
  - "How does `Promise.all()` relate to `Promise.race()`?"
---

# Quick Definition

A static method that takes an array of Promises and returns a new Promise that fulfills with an array of all fulfillment values when all input Promises fulfill, or rejects immediately when any input Promise rejects.

# Core Definition

"Promise.all() takes an array of Promise objects as its input and returns a Promise. The returned Promise will be rejected if any of the input Promises are rejected. Otherwise, it will be fulfilled with an array of the fulfillment values of each of the input Promises" (p. 377). Non-Promise values in the array are treated as already-fulfilled Promises.

# Prerequisites

- **promise-object** — Understanding Promise states and fulfillment

# Key Properties

1. Input: array of Promises (and/or non-Promise values)
2. Fulfills with array of all values (in input order) when all fulfill
3. Rejects immediately on first rejection (other Promises keep running but are ignored)
4. Non-Promise array elements treated as already-fulfilled
5. Empty array input fulfills immediately with empty array

# Construction / Recognition

```js
const urls = [url1, url2, url3];
let promises = urls.map(url => fetch(url).then(r => r.text()));
Promise.all(promises)
    .then(bodies => { /* array of strings */ })
    .catch(e => console.error(e));
```

# Context & Application

Used when multiple independent async operations should run concurrently and you need all results. Common for parallel data fetching.

# Examples

From the source text (p. 377-378): Fetching multiple URLs in parallel: map URLs to fetch Promises, pass to `Promise.all()`, receive array of response bodies.

# Relationships

## Builds Upon
- **Promise Object** — all() operates on Promises

## Related
- **Promise.allSettled()** — Waits for all without short-circuiting on rejection
- **Promise.race()** — Returns first settled Promise
- **Promise.any()** — Returns first fulfilled Promise

## Contrasts With
- **Promise.race()** — all() waits for all Promises; race() returns on the first settlement
- **Promise.allSettled()** — all() rejects on first failure; allSettled() never rejects

# Common Errors

- **Error**: Expecting the remaining Promises to be cancelled when one rejects.
  **Correction**: Promise.all() cannot cancel Promises. The other operations continue running; their results are just ignored.

# Common Confusions

- **Confusion**: Thinking Promise.all() runs Promises sequentially.
  **Clarification**: Promise.all() does not control when Promises start. The Promises run concurrently — all() just waits for them all.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.5, pages 377-378.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
