---
concept: Generators as Iterator Implementers
slug: generator-as-iterator-implementer
category: iteration
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous generators (advanced)"
chapter_number: 33
pdf_page: null
section: "33.1.4 Example: Mapping over iterables"
extraction_confidence: high
aliases:
  - "generator-based iterable"
prerequisites:
  - generator-function
  - iterable-interface
extends: []
related:
  - yield-operator
contrasts_with: []
answers_questions:
  - "What is a generator function?"
  - "What is needed to understand generator functions?"
---

# Quick Definition

Generator functions can implement custom iterables by using `* [Symbol.iterator]()` as a method, and can transform iterables by accepting them as parameters and yielding processed values.

# Core Definition

Generators serve dual roles in the iteration ecosystem: (1) as iterable implementers -- a class can use `* [Symbol.iterator]()` to make instances iterable; (2) as iterable transformers -- generator functions can accept iterables and yield transformed values, acting like lazy `.map()` and `.filter()`. Both roles leverage the fact that generators return iterable iterators.

# Prerequisites

- **generator-function** -- the mechanism used
- **iterable-interface** -- what generators implement

# Key Properties

1. `* [Symbol.iterator]()` makes a class iterable
2. Generator functions can accept and transform iterables
3. Lazy -- values produced on demand
4. Replaces manual Iterator implementation

# Construction / Recognition

```js
// Implementing iterable
class MyIterable {
  * [Symbol.iterator]() {
    yield 'good';
    yield 'morning';
  }
}

// Transforming iterables
function* mapIter(iterable, func) {
  let index = 0;
  for (const x of iterable) {
    yield func(x, index);
    index++;
  }
}
```

# Context & Application

Generators are the simplest way to make custom objects iterable and to create lazy transformation pipelines for iterables.

# Examples

```js
// Making a BinaryTree iterable
class BinaryTree {
  * [Symbol.iterator]() {
    yield this.value;
    if (this.left) yield* this.left;
    if (this.right) yield* this.right;
  }
}

// Lazy map
function* mapIter(iterable, func) {
  for (const x of iterable) yield func(x);
}
Array.from(mapIter(['a', 'b'], x => x + x)); // ['aa', 'bb']
```

(Chapter 33, Section 33.1.4, lines 299-320; Chapter 32, Section 32.6.1, lines 554-623)

# Relationships

## Builds Upon
- **generator-function** -- the implementation tool
- **iterable-interface** -- what is being implemented

## Enables
- Custom iterable data structures
- Lazy transformation pipelines

## Related
- **yield-operator** -- used to produce values

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting the `*` in `* [Symbol.iterator]()`.
  **Correction**: Without `*`, the method is a regular method that must manually return an iterator object.

# Common Confusions

- **Confusion**: Generator-based iterables are one-time iterables.
  **Clarification**: If `[Symbol.iterator]()` is a generator method on a class, each call creates a fresh generator (many-times iterable). A standalone generator function call creates a one-time iterable.

# Source Reference

Chapter 33: Synchronous generators (advanced), Section 33.1.4, lines 299-320.

# Verification Notes

- Definition source: synthesized from examples
- Confidence rationale: Demonstrated in both chapters 32 and 33
- Cross-reference status: verified
