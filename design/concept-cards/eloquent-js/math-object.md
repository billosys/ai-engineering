---
# === CORE IDENTIFICATION ===
concept: Math Object
slug: math-object

# === CLASSIFICATION ===
category: data-structures
subcategory: built-in-objects
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "The Math object"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - property
extends: []
related:
  - global-scope
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The `Math` object is a built-in namespace containing number-related utility functions and constants like `Math.max`, `Math.min`, `Math.sqrt`, `Math.random`, `Math.floor`, `Math.ceil`, `Math.round`, `Math.abs`, and `Math.PI`.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 1100-1108 of 04-data-structures-objects-and-arrays.md): "As we've seen, `Math` is a grab bag of number-related utility functions such as `Math.max` (maximum), `Math.min` (minimum), and `Math.sqrt` (square root)." And: "The `Math` object is used as a container to group a bunch of related functionality. There is only one `Math` object, and it is almost never useful as a value. Rather, it provides a *namespace* so that all these functions and values do not have to be global bindings."

# Prerequisites

- **object**: `Math` is an object used as a namespace.
- **property**: Math functions are accessed as properties.

# Key Properties

1. `Math` serves as a **namespace** to avoid polluting global scope.
2. Key functions: `max`, `min`, `sqrt`, `random`, `floor`, `ceil`, `round`, `abs`.
3. Key constants: `Math.PI`.
4. Trigonometric functions: `cos`, `sin`, `tan`, `acos`, `asin`, `atan`.
5. `Math.random()` returns a pseudorandom number between 0 (inclusive) and 1 (exclusive).

# Construction / Recognition

## To Construct/Create:
`Math` is a built-in object; you do not create it.

## To Identify/Recognize:
- Expressions starting with `Math.` followed by a function or constant name.

# Context & Application

The `Math` object is used for mathematical operations throughout JavaScript programs. The concept of using an object as a namespace to avoid global binding pollution is an important pattern.

# Examples

**Example 1** (Ch 4, lines 1135-1143):
```javascript
function randomPointOnCircle(radius) {
  let angle = Math.random() * 2 * Math.PI;
  return {x: radius * Math.cos(angle),
          y: radius * Math.sin(angle)};
}
console.log(randomPointOnCircle(2));
// → {x: 0.3667, y: 1.966}
```

**Example 2** (Ch 4, lines 1179-1182):
```javascript
console.log(Math.floor(Math.random() * 10));
// → 2
```

# Relationships

## Builds Upon
- **object** -- `Math` is an object.
- **property** -- Functions and constants are accessed as properties.

## Enables
- Mathematical computations, random number generation.

## Related
- **global-scope** -- `Math` exists to reduce global namespace pollution.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Calling `Math()` as a function or using `new Math()`.
  **Correction**: `Math` is a plain object, not a constructor. Access its properties directly: `Math.max(1, 2)`.

# Common Confusions

- **Confusion**: `Math.random()` returns integers.
  **Clarification**: `Math.random()` returns a fractional number between 0 and 1. Use `Math.floor(Math.random() * N)` for integers.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "The Math object", lines 1096-1195 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 1100-1108)
- Confidence rationale: Explicit dedicated section
- Cross-reference status: verified within chapter
