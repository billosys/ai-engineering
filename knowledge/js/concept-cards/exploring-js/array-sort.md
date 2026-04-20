---
concept: "Array .sort() Method"
slug: array-sort
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.16 .sort(): sorting Arrays"
extraction_confidence: high
aliases:
  - ".sort()"
  - "Array.prototype.sort"
prerequisites:
  - array-creation
extends: []
related:
  - array-destructive-vs-nondestructive
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`.sort()` sorts an Array in place and returns it; by default it sorts by string representation lexicographically, but accepts a compare function `(a, b) => number` to customize the ordering.

# Core Definition

`.sort()` sorts in place and returns `this`. By default, it converts elements to strings and compares them lexicographically. A compare function returns: negative if a < b, zero if equal, positive if a > b. Sorting is guaranteed stable since ES2019. The non-destructive version `.toSorted()` was added in ES2023.

# Prerequisites

- **array-creation** -- operates on arrays

# Key Properties

1. Destructive -- modifies and returns the original
2. Default: lexicographic string comparison
3. Compare function: `(a, b) => number`
4. Stable since ES2019
5. Non-destructive version: `.toSorted()` (ES2023)
6. Trick for numeric sort: `(a, z) => a - z`

# Construction / Recognition

```js
[200, 3, 10].sort(); // [10, 200, 3] -- lexicographic!
[200, 3, 10].sort((a, z) => a - z); // [3, 10, 200]
```

# Context & Application

Always provide a compare function when sorting numbers or objects. Use `Intl.Collator` for locale-aware string sorting. Use `.toSorted()` when the original must remain unchanged.

# Examples

```js
// Sorting numbers
[200, 3, 10].sort((a, z) => a - z); // [3, 10, 200]

// Sorting strings with locale
['pie', 'éclair', 'Cookie'].sort(new Intl.Collator('en').compare);

// Sorting objects
[{age: 200}, {age: 3}].sort((a, b) => a.age - b.age);
// [{age: 3}, {age: 200}]
```

(Chapter 34, Section 34.16, lines 2187-2354)

# Relationships

## Builds Upon
- **array-creation** -- operates on arrays

## Enables
- Ordered data presentation

## Related
- **array-destructive-vs-nondestructive** -- `.sort()` is destructive; `.toSorted()` is not

## Contrasts With
- None

# Common Errors

- **Error**: Sorting numbers without a compare function.
  **Correction**: Default sort is lexicographic. `[200, 3, 10].sort()` gives `[10, 200, 3]`. Always pass a numeric comparator.

# Common Confusions

- **Confusion**: `.sort()` returns a new array.
  **Clarification**: `.sort()` modifies the original and returns `this`. Use `.toSorted()` for a new array.

# Source Reference

Chapter 34: Arrays (Array), Section 34.16, lines 2187-2354.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with type signature
- Cross-reference status: verified
