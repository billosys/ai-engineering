---
# === CORE IDENTIFICATION ===
concept: Type Coercion
slug: type-coercion

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
section: "Automatic type conversion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - automatic type conversion
  - implicit type conversion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
  - number
  - string
  - boolean
extends: []
related:
  - strict-equality
  - comparison-operators
  - logical-operators
  - special-numbers
contrasts_with:
  - strict-equality

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion?"
  - "What distinguishes == and ===?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Type coercion is JavaScript's automatic conversion of a value from one type to another when an operator is applied to the "wrong" type of value.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 569-576 of 01-values-types-and-operators.md): "When an operator is applied to the 'wrong' type of value, JavaScript will quietly convert that value to the type it needs, using a set of rules that often aren't what you want or expect. This is called *type coercion*. The `null` in the first expression becomes `0` and the `\"5\"` in the second expression becomes `5` (from string to number). Yet in the third expression, `+` tries string concatenation before numeric addition, so the `1` is converted to `\"1\"` (from number to string)."

# Prerequisites

- **Value** -- Coercion converts between value types.
- **Number**, **String**, **Boolean** -- The types involved in coercion.

# Key Properties

1. Coercion is **automatic** and **implicit** -- the programmer does not request it (line 569).
2. Rules are often **unintuitive** -- "a set of rules that often aren't what you want or expect" (lines 571-572).
3. `null` becomes `0` in numeric contexts (line 573).
4. `"5" - 1` gives `4` (string to number), but `"5" + 1` gives `"51"` (number to string) (lines 558-561).
5. Non-numeric strings become `NaN` when coerced to number (lines 579-583).
6. For `==` with different types, JavaScript converts values; `null` and `undefined` equal only each other (lines 586-594).
7. Falsy values in Boolean context: `0`, `NaN`, `""` count as `false`; all others as `true` (lines 652-654).

# Construction / Recognition

## To Trigger:
1. Apply an operator to values of mismatched types: `8 * null`, `"5" - 1`.
2. Use `==` to compare values of different types.

## To Identify/Recognize:
1. An expression that combines different types without explicit conversion.
2. Surprising results from operators (like `"5" + 1` producing `"51"`).

# Context & Application

Type coercion is one of JavaScript's most controversial features. It enables flexible code but is a major source of bugs. Understanding coercion rules is essential for writing correct conditional logic and arithmetic, and motivates the recommendation to use `===` over `==`.

# Examples

**Example 1** (Ch 1, lines 555-566): Coercion demonstrations:
```js
console.log(8 * null)     // → 0
console.log("5" - 1)      // → 4
console.log("5" + 1)      // → 51
console.log("five" * 2)   // → NaN
console.log(false == 0)   // → true
```

**Example 2** (Ch 1, lines 595-600): Null/undefined equality:
```js
console.log(null == undefined);  // → true
console.log(null == 0);          // → false
```

# Relationships

## Builds Upon
- **Value**, **Number**, **String**, **Boolean** -- The types being coerced.

## Enables
- **Short-Circuit Evaluation** -- `||` and `&&` coerce left operand to Boolean.
- Understanding the need for **Strict Equality**.

## Related
- **Strict Equality** -- `===` exists to avoid coercion.
- **Special Numbers** -- `NaN` results from failed numeric coercion.

## Contrasts With
- **Strict Equality** -- Avoids coercion entirely.

# Common Errors

- **Error**: Assuming `"5" + 1` performs addition.
  **Correction**: `+` prefers string concatenation when a string is present, producing `"51"`, not `6`.

- **Error**: Assuming `null == 0` is true because null coerces to 0 in arithmetic.
  **Correction**: `null == 0` is `false`. With `==`, null only equals null or undefined.

# Common Confusions

- **Confusion**: Type coercion always follows arithmetic rules.
  **Clarification**: The `+` operator is ambiguous -- it prefers concatenation when strings are involved but addition otherwise. Other arithmetic operators (`-`, `*`, `/`) always coerce to numbers.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Automatic type conversion", lines 547-621 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated section with explicit definition using italicized term and extensive examples
- Cross-reference status: verified within chapter
