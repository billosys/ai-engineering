---
# === CORE IDENTIFICATION ===
concept: Array reduce
slug: array-reduce

# === CLASSIFICATION ===
category: higher-order-programming
subcategory: array-methods
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Higher-Order Functions"
chapter_number: 5
pdf_page: null
section: "Summarizing with reduce"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - reduce
  - fold
  - Array.prototype.reduce

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - higher-order-function
extends:
  - higher-order-function
related:
  - array-filter
  - array-map
  - composability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use map, filter, and reduce?"
---

# Quick Definition

The `reduce` method computes a single value from an array by repeatedly combining each element with a running accumulator using a combining function.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 429-434 of 05-higher-order-functions.md): "The higher-order operation that represents this pattern is called *reduce* (sometimes also called *fold*). It builds a value by repeatedly taking a single element from the array and combining it with the current value. When summing numbers, you'd start with the number zero and, for each element, add that to the sum."

Further (lines 437-439): "The parameters to `reduce` are, apart from the array, a combining function and a start value."

# Prerequisites

- **array**: `reduce` is an array method.
- **higher-order-function**: `reduce` takes a combining function as argument.

# Key Properties

1. Takes a **combining function** and an optional **start value**.
2. The combining function receives the accumulator and current element.
3. Returns a **single value** (not an array).
4. If no start value is given, the first element is used as the start.
5. Can be used for summing, finding maximums, counting, grouping, etc.

# Construction / Recognition

## To Construct/Create:
```javascript
[1, 2, 3, 4].reduce((a, b) => a + b, 0)
// → 10
```

## To Identify/Recognize:
- `.reduce(callback, initialValue)` on an array.

# Context & Application

`reduce` is the most versatile higher-order array method. It can implement `filter`, `map`, `sum`, `max`, and many other operations. It is used when you need to collapse an array into a single result.

# Examples

**Example 1** (Ch 5, lines 442-453 of 05-higher-order-functions.md) -- implementation:
```javascript
function reduce(array, combine, start) {
  let current = start;
  for (let element of array) {
    current = combine(current, element);
  }
  return current;
}
console.log(reduce([1, 2, 3, 4], (a, b) => a + b, 0));
// → 10
```

**Example 2** (Ch 5, lines 463-466) -- without start value:
```javascript
console.log([1, 2, 3, 4].reduce((a, b) => a + b));
// → 10
```

**Example 3** (Ch 5, lines 473-484) -- finding the largest script:
```javascript
function characterCount(script) {
  return script.ranges.reduce((count, [from, to]) => {
    return count + (to - from);
  }, 0);
}
console.log(SCRIPTS.reduce((a, b) => {
  return characterCount(a) < characterCount(b) ? b : a;
}));
// → {name: "Han", …}
```

# Relationships

## Builds Upon
- **array** -- Method of arrays.
- **higher-order-function** -- Takes a function as argument.

## Enables
- **composability** -- `reduce` combines with `filter` and `map` in pipelines.

## Related
- **array-filter** -- Selects elements (reduce combines them).
- **array-map** -- Transforms elements one-to-one (reduce many-to-one).

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Forgetting the start value and getting unexpected results with an empty array.
  **Correction**: Without a start value on an empty array, `reduce` throws an error. Always provide a start value when the array might be empty.

# Common Confusions

- **Confusion**: `reduce` can only sum numbers.
  **Clarification**: `reduce` can combine elements into any type of value -- strings, objects, arrays, etc. The combining function defines the operation.

# Source Reference

Chapter 5: Higher-Order Functions, Section "Summarizing with reduce", lines 420-501 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 429-434)
- Confidence rationale: Explicit section with italicized term "reduce" / "fold"
- Cross-reference status: verified against summary and composability section
