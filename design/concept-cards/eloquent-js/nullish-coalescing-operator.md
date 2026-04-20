---
# === CORE IDENTIFICATION ===
concept: Nullish Coalescing Operator
slug: nullish-coalescing-operator

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
  - "?? operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - null-value
  - undefined-value
  - logical-operators
extends: []
related:
  - short-circuit-evaluation
contrasts_with:
  - logical-operators

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes null from undefined?"
  - "What must I know before understanding closures?"
---

# Quick Definition

The `??` (nullish coalescing) operator returns the right-hand value only when the left-hand value is `null` or `undefined`, unlike `||` which triggers on any falsy value.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 658-661 of 01-values-types-and-operators.md): "The `??` operator resembles `||` but returns the value on the right only if the one on the left is `null` or `undefined`, not if it is some other value that can be converted to `false`. Often, this is preferable to the behavior of `||`."

# Prerequisites

- **Null** and **Undefined** -- `??` specifically checks for these two values.
- **Logical Operators** -- `??` is understood in contrast to `||`.

# Key Properties

1. Returns right side **only if left is `null` or `undefined`** (line 659).
2. Does **not** trigger on other falsy values like `0`, `""`, or `NaN` (lines 659-661).
3. More **precise** than `||` for default value patterns.

# Construction / Recognition

## To Construct/Create:
1. `possiblyNullish ?? defaultValue`.

## To Identify/Recognize:
1. The `??` operator in an expression.

# Context & Application

The nullish coalescing operator is the preferred way to provide default values when `0`, `""`, or `false` are valid values that should not be replaced. It was introduced to address a common pitfall with `||`.

# Examples

**Example 1** (Ch 1, lines 663-670): Contrast with `||`:
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
- **Null** and **Undefined** -- The two values that trigger the right-hand side.
- **Logical Operators** -- `??` is an alternative to `||` for defaults.

## Enables
- Safe default value patterns that preserve `0`, `""`, and `false`.

## Related
- **Short-Circuit Evaluation** -- `??` also short-circuits.

## Contrasts With
- **`||` Operator** -- Triggers on any falsy value, not just null/undefined.

# Common Errors

- **Error**: Using `||` when `0` or `""` are valid values.
  **Correction**: Use `??` instead. `0 || 100` gives `100`, but `0 ?? 100` gives `0`.

# Common Confusions

- **Confusion**: `??` and `||` behave the same way.
  **Clarification**: `||` triggers on any falsy value (`0`, `""`, `NaN`, `false`, `null`, `undefined`), while `??` triggers only on `null` and `undefined`.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Short-circuiting of logical operators", lines 657-670 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit description with clear contrast examples
- Cross-reference status: verified within chapter
