---
# === CORE IDENTIFICATION ===
concept: Short-Circuit Evaluation
slug: short-circuit-evaluation

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
section: "Short-circuiting of logical operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - short-circuiting
  - lazy evaluation of logical operators

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logical-operators
  - boolean
extends: []
related:
  - type-coercion
  - nullish-coalescing-operator
  - ternary-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Short-circuit evaluation means that `&&` and `||` evaluate their right-hand operand only when necessary, and return one of the original operand values rather than necessarily a Boolean.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 679-685 of 01-values-types-and-operators.md): "Another important property of these two operators is that the part to their right is evaluated only when necessary. In the case of `true || X`, no matter what `X` is -- even if it's a piece of program that does something *terrible* -- the result will be true, and `X` is never evaluated. The same goes for `false && X`, which is false and will ignore `X`. This is called *short-circuit evaluation*."

# Prerequisites

- **Logical Operators** -- Short-circuiting is a property of `&&` and `||`.
- **Boolean** -- The left operand is converted to Boolean to decide whether to evaluate the right.

# Key Properties

1. `||` returns the **left value** if it converts to true, otherwise the **right value** (lines 634-636).
2. `&&` returns the **left value** if it converts to false, otherwise the **right value** (lines 673-676).
3. The right side is **not evaluated** if the left side determines the result (lines 680-685).
4. Returns one of the **original values**, not necessarily a Boolean (lines 628-631).
5. Useful for **default values**: `value || "default"` (lines 648-651).
6. The ternary operator also evaluates only the selected branch (lines 688-690).

# Construction / Recognition

## To Construct/Create:
1. Default value pattern: `possiblyEmpty || "fallback"`.
2. Guard pattern: `object && object.property`.

## To Identify/Recognize:
1. `||` or `&&` used with potentially non-Boolean operands.
2. Reliance on only one side being evaluated.

# Context & Application

Short-circuit evaluation enables common JavaScript patterns like providing default values (`name || "Anonymous"`) and guard expressions (`user && user.name`). Understanding that these operators return original values, not Booleans, is key to using them idiomatically.

# Examples

**Example 1** (Ch 1, lines 640-645): Default value with `||`:
```js
console.log(null || "user")
// → user
console.log("Agnes" || "user")
// → Agnes
```

**Example 2** (Ch 1, lines 663-670): Contrast with `??`:
```js
console.log(0 || 100);
// → 100
console.log(0 ?? 100);
// → 0
console.log(null ?? 100);
// → 100
```

# Relationships

## Builds Upon
- **Logical Operators** -- Short-circuiting is a behavior of `&&` and `||`.
- **Boolean** -- Left operand is coerced to Boolean.

## Enables
- Default value patterns.
- Guard clause patterns.

## Related
- **Nullish Coalescing Operator** -- `??` is a more precise alternative to `||` for defaults.
- **Ternary Operator** -- Also evaluates only the selected branch.
- **Type Coercion** -- `0`, `""`, and `NaN` are falsy, affecting `||` defaults.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using `||` for defaults when `0` or `""` are valid values.
  **Correction**: `0 || 100` gives `100` because `0` is falsy. Use `??` instead: `0 ?? 100` gives `0`.

# Common Confusions

- **Confusion**: `||` and `&&` always return Boolean values.
  **Clarification**: They return one of the original operand values. `null || "user"` returns the string `"user"`, not `true`.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Short-circuiting of logical operators", lines 623-690 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated subsection with explicit definition using italicized term
- Cross-reference status: verified within chapter
