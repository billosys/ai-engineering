---
concept: Promise.any()
slug: promise-any
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.5.4 Promise.any()"
extraction_confidence: high
aliases: []
prerequisites:
  - promise
  - promise-combinator-functions
extends: []
related:
  - promise-all
  - aggregate-error
contrasts_with:
  - promise-race
  - promise-all
answers_questions:
  - "What distinguishes Promise.all() from Promise.race() from Promise.any()?"
---

# Quick Definition

`Promise.any()` (ES2021) returns a Promise that fulfills with the first fulfilled input Promise's value. If all input Promises reject, it rejects with an `AggregateError` containing all rejection reasons.

# Core Definition

"Exploring JavaScript" Ch. 43: "If and when the first Promise is fulfilled, p is resolved with that Promise. If all Promises are rejected, p is rejected with an instance of AggregateError that contains all rejection values." It is the inverse of `Promise.all()`: "Promise.all() is interested in all fulfillments... Promise.any() is interested in the first fulfillment."

# Prerequisites

- **Promise** -- operates on Promises
- **Promise combinator functions** -- one of the four combinators

# Key Properties

1. Introduced in ES2021
2. Fulfills with the FIRST fulfilled input Promise
3. Only rejects when ALL input Promises reject
4. Rejection value is an `AggregateError` with `.errors` array
5. Short-circuits on first fulfillment
6. Use case: trying multiple approaches and using the fastest success

# Construction / Recognition

```js
const promises = [
  Promise.reject('ERROR A'),
  Promise.reject('ERROR B'),
  Promise.resolve('result'),
];
Promise.any(promises)
  .then(result => assert.equal(result, 'result'));
```

(Ch. 43, Section 43.5.4.2, lines 1717-1728)

# Context & Application

Used when trying multiple sources and wanting the first success: downloading from multiple mirrors, trying primary then fallback services, or racing competing implementations.

# Examples

Downloading from fastest source:
```js
const resource = await Promise.any([
  fetch('http://example.com/first.txt').then(r => r.text()),
  fetch('http://example.com/second.txt').then(r => r.text()),
]);
```

(Ch. 43, Section 43.5.4.5, lines 1790-1796)

# Relationships

## Builds Upon
- **Promise** -- operates on Promises

## Related
- **AggregateError** -- rejection value type when all reject
- **Promise.all()** -- inverse relationship

## Contrasts With
- **Promise.race()** -- `.race()` settles on any settlement; `.any()` fulfills on first fulfillment
- **Promise.all()** -- `.all()` needs all fulfillments; `.any()` needs just one

# Common Errors

- **Error**: Expecting `Promise.any()` to reject on the first rejection
  **Correction**: It only rejects when ALL Promises reject; individual rejections are ignored

# Common Confusions

- **Confusion**: `Promise.any()` and `Promise.race()` behave the same
  **Clarification**: `.race()` is interested in settlements; `.any()` is interested in fulfillments only

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.5.4, lines 1661-1826.

# Verification Notes

- Definition source: direct from source text with type signature
- Confidence rationale: explicit definition with comparison to other combinators
- Cross-reference status: verified
