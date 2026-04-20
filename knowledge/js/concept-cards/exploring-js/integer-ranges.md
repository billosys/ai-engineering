---
# === CORE IDENTIFICATION ===
concept: Integer Ranges in JavaScript
slug: integer-ranges

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
section: "Ranges of integer numbers in JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
  - safe-integers
extends: []
related:
  - bitwise-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript has three important integer ranges: safe integers (53 bits plus sign), array indices (32 bits unsigned), and bitwise operator operands (32 bits signed/unsigned).

# Core Definition

Three key integer ranges: (1) Safe integers with 53-bit precision plus sign, range (-2^53, 2^53); (2) Array indices with 32-bit unsigned precision, range [0, 2^32-1); (3) Bitwise operators with 32-bit precision -- unsigned right shift uses [0, 2^32), all others use [-2^31, 2^31) (Ch. 18, Section 18.9.3).

# Prerequisites

- **number-type** -- integers are a subset of numbers
- **safe-integers** -- the most commonly referenced range

# Key Properties

1. Safe integers: 53 bits + sign, range (-2^53, 2^53)
2. Array indices: 32 bits unsigned, [0, 2^32-1) (excluding max length)
3. Typed Array indices: 53 bits (safe, unsigned)
4. Bitwise unsigned shift (>>>): [0, 2^32)
5. Other bitwise operators: [-2^31, 2^31)

# Construction / Recognition

```js
> Math.log2(Number.MAX_SAFE_INTEGER)
53
> Number.isInteger(123.0)
true
```

# Context & Application

Understanding these ranges is important when working with arrays (max ~4.3 billion elements), bitwise operations (32-bit truncation), and large numeric values (safe integer limit).

# Examples

From the source text:

```js
> Math.log2(Number.MAX_SAFE_INTEGER)
53
> Number.isInteger(123.0)
true
> Number.parseInt('123')
123
```

# Relationships

## Builds Upon
- **number-type** — integers are a subset of numbers
- **safe-integers** — the primary integer range

## Enables
- Understanding array size limits
- Correct use of bitwise operations

## Related
- **bitwise-operators** — use 32-bit integer ranges

## Contrasts With
- None

# Common Errors

- **Error**: Assuming JavaScript arrays can have more than 2^32-1 elements
  **Correction**: Array indices are 32-bit unsigned, limiting length to 2^32-1 (about 4.3 billion).

# Common Confusions

- **Confusion**: Thinking all integers have 32-bit precision
  **Clarification**: Safe integers have 53-bit precision. Only bitwise operators truncate to 32 bits.

# Source Reference

Chapter 18: Numbers, Section 18.9.3, lines 1525-1541.

# Verification Notes

- Definition source: direct
- Confidence rationale: Three ranges explicitly listed
- Cross-reference status: verified
