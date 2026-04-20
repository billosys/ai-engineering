---
# === CORE IDENTIFICATION ===
concept: Remainder Operator
slug: remainder-operator

# === CLASSIFICATION ===
category: fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Values, Types, and Operators"
chapter_number: 1
pdf_page: null
section: "Arithmetic"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - modulo
  - "% operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number
  - arithmetic-operator
extends:
  - arithmetic-operator
related:
  - operator-precedence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
---

# Quick Definition

The remainder operator (`%`) returns the remainder of dividing one number by another, and has the same precedence as multiplication and division.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 217-223 of 01-values-types-and-operators.md): "The `%` symbol is used to represent the *remainder* operation. `X % Y` is the remainder of dividing `X` by `Y`. For example, `314 % 100` produces `14`, and `144 % 12` gives `0`. The remainder operator's precedence is the same as that of multiplication and division. You'll also often see this operator referred to as *modulo*."

# Prerequisites

- **Number** -- Works with numeric values.
- **Arithmetic Operator** -- The remainder operator is an arithmetic operator.

# Key Properties

1. `X % Y` gives the **remainder** of dividing X by Y (line 219).
2. Same **precedence** as `*` and `/` (line 221).
3. Often referred to as **modulo** (line 223).
4. Useful for testing **divisibility**: if `X % Y == 0`, X is divisible by Y.

# Construction / Recognition

## To Construct/Create:
1. `X % Y` -- place `%` between two numeric values.

## To Identify/Recognize:
1. The `%` symbol used as an operator between two values.

# Context & Application

The remainder operator is commonly used to test divisibility (e.g., checking for even/odd numbers), cycling through ranges, and implementing patterns like the FizzBuzz exercise in Chapter 2.

# Examples

**Example 1** (Ch 1, lines 220-221): Basic remainder:
`314 % 100` produces `14`, and `144 % 12` gives `0`.

**Example 2** (Ch 2, lines 679-686 of 02-program-structure.md): Testing divisibility:
```js
if (current % 7 == 0) {
  console.log(current);
  break;
}
```

# Relationships

## Builds Upon
- **Number** -- Operates on numbers.
- **Arithmetic Operator** -- Is an arithmetic operator.

## Enables
- Divisibility testing in loops and conditionals.

## Related
- **Operator Precedence** -- Same precedence as `*` and `/`.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Confusing `%` with a percentage operator.
  **Correction**: `%` computes the remainder, not a percentage. `50 % 100` is `50`, not `0.5`.

# Common Confusions

- **Confusion**: Remainder and modulo are always the same.
  **Clarification**: For positive numbers they are the same. The source uses the terms interchangeably (line 223), but technically they can differ for negative numbers.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Arithmetic", lines 217-223 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified with Ch 2 usage
