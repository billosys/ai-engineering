---
# === CORE IDENTIFICATION ===
concept: Multidimensional Arrays
slug: multidimensional-arrays

# === CLASSIFICATION ===
category: arrays
subcategory: array structure
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 181
section: "7.7 Multidimensional Arrays"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "arrays of arrays"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - reading-writing-array-elements
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I represent matrices or grids in JavaScript?"
---

# Quick Definition

JavaScript does not support true multidimensional arrays, but they can be approximated by nesting arrays within arrays and using chained `[]` operators to access elements.

# Core Definition

"JavaScript does not support true multidimensional arrays, but you can approximate them with arrays of arrays. To access a value in an array of arrays, simply use the [] operator twice." (Flanagan, p. 181)

# Prerequisites

- **array-fundamentals** — Must understand arrays
- **reading-writing-array-elements** — Must understand bracket notation

# Key Properties

1. Implemented as arrays containing arrays
2. Access via chained brackets: `matrix[x][y]`
3. Rows can have different lengths (jagged arrays)
4. Must be manually initialized (nested loops)

# Construction / Recognition

```javascript
let table = new Array(10);
for (let i = 0; i < table.length; i++) {
    table[i] = new Array(10);
}
```

# Context & Application

Used for matrices, grids, game boards, and any two-dimensional data structure.

# Examples

```javascript
let table = new Array(10);
for (let i = 0; i < table.length; i++) {
    table[i] = new Array(10);
}
for (let row = 0; row < table.length; row++) {
    for (let col = 0; col < table[row].length; col++) {
        table[row][col] = row*col;
    }
}
table[5][7]  // => 35
```
(Flanagan, p. 181)

# Relationships

## Builds Upon
- **array-fundamentals** — Arrays containing arrays
- **reading-writing-array-elements** — Chained bracket access

## Enables
- Matrix and grid representations

## Related
- None specific within scope

## Contrasts With
- None specific

# Common Errors

- **Error**: Assuming `new Array(10)` creates 10 sub-arrays.
  **Correction**: You must initialize each row individually with its own array.

# Common Confusions

- **Confusion**: JavaScript has true multidimensional array syntax.
  **Clarification**: JavaScript only has arrays of arrays; there is no native matrix type.

# Source Reference

Chapter 7: Arrays, Section 7.7, page 181.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly stated
- Uncertainties: None
- Cross-reference status: Verified
