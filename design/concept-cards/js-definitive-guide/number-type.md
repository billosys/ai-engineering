---
# === CORE IDENTIFICATION ===
concept: Number Type
slug: number-type

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
pdf_page: 42
section: "3.2 Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Number
  - "IEEE 754"
  - double-precision floating-point

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-vs-object-types
  - literals
extends: []
related:
  - integer-literals
  - floating-point-literals
  - nan-and-infinity
  - bigint-type
contrasts_with:
  - bigint-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

JavaScript's Number type uses 64-bit IEEE 754 floating-point format to represent both integers and real numbers, with exact integer representation between -2^53 and 2^53.

# Core Definition

"JavaScript's primary numeric type, Number, is used to represent integers and to approximate real numbers. JavaScript represents numbers using the 64-bit floating-point format defined by the IEEE 754 standard, which means it can represent numbers as large as +/-1.7976931348623157 x 10^308 and as small as +/-5 x 10^-324." It "allows you to exactly represent all integers between -9,007,199,254,740,992 (-2^53) and 9,007,199,254,740,992 (2^53), inclusive." (p. 42)

# Prerequisites

- **primitive-vs-object-types** — Number is a primitive type
- **literals** — Numbers are written as numeric literals

# Key Properties

1. 64-bit IEEE 754 floating-point format (same as `double` in Java/C++)
2. Exact integer range: -2^53 to 2^53
3. Some operations (array indexing, bitwise) use 32-bit integers
4. Arithmetic does not raise errors for overflow, underflow, or division by zero
5. Special values: Infinity, -Infinity, NaN, -0
6. Supports underscores as numeric separators: `1_000_000`

# Construction / Recognition

Numbers appear as numeric literals or result from arithmetic operations. The `typeof` operator returns `"number"` for Number values.

# Context & Application

The Number type is used for all general-purpose numeric computation in JavaScript. For integers larger than 2^53, use BigInt instead. For financial calculations, be aware of floating-point rounding errors.

# Examples

From the source text (pp. 42-47):
```javascript
// Various number representations
0xff                    // => 255: hexadecimal
0b10101                 // => 21: binary (ES6)
0o377                   // => 255: octal (ES6)
3.14                    // floating-point
6.02e23                 // exponential notation
1_000_000_000           // underscore separators

// Math object
Math.pow(2,53)          // => 9007199254740992
Math.PI                 // => 3.141592653589793
Math.sqrt(3)            // => 1.7320508075688772

// Special values
Infinity                // overflow result
-Infinity               // negative overflow
NaN                     // not-a-number
-0                      // negative zero
```

# Relationships

## Builds Upon
- **primitive-vs-object-types** — Number is a primitive type
- **literals** — Numbers are written as literals

## Enables
- **integer-literals** — Specific formats for integer numbers
- **floating-point-literals** — Specific formats for decimal numbers
- **nan-and-infinity** — Special Number values
- **type-coercion** — Numbers participate in type conversions

## Related
- **bigint-type** — Alternative numeric type for arbitrary-precision integers

## Contrasts With
- **bigint-type** — BigInt represents arbitrary-precision integers; Number has limited precision

# Common Errors

- **Error**: Comparing floating-point results for exact equality.
  **Correction**: `.3 - .2` is not exactly equal to `.1` due to binary floating-point representation. Use `Number.EPSILON` for approximate comparisons or scaled integers for financial calculations (p. 47).

# Common Confusions

- **Confusion**: JavaScript has separate integer and float types.
  **Clarification**: JavaScript has a single Number type that represents both integers and floating-point values using IEEE 754.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.2, pages 42-49.

# Verification Notes

- Definition source: Direct quotes from p. 42
- Confidence rationale: High — clearly and thoroughly explained
- Uncertainties: None
- Cross-reference status: Verified
