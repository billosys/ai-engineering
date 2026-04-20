---
# === CORE IDENTIFICATION ===
concept: Unary Plus and Negation
slug: unary-plus-and-negation

# === CLASSIFICATION ===
category: primitive-types
subcategory: numbers
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Numbers"
chapter_number: 18
pdf_page: null
section: "Unary plus (+) and negation (-)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "unary +"
  - "unary -"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
  - converting-to-number
extends: []
related:
  - operator-coercion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

Unary plus (`+x`) coerces its operand to a number (equivalent to `Number(x)`). Unary negation (`-x`) coerces and negates. Both are ES1 features.

# Core Definition

"Both operators coerce their operands to numbers." Unary plus (`+x`) converts any value to a number, equivalent to `Number(x)`. Unary negation (`-x`) also converts and then negates the result (Ch. 18, Section 18.3.2).

# Prerequisites

- **number-type** -- the target type
- **converting-to-number** -- unary plus is equivalent to `Number()`

# Key Properties

1. `+x` converts `x` to number (ES1)
2. `-x` converts `x` to number and negates
3. `+'5'` produces `5`
4. `+'-12'` produces `-12`

# Construction / Recognition

```js
> +'5'
5
> +'-12'
-12
> -'9'
-9
```

# Context & Application

Unary `+` is a common shorthand for numeric conversion but `Number()` is more readable. Unary `+` is NOT supported for bigints.

# Examples

From the source text:

```js
> +'5'
5
> +'-12'
-12
> -'9'
-9
```

# Relationships

## Builds Upon
- **number-type** — produces numbers
- **converting-to-number** — equivalent conversion

## Enables
- Quick numeric conversion in expressions

## Related
- **operator-coercion** — unary operators coerce their operands

## Contrasts With
- None

# Common Errors

- **Error**: Using `+` on a bigint expecting numeric conversion
  **Correction**: Unary `+` throws `TypeError` for bigints. Use `Number(bigintValue)` instead.

# Common Confusions

- **Confusion**: Confusing unary `+` with the binary `+` (addition/concatenation)
  **Clarification**: Unary `+` has one operand and converts to number. Binary `+` has two operands and may concatenate strings.

# Source Reference

Chapter 18: Numbers, Section 18.3.2, lines 490-588.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit description with examples
- Cross-reference status: verified
