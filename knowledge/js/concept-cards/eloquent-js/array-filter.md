---
# === CORE IDENTIFICATION ===
concept: Array filter
slug: array-filter

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
section: "Filtering arrays"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - filter
  - Array.prototype.filter

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - higher-order-function
  - predicate-function
extends:
  - higher-order-function
related:
  - array-map
  - array-reduce
  - array-foreach
  - composability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use map, filter, and reduce?"
---

# Quick Definition

The `filter` method returns a new array containing only the elements that pass a test function, without modifying the original array.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 347-350 of 05-higher-order-functions.md), filter "filters out elements in an array that don't pass a test." Further (lines 373-376): "Note how the `filter` function, rather than deleting elements from the existing array, builds up a new array with only the elements that pass the test. This function is *pure*. It does not modify the array it is given."

The summary (lines 787-788): "The `filter` method returns a new array containing only the elements that pass the predicate function."

# Prerequisites

- **array**: `filter` is an array method.
- **higher-order-function**: `filter` takes a test function as argument.
- **predicate-function**: The test function is a predicate that returns true/false.

# Key Properties

1. Takes a test function (predicate) as argument.
2. Returns a **new array** with elements that pass the test.
3. Does **not** modify the original array (pure function).
4. The test function receives each element and should return a boolean.

# Construction / Recognition

## To Construct/Create:
```javascript
SCRIPTS.filter(s => s.direction == "ttb");
```

## To Identify/Recognize:
- `.filter(callback)` on an array, where callback returns true/false.

# Context & Application

`filter` is one of the three core higher-order array methods (along with `map` and `reduce`). It is used to select subsets of data based on criteria.

# Examples

**Example 1** (Ch 5, lines 352-365 of 05-higher-order-functions.md) -- implementation:
```javascript
function filter(array, test) {
  let passed = [];
  for (let element of array) {
    if (test(element)) {
      passed.push(element);
    }
  }
  return passed;
}
console.log(filter(SCRIPTS, script => script.living));
// → [{name: "Adlam", …}, …]
```

**Example 2** (Ch 5, lines 383-386) -- standard method:
```javascript
console.log(SCRIPTS.filter(s => s.direction == "ttb"));
// → [{name: "Mongolian", …}, …]
```

# Relationships

## Builds Upon
- **array** -- Method of arrays.
- **higher-order-function** -- Takes a function as argument.
- **predicate-function** -- The test function is a predicate.

## Enables
- **composability** -- `filter` chains with `map` and `reduce`.

## Related
- **array-map** -- Transforms elements (filter selects them).
- **array-reduce** -- Combines elements into a single value.
- **array-some** -- Tests if any element passes (filter returns all that pass).

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Expecting `filter` to modify the original array.
  **Correction**: `filter` returns a **new** array. The original is unchanged.

# Common Confusions

- **Confusion**: `filter` and `find` do the same thing.
  **Clarification**: `filter` returns **all** matching elements as an array; `find` returns only the **first** matching element (or `undefined`).

# Source Reference

Chapter 5: Higher-Order Functions, Section "Filtering arrays", lines 344-386 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 347-350 and 373-376)
- Confidence rationale: Explicit section with implementation and standard usage
- Cross-reference status: verified against summary and composability section
