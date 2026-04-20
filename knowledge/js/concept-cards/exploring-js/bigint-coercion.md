---
# === CORE IDENTIFICATION ===
concept: Coercing BigInts to Other Types
slug: bigint-coercion

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
section: "Coercing bigints to other primitive types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bigint-type
extends: []
related:
  - converting-to-boolean
  - converting-to-number
  - converting-to-string
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

BigInts can be explicitly converted to boolean, number, and string, but implicit coercion to number via unary `+` throws `TypeError` to prevent silent precision loss.

# Core Definition

Converting bigints: to boolean works (both `Boolean()` and `!`); to number works explicitly (`Number(7n)` -> `7`) but unary `+` throws `TypeError`; to string works both explicitly (`String(7n)` -> `'7'`) and via concatenation (`''+7n` -> `'7'`). The unary `+` restriction exists because much code relies on it coercing to number, and silently losing bigint precision would be dangerous (Ch. 20, Section 20.6).

# Prerequisites

- **bigint-type** -- the source type being converted

# Key Properties

1. To boolean: `Boolean(0n)` -> `false`, `Boolean(int)` -> `true` (if non-zero)
2. To number: `Number(7n)` -> `7`, but `+int` -> `TypeError`
3. To string: `String(7n)` -> `'7'`, `''+7n` -> `'7'`
4. Unary `+` intentionally throws to prevent silent precision loss

# Construction / Recognition

```js
Boolean(0n)    // false
Boolean(7n)    // true
Number(7n)     // 7
String(7n)     // '7'
''+7n          // '7'
+7n            // TypeError
```

# Context & Application

When converting bigints, always use explicit functions (`Number()`, `String()`, `Boolean()`) to make intent clear and avoid the unary `+` pitfall.

# Examples

From the source text:

```js
// Boolean
Boolean(0n)     // false
Boolean(int)    // true (for non-zero)
!0n             // true

// Number
Number(7n)      // 7 (explicit ok)
+int            // TypeError (coercion blocked)

// String
String(7n)      // '7'
''+7n           // '7'
```

# Relationships

## Builds Upon
- **bigint-type** — the type being converted from

## Enables
- Interoperability between bigints and other types

## Related
- **converting-to-boolean** — boolean conversion rules
- **converting-to-number** — number conversion rules
- **converting-to-string** — string conversion rules

## Contrasts With
- None

# Common Errors

- **Error**: Using `+bigintValue` to convert to number
  **Correction**: Use `Number(bigintValue)` instead. Unary `+` throws `TypeError` for bigints.

# Common Confusions

- **Confusion**: Thinking string concatenation with bigints throws like with symbols
  **Clarification**: `'' + 7n` works fine and produces `'7'`. Only unary `+` is blocked for bigints.

# Source Reference

Chapter 20: Bigints, Section 20.6, lines 767-865.

# Verification Notes

- Definition source: direct (conversion table provided)
- Confidence rationale: Complete conversion rules
- Cross-reference status: verified
