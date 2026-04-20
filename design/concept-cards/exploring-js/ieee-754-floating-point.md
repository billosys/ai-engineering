---
# === CORE IDENTIFICATION ===
concept: IEEE 754 Floating Point
slug: ieee-754-floating-point

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
section: "Background: floating point precision"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "double precision"
  - "IEEE 754 double"
  - "floating point representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - decimal-fraction-precision
  - safe-integers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript numbers are stored as IEEE 754 double-precision floating point: a sign bit, 52-bit fraction, and 11-bit exponent, totaling 64 bits.

# Core Definition

JavaScript numbers use three integers totaling 64 bits: a 1-bit sign ([0,1]), a 52-bit fraction ([0, 2^52-1]), and an 11-bit exponent ([-1023, 1024]). The represented value is: (-1)^sign x 0b1.fraction x 2^exponent. Zero is encoded specially using exponent -1023 and fraction 0. This representation means that some decimal fractions (like 0.1) cannot be represented exactly in base 2 (Ch. 18, Section 18.8).

# Prerequisites

- **number-type** -- IEEE 754 is the underlying representation

# Key Properties

1. 64 bits total: 1 sign + 52 fraction + 11 exponent
2. Base-2 representation
3. Cannot exactly represent all base-10 fractions (e.g., 0.1, 0.2)
4. `0.1 + 0.2` produces `0.30000000000000004`
5. Fractions with denominators having only factors of 2 and 5 can be represented exactly in base 10, but only powers of 2 work in base 2

# Construction / Recognition

The imprecision is visible in arithmetic:
```js
> 0.1 + 0.2
0.30000000000000004
> 1.3 * 3
3.9000000000000004
```

# Context & Application

Understanding IEEE 754 explains why JavaScript has precision issues with decimal fractions. For precise decimal arithmetic, use libraries like big.js or the proposed Decimal type.

# Examples

From the source text:

```js
> 0.1 + 0.2
0.30000000000000004
> 1.3 * 3
3.9000000000000004
> 1.4 * 100000000000000
139999999999999.98
```

Explanation: `0.1 = 1/10` cannot be represented in base 2 because the denominator (10) has a prime factor of 5 that cannot be converted to a power of 2.

# Relationships

## Builds Upon
- **number-type** — the underlying representation

## Enables
- Understanding precision limitations
- **decimal-fraction-precision** — the practical consequence

## Related
- **safe-integers** — integer precision limits

## Contrasts With
- None

# Common Errors

- **Error**: Comparing floating point results with `===` directly
  **Correction**: Use a tolerance/epsilon comparison, or avoid floating point for currency. Use `Math.abs(a - b) < Number.EPSILON` for near-equality.

# Common Confusions

- **Confusion**: Thinking `0.1 + 0.2 !== 0.3` is a JavaScript bug
  **Clarification**: This is inherent to IEEE 754 (base-2) floating point, shared by most programming languages.

# Source Reference

Chapter 18: Numbers, Section 18.8, lines 1177-1396.

# Verification Notes

- Definition source: direct (representation components explicitly described)
- Confidence rationale: Detailed explanation with mathematical foundation
- Cross-reference status: verified
