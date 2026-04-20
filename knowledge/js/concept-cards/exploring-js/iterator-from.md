---
concept: "Iterator.from()"
slug: iterator-from
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.7.3 Iterator.from(): creating API iterators"
extraction_confidence: high
aliases:
  - "Iterator.from"
prerequisites:
  - iterator-class
extends: []
related:
  - iterator-helper-methods
contrasts_with: []
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

`Iterator.from()` is a static method that converts any iterable or iterator into an instance of `Iterator`, ensuring access to iterator helper methods even for legacy iterators.

# Core Definition

`Iterator.from(obj)` works as follows: if `obj` is iterable, it creates an iterator via `obj[Symbol.iterator]()` and returns it if it is already an instance of `Iterator`, or wraps it otherwise. If `obj` is an iterator, it ensures it is an instance of `Iterator`. This bridges legacy iterables/iterators to the ES2025 Iterator API.

# Prerequisites

- **iterator-class** -- the target class for conversion

# Key Properties

1. Introduced in ES2025 (as part of class Iterator)
2. Accepts iterables or iterators
3. Returns an instance of Iterator
4. Wraps legacy iterators that lack Iterator API methods
5. Distinguishes "API iterators" from "legacy iterators"

# Construction / Recognition

```js
const legacyIterator = {
  next() { return { done: false, value: '#' }; }
};
Iterator.from(legacyIterator) instanceof Iterator; // true
Iterator.from(legacyIterator).take(3).toArray();
// ['#', '#', '#']
```

# Context & Application

Use `Iterator.from()` when working with library or user-created iterables that may not produce Iterator instances, ensuring helper methods are available.

# Examples

```js
const iterable = ['a', 'b'];
Iterator.from(iterable) instanceof Iterator; // true
iterable[Symbol.iterator]() instanceof Iterator; // true (built-in)

// Convert legacy iterator
const legacy = { next() { return { done: true }; } };
Iterator.from(legacy).toArray(); // []
```

(Chapter 32, Section 32.7.3, lines 942-986)

# Relationships

## Builds Upon
- **iterator-class** -- the class it produces instances of

## Enables
- Using iterator helper methods on legacy iterators

## Related
- **iterator-helper-methods** -- the methods gained through conversion

## Contrasts With
- None

# Common Errors

- **Error**: Assuming `Iterator.from()` clones or restarts iteration.
  **Correction**: It wraps the existing iterator; if already partially consumed, it continues from that point.

# Common Confusions

- **Confusion**: `Iterator.from()` and `Array.from()` do the same thing.
  **Clarification**: `Array.from()` creates an Array; `Iterator.from()` creates a lazy Iterator instance.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.7.3, lines 942-986.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with algorithm description
- Cross-reference status: verified
