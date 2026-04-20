---
# === CORE IDENTIFICATION ===
concept: BigInt Bitwise Operators
slug: bigint-bitwise-operators

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
section: "Bitwise operators (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bigint-type
  - bitwise-operators
extends: []
related: []
contrasts_with:
  - bitwise-operators

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Bigint bitwise operators work like number bitwise operators but with infinite-width two's complement for negative values. The unsigned right shift (`>>>`) is not supported for bigints.

# Core Definition

For bigints, bitwise operators interpret a negative sign as an infinite two's complement: `-1` is `...111111`, `-2` is `...111110`. Bitwise Not (`~`), And (`&`), Or (`|`), Xor (`^`), and signed shifts (`<<`, `>>`) all work. Unsigned right shift (`>>>`) throws `TypeError` because there is no "left" to shift from with infinite bits (Ch. 20, Section 20.4.5).

# Prerequisites

- **bigint-type** -- operates on bigints
- **bitwise-operators** -- understanding number bitwise operators

# Key Properties

1. Negative bigints use infinite two's complement
2. `~`, `&`, `|`, `^` work as expected
3. `<<` and `>>` work and preserve sign
4. `>>>` (unsigned right shift) throws `TypeError`
5. No fixed bit width (unlike number bitwise which uses 32 bits)

# Construction / Recognition

```js
~0b10n     // -3n (···111101)
~-2n       // 1n
-1n >> 20n // -1n (infinite ones shifted right stays infinite ones)

2n >>> 1n  // TypeError
```

# Context & Application

Use bigint bitwise operators for arbitrary-precision bit manipulation, such as implementing bit sets or cryptographic operations.

# Examples

From the source text:

```js
assert.equal(~0b10n, -3n);  // ···111101
assert.equal(~-2n, 1n);     // ···111110 -> 1

> (0b1010n | 0b0111n).toString(2)
'1111'
> (0b1010n & 0b0111n).toString(2)
'10'

> 2n << 1n
4n
> -2n >> 1n
-1n

> 2n >>> 1n
TypeError: BigInts have no unsigned right shift, use >> instead
```

# Relationships

## Builds Upon
- **bigint-type** — operates on bigints
- **bitwise-operators** — extends bitwise concepts to bigints

## Enables
- Arbitrary-precision bit manipulation

## Related
- None

## Contrasts With
- **bitwise-operators** — number bitwise uses fixed 32-bit width; bigint uses infinite width

# Common Errors

- **Error**: Using `>>>` with bigints
  **Correction**: `>>>` is not supported for bigints. Use `>>` instead.

# Common Confusions

- **Confusion**: Thinking bigint bitwise has a fixed bit width
  **Clarification**: Bigint bitwise operations work on conceptually infinite-width integers.

# Source Reference

Chapter 20: Bigints, Section 20.4.5, lines 365-502.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit examples and error messages
- Cross-reference status: verified
