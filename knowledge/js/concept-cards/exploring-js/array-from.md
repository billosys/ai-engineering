---
concept: "Array.from()"
slug: array-from
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.6.3 Converting iterables and Array-like objects to Arrays via Array.from()"
extraction_confidence: high
aliases:
  - "Array.from"
prerequisites:
  - iterable-interface
  - array-like-objects
extends: []
related:
  - array-spreading
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`Array.from()` converts any iterable or Array-like object to an Array, with an optional mapping function applied during conversion.

# Core Definition

`Array.from()` operates in two modes. Mode 1 (converting): accepts an Iterable or ArrayLike and returns an Array. Mode 2 (converting and mapping): accepts a second parameter `mapFunc` that transforms each element during conversion, avoiding the need for a separate `.map()` call.

# Prerequisites

- **iterable-interface** -- accepts iterables
- **array-like-objects** -- accepts array-like objects

# Key Properties

1. Introduced in ES2015 (ES6)
2. Accepts both iterables and array-like objects
3. Optional mapping function as second parameter
4. Treats array holes as `undefined` (unlike `.map()` which preserves holes)
5. More self-descriptive than spreading (`[...iterable]`)

# Construction / Recognition

```js
Array.from(new Set(['a', 'b'])); // ['a', 'b']
Array.from({length: 2, 0: 'a', 1: 'b'}); // ['a', 'b']
Array.from(new Set(['a', 'b']), x => x + x); // ['aa', 'bb']
```

# Context & Application

Use `Array.from()` to convert any iterable or array-like value to an Array. The mapping mode is useful for creating arrays from lengths: `Array.from({length: 3}, (_, i) => i)` produces `[0, 1, 2]`.

# Examples

```js
// Mode 1: Converting
Array.from(new Set(['a', 'b'])); // ['a', 'b']

// Mode 2: Converting and mapping
Array.from({length: 3}, () => ({})); // [{}, {}, {}]
// Each object is a new instance (unlike .fill({}))

// Creating a range
Array.from({length: 3}, (_, i) => i + 2); // [2, 3, 4]
```

(Chapter 34, Section 34.6.3, lines 907-967)

# Relationships

## Builds Upon
- **iterable-interface** -- input source
- **array-like-objects** -- alternative input source

## Enables
- Converting any iterable/array-like to Array

## Related
- **array-spreading** -- alternative conversion for iterables only

## Contrasts With
- None

# Common Errors

- **Error**: Using `new Array(3).map(() => ({}))` to create an array of objects.
  **Correction**: `.map()` preserves holes. Use `Array.from({length: 3}, () => ({}))` instead.

# Common Confusions

- **Confusion**: `Array.from()` and spreading do the same thing.
  **Clarification**: `Array.from()` also accepts array-like objects (not just iterables) and has a mapping mode.

# Source Reference

Chapter 34: Arrays (Array), Section 34.6.3, lines 907-967.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with type signatures
- Cross-reference status: verified
