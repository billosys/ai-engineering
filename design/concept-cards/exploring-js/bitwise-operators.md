---
# === CORE IDENTIFICATION ===
concept: Bitwise Operators
slug: bitwise-operators

# === CLASSIFICATION ===
category: primitive-types
subcategory: numbers
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Numbers"
chapter_number: 18
pdf_page: null
section: "Bitwise operators (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "bitwise operations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - bigint-bitwise-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript's bitwise operators work internally with 32-bit integers, converting 64-bit float operands to 32-bit integers, performing the operation, then converting back.

# Core Definition

JavaScript's bitwise operators convert their operands to 32-bit integers, perform the operation, then convert back to JavaScript numbers. They include: bitwise Not (`~`), And (`&`), Or (`|`), Xor (`^`), left shift (`<<`), signed right shift (`>>`), and unsigned right shift (`>>>`). Operand types are either Int32 (signed) or Uint32 (unsigned) (Ch. 18, Section 18.10).

# Prerequisites

- **number-type** -- bitwise operators work on numbers

# Key Properties

1. Operands converted to 32-bit integers, result converted back to float
2. Two operand types: Int32 (signed, [-2^31, 2^31)) and Uint32 (unsigned, [0, 2^32))
3. `>>>` produces unsigned results; all others produce signed
4. `~x` is bitwise Not (Int32 -> Int32)
5. `&`, `|`, `^` are binary bitwise operators (Int32 -> Int32)
6. `<<`, `>>` are signed shift; `>>>` is unsigned shift

# Construction / Recognition

```js
> 2**32 - 1 >> 0  // convert to Int32 and back
-1
> 2**31 >> 0      // highest bit is 1 (sign bit)
-2147483648
```

# Context & Application

Bitwise operators are used for flag manipulation, color channel extraction, hash functions, and low-level data processing. The 32-bit integer coercion is sometimes exploited for fast truncation to integer (`x | 0`).

# Examples

From the source text:

```js
> 2**32 - 1 >> 0  // all 32 bits set, interpreted as signed
-1
> 2**31 >> 0      // highest bit is 1 (sign bit)
-2147483648
> 2**31 - 1 >> 0  // highest bit is 0
2147483647
```

# Relationships

## Builds Upon
- **number-type** — operates on numbers

## Enables
- Low-level bit manipulation
- Fast integer truncation (`x | 0`)

## Related
- **bigint-bitwise-operators** — bigints have their own bitwise operators with infinite-width semantics

## Contrasts With
- None

# Common Errors

- **Error**: Expecting bitwise operators to work with 64-bit precision
  **Correction**: Bitwise operators truncate to 32-bit integers. Values outside the 32-bit range produce unexpected results.

# Common Confusions

- **Confusion**: Thinking `x | 0` is a no-op
  **Clarification**: It converts `x` to a 32-bit signed integer, truncating fractional parts and large values.

# Source Reference

Chapter 18: Numbers, Section 18.10, lines 1641-1780.

# Verification Notes

- Definition source: direct
- Confidence rationale: Detailed treatment of all bitwise operators
- Cross-reference status: verified
