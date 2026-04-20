---
# === CORE IDENTIFICATION ===
concept: BigInt Literals
slug: bigint-literals

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
section: "Bigint literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bigint-type
extends: []
related:
  - number-literals
  - numeric-separators
contrasts_with:
  - number-literals

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

BigInt literals are written as integer literals with an `n` suffix, supporting decimal (`123n`), hexadecimal (`0xFFn`), binary (`0b1101n`), and octal (`0o777n`) bases.

# Core Definition

BigInt literals support the same bases as number literals with an `n` suffix: decimal (`123n`), hexadecimal (`0xFFn`), binary (`0b1101n`), and octal (`0o777n`). Negative bigints use the unary minus prefix: `-123n`. Underscores can be used as separators since ES2021 (Ch. 20, Section 20.3).

# Prerequisites

- **bigint-type** -- literals create bigint values

# Key Properties

1. `n` suffix distinguishes from number literals (ES2020)
2. All four bases supported: decimal, hex, binary, octal
3. Negative via unary minus: `-123n`
4. Underscore separators since ES2021: `6_000_000n`

# Construction / Recognition

```js
123n        // decimal
0xFFn       // hexadecimal (255n)
0b1101n     // binary (13n)
0o777n      // octal (511n)
-123n       // negative
6_000_000n  // with separator (ES2021)
```

# Context & Application

Use bigint literals for constant big integer values in code. For runtime conversion, use `BigInt()`.

# Examples

From the source text:

```js
// All bases
123n     // Decimal
0xFFn    // Hexadecimal
0b1101n  // Binary
0o777n   // Octal

// Separators (ES2021)
const massOfEarthInKg = 6_000_000_000_000_000_000_000_000n;
const priceInCents = 123_000_00n;
```

# Relationships

## Builds Upon
- **bigint-type** — literals produce bigint values

## Enables
- Writing bigint constants in code

## Related
- **number-literals** — similar syntax without the `n` suffix
- **numeric-separators** — underscore separators work in bigint literals too

## Contrasts With
- **number-literals** — number literals lack the `n` suffix

# Common Errors

- **Error**: Passing `'123n'` to `BigInt()` expecting it to parse
  **Correction**: `BigInt('123n')` throws `SyntaxError`. The `n` suffix is only for literals: use `BigInt('123')`.

# Common Confusions

- **Confusion**: Thinking bigint literals are just numbers
  **Clarification**: `123n` and `123` are different types that cannot be mixed in operations.

# Source Reference

Chapter 20: Bigints, Section 20.3, lines 189-224.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete list of bases and syntax
- Cross-reference status: verified
