---
# === CORE IDENTIFICATION ===
concept: Promise.any
slug: promise-any

# === CLASSIFICATION ===
category: asynchronous-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Asynchronous Programming"
chapter_number: 11
pdf_page: null
section: "Promises"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - Promise.any()

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
extends:
  - promise
related:
  - promise-all
contrasts_with:
  - promise-all

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a promise?"
---

# Quick Definition
`Promise.any` takes an array of promises and resolves as soon as any one of them succeeds, or rejects if all of them fail.

# Core Definition
While the source primarily covers `Promise.all`, the concept of racing promises is demonstrated through patterns where the first settling promise wins. `Promise.any` resolves with the value of the first fulfilled promise, or rejects with an `AggregateError` if all promises reject.

# Prerequisites
- **Promise**: Understanding individual promise behavior

# Key Properties
1. Resolves as soon as any single promise in the array resolves
2. Rejects only if all promises reject
3. Useful for redundant async operations where any success is sufficient

# Construction / Recognition
Related pattern from the source (racing a promise against a timeout):
```javascript
function withTimeout(promise, time) {
  return new Promise((resolve, reject) => {
    promise.then(resolve, reject);
    setTimeout(() => reject("Timed out"), time);
  });
}
```
(lines 534-539)

# Context & Application
Used when you want the fastest result from multiple sources, or need any one of several fallback operations to succeed.

# Examples
The `withTimeout` function demonstrates a race-like pattern: "This makes use of the fact that a promise can be resolved or rejected only once. If the promise given as its argument resolves or rejects first, that result will be the result of the promise returned by `withTimeout`." (lines 543-548)

# Relationships
## Builds Upon
- Promise concept
## Enables
- First-success-wins patterns
## Related
- `Promise.all` (waits for all to succeed)
## Contrasts With
- `Promise.all` (which requires all to succeed)

# Common Errors
- **Error**: Confusing `Promise.any` with `Promise.race` (which resolves on first settlement, including rejection)
  **Correction**: `Promise.any` ignores rejections until all promises have rejected

# Common Confusions
- **Confusion**: `Promise.any` is the same as `Promise.race`
  **Clarification**: `Promise.race` resolves or rejects with the first settled promise; `Promise.any` specifically waits for the first *fulfilled* promise

# Source Reference
Chapter 11: Asynchronous Programming, Section "Breaking In" (related pattern), lines 534-548 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: inferred from related patterns in source
- Confidence rationale: Medium -- the concept is implied through the timeout racing pattern, not directly named
- Cross-reference status: unverified
