---
concept: Promise Concurrency Patterns
slug: promise-concurrency
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.6 Concurrency and Promise.all()"
extraction_confidence: high
aliases:
  - sequential vs concurrent execution
  - fork-join pattern
prerequisites:
  - promise
  - promise-all
extends: []
related:
  - promise-chaining
  - await-concurrency
contrasts_with: []
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

Promise concurrency is determined by when async operations are started, not how their results are handled. Starting operations before combining them with `Promise.all()` runs them concurrently; chaining with `.then()` runs them sequentially.

# Core Definition

"Exploring JavaScript" Ch. 43: "Tip for determining how 'concurrent' asynchronous code is: Focus on when asynchronous operations start, not on how their Promises are handled." `Promise.all()` implements a "fork-join" pattern: "Fork: we are forking two asynchronous computations and executing them concurrently. Join: we are joining these computations into a single 'thread' which is started once all of them are done."

# Prerequisites

- **Promise** -- concurrency involves multiple Promises
- **Promise.all()** -- primary tool for concurrent execution

# Key Properties

1. Concurrency depends on when operations START, not how results are processed
2. `.then()` chaining: sequential (second starts after first completes)
3. `Promise.all()`: concurrent (both start immediately)
4. Fork-join pattern: start multiple operations, combine results
5. Even separate `await` statements can be concurrent if operations started beforehand

# Construction / Recognition

Sequential:
```js
asyncFunc1().then(r1 => asyncFunc2().then(r2 => [r1, r2]));
```

Concurrent:
```js
Promise.all([asyncFunc1(), asyncFunc2()]);
```

(Ch. 43, Section 43.6.1-43.6.2, lines 2043-2115)

# Context & Application

Understanding concurrency patterns is essential for writing performant async code. Independent operations should run concurrently; dependent operations must run sequentially.

# Examples

From the source, both are equally concurrent:
```js
// Using Promise.all
function concurrentAll() {
  return Promise.all([asyncFunc1(), asyncFunc2()]);
}
// Using separate await
function concurrentAwait() {
  const p1 = asyncFunc1();
  const p2 = asyncFunc2();
  return p1.then(r1 => p2.then(r2 => [r1, r2]));
}
```

(Ch. 43, Section 43.6.2, lines 2085-2095)

# Relationships

## Builds Upon
- **Promise.all()** -- primary concurrent execution tool

## Related
- **Await concurrency** -- async/await version of these patterns

# Common Errors

- **Error**: Using `.then()` chains when operations are independent
  **Correction**: Use `Promise.all()` to run independent operations concurrently

# Common Confusions

- **Confusion**: `Promise.all()` makes operations parallel
  **Clarification**: Operations start concurrently; `Promise.all()` just waits for all results

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.6, lines 2041-2141.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit tip with examples
- Cross-reference status: verified against Ch. 44.7
