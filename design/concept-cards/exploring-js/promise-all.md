---
concept: Promise.all()
slug: promise-all
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.5.2 Promise.all()"
extraction_confidence: high
aliases: []
prerequisites:
  - promise
  - promise-combinator-functions
extends: []
related:
  - promise-any
  - promise-all-settled
contrasts_with:
  - promise-race
  - promise-any
answers_questions:
  - "What distinguishes Promise.all() from Promise.race() from Promise.any()?"
---

# Quick Definition

`Promise.all()` takes an iterable of Promises and returns a single Promise that is fulfilled with an Array of all fulfillment values when all input Promises are fulfilled, or rejected with the first rejection value if any input Promise is rejected.

# Core Definition

"Exploring JavaScript" Ch. 43: `Promise.all<T>(promises: Iterable<Promise<T>>): Promise<Array<T>>`. "Promise.all() returns a Promise which is: Fulfilled if all promises are fulfilled. Then its fulfillment value is an Array with the fulfillment values of promises. Rejected if at least one Promise is rejected. Then its rejection value is the rejection value of that Promise." Introduced in ES6. Short-circuits on first rejection.

# Prerequisites

- **Promise** -- operates on Promises
- **Promise combinator functions** -- one of the four combinators

# Key Properties

1. Introduced in ES6
2. Fulfills with an Array of values when ALL Promises fulfill
3. Rejects with the first rejection reason if ANY Promise rejects (short-circuits)
4. Preserves order: results Array matches input order
5. `Promise.all([])` immediately fulfills with `[]`
6. Implements fork-join concurrency pattern

# Construction / Recognition

```js
const promises = [
  Promise.resolve('result a'),
  Promise.resolve('result b'),
  Promise.resolve('result c'),
];
Promise.all(promises)
  .then(arr => assert.deepEqual(arr, ['result a', 'result b', 'result c']));
```

(Ch. 43, Section 43.5.2, lines 1324-1335)

# Context & Application

Most common combinator. Used for concurrent execution of independent async operations when all results are needed. Combined with `.map()` for parallel processing of arrays.

# Examples

Async `.map()` via `Promise.all()`:
```js
function timesTwoAsync(x) {
  return new Promise(resolve => resolve(x * 2));
}
const arr = [1, 2, 3];
const promiseArr = arr.map(timesTwoAsync);
Promise.all(promiseArr)
  .then(result => assert.deepEqual(result, [2, 4, 6]));
```

(Ch. 43, Section 43.5.2.1, lines 1386-1397)

# Relationships

## Builds Upon
- **Promise** -- operates on Promises

## Related
- **Promise.allSettled()** -- similar but doesn't short-circuit on rejection

## Contrasts With
- **Promise.race()** -- `.race()` settles on first settlement; `.all()` waits for all
- **Promise.any()** -- `.any()` fulfills on first fulfillment; `.all()` needs all fulfillments

# Common Errors

- **Error**: Expecting `Promise.all()` to continue when one Promise rejects
  **Correction**: Use `Promise.allSettled()` if you need all results regardless of rejection

# Common Confusions

- **Confusion**: `Promise.all()` runs operations sequentially
  **Clarification**: Operations run concurrently; `Promise.all()` only waits for their results

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.5.2, lines 1303-1486.

# Verification Notes

- Definition source: direct from source text with type signature
- Confidence rationale: explicit definition with multiple examples
- Cross-reference status: verified
