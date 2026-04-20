---
concept: Fixed-Layout vs. Sequence Arrays
slug: array-fixed-layout-vs-sequence
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.2 Ways of using Arrays: fixed layout vs. sequence"
extraction_confidence: high
aliases:
  - "tuple array"
  - "list array"
prerequisites:
  - array-creation
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

Arrays serve two roles: fixed-layout arrays (like tuples) have a fixed number of elements of potentially different types, while sequence arrays have a variable number of elements of the same type and serve as lists, stacks, or queues.

# Core Definition

Fixed-layout Arrays have a fixed number of indexed elements where each element can have a different type (e.g., key-value pairs from `Object.entries()`). Sequence Arrays have a variable number of elements of the same type and are used as traditional arrays, stacks, and queues.

# Prerequisites

- **array-creation** -- basic array understanding

# Key Properties

1. Fixed-layout: fixed count, mixed types (tuple-like)
2. Sequence: variable count, uniform type (list-like)
3. `Object.entries()` returns a sequence of fixed-layout pairs
4. JavaScript uses arrays for both roles (no separate tuple type)

# Construction / Recognition

```js
// Fixed-layout (tuple): [string, number]
const entry = ['key', 42];

// Sequence (list): number[]
const numbers = [1, 2, 3, 4, 5];
```

# Context & Application

Recognizing which role an array plays helps choose appropriate operations: fixed-layout arrays are typically destructured; sequence arrays are mapped, filtered, and iterated.

# Examples

```js
// Object.entries returns sequence of fixed-layout pairs
Object.entries({a: 1, b: 2});
// [ ['a', 1], ['b', 2] ]
// Outer: sequence; inner: fixed-layout
```

(Chapter 34, Section 34.2, lines 374-401)

# Relationships

## Builds Upon
- **array-creation** -- conceptual framework for array usage

## Enables
- Choosing appropriate array operations

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Treating a fixed-layout array like a sequence (e.g., filtering key-value pairs by index).
  **Correction**: Destructure fixed-layout arrays; iterate/transform sequence arrays.

# Common Confusions

- **Confusion**: JavaScript has a separate tuple type.
  **Clarification**: JavaScript uses Arrays for both tuples and lists. TypeScript distinguishes them at the type level.

# Source Reference

Chapter 34: Arrays (Array), Section 34.2, lines 374-401.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
