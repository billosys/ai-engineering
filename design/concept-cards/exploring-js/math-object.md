---
# === CORE IDENTIFICATION ===
concept: Math Object
slug: math-object

# === CLASSIFICATION ===
category: primitive-types
subcategory: numbers
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Math"
chapter_number: 19
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Math namespace"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - math-rounding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

`Math` is a built-in namespace object containing mathematical constants (like `Math.PI` and `Math.E`) and functions (like `Math.sqrt()`, `Math.abs()`, `Math.random()`) for processing numbers.

# Core Definition

"`Math` is an object with data properties and methods for processing numbers. You can see it as a poor man's module: It was created long before JavaScript had modules" (Ch. 19, introduction). It provides constants like `Math.PI` (~3.14159) and `Math.E` (~2.71828), plus functions for exponents, roots, logarithms, rounding, trigonometry, and more.

# Prerequisites

- **number-type** -- Math functions operate on numbers

# Key Properties

1. Not a constructor -- cannot use `new Math()`
2. Constants: `Math.PI`, `Math.E`, `Math.LN2`, `Math.LN10`, `Math.SQRT2`, etc. (ES1)
3. Functions: `Math.abs()`, `Math.sqrt()`, `Math.pow()`, `Math.log()`, `Math.random()`, etc.
4. `Math.random()` returns pseudo-random number in [0, 1)
5. `Math.min()` and `Math.max()` accept variadic arguments
6. `Math.sign()` returns -1, 0, or 1 (ES6)

# Construction / Recognition

```js
Math.PI          // 3.141592653589793
Math.sqrt(9)     // 3
Math.abs(-3)     // 3
Math.random()    // e.g., 0.7234...
Math.max(3, -5, 24) // 24
```

# Context & Application

`Math` is the standard utility for mathematical operations in JavaScript. Trigonometric functions use radians, not degrees.

# Examples

From the source text:

```js
> Math.sqrt(9)
3
> Math.pow(2, 3)
8
> Math.abs(-3)
3
> Math.max(3, -5, 24)
24
> Math.min(3, -5, 24)
-5
> Math.sign(-8)
-1

// Degree conversion
function degreesToRadians(degrees) {
  return degrees / 180 * Math.PI;
}
assert.equal(degreesToRadians(90), Math.PI/2);
```

# Relationships

## Builds Upon
- **number-type** — Math functions operate on numbers

## Enables
- **math-rounding** — rounding functions
- Mathematical computations

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Passing degrees to trigonometric functions
  **Correction**: `Math.sin()`, `Math.cos()`, etc. expect radians. Convert with `degrees / 180 * Math.PI`.

# Common Confusions

- **Confusion**: Thinking `Math.random()` produces cryptographically secure random numbers
  **Clarification**: `Math.random()` is pseudo-random and not suitable for security. Use `crypto.getRandomValues()` for cryptographic randomness.

# Source Reference

Chapter 19: Math, lines 1-767.

# Verification Notes

- Definition source: direct
- Confidence rationale: Comprehensive API reference in source
- Cross-reference status: verified
