---
# === CORE IDENTIFICATION ===
concept: Bitwise Operators
slug: bitwise-operators

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 94
section: "4.8.3 Bitwise Operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "bit manipulation operators"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - operator-precedence
extends: []
related:
  - unary-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`, `>>>`) perform low-level bit manipulation on 32-bit integer representations of their numeric operands.

# Core Definition

"The bitwise operators perform low-level manipulation of the bits in the binary representation of numbers... The bitwise operators expect integer operands and behave as if those values were represented as 32-bit integers rather than 64-bit floating-point values." (Ch. 4, §4.8.3)

# Prerequisites

- **primary-expressions** — Operands are numeric expressions.
- **operator-precedence** — Bitwise operators have specific precedence levels.

# Key Properties

1. Operands are coerced to 32-bit integers, dropping fractional parts and bits beyond 32.
2. `&` (AND), `|` (OR), `^` (XOR) perform Boolean operations on each bit pair.
3. `~` (NOT) is unary — inverts all bits. `~x` is equivalent to `-(x+1)`.
4. `<<` shifts left, `>>` shifts right preserving sign, `>>>` shifts right filling with zeros.
5. `NaN`, `Infinity`, `-Infinity` all convert to 0 for bitwise operations.
6. All except `>>>` work with BigInt operands.

# Construction / Recognition

```js
0x1234 & 0x00FF    // => 0x0034 (AND)
0x1234 | 0x00FF    // => 0x12FF (OR)
0xFF00 ^ 0xF0F0    // => 0x0FF0 (XOR)
~0x0F              // => -16 (NOT)
7 << 2             // => 28 (shift left)
-1 >>> 4           // => 0x0FFFFFFF (unsigned shift right)
```

# Context & Application

Bitwise operators are not commonly used in typical JavaScript programming but are useful for low-level tasks like flag manipulation, color calculations, binary protocols, and performance-critical integer arithmetic.

# Examples

From the source text (§4.8.3, pp. 94-95):

```js
0x1234 & 0x00FF   // => 0x0034
0x1234 | 0x00FF   // => 0x12FF
0xFF00 ^ 0xF0F0   // => 0x0FF0
~0x0F             // => 0xFFFFFFF0, or -16
7 << 2            // => 28
7 >> 1            // => 3
-7 >> 1           // => -4
-1 >> 4           // => -1
-1 >>> 4          // => 0x0FFFFFFF
```

# Relationships

## Builds Upon
- **operator-precedence** — Each bitwise operator has a defined precedence level

## Enables
- Low-level binary data manipulation

## Related
- **unary-operators** — `~` is a unary bitwise operator

## Contrasts With
- No specific contrast

# Common Errors

- **Error**: Forgetting that bitwise operators truncate to 32 bits.
  **Correction**: Floating-point values lose their fractional part and are treated as 32-bit integers.

# Common Confusions

- **Confusion**: Confusing `&` (bitwise AND) with `&&` (logical AND), or `|` (bitwise OR) with `||` (logical OR).
  **Clarification**: `&` and `|` operate on individual bits of integers; `&&` and `||` operate on truthy/falsy values with short-circuit behavior.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.8.3, pages 94-96.

# Verification Notes

- Definition source: Direct quote from §4.8.3
- Confidence rationale: High — detailed per-operator descriptions
- Uncertainties: None
- Cross-reference status: Verified
