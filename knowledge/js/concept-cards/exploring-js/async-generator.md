---
concept: Async Generator
slug: async-generator
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Asynchronous iteration"
chapter_number: 45
pdf_page: null
section: "45.2 Asynchronous generators"
extraction_confidence: high
aliases:
  - async generator function
  - "async function*"
prerequisites:
  - async-function
  - async-iteration-protocol
  - generator-function
extends:
  - generator-function
  - async-function
related:
  - for-await-of
contrasts_with:
  - generator-function
answers_questions:
  - "How do synchronous and asynchronous iteration protocols differ?"
---

# Quick Definition

An async generator is a function declared with `async function*` that combines async function capabilities (using `await` and `for-await-of` for input) with generator capabilities (using `yield` and `yield*` for output), producing an asynchronous iterable.

# Core Definition

"Exploring JavaScript" Ch. 45: "An asynchronous generator is two things at the same time: An async function (input): We can use await and for-await-of to retrieve data. A generator that returns an asynchronous iterable (output): We can use yield and yield* to produce data." The input can be synchronous or asynchronous; the output is always an asynchronous iterator.

# Prerequisites

- **Async function** -- async generators can `await`
- **Async iteration protocol** -- async generators produce async iterables
- **Generator function** -- async generators extend generators

# Key Properties

1. Declared with `async function*`
2. Input: can `await` Promises and `for-await-of` async iterables
3. Output: `yield` and `yield*` produce async iterable values
4. Return value is an asynchronous iterator (also iterable)
5. Combines both `await` and `yield` in a single function

# Construction / Recognition

```js
async function* asyncGen(somePromise, someAsyncIterable) {
  const x = await somePromise;         // async input
  for await (const y of someAsyncIterable) {  // async input
    yield someValue;                    // async output
    yield* otherAsyncGen();             // delegate to another async gen
  }
}
```

(Ch. 45, Section 45.2, lines 287-298)

# Context & Application

Async generators are ideal for transforming async data streams: converting between formats, filtering, mapping, and composing stream transformations.

# Examples

Creating an async iterable:
```js
async function* yield123() {
  for (let i = 1; i <= 3; i++) {
    yield i;
  }
}
```

Transforming an async iterable:
```js
async function* timesTwo(asyncNumbers) {
  for await (const x of asyncNumbers) {
    yield x * 2;
  }
}
```

(Ch. 45, Section 45.2.1, 45.2.4, lines 310-410)

# Relationships

## Builds Upon
- **Async function** -- provides `await` capability
- **Generator function** -- provides `yield` capability
- **Async iteration protocol** -- output conforms to this protocol

## Enables
- **Stream transformation** -- composable async data processing

## Contrasts With
- **Generator function** -- sync generators yield sync values; async generators yield values wrapped in Promises

# Common Errors

- **Error**: Forgetting `async` before `function*`
  **Correction**: Must use `async function*` to create an async generator

# Common Confusions

- **Confusion**: Async generators return Arrays
  **Clarification**: They return async iterables that must be consumed with `for-await-of` or converted with a helper function

# Source Reference

Chapter 45: Asynchronous iteration, Section 45.2, lines 259-498.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with dual nature explained
- Cross-reference status: verified
