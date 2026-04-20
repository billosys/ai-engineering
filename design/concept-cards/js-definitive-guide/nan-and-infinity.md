---
# === CORE IDENTIFICATION ===
concept: NaN and Infinity
slug: nan-and-infinity

# === CLASSIFICATION ===
category: type-system
subcategory: primitive-types
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 45
section: "3.2.3 Arithmetic in JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - not-a-number
  - positive infinity
  - negative infinity
  - negative zero

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - type-coercion
  - boolean-truthy-falsy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

JavaScript defines special numeric values `NaN` (not-a-number), `Infinity`, `-Infinity`, and `-0` to handle mathematical edge cases like division by zero, overflow, and invalid numeric operations.

# Core Definition

"Arithmetic in JavaScript does not raise errors in cases of overflow, underflow, or division by zero." Overflow produces `Infinity` or `-Infinity`. Underflow produces `0` or `-0`. Division by zero returns infinity (except 0/0 which returns `NaN`). "NaN also arises if you attempt to divide infinity by infinity, take the square root of a negative number, or use arithmetic operators with non-numeric operands that cannot be converted to numbers." NaN "does not compare equal to any other value, including itself." (pp. 45-47)

# Prerequisites

- **number-type** — NaN and Infinity are special Number values

# Key Properties

1. `Infinity`: result of overflow or division of non-zero by zero
2. `-Infinity`: negative overflow
3. `NaN`: result of 0/0, Infinity/Infinity, sqrt of negative, or non-numeric arithmetic
4. `-0`: negative underflow; compares equal to `0` with `===`
5. NaN does NOT equal itself: `NaN === NaN` is `false`
6. Use `Number.isNaN(x)` or `x !== x` to test for NaN
7. NaN is falsy; Infinity is truthy
8. ES6 functions: `Number.isNaN()`, `Number.isFinite()`, `Number.isInteger()`, `Number.isSafeInteger()`

# Construction / Recognition

```javascript
Infinity            // Positive infinity
-Infinity           // Negative infinity
NaN                 // Not-a-number
-0                  // Negative zero

1/0                 // => Infinity
-1/0                // => -Infinity
0/0                 // => NaN
Infinity/Infinity   // => NaN
Number.MIN_VALUE/2  // => 0 (underflow)
-Number.MIN_VALUE/2 // => -0 (negative zero)
```

# Context & Application

Understanding these special values is critical for robust numeric programming. NaN propagates through calculations (any operation with NaN produces NaN), so it can silently corrupt results if not detected. Testing for NaN requires special handling since `=== NaN` never works.

# Examples

From the source text (pp. 45-47):
```javascript
Infinity                 // A positive number too big to represent
Number.POSITIVE_INFINITY // Same value
1/0                      // => Infinity
Number.MAX_VALUE * 2     // => Infinity; overflow
NaN                      // The not-a-number value
0/0                      // => NaN
Infinity/Infinity        // => NaN

// NaN is not equal to itself
let x = NaN;
x === NaN                // => false
x !== x                  // => true (only NaN has this property)
Number.isNaN(x)          // => true

// Negative zero
let zero = 0;
let negz = -0;
zero === negz            // => true
1/zero === 1/negz        // => false: Infinity vs -Infinity
```

# Relationships

## Builds Upon
- **number-type** — These are special Number values

## Enables
- Robust error handling in numeric computations

## Related
- **type-coercion** — NaN results from failed numeric conversions
- **boolean-truthy-falsy** — NaN is falsy, Infinity is truthy

## Contrasts With
- None within this source

# Common Errors

- **Error**: Testing for NaN with `x === NaN`.
  **Correction**: NaN is not equal to itself. Use `Number.isNaN(x)` or `x !== x` instead.

- **Error**: Assuming `-0 === 0` means they are identical in all contexts.
  **Correction**: While `===` returns true, `1/0` is `Infinity` while `1/-0` is `-Infinity`.

# Common Confusions

- **Confusion**: `NaN` means "no numeric value exists."
  **Clarification**: NaN is itself a numeric value (of type Number) — it represents the result of an undefined or invalid mathematical operation.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.2.3, pages 45-47.

# Verification Notes

- Definition source: Direct quotes from pp. 45-47
- Confidence rationale: High — thoroughly explained with examples
- Uncertainties: None
- Cross-reference status: Verified
