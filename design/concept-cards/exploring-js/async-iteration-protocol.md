---
concept: Async Iteration Protocol
slug: async-iteration-protocol
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Asynchronous iteration"
chapter_number: 45
pdf_page: null
section: "45.1.1 Protocol: async iteration"
extraction_confidence: high
aliases:
  - AsyncIterable
  - AsyncIterator
prerequisites:
  - promise
  - async-function
  - iterable-interface
  - iterator-interface
extends:
  - iterable-interface
  - iterator-interface
related:
  - for-await-of-loop
  - async-generator
contrasts_with:
  - iterable-interface
answers_questions:
  - "How do synchronous and asynchronous iteration protocols differ?"
  - "What must I understand before working with async iteration?"
---

# Quick Definition

The async iteration protocol mirrors synchronous iteration but wraps iterator results in Promises: `AsyncIterable` has `[Symbol.asyncIterator]()` returning an `AsyncIterator`, whose `.next()` returns `Promise<IteratorResult<T>>` instead of `IteratorResult<T>`.

# Core Definition

"Exploring JavaScript" Ch. 45 defines the protocol: `interface AsyncIterable<T> { [Symbol.asyncIterator](): AsyncIterator<T>; }` and `interface AsyncIterator<T> { next(): Promise<IteratorResult<T>>; }`. Introduced in ES2018. "The only difference to the synchronous interfaces is the return type of .next()." The whole IteratorResult must be wrapped in a Promise because "when .next() returns a result, it starts an asynchronous computation. Whether or not that computation produces a value or signals the end of the iteration can only be determined after it is finished."

# Prerequisites

- **Promise** -- `.next()` returns Promises
- **Async function** -- async iterables are consumed in async contexts
- **Iterable interface** -- async version of sync iterable
- **Iterator interface** -- async version of sync iterator

# Key Properties

1. Introduced in ES2018
2. `[Symbol.asyncIterator]()` instead of `[Symbol.iterator]()`
3. `.next()` returns `Promise<IteratorResult<T>>` instead of `IteratorResult<T>`
4. Both `.done` and `.value` are inside the Promise (not just `.value`)
5. IteratorResult interface is unchanged: `{ value: T, done: boolean }`

# Construction / Recognition

Sync iteration interfaces:
```ts
interface Iterable<T> { [Symbol.iterator](): Iterator<T>; }
interface Iterator<T> { next(): IteratorResult<T>; }
```

Async iteration interfaces:
```ts
interface AsyncIterable<T> { [Symbol.asyncIterator](): AsyncIterator<T>; }
interface AsyncIterator<T> { next(): Promise<IteratorResult<T>>; }
```

(Ch. 45, Section 45.1.1, lines 70-121)

# Context & Application

Used for iterating over data that arrives asynchronously: streams, paginated API responses, real-time data feeds.

# Examples

```js
const asyncIterable = syncToAsyncIterable(['a', 'b']);
const asyncIterator = asyncIterable[Symbol.asyncIterator]();
assert.deepEqual(await asyncIterator.next(), { value: 'a', done: false });
assert.deepEqual(await asyncIterator.next(), { value: 'b', done: false });
assert.deepEqual(await asyncIterator.next(), { value: undefined, done: true });
```

(Ch. 45, Section 45.1.2, lines 170-184)

# Relationships

## Builds Upon
- **Iterable interface** -- async version of sync iterable
- **Iterator interface** -- async version of sync iterator

## Enables
- **for-await-of loop** -- consumes async iterables
- **Async generator** -- produces async iterables

## Contrasts With
- **Iterable interface** -- sync returns values directly; async wraps in Promises

# Common Errors

- **Error**: Wrapping only `.value` in a Promise instead of the whole IteratorResult
  **Correction**: The Promise must wrap the entire `{ value, done }` object

# Common Confusions

- **Confusion**: Async iteration is just sync iteration with Promise values
  **Clarification**: The entire IteratorResult is wrapped in a Promise, including `.done`, because both value and completion are determined asynchronously

# Source Reference

Chapter 45: Asynchronous iteration, Section 45.1.1, lines 59-121.

# Verification Notes

- Definition source: direct from source text with TypeScript interfaces
- Confidence rationale: explicit protocol definition with rationale
- Cross-reference status: verified
