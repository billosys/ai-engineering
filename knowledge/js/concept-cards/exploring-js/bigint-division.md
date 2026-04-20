---
# === CORE IDENTIFICATION ===
concept: BigInt Division
slug: bigint-division

# === CLASSIFICATION ===
category: primitive-types
subcategory: bigints
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Bigints -- arbitrary-precision integers (advanced)"
chapter_number: 20
pdf_page: null
section: "Arithmetic operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bigint-type
extends: []
related:
  - math-rounding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

BigInt division (`/`) and remainder (`%`) round toward zero by removing the fractional part, similar to `Math.trunc()` for numbers.

# Core Definition

"`/` and `%` round towards zero by removing the fraction (like `Math.trunc()`)" (Ch. 20, Section 20.4.1). Since bigints are integers, division cannot produce fractions -- the result is truncated.

# Prerequisites

- **bigint-type** -- division operates on bigints

# Key Properties

1. `1n / 2n` is `0n` (truncated toward zero)
2. Remainder matches first operand sign (like `%` for numbers)
3. No fractional results possible

# Construction / Recognition

```js
> 1n / 2n
0n
> 7n / 2n
3n
```

# Context & Application

BigInt division always truncates. If you need a remainder, use `%`. For precise division, multiply first to avoid truncation.

# Examples

From the source text:

```js
> 1n / 2n
0n
```

# Relationships

## Builds Upon
- **bigint-type** — operates on bigints

## Enables
- Integer division arithmetic

## Related
- **math-rounding** — `Math.trunc()` has the same rounding behavior

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `1n / 2n` to return `0.5n`
  **Correction**: BigInts are integers only. Division truncates: `1n / 2n` is `0n`.

# Common Confusions

- **Confusion**: Thinking bigint division rounds to nearest
  **Clarification**: It always truncates toward zero (like `Math.trunc()`), not to nearest.

# Source Reference

Chapter 20: Bigints, Section 20.4.1, lines 258-300.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit statement with example
- Cross-reference status: verified
