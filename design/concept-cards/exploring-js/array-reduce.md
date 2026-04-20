---
concept: "Array .reduce() Method"
slug: array-reduce
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.15 .reduce(): computing a summary for an Array"
extraction_confidence: high
aliases:
  - ".reduce()"
  - "Array.prototype.reduce"
  - "foldl"
prerequisites:
  - array-creation
extends: []
related:
  - array-map
  - array-filter
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`.reduce()` computes a single summary value from an Array by repeatedly applying a callback that combines an accumulator with each element, working left to right.

# Core Definition

Method `.reduce()` is a powerful tool for computing a "summary" of an Array. The callback `(accumulator, element, index, array) => newAccumulator` is called for each element, combining the current accumulator with the element. The `init` parameter provides the initial accumulator value. The final accumulator is the result. Also known as `foldl` (fold left) in functional programming.

# Prerequisites

- **array-creation** -- operates on arrays

# Key Properties

1. Callback: `(accumulator, element, index, array) => newAccumulator`
2. Optional `init` parameter for initial accumulator
3. Without `init`, first element is initial accumulator
4. Empty array without `init` throws TypeError
5. `.reduceRight()` processes from end to start
6. Cannot terminate early (unlike for-of with break)

# Construction / Recognition

```js
[1, 2, 3].reduce((sum, elem) => sum + elem, 0); // 6
```

# Context & Application

`.reduce()` is general-purpose: it can compute sums, build new arrays, find values, or perform any accumulation. However, for-of loops may be clearer for complex reductions.

# Examples

```js
function addAll(arr) {
  return arr.reduce((sum, element) => sum + element, 0);
}
addAll([1, 2, 3]); // 6

// Double array elements via reduce
function double(inArr) {
  return inArr.reduce((outArr, element) => {
    outArr.push(element * 2);
    return outArr;
  }, []);
}
double([1, 2, 3]); // [2, 4, 6]
```

(Chapter 34, Section 34.15, lines 1923-2166)

# Relationships

## Builds Upon
- **array-creation** -- operates on arrays

## Enables
- Any accumulation/summary computation

## Related
- **array-map** -- can be implemented via reduce
- **array-filter** -- can be implemented via reduce

## Contrasts With
- None

# Common Errors

- **Error**: Calling `.reduce()` on an empty array without an `init` value.
  **Correction**: Always provide `init` when the array might be empty, or handle the TypeError.

# Common Confusions

- **Confusion**: `.reduce()` is always better than a for-of loop.
  **Clarification**: For-of may be easier to understand and allows early termination via `break`.

# Source Reference

Chapter 34: Arrays (Array), Section 34.15, lines 1923-2166.

# Verification Notes

- Definition source: direct
- Confidence rationale: Extensively explained with multiple examples
- Cross-reference status: verified
