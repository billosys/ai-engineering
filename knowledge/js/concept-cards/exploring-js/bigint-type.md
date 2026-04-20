---
# === CORE IDENTIFICATION ===
concept: BigInt Type
slug: bigint-type

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
section: "Bigints"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "bigint"
  - "BigInt"
  - "arbitrary-precision integer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
  - safe-integers
extends: []
related:
  - bigint-literals
  - bigint-json
contrasts_with:
  - number-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

BigInt is a primitive data type for integers with arbitrary precision -- their storage adapts to the size of the integer, with no upper or lower limit. Introduced in ES2020.

# Core Definition

"*Bigint* is a primitive data type for integers. Bigints don't have a fixed storage size in bits; their sizes adapt to the integers they represent: Small integers are represented with fewer bits than large integers. There is no negative lower limit or positive upper limit for the integers that can be represented" (Ch. 20, Section 20.2). `typeof 123n` returns `'bigint'`.

# Prerequisites

- **number-type** -- bigints exist because numbers have limited integer precision
- **safe-integers** -- understanding why 53-bit integers are insufficient

# Key Properties

1. Primitive type with `typeof` returning `'bigint'` (ES2020)
2. Arbitrary precision: no fixed size limit
3. Literal syntax: suffix `n` (e.g., `123n`)
4. Cannot mix bigints and numbers in operations (throws `TypeError`)
5. Operators `+`, `-`, `*`, `**`, `/`, `%` work with bigints
6. Division rounds toward zero (like `Math.trunc()`)
7. Unary `+` is NOT supported for bigints

# Construction / Recognition

```js
123n              // bigint literal
typeof 123n       // 'bigint'
123n * 456n       // 56088n
BigInt('123')     // 123n
```

# Context & Application

Use bigints when working with integers beyond the 53-bit safe range: database IDs, financial calculations (amounts in cents), cryptographic values, or timestamps requiring high precision.

# Examples

From the source text:

```js
> 123n * 456n
56088n
> typeof 123n
'bigint'

// Beyond 53 bits
> 2n**53n + 1n
9007199254740993n  // correct!
> 2**53 + 1
9007199254740992   // wrong with regular numbers

// Cannot mix with numbers
> 2n + 1
TypeError: Cannot mix BigInt and other types, use explicit conversions
```

# Relationships

## Builds Upon
- **number-type** — bigints address number type's integer precision limitations
- **safe-integers** — motivation for bigints

## Enables
- **bigint-literals** — syntax for creating bigints
- Arbitrary-precision integer arithmetic

## Related
- **bigint-json** — serialization challenges with bigints

## Contrasts With
- **number-type** — numbers are 64-bit floats with limited integer precision

# Common Errors

- **Error**: Mixing bigints and numbers: `2n + 1`
  **Correction**: Convert explicitly: `2n + BigInt(1)` or `Number(2n) + 1`.

- **Error**: Using unary `+` on bigints: `+23n`
  **Correction**: This throws `TypeError`. Use `Number(23n)` for explicit conversion.

# Common Confusions

- **Confusion**: Thinking `BigInt` can represent fractions
  **Clarification**: BigInts are integers only. Division truncates: `1n / 2n` is `0n`.

# Source Reference

Chapter 20: Bigints, Section 20.2, lines 94-188.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with comprehensive examples
- Cross-reference status: verified
