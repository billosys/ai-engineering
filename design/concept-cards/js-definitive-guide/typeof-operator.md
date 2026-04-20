---
# === CORE IDENTIFICATION ===
concept: The typeof Operator
slug: typeof-operator

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 110
section: "4.13.3 The typeof Operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
extends: []
related:
  - instanceof-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `typeof` operator is a unary operator that returns a string indicating the type of its operand, such as `"number"`, `"string"`, `"object"`, `"function"`, or `"undefined"`.

# Core Definition

"typeof is a unary operator that is placed before its single operand, which can be of any type. Its value is a string that specifies the type of the operand." (Ch. 4, §4.13.3)

# Prerequisites

- **primary-expressions** — `typeof` takes any expression as operand.

# Key Properties

1. Returns: `"undefined"`, `"boolean"`, `"number"`, `"bigint"`, `"string"`, `"symbol"`, `"function"`, or `"object"`.
2. `typeof null` returns `"object"` (a historical bug in the language).
3. `typeof` for any function returns `"function"`.
4. `typeof` for all non-function objects (including arrays) returns `"object"`.
5. `typeof` does not distinguish between different classes of objects — use `instanceof` for that.

# Construction / Recognition

```js
typeof value    // Returns a string describing the type
```

# Context & Application

`typeof` is used for runtime type checking, especially to test whether a variable is defined (`typeof x === "undefined"`) without risking a ReferenceError.

# Examples

From the source text (§4.13.3, pp. 110-111):

| x | typeof x |
|---|----------|
| `undefined` | `"undefined"` |
| `null` | `"object"` |
| `true` or `false` | `"boolean"` |
| any number or NaN | `"number"` |
| any BigInt | `"bigint"` |
| any string | `"string"` |
| any symbol | `"symbol"` |
| any function | `"function"` |
| any nonfunction object | `"object"` |

```js
(typeof value === "string") ? "'" + value + "'" : value.toString()
```

# Relationships

## Builds Upon
- **primary-expressions** — Operates on any expression

## Enables
- Runtime type checking and conditional type handling

## Related
- **instanceof-operator** — Distinguishes between object classes (what `typeof` cannot do)

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `typeof` to check for `null`.
  **Correction**: `typeof null` is `"object"`. Test for null explicitly: `value === null`.

# Common Confusions

- **Confusion**: Expecting `typeof` to distinguish arrays from plain objects.
  **Clarification**: Both return `"object"`. Use `Array.isArray()` to test for arrays.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.13.3, pages 110-111.

# Verification Notes

- Definition source: Direct quote from §4.13.3
- Confidence rationale: High — complete type table provided
- Uncertainties: None
- Cross-reference status: Verified
