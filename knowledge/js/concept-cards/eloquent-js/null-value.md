---
# === CORE IDENTIFICATION ===
concept: "Null"
slug: null-value

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
section: "Empty values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
extends: []
related:
  - undefined-value
  - type-coercion
contrasts_with:
  - undefined-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes null from undefined?"
  - "What is a value in JavaScript?"
---

# Quick Definition

`null` is a special value that denotes the intentional absence of a meaningful value, paired with `undefined` as one of JavaScript's two "empty values."

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 530-533 of 01-values-types-and-operators.md): "There are two special values, written `null` and `undefined`, that are used to denote the absence of a *meaningful* value. They are themselves values, but they carry no information."

# Prerequisites

- **Value** -- `null` is itself a value.

# Key Properties

1. Denotes the **absence of a meaningful value**.
2. Is itself a value, but **carries no information**.
3. Treated as mostly interchangeable with `undefined` in practice (lines 543-545).
4. `null == undefined` is `true` (lines 595-597).
5. `null == 0` is `false` -- `null` only equals `null` or `undefined` with `==` (lines 592-600).
6. In type coercion, `null` becomes `0` in numeric contexts (e.g., `8 * null` produces `0`, line 556-557).

# Construction / Recognition

## To Construct/Create:
1. Use the keyword `null` directly.

## To Identify/Recognize:
1. Compare with `=== null`.
2. Note: `typeof null` returns `"object"` (a historical JavaScript bug), not `"null"`.

# Context & Application

`null` is used when a programmer wants to explicitly indicate "no value" or "empty." It is useful for testing whether a value has a real value: "When you want to test whether a value has a real value instead of `null` or `undefined`, you can compare it to `null` with the `==` or `!=` operator" (lines 603-606).

# Examples

**Example 1** (Ch 1, lines 556-557): Null in arithmetic (type coercion):
```js
console.log(8 * null)
// → 0
```

**Example 2** (Ch 1, lines 595-600): Null equality comparisons:
```js
console.log(null == undefined);
// → true
console.log(null == 0);
// → false
```

# Relationships

## Builds Upon
- **Value** -- `null` is a type of value.

## Enables
- **Type Coercion** -- `null` participates in coercion rules (becomes `0` in numeric contexts).

## Related
- **Undefined** -- The other "empty value."

## Contrasts With
- **Undefined** -- While mostly interchangeable, `null` is typically used for intentional absence, while `undefined` means "not yet assigned."

# Common Errors

- **Error**: Using `typeof null` to check for null.
  **Correction**: `typeof null` returns `"object"`, not `"null"`. Use `=== null` instead.

# Common Confusions

- **Confusion**: `null` and `undefined` serve importantly different purposes.
  **Clarification**: "The difference in meaning between `undefined` and `null` is an accident of JavaScript's design, and it doesn't matter most of the time" (lines 541-543).

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Empty values", lines 527-545 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit description in dedicated section
- Cross-reference status: verified with type coercion section
