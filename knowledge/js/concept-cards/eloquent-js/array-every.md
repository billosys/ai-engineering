---
# === CORE IDENTIFICATION ===
concept: Array every
slug: array-every

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
section: "Exercises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - every
  - Array.prototype.every

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - higher-order-function
  - predicate-function
extends:
  - higher-order-function
related:
  - array-some
  - array-filter
contrasts_with:
  - array-some

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use map, filter, and reduce?"
---

# Quick Definition

The `every` method tests whether all elements in an array pass a given test function, returning `true` only if every element matches.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 822-826 of 05-higher-order-functions.md): "Arrays also have an `every` method analogous to the `some` method. This method returns `true` when the given function returns `true` for *every* element in the array. In a way, `some` is a version of the `||` operator that acts on arrays, and `every` is like the `&&` operator."

# Prerequisites

- **array**: `every` is an array method.
- **higher-order-function**: `every` takes a test function.
- **predicate-function**: The test function returns true/false.

# Key Properties

1. Returns `true` if the test function returns true for **every** element.
2. Returns `false` as soon as one element fails the test (short-circuits).
3. Analogous to the `&&` (AND) operator acting on arrays.
4. Returns `true` for an empty array.

# Construction / Recognition

## To Construct/Create:
```javascript
[1, 2, 3].every(n => n > 0)  // → true
[1, -1, 3].every(n => n > 0) // → false
```

## To Identify/Recognize:
- `.every(callback)` on an array.

# Context & Application

`every` is used for validation -- checking that all elements in a collection meet a requirement.

# Examples

**Example 1** (Ch 5, lines 822-826 of 05-higher-order-functions.md):
The description provides the conceptual model: "`some` is a version of the `||` operator that acts on arrays, and `every` is like the `&&` operator."

# Relationships

## Builds Upon
- **array** -- Method of arrays.
- **higher-order-function** -- Takes a function as argument.

## Enables
- Validation patterns (all elements must pass).

## Related
- **array-filter** -- Returns matching elements; `every` checks if all match.

## Contrasts With
- **array-some** -- `some` checks if any element passes; `every` checks if all pass.

# Common Errors

- **Error**: Assuming `every` returns `false` for empty arrays.
  **Correction**: `every` returns `true` for empty arrays (vacuous truth).

# Common Confusions

- **Confusion**: `every` and `some` behave the same way.
  **Clarification**: `every` is like `&&` (all must pass); `some` is like `||` (at least one must pass).

# Source Reference

Chapter 5: Higher-Order Functions, Exercises section "Everything", lines 819-831 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 822-826)
- Confidence rationale: Explicit description in exercises section
- Cross-reference status: verified against `some` description
