---
concept: "Array .at() Method"
slug: array-at-method
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.3.3.1 .at(): reading single elements (supports negative indices)"
extraction_confidence: high
aliases:
  - ".at()"
  - "Array.prototype.at"
prerequisites:
  - array-creation
extends: []
related:
  - array-length
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

The `.at()` method (ES2022) returns the element at a given index, supporting negative indices where `-1` refers to the last element, `-2` to the second-last, and so on.

# Core Definition

The Array method `.at()` returns the element at a given index, supporting both positive and negative indices. Negative indices are added to `.length` to compute the actual index. This contrasts with the bracket operator `[]` which does not support negative indices and interprets them as non-element property keys.

# Prerequisites

- **array-creation** -- must have an array to index

# Key Properties

1. Introduced in ES2022
2. Supports negative indices (`-1` = last element)
3. Returns `undefined` for out-of-range indices
4. Read-only (cannot use `.at()` for assignment)

# Construction / Recognition

```js
['a', 'b', 'c'].at(0);   // 'a'
['a', 'b', 'c'].at(-1);  // 'c'
['a', 'b', 'c'].at(-2);  // 'b'
```

# Context & Application

Use `.at()` when you need to access elements from the end of an array without computing `arr.length - n` manually.

# Examples

```js
const arr = ['a', 'b', 'c'];
assert.equal(arr.at(0), 'a');
assert.equal(arr.at(-1), 'c');

// bracket operator does NOT support negative indices
arr[-1] = 'non-element property';
assert.equal(arr[-1], 'non-element property');
assert.deepEqual(Array.from(arr), ['a', 'b', 'c']); // unchanged
```

(Chapter 34, Section 34.3.3.1, lines 528-560)

# Relationships

## Builds Upon
- **array-creation** -- indexing into arrays

## Enables
- Convenient end-of-array access

## Related
- **array-length** -- negative indices computed from length

## Contrasts With
- None

# Common Errors

- **Error**: Using `arr[-1]` to get the last element.
  **Correction**: `arr[-1]` accesses a string property key `'-1'`, not an index. Use `arr.at(-1)`.

# Common Confusions

- **Confusion**: `.at()` can be used for assignment.
  **Clarification**: `.at()` is read-only. Use `arr[arr.length - 1] = val` for assignment at the end.

# Source Reference

Chapter 34: Arrays (Array), Section 34.3.3.1, lines 528-560.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2022 marker
- Cross-reference status: verified
