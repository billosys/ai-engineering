---
concept: "Array .slice() Method"
slug: array-slice
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.1.2 The most commonly used Array methods"
extraction_confidence: high
aliases:
  - ".slice()"
  - "Array.prototype.slice"
prerequisites:
  - array-creation
extends: []
related:
  - array-copying
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`.slice(start?, end?)` returns a new Array containing a shallow copy of elements from `start` up to (but not including) `end`, supporting negative indices; without arguments, it produces a complete shallow copy.

# Core Definition

The Array method `.slice(start, end)` extracts a contiguous subsequence as a new Array. Both `start` and `end` support negative indices. Without arguments, `.slice()` creates a complete shallow copy of the array.

# Prerequisites

- **array-creation** -- operates on arrays

# Key Properties

1. Non-destructive -- returns a new Array
2. Supports negative indices
3. `end` is exclusive
4. `.slice()` with no args = shallow copy
5. Commonly used for extracting portions of arrays

# Construction / Recognition

```js
['a', 'b', 'c'].slice(1, 3);  // ['b', 'c']
['a', 'b', 'c'].slice(-1);    // ['c']
['a', 'b', 'c'].slice();      // ['a', 'b', 'c'] (copy)
```

# Context & Application

Use `.slice()` for extracting sub-arrays, making copies before destructive operations, and getting the last N elements.

# Examples

```js
const arr = ['a', 'b', 'c'];
assert.deepEqual(arr.slice(1, 3), ['b', 'c']);
assert.deepEqual(arr.slice(-1), ['c']);
assert.deepEqual(arr.slice(), ['a', 'b', 'c']); // complete copy
```

(Chapter 34, Section 34.1.2, lines 333-341)

# Relationships

## Builds Upon
- **array-creation** -- extracts from arrays

## Enables
- Sub-array extraction
- **array-copying** -- one of the copy methods

## Related
- **array-copying** -- `.slice()` is a copy technique

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `.slice()` to modify the original array.
  **Correction**: `.slice()` is non-destructive. Use `.splice()` for destructive extraction.

# Common Confusions

- **Confusion**: `.slice()` and `.splice()` do the same thing.
  **Clarification**: `.slice()` is non-destructive and returns a copy. `.splice()` is destructive and modifies the original.

# Source Reference

Chapter 34: Arrays (Array), Section 34.1.2, lines 333-341.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified
