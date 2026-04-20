---
# === CORE IDENTIFICATION ===
concept: Boolean
slug: boolean

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
section: "Boolean values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Boolean value
  - Boolean type

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
extends: []
related:
  - comparison-operators
  - logical-operators
  - type-coercion
  - conditional-execution
contrasts_with:
  - number
  - string

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

The Boolean type has just two values, `true` and `false`, used to distinguish between two possibilities such as "yes" and "no" or "on" and "off".

# Core Definition

As defined in "Eloquent JavaScript" (Ch 1, lines 390-393 of 01-values-types-and-operators.md): "It is often useful to have a value that distinguishes between only two possibilities, like 'yes' and 'no' or 'on' and 'off'. For this purpose, JavaScript has a *Boolean* type, which has just two values, true and false, written as those words."

# Prerequisites

- **Value** -- Booleans are a type of value.

# Key Properties

1. Only **two values**: `true` and `false`.
2. Produced by **comparison operators** (`>`, `<`, `>=`, `<=`, `==`, `!=`, `===`, `!==`).
3. Can be combined with **logical operators** (`&&`, `||`, `!`).
4. Central to **conditional execution** -- `if` statements and loops evaluate Boolean conditions.
5. Other values can be **converted** to Boolean: `0`, `NaN`, and `""` count as `false`; all other values count as `true` (lines 652-654).

# Construction / Recognition

## To Construct/Create:
1. Use the literal keywords: `true`, `false`.
2. Use comparison operators: `3 > 2` produces `true`.
3. Use logical operators: `!false` produces `true`.

## To Identify/Recognize:
1. `typeof` returns `"boolean"`.
2. The value is exactly `true` or `false`.

# Context & Application

Booleans are the basis of all decision-making in programs. Every conditional (`if`, `while`, `for`) ultimately depends on a Boolean condition to determine which code path to follow.

# Examples

**Example 1** (Ch 1, lines 401-406): Comparison producing Booleans:
```js
console.log(3 > 2)
// → true
console.log(3 < 2)
// → false
```

**Example 2** (Ch 1, lines 470-475): Logical operators on Booleans:
```js
console.log(true && false)
// → false
console.log(true && true)
// → true
```

# Relationships

## Builds Upon
- **Value** -- Booleans are a type of value.

## Enables
- **Conditional Execution** -- `if`/`else` depends on Boolean values.
- **While Loop** -- Loop condition must evaluate to Boolean.
- **Logical Operators** -- Operate on and produce Booleans.

## Related
- **Comparison Operators** -- Produce Boolean values.
- **Type Coercion** -- Non-Boolean values are coerced to Boolean in conditional contexts.

## Contrasts With
- **Number** -- Many possible values; Boolean has only two.
- **String** -- Represents text; Boolean represents truth values.

# Common Errors

- **Error**: Assuming only `true` and `false` can be used in conditions.
  **Correction**: Any value can be used in a Boolean context. `0`, `NaN`, `""`, `null`, and `undefined` are falsy; all others are truthy.

# Common Confusions

- **Confusion**: `0` and `false` are the same thing.
  **Clarification**: `0` is a number and `false` is a Boolean, but `0 == false` is `true` due to type coercion. They are not identical (`0 === false` is `false`).

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Boolean values", lines 387-525 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term in dedicated section
- Cross-reference status: verified within chapter
