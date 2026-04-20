---
concept: for-of with Array Methods
slug: array-for-of-patterns
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.4 for-of and Arrays"
extraction_confidence: high
aliases: []
prerequisites:
  - for-of-loop
  - array-creation
extends: []
related:
  - array-destructuring
contrasts_with: []
answers_questions:
  - "How do I use `for-of` loops with iterables?"
---

# Quick Definition

for-of works with Arrays in three patterns: iterating over elements directly, over indices via `.keys()`, and over [index, element] pairs via `.entries()` with destructuring.

# Core Definition

Three common patterns for using for-of with Arrays: (1) `for (const elem of arr)` iterates over elements; (2) `for (const index of arr.keys())` iterates over indices; (3) `for (const [index, element] of arr.entries())` iterates over index-element pairs using destructuring.

# Prerequisites

- **for-of-loop** -- the iteration construct
- **array-creation** -- arrays to iterate over

# Key Properties

1. `for (const elem of arr)` -- elements
2. `for (const i of arr.keys())` -- indices
3. `for (const [i, e] of arr.entries())` -- pairs with destructuring
4. All three use the iteration protocol

# Construction / Recognition

```js
for (const element of ['a', 'b']) { }
for (const index of ['a', 'b'].keys()) { }
for (const [index, element] of ['a', 'b'].entries()) { }
```

# Context & Application

These three patterns cover all common array iteration needs without resorting to index-based for loops.

# Examples

```js
for (const [index, element] of ['a', 'b'].entries()) {
  console.log(index, element);
}
// 0 a
// 1 b
```

(Chapter 34, Section 34.4, lines 745-800)

# Relationships

## Builds Upon
- **for-of-loop** -- the iteration construct
- **array-creation** -- the iterable

## Enables
- Index-aware iteration without traditional for loops

## Related
- **array-destructuring** -- used with `.entries()`

## Contrasts With
- None

# Common Errors

- **Error**: Using `for (const x in arr)` instead of `for (const x of arr)`.
  **Correction**: `for-in` iterates over property keys (strings, including non-index); `for-of` iterates over values.

# Common Confusions

- **Confusion**: `.entries()` returns an Array.
  **Clarification**: `.entries()` returns an iterator over [index, element] pairs, not an Array.

# Source Reference

Chapter 34: Arrays (Array), Section 34.4, lines 745-800.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified
