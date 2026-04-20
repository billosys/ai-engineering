---
# === CORE IDENTIFICATION ===
concept: Unary Arithmetic Operators
slug: unary-operators

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 92
section: "4.8.2 Unary Arithmetic Operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "increment operator"
  - "decrement operator"
  - "unary plus"
  - "unary minus"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - operator-precedence
extends: []
related:
  - addition-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The unary arithmetic operators (`+`, `-`, `++`, `--`) operate on a single operand: unary plus converts to number, unary minus negates, and increment/decrement add or subtract 1 with an assignment side effect.

# Core Definition

"Unary operators modify the value of a single operand to produce a new value. In JavaScript, the unary operators all have high precedence and are all right-associative. The arithmetic unary operators described in this section (+, -, ++, and --) all convert their single operand to a number, if necessary." (Ch. 4, §4.8.2)

# Prerequisites

- **primary-expressions** — Unary operators take a single expression as operand.
- **operator-precedence** — Unary operators have high precedence.

# Key Properties

1. Unary `+` converts its operand to a number (or NaN). Cannot be used with BigInt.
2. Unary `-` converts to number then negates.
3. `++` (pre/post-increment): requires an lvalue, adds 1, assigns back. Pre-increment returns new value; post-increment returns old value.
4. `--` (pre/post-decrement): same as `++` but subtracts 1.
5. `++` never performs string concatenation: `++x` on string `"1"` produces number `2`, not `"11"`.
6. No line break allowed between post-increment/decrement operator and its operand (ASI).

# Construction / Recognition

```js
+x     // Convert to number
-x     // Negate
++i    // Pre-increment
i++    // Post-increment
--i    // Pre-decrement
i--    // Post-decrement
```

# Context & Application

Increment/decrement operators are most commonly used in `for` loop counters. Unary `+` is a concise way to convert strings to numbers. Understanding pre- vs. post-increment is essential for correct loop and expression behavior.

# Examples

From the source text (§4.8.2, pp. 92-94):

```js
let i = 1, j = ++i;   // i and j are both 2
let n = 1, m = n++;   // n is 2, m is 1
```

Note: `x++` is not the same as `x=x+1` — `++` never concatenates strings. If `x` is `"1"`, `++x` is the number `2`, but `x+1` is the string `"11"`.

# Relationships

## Builds Upon
- **operator-precedence** — Unary operators have high precedence, right-to-left associativity

## Enables
- **for-loop** — `++` and `--` are commonly used in for loop increment expressions

## Related
- **addition-operator** — `++` differs from `+1` in that it never concatenates

## Contrasts With
- No specific contrast

# Common Errors

- **Error**: Expecting `x++` to return the incremented value.
  **Correction**: Post-increment returns the original value. Use `++x` if you need the incremented value.

# Common Confusions

- **Confusion**: Believing `x++` is identical to `x = x + 1`.
  **Clarification**: `++` always converts to number and adds 1. `x + 1` may concatenate if `x` is a string.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.8.2, pages 92-94.

# Verification Notes

- Definition source: Direct quote from §4.8.2
- Confidence rationale: High — detailed descriptions of each operator
- Uncertainties: None
- Cross-reference status: Verified
