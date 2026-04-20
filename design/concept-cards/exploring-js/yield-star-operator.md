---
concept: "yield* Operator"
slug: yield-star-operator
category: iteration
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous generators (advanced)"
chapter_number: 33
pdf_page: null
section: "33.2.1 Calling generators via yield*"
extraction_confidence: high
aliases:
  - "yield*"
  - "yield star"
  - "generator delegation"
prerequisites:
  - generator-function
  - yield-operator
extends: []
related:
  - iterable-interface
contrasts_with: []
answers_questions:
  - "What is needed to understand generator functions?"
---

# Quick Definition

The `yield*` operator delegates yielding to another iterable or generator, yielding all of its values as if they were yielded directly by the enclosing generator.

# Core Definition

`yield*` delegates to another iterable: it yields everything that is yielded by the target. It is roughly equivalent to `for (const x of iterable) { yield x; }`. Importantly, `yield*` works with any iterable, not just generators. It enables recursive generators for tree-like data structures.

# Prerequisites

- **generator-function** -- yield* is used inside generators
- **yield-operator** -- yield* builds on yield

# Key Properties

1. Introduced in ES2015 (ES6)
2. Delegates to any iterable (arrays, other generators, etc.)
3. Equivalent to iterating and yielding each value
4. Enables recursive generator patterns
5. Calling a generator without yield* returns an unused iterator

# Construction / Recognition

```js
function* compute() {
  yield* helper();     // delegate to another generator
  yield* [1, 2];       // delegate to an array
}
```

# Context & Application

`yield*` is essential for composing generators and for recursive traversals of tree-like data structures, where each subtree is iterated by delegating to a recursive generator call.

# Examples

```js
function* helper() { yield 'a'; yield 'b'; }
function* compute() { yield* helper(); }
Array.from(compute()); // ['a', 'b']

// Recursive tree traversal
class BinaryTree {
  constructor(value, left=null, right=null) { /* ... */ }
  * [Symbol.iterator]() {
    yield this.value;
    if (this.left) yield* this.left;
    if (this.right) yield* this.right;
  }
}
```

(Chapter 33, Section 33.2.1-33.2.2, lines 332-467)

# Relationships

## Builds Upon
- **generator-function** -- used inside generators
- **yield-operator** -- delegates yield behavior

## Enables
- Recursive generators
- Generator composition

## Related
- **iterable-interface** -- yield* works with any iterable

## Contrasts With
- None

# Common Errors

- **Error**: Calling another generator function without `yield*` and expecting its values to appear.
  **Correction**: `helper()` returns an iterator but does nothing with it. Use `yield* helper()` to delegate.

# Common Confusions

- **Confusion**: `yield*` only works with generators.
  **Clarification**: `yield*` works with any iterable, including arrays: `yield* [1, 2]`.

# Source Reference

Chapter 33: Synchronous generators (advanced), Section 33.2, lines 332-467.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with multiple examples
- Cross-reference status: verified
