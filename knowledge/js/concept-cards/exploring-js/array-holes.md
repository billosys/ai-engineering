---
concept: Array Holes
slug: array-holes
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.10.2 Arrays can have holes"
extraction_confidence: high
aliases:
  - "sparse array"
  - "dense array"
  - "empty slots"
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

Array holes are missing elements at certain indices, making the array "sparse" rather than "dense"; different array methods handle holes inconsistently, so holes should be avoided.

# Core Definition

An Array is dense if all indices from 0 to `length-1` exist, and sparse if some indices are missing (holes). Arrays can be sparse because they are actually dictionaries from indices to values. Holes can be created by skipping indices, using `delete`, or increasing `.length`. Array methods handle holes inconsistently: `.filter()` removes them, `.map()` preserves them, `Array.from()` treats them as `undefined`.

# Prerequisites

- **array-creation** -- understanding arrays

# Key Properties

1. Holes are missing elements, not `undefined` values
2. Created by skipping indices, `delete arr[i]`, commas in literals `['a', , 'c']`, or increasing `.length`
3. `.filter()` removes holes; `.map()` preserves them; `.every()` ignores them; `Array.from()` converts to `undefined`
4. Recommendation: avoid holes -- they complicate code and reduce performance
5. Engines optimize dense arrays for speed

# Construction / Recognition

```js
const arr = ['a', , 'c']; // hole at index 1
Object.keys(arr); // ['0', '2'] -- no key '1'
0 in arr; // true
1 in arr; // false (hole)
```

# Context & Application

Holes are an advanced concept that developers should generally avoid. Understanding them helps when debugging unexpected behavior from array methods applied to sparse arrays.

# Examples

```js
['a', , 'b'].filter(x => true); // ['a', 'b'] -- holes removed
['a', , 'b'].map(x => 'c');     // ['c', , 'c'] -- hole preserved
Array.from(['a', , 'b']);        // ['a', undefined, 'b'] -- hole -> undefined
```

(Chapter 34, Section 34.10.2, lines 1273-1408)

# Relationships

## Builds Upon
- **array-creation** -- arrays can be sparse

## Enables
- Understanding of array method edge cases

## Related
- **array-length** -- holes affect length

## Contrasts With
- None

# Common Errors

- **Error**: Assuming `new Array(3)` creates an array with three `undefined` elements.
  **Correction**: `new Array(3)` creates three holes, which behave differently from `undefined` in some methods.

# Common Confusions

- **Confusion**: Holes and `undefined` are the same.
  **Clarification**: A hole is a missing element (no property key exists); `undefined` is an actual value. `[, 'a']` has a hole at 0; `[undefined, 'a']` has a value at 0.

# Source Reference

Chapter 34: Arrays (Array), Section 34.10.2, lines 1273-1408.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with examples of inconsistent handling
- Cross-reference status: verified
