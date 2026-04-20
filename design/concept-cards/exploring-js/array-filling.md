---
concept: Creating and Filling Arrays
slug: array-filling
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.8 Creating and filling Arrays with arbitrary lengths"
extraction_confidence: high
aliases:
  - ".fill()"
  - "Array.fill"
prerequisites:
  - array-creation
  - array-from
extends: []
related:
  - array-holes
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

Arrays of arbitrary length can be created with `new Array(n).fill(value)` for primitives, or `Array.from({length: n}, () => ({}))` for unique objects, avoiding the shared-reference pitfall of `.fill()` with objects.

# Core Definition

Techniques for creating and filling arrays: (1) push elements in a loop, (2) `new Array(n).fill(primitiveValue)`, (3) `Array.from({length: n}, callback)` for objects (each call produces a new instance), (4) `new Array(n).keys()` for integer ranges starting at zero. Using `.fill()` with objects fills every slot with the same reference.

# Prerequisites

- **array-creation** -- basic array knowledge
- **array-from** -- used for the mapping mode

# Key Properties

1. `.fill(value)` replaces every element/hole with value
2. `.fill()` with objects shares one reference across all slots
3. `Array.from({length: n}, callback)` creates unique objects per slot
4. `.map()` does not work on holes but `Array.from()` treats holes as `undefined`

# Construction / Recognition

```js
new Array(3).fill(0);               // [0, 0, 0]
Array.from({length: 3}, () => ({})); // [{}, {}, {}] -- unique
new Array(3).fill({});               // [{}, {}, {}] -- SAME object!
```

# Context & Application

Use when you need arrays of a specific size initialized with specific values. The `Array.from()` pattern is essential when each element must be a distinct object.

# Examples

```js
// Shared reference pitfall
const arr = new Array(3).fill({});
arr[0].prop = true;
// All three elements have {prop: true} -- same object!

// Fix: use Array.from
const fixed = Array.from({length: 3}, () => ({}));
fixed[0].prop = true;
// Only fixed[0] has {prop: true}

// Integer range
Array.from({length: 3}, (_, i) => i + 2); // [2, 3, 4]
```

(Chapter 34, Section 34.8, lines 998-1138)

# Relationships

## Builds Upon
- **array-creation** -- creating arrays
- **array-from** -- mapping mode

## Enables
- Initialized arrays of specific sizes

## Related
- **array-holes** -- `new Array(n)` creates holes

## Contrasts With
- None

# Common Errors

- **Error**: Using `new Array(3).fill({})` expecting three independent objects.
  **Correction**: `.fill({})` puts the same object in every slot. Use `Array.from({length: 3}, () => ({}))`.

# Common Confusions

- **Confusion**: `new Array(3).map(() => ({}))` creates three objects.
  **Clarification**: `.map()` skips holes. `new Array(3)` has 3 holes, so `.map()` returns `[, , ,]`.

# Source Reference

Chapter 34: Arrays (Array), Section 34.8, lines 998-1138.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated with pitfall
- Cross-reference status: verified
