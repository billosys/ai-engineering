---
# === CORE IDENTIFICATION ===
concept: Array some
slug: array-some

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
section: "Strings and character codes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - some
  - Array.prototype.some

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - higher-order-function
  - predicate-function
extends:
  - higher-order-function
related:
  - array-every
  - array-filter
contrasts_with:
  - array-every

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use map, filter, and reduce?"
---

# Quick Definition

The `some` method tests whether any element in an array passes a given test function, returning `true` if at least one element matches.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 616-618 of 05-higher-order-functions.md): "The `some` method is another higher-order function. It takes a test function and tells you whether that function returns true for any of the elements in the array."

The summary (lines 791-792): "The `some` method tests whether any element matches a given predicate function."

# Prerequisites

- **array**: `some` is an array method.
- **higher-order-function**: `some` takes a test function.
- **predicate-function**: The test function returns true/false.

# Key Properties

1. Returns `true` if the test function returns true for **any** element.
2. Returns `false` if no element passes the test.
3. Short-circuits: stops iterating once a true result is found.
4. Analogous to the `||` (OR) operator acting on arrays (Ch 5, line 825).

# Construction / Recognition

## To Construct/Create:
```javascript
script.ranges.some(([from, to]) => {
  return code >= from && code < to;
})
```

## To Identify/Recognize:
- `.some(callback)` on an array.

# Context & Application

`some` is used to check if at least one element in an array meets a condition. In Ch 5, it is used in the `characterScript` function to check if a character code falls within any of a script's ranges.

# Examples

**Example 1** (Ch 5, lines 599-613 of 05-higher-order-functions.md):
```javascript
function characterScript(code) {
  for (let script of SCRIPTS) {
    if (script.ranges.some(([from, to]) => {
      return code >= from && code < to;
    })) {
      return script;
    }
  }
  return null;
}
console.log(characterScript(121));
// → {name: "Latin", …}
```

# Relationships

## Builds Upon
- **array** -- Method of arrays.
- **higher-order-function** -- Takes a function as argument.

## Enables
- Existence checks on array elements.

## Related
- **array-filter** -- Returns all matches; `some` just checks existence.

## Contrasts With
- **array-every** -- `every` requires all elements to pass; `some` requires at least one.

# Common Errors

- **Error**: Using `some` when you need the matching element.
  **Correction**: Use `find` to get the element itself, not just a boolean.

# Common Confusions

- **Confusion**: `some` and `includes` are the same.
  **Clarification**: `includes` checks for a specific value; `some` checks against a condition (predicate function).

# Source Reference

Chapter 5: Higher-Order Functions, Section "Strings and character codes", lines 616-618 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 616-618)
- Confidence rationale: Explicit description with example usage
- Cross-reference status: verified against summary and `every` exercise
