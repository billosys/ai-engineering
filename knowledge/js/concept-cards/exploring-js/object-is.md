---
# === CORE IDENTIFICATION ===
concept: Object.is()
slug: object-is

# === CLASSIFICATION ===
category: types-values
subcategory: operators
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Operators"
chapter_number: 15
pdf_page: null
section: "Even stricter than ===: Object.is() (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "same-value equality"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - strict-equality-operator
extends:
  - strict-equality-operator
related:
  - nan-value
contrasts_with:
  - strict-equality-operator
  - loose-equality-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do `==` (loose equality) and `===` (strict equality) relate to type coercion?"
---

# Quick Definition

`Object.is()` is a comparison method that is even stricter than `===`: it considers `NaN` equal to itself and distinguishes `+0` from `-0`.

# Core Definition

`Object.is()` compares two values using the SameValue algorithm. Unlike `===`, it returns `true` for `Object.is(NaN, NaN)` and `false` for `Object.is(0, -0)`. This makes it useful for cases where `===` has edge-case limitations (Ch. 15, Section 15.5.4).

# Prerequisites

- **strict-equality-operator** -- Object.is() refines strict equality behavior

# Key Properties

1. `Object.is(NaN, NaN)` returns `true` (unlike `===`)
2. `Object.is(0, -0)` returns `false` (unlike `===` which returns `true`)
3. For all other values, behaves identically to `===`
4. Useful for implementing NaN-aware comparisons

# Construction / Recognition

```js
Object.is(3, 3)     // true
Object.is(3, '3')   // false
Object.is(NaN, NaN) // true
Object.is(0, -0)    // false
```

# Context & Application

`Object.is()` is useful when you need NaN-aware comparison, such as implementing array search functions that can find NaN values. The `-0` distinction is rarely needed in practice.

# Examples

From the source text:

```js
> Object.is(NaN, NaN)
true
> NaN === NaN
false

> Object.is(0, -0)
false
> 0 === -0
true
```

Using `Object.is()` to find NaN in arrays:
```js
const myIndexOf = (arr, elem) => {
  return arr.findIndex(x => Object.is(x, elem));
};
> myIndexOf([0,NaN,2], NaN)
1
> [0,NaN,2].indexOf(NaN)
-1
```

# Relationships

## Builds Upon
- **strict-equality-operator** — Object.is() is a refinement of strict equality

## Enables
- NaN-aware search algorithms

## Related
- **nan-value** — Object.is() solves NaN's self-inequality problem

## Contrasts With
- **strict-equality-operator** — `===` treats NaN as not equal to itself
- **loose-equality-operator** — `==` uses coercion, `Object.is()` never does

# Common Errors

- **Error**: Using `Object.is()` as a general replacement for `===`
  **Correction**: `===` is sufficient for nearly all comparisons. `Object.is()` is only needed for NaN detection or -0 distinction.

# Common Confusions

- **Confusion**: Thinking `Object.is()` does deep structural comparison
  **Clarification**: Like `===`, `Object.is()` compares objects by identity (reference), not by structure.

# Source Reference

Chapter 15: Operators, Section 15.5.4, lines 695-761.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit comparison with `===` provided
- Cross-reference status: verified
