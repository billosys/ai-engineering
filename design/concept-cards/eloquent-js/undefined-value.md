---
# === CORE IDENTIFICATION ===
concept: Undefined
slug: undefined-value

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
  - null-value
  - binding
contrasts_with:
  - null-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes null from undefined?"
  - "What is a value in JavaScript?"
---

# Quick Definition

`undefined` is a special value that denotes the absence of a meaningful value, yielded by operations that do not produce a meaningful result and by bindings that have not been assigned a value.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 530-538 of 01-values-types-and-operators.md): "There are two special values, written `null` and `undefined`, that are used to denote the absence of a *meaningful* value. They are themselves values, but they carry no information." Further: "Many operations in the language that don't produce a meaningful value yield `undefined` simply because they have to yield *some* value."

# Prerequisites

- **Value** -- `undefined` is itself a value.

# Key Properties

1. Denotes the **absence of a meaningful value**.
2. Is itself a value, but **carries no information**.
3. Yielded by operations that **don't produce a meaningful result**.
4. The value of a **binding defined without assignment** (Ch 2, lines 172-174).
5. Treated as mostly interchangeable with `null` in practice (lines 543-545).
6. `null == undefined` is `true`, but `null == 0` is `false` (lines 595-600).

# Construction / Recognition

## To Construct/Create:
1. Declare a binding without assigning a value: `let x;` -- `x` is `undefined`.
2. Access a missing property on an object.
3. Call a function that has no `return` statement.

## To Identify/Recognize:
1. `typeof undefined` returns `"undefined"`.
2. Compare with `=== undefined`.

# Context & Application

`undefined` appears naturally in JavaScript when values are expected but not provided. Understanding when and why `undefined` appears is essential for debugging and for writing robust code that handles missing values.

# Examples

**Example 1** (Ch 2, lines 171-174 of 02-program-structure.md): Binding without a value:
"When you define a binding without giving it a value, the tentacle has nothing to grasp, so it ends in thin air. If you ask for the value of an empty binding, you'll get the value `undefined`."

**Example 2** (Ch 1, lines 595-600): Comparison with null:
```js
console.log(null == undefined);
// → true
console.log(null == 0);
// → false
```

# Relationships

## Builds Upon
- **Value** -- `undefined` is a type of value.

## Enables
- **Binding** -- Understanding what uninitialized bindings hold.
- **Type Coercion** -- `undefined` participates in coercion rules.

## Related
- **Null** -- The other "empty value" in JavaScript.

## Contrasts With
- **Null** -- While mostly interchangeable, `undefined` typically means "not yet assigned" while `null` is used for intentional absence of value.

# Common Errors

- **Error**: Treating `undefined` as a reliable indicator of an error condition.
  **Correction**: `undefined` is the default value for many normal operations (uninitialized bindings, missing function returns). It does not necessarily indicate an error.

# Common Confusions

- **Confusion**: `undefined` and `null` have meaningfully different purposes.
  **Clarification**: "The difference in meaning between `undefined` and `null` is an accident of JavaScript's design, and it doesn't matter most of the time" (lines 541-543). In practice, treat them as mostly interchangeable.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Empty values", lines 527-545 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit description in dedicated section
- Cross-reference status: verified with Ch 2 binding discussion
