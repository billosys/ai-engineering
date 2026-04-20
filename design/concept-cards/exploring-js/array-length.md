---
concept: Array .length Property
slug: array-length
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.3.2 The .length of an Array"
extraction_confidence: high
aliases:
  - ".length"
  - "Array length"
prerequisites:
  - array-creation
extends: []
related:
  - array-holes
contrasts_with:
  - map-size
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

The `.length` property of an Array is always the highest index plus one; it can be both read and written to, with setting it to a smaller value pruning elements from the end.

# Core Definition

Every Array has a `.length` property that can be used to both read and change the number of elements. The length is always the highest index plus one. Writing to `arr[arr.length]` appends an element. Setting `.length` to a smaller value destructively removes elements. Setting `.length` to 0 clears the array.

# Prerequisites

- **array-creation** -- arrays must exist to have length

# Key Properties

1. Always equals highest index + 1
2. Writable -- setting it prunes or extends the array
3. `.length = 0` clears an array
4. Based on indices (unlike `.size` for Maps/Sets which counts elements)
5. Holes affect length but not actual element count

# Construction / Recognition

```js
const arr = ['a', 'b'];
arr.length;        // 2
arr.length = 1;    // prunes to ['a']
arr[arr.length] = 'b'; // appends
```

# Context & Application

Understanding `.length` is essential for array manipulation, clearing, and bounds checking. The distinction between `.length` (index-based) and `.size` (count-based) matters when choosing between arrays and maps/sets.

# Examples

```js
const arr = ['a', 'b', 'c'];
assert.equal(arr.length, 3);
arr.length = 1;
assert.deepEqual(arr, ['a']);
arr[arr.length] = 'b';
assert.deepEqual(arr, ['a', 'b']);
```

(Chapter 34, Section 34.3.2, lines 454-499)

# Relationships

## Builds Upon
- **array-creation** -- fundamental array property

## Enables
- Array truncation and clearing

## Related
- **array-holes** -- holes affect length

## Contrasts With
- **map-size** -- Maps use `.size` (element count), not `.length`

# Common Errors

- **Error**: Expecting `.length` to reflect only non-hole elements.
  **Correction**: `.length` is highest index + 1, regardless of holes.

# Common Confusions

- **Confusion**: `.length` and `.size` are interchangeable.
  **Clarification**: `.length` is index-based (Arrays, strings); `.size` counts elements (Maps, Sets).

# Source Reference

Chapter 34: Arrays (Array), Section 34.3.2, lines 454-499.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified (also referenced in Map chapter 36.7.4)
