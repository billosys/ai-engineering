---
concept: Promise.race()
slug: promise-race
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.5.3 Promise.race()"
extraction_confidence: high
aliases: []
prerequisites:
  - promise
  - promise-combinator-functions
extends: []
related:
  - promise-any
contrasts_with:
  - promise-all
  - promise-any
answers_questions:
  - "What distinguishes Promise.all() from Promise.race() from Promise.any()?"
---

# Quick Definition

`Promise.race()` returns a Promise that is settled as soon as the first input Promise is settled, adopting that Promise's settlement value -- whether fulfillment or rejection.

# Core Definition

"Exploring JavaScript" Ch. 43: `Promise.race<T>(promises: Iterable<Promise<T>>): Promise<T>`. "Promise.race() returns a Promise q which is settled as soon as the first Promise p among promises is settled. q has the same settlement value as p." Introduced in ES6. Short-circuits on first settlement. `Promise.race([])` is never settled.

# Prerequisites

- **Promise** -- operates on Promises
- **Promise combinator functions** -- one of the four combinators

# Key Properties

1. Introduced in ES6
2. Settles with the first settled input Promise (fulfillment OR rejection)
3. Short-circuits immediately on first settlement
4. `Promise.race([])` produces a never-settled Promise
5. Primary use case: implementing timeouts

# Construction / Recognition

```js
const promises = [
  new Promise((resolve, reject) =>
    setTimeout(() => resolve('result'), 100)),
  new Promise((resolve, reject) =>
    setTimeout(() => reject('ERROR'), 200)),
];
Promise.race(promises)
  .then(result => assert.equal(result, 'result'));
```

(Ch. 43, Section 43.5.3, lines 1511-1522)

# Context & Application

Primarily used for timeout patterns: race an async operation against a timer that rejects after a deadline.

# Examples

Timeout pattern:
```js
function timeout(timeoutInMs, promise) {
  return Promise.race([
    promise,
    rejectAfter(timeoutInMs, new Error('Operation timed out')),
  ]);
}
```

(Ch. 43, Section 43.5.3.1, lines 1588-1595)

# Relationships

## Builds Upon
- **Promise** -- operates on Promises

## Related
- **Promise.any()** -- similar but only cares about fulfillments

## Contrasts With
- **Promise.all()** -- `.all()` waits for all; `.race()` settles on first
- **Promise.any()** -- `.any()` ignores rejections until all reject; `.race()` settles on any settlement

# Common Errors

- **Error**: Thinking `Promise.race()` cancels losing Promises
  **Correction**: Losing Promises continue running; only their settlements are ignored

# Common Confusions

- **Confusion**: `Promise.race()` and `Promise.any()` are the same
  **Clarification**: `.race()` is interested in settlements (any); `.any()` is interested in fulfillments only

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.5.3, lines 1492-1659.

# Verification Notes

- Definition source: direct from source text with type signature
- Confidence rationale: explicit definition with timeout example
- Cross-reference status: verified
