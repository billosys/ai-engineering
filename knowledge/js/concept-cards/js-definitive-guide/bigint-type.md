---
# === CORE IDENTIFICATION ===
concept: BigInt Type
slug: bigint-type

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
pdf_page: 48
section: "3.2.5 Arbitrary Precision Integers with BigInt"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - BigInt
  - arbitrary precision integer

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - integer-literals
  - strict-vs-loose-equality
contrasts_with:
  - number-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes `==` from `===`?"
---

# Quick Definition

BigInt is an ES2020 numeric type for arbitrary-precision integers, written as integer literals suffixed with `n`, which cannot be mixed with regular Numbers in arithmetic operations.

# Core Definition

"One of the newest features of JavaScript, defined in ES2020, is a new numeric type known as BigInt." "BigInt is a numeric type whose values are integers. The type was added to JavaScript mainly to allow the representation of 64-bit integers, which are required for compatibility with many other programming languages and APIs. But BigInt values can have thousands or even millions of digits." (p. 48)

# Prerequisites

- **number-type** — BigInt exists to overcome Number's integer precision limits

# Key Properties

1. Written as integer literals with an `n` suffix: `1234n`
2. Supports 0b, 0o, 0x prefixes for binary, octal, hex
3. `BigInt()` function converts numbers/strings to BigInt
4. Standard arithmetic operators work (+, -, *, /, %, **)
5. Division truncates toward zero (drops remainder)
6. Cannot mix BigInt and Number operands in arithmetic
7. Comparison operators DO work with mixed types
8. `0 == 0n` is true but `0 === 0n` is false (different types)
9. Math object functions do not accept BigInt arguments

# Construction / Recognition

```javascript
1234n                           // A BigInt literal
0b111111n                       // Binary BigInt
0o7777n                         // Octal BigInt
0x8000000000000000n             // => 2n**63n: 64-bit integer
BigInt(Number.MAX_SAFE_INTEGER) // => 9007199254740991n
BigInt("1" + "0".repeat(100))   // => 10n**100n: one googol
```

# Context & Application

BigInt is primarily used for interoperability with other languages/APIs requiring 64-bit integers, and for any computation requiring integer precision beyond 2^53. Not suitable for cryptography (timing attacks not prevented).

# Examples

From the source text (pp. 48-49):
```javascript
1234n                    // A not-so-big BigInt literal
0x8000000000000000n      // => 2n**63n: A 64-bit integer

// Arithmetic
1000n + 2000n            // => 3000n
3000n / 997n             // => 3n: the quotient is 3
3000n % 997n             // => 9n: and the remainder is 9
(2n ** 131071n) - 1n     // A Mersenne prime with 39457 decimal digits

// Mixed comparisons
1 < 2n                   // => true
0 == 0n                  // => true
0 === 0n                 // => false: the === checks for type equality as well
```

# Relationships

## Builds Upon
- **number-type** — BigInt addresses Number's integer precision limitations

## Enables
- 64-bit integer interoperability

## Related
- **integer-literals** — BigInt literals share base prefixes with integer literals
- **strict-vs-loose-equality** — Demonstrates `==` vs `===` with different types

## Contrasts With
- **number-type** — BigInt can only represent integers; Number can represent floats. BigInt has arbitrary precision; Number is limited to 2^53.

# Common Errors

- **Error**: Mixing BigInt and Number in arithmetic: `1n + 1`.
  **Correction**: Both operands must be the same type. Use `1n + 1n` or `1 + 1`.

# Common Confusions

- **Confusion**: BigInt is just a larger Number.
  **Clarification**: BigInt is a completely separate type. "Neither type is more general than the other" — BigInt handles only integers; Number handles floats but with limited precision (p. 49).

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.2.5, pages 48-49.

# Verification Notes

- Definition source: Direct quotes from pp. 48-49
- Confidence rationale: High — clearly defined with examples
- Uncertainties: None
- Cross-reference status: Verified
