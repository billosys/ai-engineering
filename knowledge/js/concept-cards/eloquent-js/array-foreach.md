---
# === CORE IDENTIFICATION ===
concept: Array forEach
slug: array-foreach

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
section: "Higher-order functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - forEach

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - higher-order-function
extends:
  - higher-order-function
related:
  - array-filter
  - array-map
  - for-loop
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use map, filter, and reduce?"
---

# Quick Definition

`forEach` is a built-in array method that calls a provided function once for each element in the array, providing something like a `for`/`of` loop as a higher-order function.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 275-278 of 05-higher-order-functions.md): "There is a built-in array method, `forEach`, that provides something like a `for`/`of` loop as a higher-order function."

The chapter summary (line 786) adds: "You can use `forEach` to loop over the elements in an array."

# Prerequisites

- **array**: `forEach` is an array method.
- **higher-order-function**: `forEach` takes a function as argument.

# Key Properties

1. Calls the given function for each element in the array.
2. Does not return a useful value (returns `undefined`).
3. Used for side effects (e.g., logging each element).
4. Similar to a `for`/`of` loop but as a method call.

# Construction / Recognition

## To Construct/Create:
```javascript
["A", "B"].forEach(l => console.log(l));
```

## To Identify/Recognize:
- `.forEach(callback)` on an array.

# Context & Application

`forEach` is useful for performing side effects on each element. For transforming data, `map`, `filter`, and `reduce` are usually preferred.

# Examples

**Example 1** (Ch 5, lines 279-283 of 05-higher-order-functions.md):
```javascript
["A", "B"].forEach(l => console.log(l));
// → A
// → B
```

# Relationships

## Builds Upon
- **array** -- Method of arrays.
- **higher-order-function** -- Takes a function as argument.

## Enables
- Iteration patterns without explicit loops.

## Related
- **array-filter** -- Returns filtered array (forEach does not return).
- **array-map** -- Returns transformed array.
- **for-loop** -- `forEach` provides loop-like behavior.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using `forEach` when you need the result (e.g., a new array).
  **Correction**: Use `map` or `filter` when you need a return value. `forEach` returns `undefined`.

# Common Confusions

- **Confusion**: `forEach` and `map` are interchangeable.
  **Clarification**: `forEach` is for side effects; `map` is for transforming and creating a new array.

# Source Reference

Chapter 5: Higher-Order Functions, Section "Higher-order functions", lines 275-283 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 275-278)
- Confidence rationale: Explicit description with example
- Cross-reference status: verified against summary
