---
concept: Promise.allSettled()
slug: promise-all-settled
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.5.5 Promise.allSettled()"
extraction_confidence: high
aliases: []
prerequisites:
  - promise
  - promise-combinator-functions
extends: []
related:
  - promise-all
contrasts_with:
  - promise-all
answers_questions:
  - "What distinguishes Promise.all() from Promise.race() from Promise.any()?"
---

# Quick Definition

`Promise.allSettled()` (ES2020) returns a Promise that fulfills with an Array of settlement objects once ALL input Promises are settled, never short-circuiting, providing both fulfillment values and rejection reasons.

# Core Definition

"Exploring JavaScript" Ch. 43: "Promise.allSettled() returns a Promise out. Once all promises are settled, out is fulfilled with an Array." Each element is either `{ status: 'fulfilled', value: v }` or `{ status: 'rejected', reason: r }`. "Unless there is an error when iterating over promises, the output Promise out is never rejected." Introduced in ES2020.

# Prerequisites

- **Promise** -- operates on Promises
- **Promise combinator functions** -- one of the four combinators

# Key Properties

1. Introduced in ES2020
2. Waits for ALL Promises to settle (no short-circuiting)
3. Output Promise is always fulfilled (never rejected unless iteration error)
4. Result Array contains settlement objects with `status`, `value`/`reason`
5. Use case: collecting all results regardless of individual success/failure

# Construction / Recognition

```js
Promise.allSettled([
  Promise.resolve('value'),
  Promise.reject('ERROR'),
])
.then(arr => assert.deepEqual(arr, [
  { status: 'fulfilled', value: 'value' },
  { status: 'rejected',  reason: 'ERROR' },
]));
```

(Ch. 43, Section 43.5.5.1, lines 1896-1906)

# Context & Application

Used when you need results from all operations regardless of individual failures: downloading multiple resources where some may fail, batch operations with partial success.

# Examples

From the source, downloading with error tolerance:
```js
const result = Promise.allSettled(
  urls.map(url => downloadText(url))
);
result.then(arr => {
  // arr contains both successes and failures
});
```

(Ch. 43, Section 43.5.5.2, lines 1934-1953)

# Relationships

## Builds Upon
- **Promise** -- operates on Promises

## Contrasts With
- **Promise.all()** -- `.all()` short-circuits on first rejection; `.allSettled()` never short-circuits

# Common Errors

- **Error**: Expecting `.allSettled()` to reject if any Promise rejects
  **Correction**: It always fulfills; rejections are captured as settlement objects

# Common Confusions

- **Confusion**: The settlement objects have the same shape for fulfillment and rejection
  **Clarification**: Fulfilled: `{ status: 'fulfilled', value }`, Rejected: `{ status: 'rejected', reason }`

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.5.5, lines 1827-2007.

# Verification Notes

- Definition source: direct from source text with type signatures
- Confidence rationale: explicit definition with settlement object types
- Cross-reference status: verified
