---
concept: Array Element Callbacks
slug: array-element-callbacks
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.13 Array methods that accept element callbacks"
extraction_confidence: high
aliases:
  - "callback signature"
  - "element callback"
prerequisites:
  - array-creation
extends: []
related:
  - array-map
  - array-filter
  - array-reduce
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

Many Array methods accept an element callback with signature `(value, index, array) => result`, where only `value` is required and the callback's expected return type varies by method.

# Core Definition

Array methods that accept callbacks feed Array elements to them. The common callback signature is `(value: T, index: number, array: Array<T>) => ResultType`. Methods are grouped by purpose: finding (`.find`, `.findIndex`), transforming (`.map`, `.filter`, `.flatMap`), computing summaries (`.every`, `.some`, `.reduce`), and looping (`.forEach`).

# Prerequisites

- **array-creation** -- callback methods operate on arrays

# Key Properties

1. Callback receives (value, index, array) -- can ignore any
2. Finding: .find(), .findLast(), .findIndex(), .findLastIndex()
3. Transforming: .map(), .filter(), .flatMap()
4. Summaries: .every(), .some(), .reduce(), .reduceRight()
5. Looping: .forEach()
6. Return type depends on the method

# Construction / Recognition

```js
// .map() expects a return value
[1, 2, 3].map(x => x * 2);

// .find() expects a boolean
['a', 'bb'].find(str => str.length >= 2);
```

# Context & Application

Understanding the common callback pattern helps learn all callback-accepting methods at once. The three parameters cover most use cases.

# Examples

```js
// Using all three callback parameters
['a', 'b', 'c'].map((value, index, array) => {
  return `${index}:${value} of ${array.length}`;
});
// ['0:a of 3', '1:b of 3', '2:c of 3']
```

(Chapter 34, Section 34.13, lines 1642-1702)

# Relationships

## Builds Upon
- **array-creation** -- pattern used by array methods

## Enables
- Understanding all callback-based array methods uniformly

## Related
- **array-map** -- uses element callbacks
- **array-filter** -- uses element callbacks
- **array-reduce** -- uses a different callback pattern (accumulator)

## Contrasts With
- None

# Common Errors

- **Error**: Passing a function that expects different parameter order (e.g., `parseInt` to `.map()`).
  **Correction**: Be aware that `.map()` passes (value, index, array). `['1','2'].map(Number)` is safe; `['1','2'].map(parseInt)` is not.

# Common Confusions

- **Confusion**: `.forEach()` and `.map()` are interchangeable.
  **Clarification**: `.map()` returns a new array of results; `.forEach()` returns undefined and is for side effects.

# Source Reference

Chapter 34: Arrays (Array), Section 34.13, lines 1642-1702.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with type signature
- Cross-reference status: verified
