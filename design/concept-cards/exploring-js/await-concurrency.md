---
concept: Concurrency with Await
slug: await-concurrency
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.7 Concurrency and await"
extraction_confidence: high
aliases:
  - sequential vs concurrent await
prerequisites:
  - async-function
  - await-operator
  - promise-all
extends: []
related:
  - promise-concurrency
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
---

# Quick Definition

Sequential `await` statements execute operations one after another; to run operations concurrently, start them before awaiting, or use `Promise.all()` to await multiple operations that were started simultaneously.

# Core Definition

"Exploring JavaScript" Ch. 44: "If we prefix the invocations of multiple Promise-based functions with await, then those functions are executed sequentially." For concurrent execution: "If we want to run multiple Promise-based functions concurrently, we can use the utility method Promise.all()." The key insight is that "what counts is when we start a Promise-based computation; not how we process its result."

# Prerequisites

- **Async function** -- context for `await` usage
- **Await operator** -- mechanism for pausing
- **Promise.all()** -- tool for concurrent awaiting

# Key Properties

1. Sequential: `await f1(); await f2();` -- f2 starts only after f1 completes
2. Concurrent via `Promise.all()`: `await Promise.all([f1(), f2()])`
3. Concurrent via separate starts: `const p1 = f1(); const p2 = f2(); await p1; await p2;`
4. Options 2 and 3 produce the same output ordering

# Construction / Recognition

Sequential:
```js
const result1 = await returnAfterPause('first');
const result2 = await returnAfterPause('second');
// Output: START first, END first, START second, END second
```

Concurrent:
```js
const result = await Promise.all([
  returnAfterPause('first'),
  returnAfterPause('second'),
]);
// Output: START first, START second, END first, END second
```

(Ch. 44, Section 44.7, lines 764-841)

# Context & Application

Essential for writing performant async code. Independent operations should use `Promise.all()` for concurrency.

# Examples

See construction examples above. (Ch. 44, Section 44.7.1-44.7.2, lines 764-841)

# Relationships

## Builds Upon
- **Await operator** -- sequential vs concurrent use of await
- **Promise.all()** -- enables concurrent awaiting

## Related
- **Promise concurrency** -- same concept from the Promise perspective

# Common Errors

- **Error**: Awaiting each operation sequentially when they are independent
  **Correction**: Use `Promise.all()` to run independent operations concurrently

# Common Confusions

- **Confusion**: Separate `await` statements are always sequential
  **Clarification**: If operations are started before awaiting (stored in variables), they run concurrently

# Source Reference

Chapter 44: Async functions, Section 44.7, lines 739-841.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with clear examples
- Cross-reference status: verified against Ch. 43.6
