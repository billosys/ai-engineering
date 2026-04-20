---
# === CORE IDENTIFICATION ===
concept: Number
slug: number

# === CLASSIFICATION ===
category: fundamentals
subcategory: types
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Values, Types, and Operators"
chapter_number: 1
pdf_page: null
section: "Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - numeric value
  - number type

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
extends: []
related:
  - arithmetic-operator
  - operator-precedence
  - special-numbers
contrasts_with:
  - string
  - boolean

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

The number type in JavaScript represents numeric values using 64 bits, supporting integers, fractional numbers, and scientific notation.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 99-101 of 01-values-types-and-operators.md): "Values of the *number* type are, unsurprisingly, numeric values." JavaScript uses 64 bits to store a single number value (line 113-114), which can represent up to about 18 quintillion different numbers. Due to bits reserved for sign and decimal point, the actual maximum whole number is approximately 9 quadrillion (line 136-137).

# Prerequisites

- **Value** -- Numbers are a type of value.

# Key Properties

1. Stored using **64 bits** of memory.
2. Support **whole numbers** (integers) and **fractional numbers** (written with a dot, e.g., `9.81`).
3. Support **scientific notation** (e.g., `2.998e8` = 299,800,000).
4. Integer arithmetic within 9 quadrillion is **guaranteed precise** (line 161-162).
5. Fractional numbers are **approximations**, not precise values (lines 163-168).
6. Include three **special values**: `Infinity`, `-Infinity`, and `NaN`.

# Construction / Recognition

## To Construct/Create:
1. Write a numeric literal: `13`, `9.81`, `2.998e8`.
2. Perform arithmetic operations on other numbers.

## To Identify/Recognize:
1. `typeof` returns `"number"`.

# Context & Application

Numbers are used for all arithmetic and counting in JavaScript programs. Understanding their 64-bit floating-point representation is important for avoiding precision issues with fractional arithmetic.

# Examples

**Example 1** (Ch 1, lines 103-105): A simple integer:
```js
13
```

**Example 2** (Ch 1, lines 143-145): A fractional number:
```js
9.81
```

**Example 3** (Ch 1, lines 152-154): Scientific notation:
```js
2.998e8
```
"That's 2.998 x 10^8 = 299,800,000."

# Relationships

## Builds Upon
- **Value** -- Numbers are a type of value.

## Enables
- **Arithmetic Operator** -- Arithmetic operates on numbers.
- **Comparison Operators** -- Numbers can be compared.
- **Type Coercion** -- Other types may be coerced to numbers.

## Related
- **Special Numbers** -- Infinity, -Infinity, and NaN.
- **Operator Precedence** -- Determines order of arithmetic operations.

## Contrasts With
- **String** -- Text values, not numeric.
- **Boolean** -- Only two values (true/false), not numeric range.

# Common Errors

- **Error**: Assuming fractional arithmetic is always precise.
  **Correction**: "Treat fractional digital numbers as approximations, not as precise values" (lines 167-168).

- **Error**: Assuming all whole numbers can be represented exactly.
  **Correction**: Only integers up to about 9 quadrillion are guaranteed precise (line 136-137).

# Common Confusions

- **Confusion**: JavaScript has separate integer and float types.
  **Clarification**: JavaScript has a single `number` type that uses 64-bit floating point for all numeric values.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Numbers", lines 96-241 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated section with thorough explanation
- Cross-reference status: verified within chapter
