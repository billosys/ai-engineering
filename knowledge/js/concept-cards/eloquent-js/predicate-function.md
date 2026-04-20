---
# === CORE IDENTIFICATION ===
concept: Predicate Function
slug: predicate-function

# === CLASSIFICATION ===
category: higher-order-programming
subcategory: function-patterns
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Higher-Order Functions"
chapter_number: 5
pdf_page: null
section: "Summary"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - test function
  - predicate

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - boolean
extends: []
related:
  - array-filter
  - array-some
  - array-every
  - array-find
  - higher-order-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use map, filter, and reduce?"
---

# Quick Definition

A predicate function is a function that returns a boolean value, used as a test to determine whether an element satisfies a condition. It is the argument type expected by `filter`, `some`, `every`, and `find`.

# Core Definition

As described in the "Eloquent JavaScript" summary (Ch 5, lines 787-793 of 05-higher-order-functions.md): "The `filter` method returns a new array containing only the elements that pass the predicate function... The `some` method tests whether any element matches a given predicate function, while `find` finds the first element that matches a predicate."

# Prerequisites

- **function-definition**: Predicate functions are functions.
- **boolean**: Predicate functions return boolean values.

# Key Properties

1. Returns `true` or `false`.
2. Used as the "test" argument in `filter`, `some`, `every`, and `find`.
3. Receives an array element as argument.
4. Determines inclusion/exclusion criteria.

# Construction / Recognition

## To Construct/Create:
```javascript
// A predicate testing if a script is living
s => s.living

// A predicate testing if a number is even
n => n % 2 == 0
```

## To Identify/Recognize:
- A function passed to `filter`, `some`, `every`, or `find`.
- A function that returns a boolean.

# Context & Application

Predicate functions are the standard pattern for expressing conditions in higher-order programming. They decouple the "what to test" from the "how to iterate."

# Examples

**Example 1** (Ch 5, lines 383-386):
```javascript
SCRIPTS.filter(s => s.direction == "ttb")
```
Here `s => s.direction == "ttb"` is the predicate.

**Example 2** (Ch 5, lines 602-604):
```javascript
script.ranges.some(([from, to]) => {
  return code >= from && code < to;
})
```

# Relationships

## Builds Upon
- **function-definition** -- Predicate functions are functions.
- **boolean** -- They return booleans.

## Enables
- **array-filter**, **array-some**, **array-every**, **array-find** -- All use predicates.

## Related
- **higher-order-function** -- Predicates are passed to higher-order functions.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Writing a predicate that returns a non-boolean (truthy/falsy) value without realizing it.
  **Correction**: While JavaScript coerces truthy/falsy, it is clearer to return explicit booleans from predicates.

# Common Confusions

- **Confusion**: Predicates and transformation functions are the same.
  **Clarification**: Predicates return booleans (used with `filter`, `some`). Transformation functions return transformed values (used with `map`).

# Source Reference

Chapter 5: Higher-Order Functions, Summary, lines 787-793 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: synthesized from summary usage of term "predicate function"
- Confidence rationale: Term used explicitly in summary
- Cross-reference status: verified against filter, some, and find sections
