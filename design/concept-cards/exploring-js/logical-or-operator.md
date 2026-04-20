---
# === CORE IDENTIFICATION ===
concept: Logical Or Operator
slug: logical-or-operator

# === CLASSIFICATION ===
category: primitive-types
subcategory: booleans
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Booleans"
chapter_number: 17
pdf_page: null
section: "Logical Or (||)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "||"
  - "logical OR"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - falsy-and-truthy-values
extends: []
related:
  - logical-and-operator
  - short-circuiting
  - value-preservation
  - nullish-coalescing-operator
contrasts_with:
  - logical-and-operator
  - nullish-coalescing-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

The logical Or operator (`||`) returns the first truthy operand or the last operand if all are falsy. It is value-preserving and short-circuiting.

# Core Definition

The expression `a || b` is evaluated as: (1) evaluate `a`; (2) if the result is truthy, return it; (3) otherwise, evaluate `b` and return the result. Equivalent to `a ? a : b`. It is *value-preserving* and *short-circuiting* (Ch. 17, Section 17.5.4).

# Prerequisites

- **falsy-and-truthy-values** -- determines which operand is returned

# Key Properties

1. Value-preserving: returns actual operand values, not booleans
2. Short-circuiting: second operand not evaluated if first is truthy
3. Equivalent to `a ? a : b`
4. Legacy use for default values (superseded by `??`)

# Construction / Recognition

```js
true || 'abc'    // true (short-circuits)
false || 'abc'   // 'abc' (returns second operand)
'abc' || 'def'   // 'abc' (first is truthy)
```

# Context & Application

Before ES2020, `||` was the standard way to provide default values. It has been largely superseded by `??` for that purpose, since `||` treats `0`, `''`, and `false` as triggers for the default.

# Examples

From the source text:

```js
> true || false
true
> true || 'abc'
true
> false || true
true
> false || 'abc'
'abc'
> 'abc' || 'def'
'abc'
```

Legacy default value pattern:
```js
const valueToUse = receivedValue || defaultValue;
```

# Relationships

## Builds Upon
- **falsy-and-truthy-values** — determines behavior

## Enables
- Legacy default value patterns

## Related
- **nullish-coalescing-operator** — modern replacement for default values
- **short-circuiting** — key behavior
- **value-preservation** — operands returned unchanged

## Contrasts With
- **logical-and-operator** — `&&` returns first falsy; `||` returns first truthy
- **nullish-coalescing-operator** — `??` only triggers for nullish, not all falsy

# Common Errors

- **Error**: Using `||` for defaults when `0` or `''` are valid values
  **Correction**: Use `??` instead, which only triggers for `undefined` and `null`.

# Common Confusions

- **Confusion**: Thinking `||` and `??` are interchangeable
  **Clarification**: `false || 'default'` returns `'default'`, but `false ?? 'default'` returns `false`.

# Source Reference

Chapter 17: Booleans, Section 17.5.4, lines 579-628.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit algorithm with examples
- Cross-reference status: verified against Ch. 16 `??` comparison
