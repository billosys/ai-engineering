---
# === CORE IDENTIFICATION ===
concept: The void Operator
slug: void-operator

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 112
section: "4.13.6 The void Operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
extends: []
related:
  - unary-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `void` operator evaluates its operand and then discards the value, always returning `undefined`. It is rarely used in modern JavaScript.

# Core Definition

"void is a unary operator that appears before its single operand, which may be of any type. This operator is unusual and infrequently used; it evaluates its operand, then discards the value and returns undefined." (Ch. 4, §4.13.6)

# Prerequisites

- **primary-expressions** — `void` takes any expression as operand.

# Key Properties

1. Always returns `undefined`.
2. The operand is evaluated (side effects occur), but the value is discarded.
3. Useful only when the operand has side effects but you want to suppress the return value.
4. One niche use: with arrow functions to suppress return values: `() => void counter++`.

# Construction / Recognition

```js
void expression
```

# Context & Application

The `void` operator is obscure and rarely needed. Its primary modern use case is suppressing the return value of arrow function shorthand when the function should return `undefined`.

# Examples

From the source text (§4.13.6, p. 112):

```js
let counter = 0;
const increment = () => void counter++;
increment()   // => undefined
counter       // => 1
```

# Relationships

## Builds Upon
- **primary-expressions** — Operates on any expression

## Enables
- No specific concepts

## Related
- **unary-operators** — Another unary operator category

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Expecting `void` to prevent side effects.
  **Correction**: `void` evaluates its operand (including side effects) — it only discards the return value.

# Common Confusions

- **Confusion**: Confusing `void` with `undefined`.
  **Clarification**: `void` is an operator that *produces* `undefined`; it is not a synonym for the value itself.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.13.6, page 112.

# Verification Notes

- Definition source: Direct quote from §4.13.6
- Confidence rationale: High — clearly described
- Uncertainties: None
- Cross-reference status: Verified
