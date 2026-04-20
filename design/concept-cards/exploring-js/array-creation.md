---
concept: Array Creation
slug: array-creation
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.3.1 Creating, reading, writing Arrays"
extraction_confidence: high
aliases:
  - "Array literal"
  - "creating arrays"
prerequisites: []
extends: []
related:
  - array-from
  - array-length
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

Arrays are created primarily via Array literals (`[a, b, c]`), which use square brackets to define an ordered list of elements; they can also be created with `Array.from()`, `Array.of()`, or the `Array` constructor.

# Core Definition

The best way to create an Array is via an Array literal, which starts and ends with square brackets. Trailing commas are allowed and ignored. Elements are accessed via zero-based numeric indices in brackets. The range of Array indices is 32-bit (0 to 2^32-2). Arrays in JavaScript are flexible data structures used as lists, stacks, queues, and tuples.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Array literals: `['a', 'b', 'c']`
2. Read elements: `arr[0]`
3. Write elements: `arr[0] = 'x'`
4. `.at()` method supports negative indices (ES2022)
5. Trailing commas in literals are ignored
6. `Array.isArray()` checks if a value is an Array

# Construction / Recognition

```js
const arr = ['a', 'b', 'c'];
arr[0];      // 'a' (read)
arr.at(-1);  // 'c' (negative index, ES2022)
arr[0] = 'x'; // write
```

# Context & Application

Array literals are the standard way to create arrays. Use `Array.from()` for converting iterables/array-like objects, and `new Array(n).fill(value)` for creating arrays of a specific size.

# Examples

```js
const arr = ['a', 'b', 'c'];
assert.equal(arr[0], 'a');
assert.equal(arr.at(-1), 'c');
arr[0] = 'x';
assert.deepEqual(arr, ['x', 'b', 'c']);
```

(Chapter 34, Section 34.3.1, lines 403-449)

# Relationships

## Builds Upon
- No prerequisites

## Enables
- All array operations and methods

## Related
- **array-from** -- alternative creation method
- **array-length** -- property tracking element count

## Contrasts With
- None

# Common Errors

- **Error**: Using `new Array(3)` expecting `[3]` but getting an array with 3 holes.
  **Correction**: `new Array(3)` creates an array of length 3 with holes. Use `[3]` for a single-element array.

# Common Confusions

- **Confusion**: The bracket operator `[]` supports negative indices.
  **Clarification**: `arr[-1]` sets a non-element property, not the last element. Use `arr.at(-1)` instead.

# Source Reference

Chapter 34: Arrays (Array), Section 34.3.1, lines 403-449.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
