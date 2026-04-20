---
concept: Iteration Data Producers
slug: iteration-data-producers
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.9.1 Synchronous iteration: data producers"
extraction_confidence: high
aliases:
  - "built-in iterables"
prerequisites:
  - iteration-protocol
extends: []
related:
  - iteration-data-consumers
contrasts_with: []
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

Built-in iterable data producers include Strings, Arrays, Sets, Maps, and DOM data structures, each exposing their contents through the iteration protocol via `[Symbol.iterator]()` and often `.keys()`, `.values()`, `.entries()`.

# Core Definition

These data structures are iterable: Strings, Arrays, Sets, Maps, and (in browsers) DOM data structures. Arrays, Sets, and Maps additionally have `.keys()`, `.values()`, and `.entries()` methods that return iterable iterators. Generators also produce iterables. `Object.keys()`, `Object.values()`, and `Object.entries()` return Arrays (not iterators).

# Prerequisites

- **iteration-protocol** -- producers implement the protocol

# Key Properties

1. Strings iterate over Unicode code points
2. Arrays iterate over elements
3. Sets iterate over elements (insertion order)
4. Maps iterate over [key, value] pairs (insertion order)
5. `.keys()`, `.values()`, `.entries()` available on Arrays, Sets, Maps
6. `Object.keys/values/entries()` return Arrays (not iterators)

# Construction / Recognition

```js
for (const char of 'abc') { }  // string iteration
for (const elem of [1,2]) { }  // array iteration
for (const val of new Set([1,2])) { } // set iteration
for (const [k,v] of new Map([['a',1]])) { } // map iteration
```

# Context & Application

Knowing which data structures are iterable is essential for using for-of, spread, and destructuring effectively.

# Examples

```js
// All built-in iterables work uniformly
const consumers = [
  Array.from,
  x => [...x],
  x => { for (const v of x) return v; }
];
// Each consumer works with any iterable
```

(Chapter 32, Section 32.9.1, lines 1272-1313)

# Relationships

## Builds Upon
- **iteration-protocol** -- these structures implement it

## Enables
- Uniform data access across collection types

## Related
- **iteration-data-consumers** -- the other side of the protocol

## Contrasts With
- None

# Common Errors

- **Error**: Expecting plain objects to be iterable data producers.
  **Correction**: Plain objects are not iterable. Use `Object.entries(obj)` to get an iterable.

# Common Confusions

- **Confusion**: `Object.entries()` returns an iterator.
  **Clarification**: `Object.entries()` returns an Array. `.entries()` on Arrays/Sets/Maps returns an iterator.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.9.1, lines 1272-1313.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly enumerated
- Cross-reference status: verified
