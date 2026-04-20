---
concept: Async Generators
slug: async-generators
category: async-programming
subcategory: async-iteration
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 389
section: "13.4.3 Asynchronous Generators"
extraction_confidence: high
aliases:
  - "async function*"
prerequisites:
  - generator-functions
  - async-functions
  - async-iterators
extends: []
related:
  - for-await-loop
contrasts_with: []
answers_questions:
  - "What must I understand before learning about async iteration?"
---

# Quick Definition

Functions declared with `async function*` that combine async and generator features — they can use both `await` (to consume Promises) and `yield` (to produce async iteration values), with yielded values automatically wrapped in Promises.

# Core Definition

"An async generator has the features of async functions and the features of generators: you can use await as you would in a regular async function, and you can use yield as you would in a regular generator. But values that you yield are automatically wrapped in Promises" (p. 389). Syntax: `async function*`.

# Prerequisites

- **generator-functions** — Async generators extend generators
- **async-functions** — Async generators extend async functions
- **async-iterators** — Async generators produce async iterables

# Key Properties

1. Declared with `async function*`
2. Can use both `await` and `yield`
3. Yielded values are automatically wrapped in Promises
4. Returns an asynchronous iterator
5. Consumed with `for await...of` loops

# Construction / Recognition

```js
async function* clock(interval, max=Infinity) {
    for(let count = 1; count <= max; count++) {
        await elapsedTime(interval);
        yield count;
    }
}
async function test() {
    for await (let tick of clock(300, 100)) {
        console.log(tick);
    }
}
```

# Context & Application

The simplest way to create asynchronous iterators, just as regular generators are the simplest way to create synchronous iterators. Ideal for transforming async data streams.

# Examples

From the source text (p. 389-390): `async function* clock(interval, max)` that awaits a timer between yields, producing a stream of incrementing values at fixed intervals.

# Relationships

## Builds Upon
- **Generator Functions** — Adds async capabilities to generators
- **Async Functions** — Adds yield capabilities to async functions
- **Async Iterators** — Async generators produce async iterators

## Related
- **for/await Loop** — The natural consumer of async generators

# Common Errors

- **Error**: Trying to use `yield` in a regular `async function` (not `async function*`).
  **Correction**: `yield` requires the `function*` syntax. Use `async function*` for both await and yield.

# Common Confusions

- **Confusion**: Thinking `async function*` returns a regular iterator.
  **Clarification**: It returns an asynchronous iterator whose `next()` method returns Promises. Use `for await...of` to consume it.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.4.3, pages 389-390.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
