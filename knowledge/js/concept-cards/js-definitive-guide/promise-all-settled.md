---
concept: Promise.allSettled()
slug: promise-all-settled
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 378
section: "13.2.5 Promises in Parallel"
extraction_confidence: high
aliases: []
prerequisites:
  - promise-all
extends: []
related:
  - promise-any
  - promise-race
contrasts_with:
  - promise-all
answers_questions:
  - "How does `Promise.all()` relate to `Promise.race()`?"
---

# Quick Definition

An ES2020 static method that takes an array of Promises and returns a Promise that always fulfills (never rejects) with an array of result objects describing each Promise's outcome as either `{status: "fulfilled", value}` or `{status: "rejected", reason}`.

# Core Definition

"Promise.allSettled() never rejects the returned Promise, and it does not fulfill that Promise until all of the input Promises have settled" (p. 378). Each result object has a `status` property ("fulfilled" or "rejected") plus either a `value` or `reason` property.

# Prerequisites

- **promise-all** — allSettled() is a variant of all() that handles rejections differently

# Key Properties

1. Never rejects — always fulfills with an array of status objects
2. Waits for all input Promises to settle (not just the first rejection)
3. Result objects: `{status: "fulfilled", value: ...}` or `{status: "rejected", reason: ...}`
4. Introduced in ES2020

# Construction / Recognition

```js
Promise.allSettled([Promise.resolve(1), Promise.reject(2), 3]).then(results => {
    results[0]  // => { status: "fulfilled", value: 1 }
    results[1]  // => { status: "rejected", reason: 2 }
    results[2]  // => { status: "fulfilled", value: 3 }
});
```

# Context & Application

Used when you want to attempt multiple operations and handle each result individually, regardless of whether some fail. Ideal for batch operations where partial success is acceptable.

# Examples

From the source text (p. 378): Three Promises — one resolved, one rejected, one non-Promise value — all produce status objects in the results array.

# Relationships

## Builds Upon
- **Promise.all()** — allSettled() is the "never reject" variant

## Contrasts With
- **Promise.all()** — all() rejects on first failure; allSettled() always fulfills after all settle

# Common Errors

- **Error**: Checking `results[i].value` without first checking `results[i].status`.
  **Correction**: Always check `status` first. Rejected results have `reason` instead of `value`.

# Common Confusions

- **Confusion**: Thinking allSettled() is just all() with error swallowing.
  **Clarification**: allSettled() provides structured result objects with explicit status, not just values. It gives complete information about each Promise's outcome.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.5, page 378.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
