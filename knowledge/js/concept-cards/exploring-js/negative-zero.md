---
# === CORE IDENTIFICATION ===
concept: Negative Zero
slug: negative-zero

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
section: "Even stricter than ===: Object.is() (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-0"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
  - ieee-754-floating-point
extends: []
related:
  - object-is
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript has both positive zero (`0`) and negative zero (`-0`). They are considered equal by `===` but distinguished by `Object.is()`. Negative zero is an IEEE 754 artifact rarely encountered in practice.

# Core Definition

IEEE 754 double precision has two representations of zero: `+0` and `-0`. In JavaScript, `0 === -0` is `true`, but `Object.is(0, -0)` is `false`. Negative zero can be produced by certain operations like `-Math.pow(0, 1)` and is mostly irrelevant in practice (Ch. 15, Section 15.5.4).

# Prerequisites

- **number-type** -- negative zero is a number value
- **ieee-754-floating-point** -- negative zero is an IEEE 754 feature

# Key Properties

1. `0 === -0` is `true`
2. `Object.is(0, -0)` is `false`
3. `-0` converts to string `'0'` (not `'-0'`)
4. Rarely encountered in practice
5. Produced by signed division of zero or similar operations

# Construction / Recognition

```js
> 0 === -0
true
> Object.is(0, -0)
false
```

# Context & Application

Negative zero is mostly an academic curiosity. The distinction rarely matters in real code, but `Object.is()` can detect it when needed.

# Examples

From the source text:

```js
> Object.is(0, -0)
false
> 0 === -0
true
```

# Relationships

## Builds Upon
- **number-type** — negative zero is a number
- **ieee-754-floating-point** — explains why it exists

## Enables
- Nothing practical in most code

## Related
- **object-is** — can distinguish `0` from `-0`

## Contrasts With
- None

# Common Errors

- **Error**: None common -- negative zero rarely causes problems

# Common Confusions

- **Confusion**: Thinking negative zero is a bug
  **Clarification**: It is a valid IEEE 754 value. The sign bit is set but the value is zero.

# Source Reference

Chapter 15: Operators, Section 15.5.4, lines 724-734.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit comparison in source
- Cross-reference status: verified
