---
concept: for-of Loop
slug: for-of-loop
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.3.4 Iterating via iteration-based language constructs"
extraction_confidence: high
aliases:
  - "for...of"
  - "for-of statement"
prerequisites:
  - iteration-protocol
  - iterable-interface
extends: []
related:
  - spread-syntax
  - array-destructuring
contrasts_with: []
answers_questions:
  - "How does `for-of` relate to the iteration protocol?"
  - "How do I use `for-of` loops with iterables?"
---

# Quick Definition

The `for-of` loop is an iteration-based language construct that sequentially visits the values of any iterable object, using the iteration protocol internally.

# Core Definition

The `for-of` loop is the most important iteration-based language construct, described by Rauschmayer as the primary consumer of the iteration protocol. It works with any iterable -- Arrays, Sets, Maps, strings, generators, and custom iterables. The loop internally calls `[Symbol.iterator]()` and repeatedly invokes `.next()` until `.done` is `true`.

# Prerequisites

- **iteration-protocol** -- for-of is built on top of it
- **iterable-interface** -- the value after `of` must be iterable

# Key Properties

1. Introduced in ES2015 (ES6)
2. Works with any iterable, not just Arrays
3. Can be combined with destructuring in the loop variable
4. The same iteration code works identically for Arrays, Sets, and other iterables
5. Supports `break` and `continue` for early termination and skipping

# Construction / Recognition

```js
for (const element of iterable) {
  // process element
}

// With destructuring (e.g., Map entries)
for (const [key, value] of map) {
  // process key-value pair
}
```

# Context & Application

Use for-of whenever you need to process the elements of a collection sequentially. It is preferred over `.forEach()` because it supports `break`, `continue`, and `return`, and works with all iterables, not just Arrays.

# Examples

```js
// Iterating over an Array
for (const x of ['hello', 'beautiful', 'world']) {
  console.log(x);
}
// Output: hello, beautiful, world

// Iterating over a Set (same code!)
for (const x of new Set(['hello', 'beautiful', 'world'])) {
  console.log(x);
}

// Iterating over Array [index, element] pairs
for (const [index, element] of ['a', 'b'].entries()) {
  console.log(index, element);
}
```

(Chapter 32, Section 32.3.4, lines 285-355; Chapter 34, Section 34.4, lines 745-800)

# Relationships

## Builds Upon
- **iteration-protocol** -- uses the protocol internally
- **iterable-interface** -- requires an iterable operand

## Enables
- Uniform processing of any iterable data structure

## Related
- **spread-syntax** -- another iteration consumer
- **array-destructuring** -- can be combined with for-of

## Contrasts With
- None at this scope

# Common Errors

- **Error**: Using `for-of` on a plain object, which is not iterable.
  **Correction**: Use `for (const [k,v] of Object.entries(obj))` instead.

# Common Confusions

- **Confusion**: `for-of` and `for-in` are interchangeable.
  **Clarification**: `for-in` iterates over property keys (including inherited ones); `for-of` iterates over iterable values. They serve different purposes.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.3.4, lines 285-355.

# Verification Notes

- Definition source: direct
- Confidence rationale: Extensively demonstrated across multiple chapters
- Cross-reference status: verified
