---
# === CORE IDENTIFICATION ===
concept: Special Numbers
slug: special-numbers

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
section: "Special numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Infinity
  - NaN
  - not a number

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number
extends: []
related:
  - type-coercion
  - comparison-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

JavaScript has three special number values: `Infinity`, `-Infinity`, and `NaN` ("not a number"), which are of the number type but do not behave like normal numbers.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 228-241 of 01-values-types-and-operators.md): "There are three special values in JavaScript that are considered numbers but don't behave like normal numbers. The first two are `Infinity` and `-Infinity`, which represent the positive and negative infinities." And: "`NaN` stands for 'not a number', even though it *is* a value of the number type. You'll get this result when you, for example, try to calculate `0 / 0` (zero divided by zero), `Infinity - Infinity`, or any number of other numeric operations that don't yield a meaningful result."

# Prerequisites

- **Number** -- Special numbers are values of the number type.

# Key Properties

1. `Infinity` and `-Infinity` represent **positive and negative infinities**.
2. `Infinity - 1` is still `Infinity` -- infinity-based computation is not mathematically sound (lines 231-234).
3. `NaN` denotes a **nonsensical numeric computation** (lines 237-241).
4. `NaN` is the **only value not equal to itself**: `NaN == NaN` is `false` (lines 444-450).
5. `NaN` is produced by operations like `0 / 0`, `Infinity - Infinity`, and converting non-numeric strings to numbers (lines 239-241, 580-583).
6. Further arithmetic on `NaN` keeps producing `NaN` (lines 581-582).

# Construction / Recognition

## To Construct/Create:
1. `Infinity`: divide a positive number by 0, or use the literal `Infinity`.
2. `-Infinity`: divide a negative number by 0, or negate `Infinity`.
3. `NaN`: `0 / 0`, `Infinity - Infinity`, `Number("five")`.

## To Identify/Recognize:
1. Use `Number.isNaN(value)` to test for `NaN`.
2. Do not use `== NaN` since `NaN` is not equal to itself.

# Context & Application

Special numbers appear when arithmetic produces non-standard results. Understanding `NaN` is particularly important because it signals accidental type conversions or invalid operations, and its self-inequality property is a common source of bugs.

# Examples

**Example 1** (Ch 1, lines 447-450): NaN self-inequality:
```js
console.log(NaN == NaN)
// → false
```

**Example 2** (Ch 1, lines 556-563): NaN from type coercion:
```js
console.log("five" * 2)
// → NaN
```

# Relationships

## Builds Upon
- **Number** -- Special numbers are of the number type.

## Enables
- **Type Coercion** -- Understanding NaN is essential for recognizing failed coercions.

## Related
- **Comparison Operators** -- NaN behaves uniquely in comparisons.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Testing for `NaN` using `value == NaN`.
  **Correction**: Since `NaN == NaN` is `false`, use `Number.isNaN(value)` instead.

# Common Confusions

- **Confusion**: `NaN` means the value is not of the number type.
  **Clarification**: `NaN` *is* a value of the number type (`typeof NaN` returns `"number"`). It simply indicates a nonsensical numeric result.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Special numbers", lines 225-241 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated subsection with explicit definitions
- Cross-reference status: verified with comparison and type coercion sections
