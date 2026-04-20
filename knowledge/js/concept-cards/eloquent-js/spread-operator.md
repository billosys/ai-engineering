---
# === CORE IDENTIFICATION ===
concept: Spread Operator
slug: spread-operator

# === CLASSIFICATION ===
category: data-structures
subcategory: syntax
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Rest parameters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - spread syntax
  - triple-dot operator

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - rest-parameters
extends: []
related:
  - rest-parameters
  - object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The spread operator (`...`) expands an array or object into individual elements in function calls, array literals, or object literals.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 1059-1070 of 04-data-structures-objects-and-arrays.md): "You can use a similar three-dot notation to *call* a function with an array of arguments." This "'spreads' out the array into the function call, passing its elements as separate arguments." It also works in array literals (lines 1075-1083) and object literals (lines 1086-1094).

# Prerequisites

- **array**: Spread can expand arrays.
- **rest-parameters**: Same syntax but different direction (spread expands, rest collects).

# Key Properties

1. In function calls: `max(...numbers)` passes array elements as individual arguments.
2. In array literals: `["will", ...words, "understand"]` inserts elements.
3. In object literals: `{...coordinates, y: 5}` copies properties (last value wins).
4. Uses the same `...` syntax as rest parameters but in a different context.

# Construction / Recognition

## To Construct/Create:
```javascript
// In function calls
let numbers = [5, 1, 7];
console.log(max(...numbers)); // → 7

// In array literals
let words = ["never", "fully"];
console.log(["will", ...words, "understand"]);
// → ["will", "never", "fully", "understand"]

// In object literals
let coordinates = {x: 10, y: 0};
console.log({...coordinates, y: 5, z: 1});
// → {x: 10, y: 5, z: 1}
```

## To Identify/Recognize:
- `...` used inside a function call, array literal, or object literal (not in parameter position).

# Context & Application

The spread operator is used for array copying, merging objects, passing arrays as arguments, and constructing new arrays/objects from existing ones.

# Examples

**Example 1** (Ch 4, lines 1062-1066):
```javascript
let numbers = [5, 1, 7];
console.log(max(...numbers));
// → 7
```

**Example 2** (Ch 4, lines 1079-1083):
```javascript
let words = ["never", "fully"];
console.log(["will", ...words, "understand"]);
// → ["will", "never", "fully", "understand"]
```

**Example 3** (Ch 4, lines 1090-1094):
```javascript
let coordinates = {x: 10, y: 0};
console.log({...coordinates, y: 5, z: 1});
// → {x: 10, y: 5, z: 1}
```

# Relationships

## Builds Upon
- **array** -- Spreads arrays.
- **rest-parameters** -- Same syntax, opposite direction.

## Enables
- Immutable update patterns for objects and arrays.

## Related
- **object** -- Spread works with objects.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Confusing spread (expanding) with rest (collecting).
  **Correction**: In a parameter position, `...` collects (rest). In a call/literal position, `...` expands (spread).

# Common Confusions

- **Confusion**: Spread creates deep copies of objects.
  **Clarification**: Spread creates a **shallow** copy. Nested objects are still shared by reference.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Rest parameters", lines 1058-1094 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (paraphrased from lines 1059-1094)
- Confidence rationale: Explicit examples in three contexts
- Cross-reference status: verified within chapter
