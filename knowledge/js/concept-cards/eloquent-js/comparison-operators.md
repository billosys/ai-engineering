---
# === CORE IDENTIFICATION ===
concept: Comparison Operators
slug: comparison-operators

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
section: "Comparison"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - relational operators

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
  - boolean
extends: []
related:
  - strict-equality
  - type-coercion
  - binary-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes == and ===?"
  - "What is a value in JavaScript?"
---

# Quick Definition

Comparison operators (`>`, `<`, `>=`, `<=`, `==`, `!=`, `===`, `!==`) compare two values and produce a Boolean result indicating whether the comparison holds true.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 409-412 of 01-values-types-and-operators.md): "The `>` and `<` signs are the traditional symbols for 'is greater than' and 'is less than', respectively. They are binary operators. Applying them results in a Boolean value that indicates whether they hold true in this case." Additional operators include `>=` (greater than or equal to), `<=` (less than or equal to), `==` (equal to), and `!=` (not equal to) (lines 432-434).

# Prerequisites

- **Value** -- Comparisons operate on values.
- **Boolean** -- Comparisons produce Boolean results.

# Key Properties

1. All comparison operators are **binary** -- they take two operands.
2. They produce **Boolean values** (`true` or `false`).
3. Strings are compared by **Unicode code** from left to right (lines 428-429).
4. Uppercase letters are "less" than lowercase in string comparison (line 426).
5. `==` performs **type coercion** when types differ (lines 586-593).
6. `===` and `!==` test **precise equality** without type conversion (lines 613-615).
7. `NaN` is not equal to itself: `NaN == NaN` is `false` (lines 444-450).

# Construction / Recognition

## To Construct/Create:
1. Place a comparison operator between two values: `3 > 2`, `"a" == "b"`.

## To Identify/Recognize:
1. Operators `>`, `<`, `>=`, `<=`, `==`, `!=`, `===`, `!==` in expressions.
2. The result is always a Boolean.

# Context & Application

Comparison operators are essential for all decision-making in programs -- they are used in `if` conditions, `while` loop conditions, and any logic that depends on relationships between values.

# Examples

**Example 1** (Ch 1, lines 401-406): Numeric comparison:
```js
console.log(3 > 2)
// → true
console.log(3 < 2)
// → false
```

**Example 2** (Ch 1, lines 418-421): String comparison:
```js
console.log("Aardvark" < "Zoroaster")
// → true
```

**Example 3** (Ch 1, lines 436-441): Equality and inequality:
```js
console.log("Garnet" != "Ruby")
// → true
console.log("Pearl" == "Amethyst")
// → false
```

# Relationships

## Builds Upon
- **Value** -- Comparisons operate on values.
- **Boolean** -- Comparisons produce Booleans.

## Enables
- **Conditional Execution** -- `if` statements use comparison results.
- **While Loop** -- Loop conditions use comparisons.

## Related
- **Strict Equality** -- `===` and `!==` avoid type coercion.
- **Type Coercion** -- `==` triggers type conversion.
- **Binary Operator** -- All comparison operators are binary.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using `==` when precise type matching is needed.
  **Correction**: Use `===` to prevent type coercion: `"" === false` is `false`, while `"" == false` is `true`.

- **Error**: Comparing with `NaN` using `==`.
  **Correction**: `NaN == NaN` is `false`. Use `Number.isNaN()` instead.

# Common Confusions

- **Confusion**: String comparison uses dictionary order.
  **Clarification**: String comparison uses Unicode code order, where uppercase letters are "less" than lowercase (e.g., `"Z" < "a"`).

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Comparison", lines 395-455 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated subsection with thorough examples
- Cross-reference status: verified within chapter
