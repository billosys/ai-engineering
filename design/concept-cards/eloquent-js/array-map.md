---
# === CORE IDENTIFICATION ===
concept: Array map
slug: array-map

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
section: "Transforming with map"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - map
  - Array.prototype.map

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - higher-order-function
extends:
  - higher-order-function
related:
  - array-filter
  - array-reduce
  - composability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use map, filter, and reduce?"
---

# Quick Definition

The `map` method transforms an array by applying a function to every element, building a new array of the same length from the returned values.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 396-400 of 05-higher-order-functions.md): "The `map` method transforms an array by applying a function to all of its elements and building a new array from the returned values. The new array will have the same length as the input array, but its content will have been *mapped* to a new form by the function."

The summary (lines 789-790): "You can transform an array by putting each element through a function using `map`."

# Prerequisites

- **array**: `map` is an array method.
- **higher-order-function**: `map` takes a transformation function as argument.

# Key Properties

1. Takes a transformation function as argument.
2. Returns a **new array** with the same length.
3. Each element is passed through the function; the return value becomes the new element.
4. Does not modify the original array.
5. `map` is a standard array method.

# Construction / Recognition

## To Construct/Create:
```javascript
let names = SCRIPTS.filter(s => s.direction == "rtl").map(s => s.name);
```

## To Identify/Recognize:
- `.map(callback)` on an array, where callback transforms each element.

# Context & Application

`map` is one of the three core higher-order array methods. It is used when you need to transform every element of an array into something else (e.g., extracting a property, computing a derived value).

# Examples

**Example 1** (Ch 5, lines 402-414 of 05-higher-order-functions.md) -- implementation and usage:
```javascript
function map(array, transform) {
  let mapped = [];
  for (let element of array) {
    mapped.push(transform(element));
  }
  return mapped;
}

let rtlScripts = SCRIPTS.filter(s => s.direction == "rtl");
console.log(map(rtlScripts, s => s.name));
// → ["Adlam", "Arabic", "Imperial Aramaic", …]
```

**Example 2** (Ch 5, lines 538-539) -- in a pipeline:
```javascript
SCRIPTS.filter(s => s.living).map(s => s.year)
```

# Relationships

## Builds Upon
- **array** -- Method of arrays.
- **higher-order-function** -- Takes a function as argument.

## Enables
- **composability** -- `map` chains with `filter` and `reduce`.

## Related
- **array-filter** -- Selects elements (map transforms them).
- **array-reduce** -- Combines elements (map transforms one-to-one).

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using `map` for side effects instead of `forEach`.
  **Correction**: `map` is for creating a new transformed array. Use `forEach` for side effects.

# Common Confusions

- **Confusion**: `map` modifies the original array.
  **Clarification**: `map` returns a new array; the original is unchanged.

# Source Reference

Chapter 5: Higher-Order Functions, Section "Transforming with map", lines 388-418 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 396-400)
- Confidence rationale: Explicit section with implementation and standard usage
- Cross-reference status: verified against summary and composability section
