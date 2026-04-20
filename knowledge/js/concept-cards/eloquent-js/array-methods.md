---
# === CORE IDENTIFICATION ===
concept: Array Methods
slug: array-methods

# === CLASSIFICATION ===
category: data-structures
subcategory: array-operations
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Further arrayology"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - array operations

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - method
extends: []
related:
  - array-filter
  - array-map
  - array-reduce
  - object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create and manipulate an array?"
---

# Quick Definition

Arrays provide built-in methods for adding, removing, searching, and slicing elements, including `push`, `pop`, `shift`, `unshift`, `indexOf`, `lastIndexOf`, `includes`, `slice`, and `concat`.

# Core Definition

Arrays in JavaScript have numerous built-in methods for manipulation. As described in "Eloquent JavaScript" (Ch 4): `push` and `pop` add/remove from the end (lines 243-245); `unshift` and `shift` add/remove from the start (lines 844-845); `indexOf` and `lastIndexOf` search for values (lines 870-873); `includes` checks for presence (lines 672-674); `slice` extracts sub-arrays (lines 887-890); `concat` joins arrays (lines 905-907).

# Prerequisites

- **array**: These methods operate on arrays.
- **method**: Array methods are properties that hold functions.

# Key Properties

1. **push/pop**: Add/remove from the end of an array.
2. **unshift/shift**: Add/remove from the start of an array.
3. **indexOf/lastIndexOf**: Search for a value and return its index (or -1).
4. **includes**: Returns `true` if the array contains a given value.
5. **slice**: Returns a sub-array between start (inclusive) and end (exclusive).
6. **concat**: Creates a new array by joining arrays together.

# Construction / Recognition

## To Construct/Create:
```javascript
let arr = [1, 2, 3];
arr.push(4);        // [1, 2, 3, 4]
arr.pop();          // returns 4, arr is [1, 2, 3]
arr.unshift(0);     // [0, 1, 2, 3]
arr.shift();        // returns 0, arr is [1, 2, 3]
```

## To Identify/Recognize:
- Method calls on array values using dot notation.

# Context & Application

Array methods are the primary tools for manipulating ordered collections in JavaScript. Push/pop implement stack behavior; shift/push implement queue behavior.

# Examples

**Example 1** (Ch 4, lines 230-240 of 04-data-structures-objects-and-arrays.md) -- push and pop:
```javascript
let sequence = [1, 2, 3];
sequence.push(4);
sequence.push(5);
console.log(sequence);
// → [1, 2, 3, 4, 5]
console.log(sequence.pop());
// → 5
```

**Example 2** (Ch 4, lines 875-880) -- indexOf and lastIndexOf:
```javascript
console.log([1, 2, 3, 2, 1].indexOf(2));
// → 1
console.log([1, 2, 3, 2, 1].lastIndexOf(2));
// → 3
```

**Example 3** (Ch 4, lines 892-897) -- slice:
```javascript
console.log([0, 1, 2, 3, 4].slice(2, 4));
// → [2, 3]
console.log([0, 1, 2, 3, 4].slice(2));
// → [2, 3, 4]
```

**Example 4** (Ch 4, lines 915-921) -- concat and slice together:
```javascript
function remove(array, index) {
  return array.slice(0, index)
    .concat(array.slice(index + 1));
}
console.log(remove(["a", "b", "c", "d", "e"], 2));
// → ["a", "b", "d", "e"]
```

# Relationships

## Builds Upon
- **array** -- These methods operate on arrays.
- **method** -- Array methods are methods.

## Enables
- More complex data manipulation patterns.
- **array-filter**, **array-map**, **array-reduce** -- Higher-order array methods (Ch 5).

## Related
- **object** -- `Object.keys` and `Object.assign` are related utility functions.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Expecting `indexOf` to return `undefined` when not found.
  **Correction**: `indexOf` returns `-1` when the value is not found.

# Common Confusions

- **Confusion**: `push`/`pop` and `shift`/`unshift` names are arbitrary.
  **Clarification**: "These somewhat silly names are the traditional terms for operations on a *stack*." Push/pop operate on the end (stack); shift/unshift operate on the start.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Sections "Methods" and "Further arrayology", lines 194-927 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: synthesized from multiple method descriptions across Ch 4
- Confidence rationale: Multiple explicit descriptions of each method
- Cross-reference status: verified within chapter
