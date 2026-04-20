---
concept: Asynchronous Iterators
slug: async-iterators
category: async-programming
subcategory: async-iteration
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 388
section: "13.4.2 Asynchronous Iterators"
extraction_confidence: high
aliases:
  - "Symbol.asyncIterator"
  - "async iteration protocol"
prerequisites:
  - iterator-protocol
  - promise-object
  - async-functions
extends:
  - iterator-protocol
related:
  - for-await-loop
  - async-generators
contrasts_with:
  - iterator-protocol
answers_questions:
  - "What must I understand before learning about async iteration?"
---

# Quick Definition

An extension of the iterator protocol for asynchronous data sources, where objects implement `Symbol.asyncIterator` to return iterators whose `next()` method returns Promises that resolve to iteration result objects.

# Core Definition

"An asynchronously iterable object implements a method with the symbolic name Symbol.asyncIterator instead of Symbol.iterator. Second, the next() method of an asynchronous iterator returns a Promise that resolves to an iterator result object instead of returning an iterator result object directly" (p. 389). Both the value and done properties are asynchronous.

# Prerequisites

- **iterator-protocol** — Async iterators extend the synchronous protocol
- **promise-object** — Async iterators produce Promises
- **async-functions** — Needed to consume async iterators

# Key Properties

1. `Symbol.asyncIterator` instead of `Symbol.iterator`
2. `next()` returns a Promise for `{value, done}` (not the result directly)
3. Both value and done can be determined asynchronously
4. Consumed with `for await...of` loops
5. ES2018 feature

# Construction / Recognition

```js
function clock(interval, max=Infinity) {
    return {
        startTime: Date.now(), count: 1,
        async next() {
            if (this.count > max) return { done: true };
            await until(this.startTime + this.count * interval);
            return { value: this.count++ };
        },
        [Symbol.asyncIterator]() { return this; }
    };
}
```

# Context & Application

Represents streams of asynchronous data: Node readable streams, server-sent events, WebSocket messages, or any repeated async event source.

# Examples

From the source text (p. 389-391): The `clock()` function as a manual async iterator with `async next()` method. Node 12 readable streams are asynchronously iterable.

# Relationships

## Builds Upon
- **Iterator Protocol** — Extends the sync protocol with Promises

## Enables
- **for/await Loop** — The primary consumer of async iterators
- **Async Generators** — A simpler way to create async iterators

## Contrasts With
- **Iterator Protocol** — Sync iterators return results directly; async iterators return Promises

# Common Errors

- **Error**: Implementing `Symbol.iterator` instead of `Symbol.asyncIterator` for async data sources.
  **Correction**: For truly asynchronous iteration (where the choice of when to end is async), use `Symbol.asyncIterator`.

# Common Confusions

- **Confusion**: Thinking for/await on an array of Promises creates an async iterator.
  **Clarification**: for/await works with regular iterables (awaiting each value) and async iterables. An array of Promises uses the sync iterator; true async iterators use `Symbol.asyncIterator`.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.4.2, pages 388-391.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
