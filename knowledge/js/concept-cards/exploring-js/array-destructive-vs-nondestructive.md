---
concept: Destructive vs. Non-Destructive Array Operations
slug: array-destructive-vs-nondestructive
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.11 Destructive vs. non-destructive Array operations"
extraction_confidence: high
aliases:
  - "mutating vs immutable array methods"
  - ".toReversed()"
  - ".toSorted()"
  - ".toSpliced()"
  - ".with()"
prerequisites:
  - array-creation
extends: []
related:
  - array-push-pop-shift-unshift
  - array-sort
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

Destructive array methods (`.reverse()`, `.sort()`, `.splice()`) modify the original array in place, while their non-destructive counterparts (`.toReversed()`, `.toSorted()`, `.toSpliced()`, `.with()`) return new arrays with changes applied to a copy.

# Core Definition

Some Array operations are destructive (they change the Array they operate on). Others are non-destructive (they produce new Arrays). ES2023 introduced non-destructive versions of the three common destructive methods: `.toReversed()`, `.toSorted(compareFn)`, `.toSpliced(start, deleteCount, ...items)`. ES2023 also introduced `.with(index, value)` as the non-destructive version of bracket assignment.

# Prerequisites

- **array-creation** -- understanding arrays

# Key Properties

1. ES2023 introduced `.toReversed()`, `.toSorted()`, `.toSpliced()`, `.with()`
2. Destructive methods return the modified array (same reference)
3. Non-destructive methods return a new array (original unchanged)
4. Can make destructive methods non-destructive by copying first: `[...arr].reverse()`

# Construction / Recognition

```js
const arr = ['a', 'b', 'c'];
arr.with(1, 'x');      // ['a', 'x', 'c'] -- new array
arr.toReversed();       // ['c', 'b', 'a'] -- new array
// arr is still ['a', 'b', 'c']
```

# Context & Application

Prefer non-destructive methods in functional programming styles or when the original array must remain unchanged (e.g., React state).

# Examples

```js
const original = ['a', 'b', 'c'];
const reversed = original.toReversed();
assert.deepEqual(reversed, ['c', 'b', 'a']);
assert.deepEqual(original, ['a', 'b', 'c']); // unchanged

// Before ES2023: copy then mutate
const reversed2 = [...original].reverse();
```

(Chapter 34, Section 34.11, lines 1410-1510)

# Relationships

## Builds Upon
- **array-creation** -- operates on arrays

## Enables
- Immutable array patterns

## Related
- **array-sort** -- `.sort()` is destructive; `.toSorted()` is not
- **array-push-pop-shift-unshift** -- other destructive methods

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `.reverse()` to return a new array.
  **Correction**: `.reverse()` modifies and returns `this`. Use `.toReversed()` for a new array.

# Common Confusions

- **Confusion**: `.sort()` and `.toSorted()` behave identically.
  **Clarification**: `.sort()` modifies the original; `.toSorted()` returns a new sorted array.

# Source Reference

Chapter 34: Arrays (Array), Section 34.11, lines 1410-1510.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2023 markers
- Cross-reference status: verified
