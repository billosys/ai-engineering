---
concept: yield Operator
slug: yield-operator
category: iteration
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous generators (advanced)"
chapter_number: 33
pdf_page: null
section: "33.1.2 yield pauses a generator function"
extraction_confidence: high
aliases:
  - "yield"
  - "yield keyword"
prerequisites:
  - generator-function
extends: []
related:
  - yield-star-operator
  - iterator-result
contrasts_with: []
answers_questions:
  - "What is a generator function?"
  - "What is needed to understand generator functions?"
---

# Quick Definition

The `yield` operator pauses a generator function and returns a value to the caller via the iterator's `.next()` method; execution resumes from the same point on the next `.next()` call.

# Core Definition

`yield` does more than add values to iterators -- it also pauses and exits the generator function. Like `return`, a `yield` exits the body and returns a value (to/via `.next()`). Unlike `return`, if we repeat the invocation (of `.next()`), execution resumes directly after the `yield`. This pause-resume mechanism enables lazy, on-demand value production.

# Prerequisites

- **generator-function** -- yield only works inside generators

# Key Properties

1. Introduced in ES2015 (ES6)
2. Pauses generator execution and returns `{ value, done: false }`
3. Execution resumes after yield on next `.next()` call
4. Can be used inside loops (but not inside callbacks)
5. When the generator body completes, `.next()` returns `{ value: undefined, done: true }`
6. Enables lazy evaluation and coroutine-like behavior

# Construction / Recognition

```js
function* genFunc() {
  yield 'a';   // pause here, return 'a'
  yield 'b';   // pause here, return 'b'
  // function ends, done: true
}
```

# Context & Application

`yield` enables generators to produce values on demand, which is essential for lazy sequences, infinite iterators, and processing pipelines where computing all values upfront would be wasteful or impossible.

# Examples

```js
let location = 0;
function* genFunc2() {
  location = 1; yield 'a';
  location = 2; yield 'b';
  location = 3;
}

const iter = genFunc2();
// location === 0 (paused before body)
iter.next(); // { value: 'a', done: false }, location === 1
iter.next(); // { value: 'b', done: false }, location === 2
iter.next(); // { value: undefined, done: true }, location === 3
```

(Chapter 33, Section 33.1.2, lines 134-217)

# Relationships

## Builds Upon
- **generator-function** -- yield only works inside generators

## Enables
- Lazy value production
- Incremental data processing

## Related
- **yield-star-operator** -- delegates yielding to another generator/iterable
- **iterator-result** -- yield produces IteratorResult objects

## Contrasts With
- None

# Common Errors

- **Error**: Using `yield` inside a callback passed to `.forEach()` or `.map()`.
  **Correction**: `yield` can only be used directly inside generators, not in nested callbacks. Use a for-of loop instead.

# Common Confusions

- **Confusion**: `yield` immediately runs all remaining generator code.
  **Clarification**: `yield` pauses execution. Only the next `.next()` call resumes it up to the next `yield` or the end.

# Source Reference

Chapter 33: Synchronous generators (advanced), Section 33.1.2, lines 134-217.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated with step-by-step execution
- Cross-reference status: verified
