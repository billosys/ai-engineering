---
# === CORE IDENTIFICATION ===
concept: Loose Equality
slug: loose-equality

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
section: "Automatic type conversion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - abstract equality
  - double equals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - comparison-operators
  - type-coercion
extends:
  - comparison-operators
related:
  - type-coercion
contrasts_with:
  - strict-equality

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes == and ===?"
  - "What is type coercion?"
---

# Quick Definition

The loose equality operator (`==`) compares two values for equality but performs type coercion when the types differ, following a complicated set of rules that can produce surprising results.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 586-594 of 01-values-types-and-operators.md): "When comparing values of the same type using the `==` operator, the outcome is easy to predict: you should get true when both values are the same, except in the case of `NaN`. But when the types differ, JavaScript uses a complicated and confusing set of rules to determine what to do. In most cases, it just tries to convert one of the values to the other value's type. However, when `null` or `undefined` occurs on either side of the operator, it produces true only if both sides are one of `null` or `undefined`."

# Prerequisites

- **Comparison Operators** -- `==` is a comparison operator.
- **Type Coercion** -- `==` triggers coercion when types differ.

# Key Properties

1. Same types: straightforward equality (except NaN) (line 587-588).
2. Different types: **coerces** one value to the other's type (lines 590-591).
3. Special rule: `null == undefined` is `true`, but `null == 0` is `false` (lines 592-594).
4. `0 == false` and `"" == false` are `true` due to coercion (line 611).
5. The source recommends using `===` instead "defensively" (lines 618-619).

# Construction / Recognition

## To Construct/Create:
1. `value1 == value2` -- compares with coercion.
2. `value1 != value2` -- not-equal with coercion.

## To Identify/Recognize:
1. Two-character comparison: `==` or `!=`.

# Context & Application

Loose equality is the default equality operator in JavaScript but is widely considered error-prone due to its coercion rules. Most style guides recommend strict equality (`===`) instead. However, `== null` is a useful idiom for checking both null and undefined.

# Examples

**Example 1** (Ch 1, lines 555-566): Coercion surprises:
```js
console.log(false == 0)
// → true
```

**Example 2** (Ch 1, lines 595-600): Null/undefined special case:
```js
console.log(null == undefined);
// → true
console.log(null == 0);
// → false
```

**Example 3** (Ch 1, lines 603-606): Useful idiom: "When you want to test whether a value has a real value instead of `null` or `undefined`, you can compare it to `null` with the `==` or `!=` operator."

# Relationships

## Builds Upon
- **Comparison Operators** -- `==` is a comparison operator.
- **Type Coercion** -- `==` performs coercion.

## Enables
- The `== null` idiom for null/undefined checking.

## Related
- **Type Coercion** -- The mechanism behind `==`'s behavior.

## Contrasts With
- **Strict Equality** (`===`) -- Compares without any type conversion.

# Common Errors

- **Error**: Using `==` and getting unexpected true results from type coercion.
  **Correction**: `0 == ""` is `true` (both coerce). Use `===` to avoid this: `0 === ""` is `false`.

# Common Confusions

- **Confusion**: `==` is always wrong to use.
  **Clarification**: `==` is useful for checking `null`/`undefined` together: `value == null` catches both. But the source recommends `===` as the default.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Automatic type conversion", lines 586-621 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit description with detailed rules
- Cross-reference status: verified within chapter
