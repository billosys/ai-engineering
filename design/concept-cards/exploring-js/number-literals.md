---
# === CORE IDENTIFICATION ===
concept: Number Literals
slug: number-literals

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
section: "Number literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "numeric literals"
  - "integer literals"
  - "floating point literals"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - numeric-separators
contrasts_with:
  - bigint-literals

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

JavaScript supports number literals in four integer bases (binary, octal, decimal, hexadecimal) and decimal floating point notation with optional exponents.

# Core Definition

Integer literals support four bases: binary (`0b11`), octal (`0o10`), decimal (`35`), and hexadecimal (`0xE7`). Binary and octal prefixes were introduced in ES6. Floating point literals only use base 10, supporting fractions and exponent notation (`3e2` means 3 x 10^2). A syntactic pitfall exists with decimal integer properties: `7.toString()` is a syntax error because the dot is parsed as a decimal point (Ch. 18, Section 18.2).

# Prerequisites

- **number-type** -- understanding the number type these literals create

# Key Properties

1. Binary: `0b11` (ES6)
2. Octal: `0o10` (ES6)
3. Decimal: `35` (ES1)
4. Hexadecimal: `0xE7` (ES1)
5. Floating point: `3e2` (300), `3e-2` (0.03) (ES1)
6. Pitfall: `7.toString()` is a SyntaxError; use `(7).toString()` or `7..toString()`

# Construction / Recognition

```js
assert.equal(0b11, 3);    // binary
assert.equal(0o10, 8);    // octal
assert.equal(35, 35);     // decimal
assert.equal(0xE7, 231);  // hexadecimal
```

# Context & Application

Most code uses decimal literals. Binary and hexadecimal are common for bitwise operations and color values. Octal is less common but used for file permissions.

# Examples

From the source text:

```js
assert.equal(0b11, 3);   // Binary (base 2)
assert.equal(0o10, 8);   // Octal (base 8)
assert.equal(35, 35);    // Decimal (base 10)
assert.equal(0xE7, 231); // Hexadecimal (base 16)

// Floating point
> 3e2
300
> 3e-2
0.03
```

Workarounds for the decimal integer property pitfall:
```js
(7).toString(2)
7.0.toString(2)
7..toString(2)
7 .toString(2)  // space before dot
```

# Relationships

## Builds Upon
- **number-type** — literals create number values

## Enables
- Writing numeric constants in code

## Related
- **numeric-separators** — underscores can be used within literals for readability

## Contrasts With
- **bigint-literals** — bigint literals have an `n` suffix

# Common Errors

- **Error**: Writing `7.toString()` expecting method access
  **Correction**: The dot is parsed as a decimal point. Use `(7).toString()`.

# Common Confusions

- **Confusion**: Thinking non-decimal literals create different types
  **Clarification**: All number literals produce the same `number` type regardless of base.

# Source Reference

Chapter 18: Numbers, Section 18.2, lines 112-199.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete examples for all bases
- Cross-reference status: verified
