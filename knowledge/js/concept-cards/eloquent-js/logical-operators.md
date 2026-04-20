---
# === CORE IDENTIFICATION ===
concept: Logical Operators
slug: logical-operators

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
section: "Logical operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean
extends: []
related:
  - short-circuit-evaluation
  - operator-precedence
  - nullish-coalescing-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

JavaScript supports three logical operators: `&&` (and), `||` (or), and `!` (not), which are used to reason about and combine Boolean values.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 460-462 of 01-values-types-and-operators.md): "There are also some operations that can be applied to Boolean values themselves. JavaScript supports three logical operators: *and*, *or*, and *not*. These can be used to 'reason' about Booleans."

# Prerequisites

- **Boolean** -- Logical operators primarily work with Boolean values.

# Key Properties

1. `&&` (logical and) -- "its result is true only if both the values given to it are true" (lines 466-468).
2. `||` (logical or) -- "it produces true if either of the values given to it is true" (lines 478-479).
3. `!` (logical not) -- "a unary operator that flips the value given to it" (lines 489-491).
4. **Precedence order**: `||` is lowest, then `&&`, then comparison operators (lines 497-499).
5. With non-Boolean values, `&&` and `||` return one of the **original values**, not necessarily a Boolean (lines 626-631).
6. Support **short-circuit evaluation** (lines 679-685).

# Construction / Recognition

## To Construct/Create:
1. `&&`: `condition1 && condition2`
2. `||`: `condition1 || condition2`
3. `!`: `!condition`

## To Identify/Recognize:
1. The symbols `&&`, `||`, or `!` in expressions.

# Context & Application

Logical operators are essential for combining conditions in `if` statements and loops. Their short-circuit behavior and ability to return non-Boolean values make them powerful tools for default values and guard clauses.

# Examples

**Example 1** (Ch 1, lines 470-475): Logical AND:
```js
console.log(true && false)
// → false
console.log(true && true)
// → true
```

**Example 2** (Ch 1, lines 481-486): Logical OR:
```js
console.log(false || true)
// → true
console.log(false || false)
// → false
```

**Example 3** (Ch 1, lines 503-505): Combined expression with precedence:
```js
1 + 1 == 2 && 10 * 10 > 50
```
Arithmetic first, then comparison, then `&&`.

# Relationships

## Builds Upon
- **Boolean** -- Logical operators reason about Booleans.

## Enables
- **Short-Circuit Evaluation** -- An important behavior of `&&` and `||`.
- **Conditional Execution** -- Complex conditions often use logical operators.

## Related
- **Operator Precedence** -- Determines how logical operators interact with others.
- **Nullish Coalescing Operator** -- `??` is related to `||`.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming `&&` and `||` always return Boolean values.
  **Correction**: They return one of the original operand values. `null || "user"` returns `"user"`, not `true`.

# Common Confusions

- **Confusion**: `&&` and `||` evaluate both sides.
  **Clarification**: They use short-circuit evaluation -- the right side is evaluated only when necessary.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Logical operators", lines 457-505 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated subsection with explicit definitions for each operator
- Cross-reference status: verified within chapter
