---
concept: "Array .map() Method"
slug: array-map
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.14.1 .map(): Each output element is derived from its input element"
extraction_confidence: high
aliases:
  - ".map()"
  - "Array.prototype.map"
prerequisites:
  - array-creation
extends: []
related:
  - array-filter
  - array-flat-map
  - iterator-helper-methods
contrasts_with:
  - array-flat-map
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`.map()` creates a new Array where each element is the result of calling a provided callback function on the corresponding element of the original Array.

# Core Definition

The Array method `.map()` applies a callback `(value, index, array) => result` to each element of an Array, returning a new Array of the same length containing the callback results. The original Array is not modified.

# Prerequisites

- **array-creation** -- operates on arrays

# Key Properties

1. Non-destructive -- returns a new Array
2. Output has same length as input
3. Callback receives (value, index, array)
4. Preserves but skips holes
5. One-to-one transformation: each input element produces exactly one output element

# Construction / Recognition

```js
[1, 2, 3].map(x => x * 3); // [3, 6, 9]
['how', 'are', 'you'].map(str => str.toUpperCase());
// ['HOW', 'ARE', 'YOU']
```

# Context & Application

`.map()` is the primary transformation method for arrays. Use it when you need to derive a new value from each element without changing the number of elements.

# Examples

```js
[1, 2, 3].map(x => x * 3); // [3, 6, 9]
[true, true, true].map((_x, index) => index); // [0, 1, 2]
```

(Chapter 34, Section 34.14.1, lines 1709-1746)

# Relationships

## Builds Upon
- **array-creation** -- transforms arrays

## Enables
- Data transformation patterns

## Related
- **array-filter** -- selects elements; `.map()` transforms them
- **array-flat-map** -- one-to-many transformation
- **iterator-helper-methods** -- `.map()` also available on iterators

## Contrasts With
- **array-flat-map** -- `.map()` is one-to-one; `.flatMap()` is one-to-many

# Common Errors

- **Error**: Using `.map()` for side effects without using the return value.
  **Correction**: Use `.forEach()` for side effects; `.map()` is for transformations.

# Common Confusions

- **Confusion**: `.map()` can change the number of output elements.
  **Clarification**: `.map()` always produces the same number of elements. Use `.flatMap()` or `.filter()` to change count.

# Source Reference

Chapter 34: Arrays (Array), Section 34.14.1, lines 1709-1746.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with implementation
- Cross-reference status: verified
