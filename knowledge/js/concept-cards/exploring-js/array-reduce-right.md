---
concept: "Array .reduceRight() Method"
slug: array-reduce-right
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.15.3 .reduceRight(): the end-to-start version of .reduce()"
extraction_confidence: high
aliases:
  - ".reduceRight()"
prerequisites:
  - array-reduce
extends:
  - array-reduce
related: []
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`.reduceRight()` works like `.reduce()` but processes elements from end to start (right to left), which matters when the reduction is not commutative.

# Core Definition

`.reduceRight()` has the same functionality as `.reduce()` but visits elements from end to start. The difference matters when the operation is order-dependent, such as string concatenation.

# Prerequisites

- **array-reduce** -- same API, different direction

# Key Properties

1. Processes elements right to left
2. Same callback signature as `.reduce()`
3. Same `init` parameter behavior
4. Order matters for non-commutative operations

# Construction / Recognition

```js
['a', 'b', 'c'].reduce((acc, x) => acc + x);      // 'abc'
['a', 'b', 'c'].reduceRight((acc, x) => acc + x);  // 'cba'
```

# Context & Application

Use `.reduceRight()` when the fold direction matters, such as right-to-left function composition or reversing accumulation.

# Examples

```js
assert.equal(
  ['a', 'b', 'c'].reduceRight((acc, x) => acc + x),
  'cba'
);
```

(Chapter 34, Section 34.15.3, lines 2168-2185)

# Relationships

## Builds Upon
- **array-reduce** -- right-to-left variant

## Enables
- Right-to-left accumulation patterns

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Using `.reduceRight()` when `.reduce()` suffices for commutative operations.
  **Correction**: For commutative operations (addition, multiplication), `.reduce()` and `.reduceRight()` produce the same result.

# Common Confusions

- **Confusion**: `.reduceRight()` reverses the array.
  **Clarification**: It doesn't reverse the array; it processes elements from end to start.

# Source Reference

Chapter 34: Arrays (Array), Section 34.15.3, lines 2168-2185.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
