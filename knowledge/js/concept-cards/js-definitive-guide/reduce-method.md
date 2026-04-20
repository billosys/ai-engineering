---
# === CORE IDENTIFICATION ===
concept: reduce() and reduceRight()
slug: reduce-method

# === CLASSIFICATION ===
category: arrays
subcategory: array methods
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 185
section: "7.8.1 Array Iterator Methods - reduce() and reduceRight()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "fold"
  - "inject"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - map-method
extends: []
related:
  - foreach-method
  - higher-order-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I combine all elements of an array into a single value?"
---

# Quick Definition

`reduce()` combines array elements into a single value by repeatedly applying a function that takes an accumulator and the current element; `reduceRight()` processes from right to left.

# Core Definition

"The reduce() and reduceRight() methods combine the elements of an array, using the function you specify, to produce a single value. This is a common operation in functional programming and also goes by the names 'inject' and 'fold.'" The reduction function receives (accumulator, value, index, array). The optional second argument to reduce() is the initial accumulator value; without it, the first element is used. (Flanagan, p. 185-186)

# Prerequisites

- **array-fundamentals** — Must understand arrays
- **map-method** — Understanding functional array methods

# Key Properties

1. Reduces array to a single value
2. Callback: (accumulator, value, index, array)
3. Optional initial value as second argument to reduce()
4. Without initial value, first element is used as accumulator
5. Empty array with no initial value throws TypeError
6. reduceRight() processes from highest index to lowest
7. Neither accepts a `this` argument for the callback

# Construction / Recognition

```javascript
let result = array.reduce((acc, val) => acc + val, initialValue);
let result = array.reduceRight((acc, val) => fn(val, acc));
```

# Context & Application

Used for aggregation (sums, products, max/min), accumulating values, and building composite results from arrays. Central to functional programming patterns.

# Examples

```javascript
let a = [1,2,3,4,5];
a.reduce((x,y) => x+y, 0)          // => 15; the sum
a.reduce((x,y) => x*y, 1)          // => 120; the product
a.reduce((x,y) => (x > y) ? x : y) // => 5; the largest

// reduceRight for right-to-left associativity:
let a = [2, 3, 4];
a.reduceRight((acc,val) => Math.pow(val,acc))  // => 2.4178516392292583e+24
```
(Flanagan, p. 185-186)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype
- **map-method** — Both are functional array processing methods

## Enables
- **higher-order-functions** — Reduce is a key higher-order function pattern
- Functional programming computations

## Related
- **foreach-method** — Iterative counterpart (side-effect based)

## Contrasts With
- None specific

# Common Errors

- **Error**: Calling reduce() on an empty array with no initial value.
  **Correction**: Always provide an initial value when the array might be empty, or handle the TypeError.

# Common Confusions

- **Confusion**: reduce() is only for numeric operations.
  **Clarification**: reduce() can combine any two values into one of the same type, including objects and strings.

# Source Reference

Chapter 7: Arrays, Section 7.8.1, pages 185-186.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
