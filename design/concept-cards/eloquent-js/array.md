---
# === CORE IDENTIFICATION ===
concept: Array
slug: array

# === CLASSIFICATION ===
category: data-structures
subcategory: collections
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Datasets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - arrays
  - list (informal)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
  - number
extends: []
related:
  - object
  - property
  - array-methods
  - mutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create and manipulate an array?"
  - "How do arrays relate to objects in JavaScript?"
---

# Quick Definition

An array is a JavaScript data type for storing ordered sequences of values, written as a list of values between square brackets separated by commas.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 109-112 of 04-data-structures-objects-and-arrays.md): "Fortunately, JavaScript provides a data type specifically for storing sequences of values. It is called an *array* and is written as a list of values between square brackets, separated by commas."

Further (lines 380-384): "Arrays, then, are just a kind of object specialized for storing sequences of things. If you evaluate `typeof []`, it produces `'object'`."

# Prerequisites

- **value**: Arrays store values.
- **number**: Array indices are numbers (zero-based).

# Key Properties

1. Written with square brackets: `[2, 3, 5, 7, 11]`.
2. Elements accessed by **zero-based index**: `arr[0]` is the first element.
3. "Think of the index as the number of items to skip, counting from the start" (line 136).
4. Arrays are objects under the hood (`typeof [] === "object"`).
5. Have a `length` property indicating the number of elements.
6. Elements are stored as properties with numeric names.

# Construction / Recognition

## To Construct/Create:
```javascript
let listOfNumbers = [2, 3, 5, 7, 11];
```

## To Identify/Recognize:
- Square bracket notation with comma-separated values.
- `typeof` returns `"object"`.

# Context & Application

Arrays are the primary data structure for ordered collections in JavaScript. They are essential for storing lists of data, iterating over elements, and working with higher-order functions like `map`, `filter`, and `reduce`.

# Examples

**Example 1** (Ch 4, lines 114-122 of 04-data-structures-objects-and-arrays.md):
```javascript
let listOfNumbers = [2, 3, 5, 7, 11];
console.log(listOfNumbers[2]);
// → 5
console.log(listOfNumbers[0]);
// → 2
console.log(listOfNumbers[2 - 1]);
// → 3
```

# Relationships

## Builds Upon
- **value** -- Arrays store values of any type.
- **number** -- Array indices are numbers.

## Enables
- **array-methods** -- push, pop, slice, indexOf, etc.
- **higher-order-function** -- forEach, filter, map, reduce operate on arrays.

## Related
- **object** -- Arrays are a specialized kind of object.
- **property** -- Array elements are properties with numeric names.

## Contrasts With
- None within this source (implicitly contrasts with objects, which use named properties).

# Common Errors

- **Error**: Forgetting that array indices start at 0, not 1.
  **Correction**: The first element is at index 0: `arr[0]`.

# Common Confusions

- **Confusion**: Arrays and objects are completely different types.
  **Clarification**: "Arrays, then, are just a kind of object specialized for storing sequences of things."

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Datasets", lines 93-137 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 109-112)
- Confidence rationale: Explicit definition with italicized term "array"
- Cross-reference status: verified against objects section
