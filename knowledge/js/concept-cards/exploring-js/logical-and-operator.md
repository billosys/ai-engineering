---
# === CORE IDENTIFICATION ===
concept: Logical And Operator
slug: logical-and-operator

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
section: "Logical And (x && y)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "&&"
  - "logical AND"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - falsy-and-truthy-values
extends: []
related:
  - logical-or-operator
  - short-circuiting
  - value-preservation
contrasts_with:
  - logical-or-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

The logical And operator (`&&`) returns the first falsy operand or the last operand if all are truthy. It is value-preserving and short-circuiting.

# Core Definition

The expression `a && b` is evaluated as: (1) evaluate `a`; (2) if the result is falsy, return it; (3) otherwise, evaluate `b` and return the result. It is equivalent to `!a ? a : b`. The operator is *value-preserving* (operands are returned unchanged, not converted to boolean) and *short-circuiting* (the second operand is not evaluated if the first is falsy) (Ch. 17, Section 17.5.3).

# Prerequisites

- **falsy-and-truthy-values** -- determines which operand is returned

# Key Properties

1. Value-preserving: returns actual operand values, not booleans
2. Short-circuiting: second operand not evaluated if first is falsy
3. Equivalent to `!a ? a : b`

# Construction / Recognition

```js
false && 'abc'  // false (short-circuits)
true && 'abc'   // 'abc' (returns second operand)
'' && 'abc'     // '' (short-circuits on falsy)
```

# Context & Application

Used for conditional execution (`condition && doSomething()`) and guarding expressions. The short-circuiting behavior makes it useful for safely accessing properties.

# Examples

From the source text:

```js
> false && true
false
> false && 'abc'
false
> true && false
false
> true && 'abc'
'abc'
> '' && 'abc'
''
```

# Relationships

## Builds Upon
- **falsy-and-truthy-values** — determines behavior

## Enables
- Guard expressions and conditional execution patterns

## Related
- **logical-or-operator** — complementary operator
- **short-circuiting** — key behavior of `&&`
- **value-preservation** — operands returned unchanged

## Contrasts With
- **logical-or-operator** — `||` returns first truthy operand; `&&` returns first falsy

# Common Errors

- **Error**: Expecting `&&` to always return a boolean
  **Correction**: `&&` returns the actual operand value, not a boolean conversion.

# Common Confusions

- **Confusion**: Thinking `0 && 'hello'` returns `false`
  **Clarification**: It returns `0` (the actual falsy value), not `false`.

# Source Reference

Chapter 17: Booleans, Section 17.5.3, lines 543-577.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit algorithm with examples
- Cross-reference status: verified
