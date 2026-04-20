---
concept: "Array .filter() Method"
slug: array-filter
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.14.2 .filter(): Only keep some of the elements"
extraction_confidence: high
aliases:
  - ".filter()"
  - "Array.prototype.filter"
prerequisites:
  - array-creation
extends: []
related:
  - array-map
  - array-flat-map
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`.filter()` creates a new Array containing only the elements for which the provided callback returns a truthy value, effectively selecting a subset of the original.

# Core Definition

The Array method `.filter()` returns a new Array collecting all elements for which the callback returns a truthy value. The callback has signature `(value, index, array) => boolean`. The original Array is not modified.

# Prerequisites

- **array-creation** -- operates on arrays

# Key Properties

1. Non-destructive -- returns a new Array
2. Output length is less than or equal to input length
3. Callback receives (value, index, array)
4. Removes holes from sparse arrays
5. Elements are not transformed, only selected

# Construction / Recognition

```js
[-1, 2, 5, -7, 6].filter(x => x >= 0); // [2, 5, 6]
['a', 'b', 'c', 'd'].filter((_x, i) => (i % 2) === 0); // ['a', 'c']
```

# Context & Application

Use `.filter()` when you need to select elements meeting a condition. Combine with `.map()` for select-and-transform operations, or use `.flatMap()` to do both in one step.

# Examples

```js
[-1, 2, 5, -7, 6].filter(x => x >= 0); // [2, 5, 6]

// Removes holes
['a', , 'b'].filter(x => true); // ['a', 'b']
```

(Chapter 34, Section 34.14.2, lines 1748-1787)

# Relationships

## Builds Upon
- **array-creation** -- operates on arrays

## Enables
- Subset selection patterns

## Related
- **array-map** -- often combined with filter
- **array-flat-map** -- can do filter+map in one step

## Contrasts With
- None

# Common Errors

- **Error**: Using `.filter()` to transform elements.
  **Correction**: `.filter()` only selects; use `.map()` to transform.

# Common Confusions

- **Confusion**: `.filter()` modifies the original array.
  **Clarification**: `.filter()` is non-destructive; it returns a new Array.

# Source Reference

Chapter 34: Arrays (Array), Section 34.14.2, lines 1748-1787.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with implementation
- Cross-reference status: verified
