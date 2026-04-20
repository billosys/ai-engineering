---
# === CORE IDENTIFICATION ===
concept: Decimal Fraction Precision
slug: decimal-fraction-precision

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
section: "The precision of numbers: careful with decimal fractions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "floating point precision"
  - "rounding errors"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ieee-754-floating-point
extends: []
related:
  - number-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript's base-2 floating point representation means decimal fractions like 0.1 and 0.2 cannot be represented precisely, leading to rounding errors in arithmetic.

# Core Definition

"Internally, JavaScript floating point numbers are represented with base 2 (according to the IEEE 754 standard). That means that decimal fractions (base 10) can't always be represented precisely." This produces rounding errors: `0.1 + 0.2` is `0.30000000000000004`. To compute precisely with decimals, use base-10 libraries like big.js or the proposed Decimal type (Ch. 18, Section 18.6).

# Prerequisites

- **ieee-754-floating-point** -- understanding why base-2 cannot represent all base-10 fractions

# Key Properties

1. `0.1 + 0.2 !== 0.3` (produces `0.30000000000000004`)
2. Fractions representable in base 2: those with power-of-2 denominators (0.5, 0.25, 0.125)
3. Fractions NOT representable: 0.1 (1/10), 0.2 (2/10), 0.3 (3/10)
4. Solutions: base-10 libraries (big.js), proposed Decimal type, or integer arithmetic for currency

# Construction / Recognition

```js
> 0.1 + 0.2
0.30000000000000004
> 1.3 * 3
3.9000000000000004
```

# Context & Application

This is critical for financial calculations. Never use floating point for money. Instead, work in integer cents or use a decimal library.

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

# Relationships

## Builds Upon
- **ieee-754-floating-point** — the root cause of imprecision

## Enables
- Awareness needed for financial and scientific computing

## Related
- **number-type** — affects all JavaScript numbers

## Contrasts With
- None

# Common Errors

- **Error**: Using `if (0.1 + 0.2 === 0.3)` as a condition
  **Correction**: This is `false`. Use tolerance-based comparison or avoid decimal fractions.

# Common Confusions

- **Confusion**: Thinking this is a JavaScript-specific problem
  **Clarification**: This affects any language using IEEE 754 doubles (Java, Python, C++, etc.).

# Source Reference

Chapter 18: Numbers, Section 18.6, lines 1152-1171.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit examples and explanation
- Cross-reference status: verified
