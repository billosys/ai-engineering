---
# === CORE IDENTIFICATION ===
concept: Math Rounding Functions
slug: math-rounding

# === CLASSIFICATION ===
category: primitive-types
subcategory: numbers
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Math"
chapter_number: 19
pdf_page: null
section: "Rounding"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Math.floor"
  - "Math.ceil"
  - "Math.round"
  - "Math.trunc"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - math-object
extends: []
related:
  - converting-to-number
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript provides four rounding functions: `Math.floor()` (round down), `Math.ceil()` (round up), `Math.round()` (round to nearest, .5 rounds up), and `Math.trunc()` (remove fractional part).

# Core Definition

Four approaches to rounding: `Math.floor(x)` returns the largest integer <= x; `Math.ceil(x)` returns the smallest integer >= x; `Math.round(x)` returns the nearest integer (.5 rounds toward +infinity); `Math.trunc(x)` removes the decimal fraction. Their behavior differs notably with negative numbers (Ch. 19, Section 19.3.1).

# Prerequisites

- **math-object** -- rounding functions are methods of Math

# Key Properties

1. `Math.floor()`: toward -infinity (ES1)
2. `Math.ceil()`: toward +infinity (ES1)
3. `Math.round()`: to nearest, .5 toward +infinity (ES1)
4. `Math.trunc()`: toward zero (ES6)
5. For negative numbers: `Math.floor(-2.1)` is `-3`, `Math.trunc(-2.1)` is `-2`

# Construction / Recognition

```js
Math.floor(2.9)  // 2
Math.ceil(2.1)   // 3
Math.round(2.5)  // 3
Math.trunc(2.9)  // 2
```

# Context & Application

Use `Math.trunc()` to convert floats to integers (similar to integer truncation in C). Use `Math.floor()` for consistent downward rounding (important for array indexing with division).

# Examples

From the source text, rounding table for representative values:

| Input  | floor | ceil | round | trunc |
|--------|-------|------|-------|-------|
| -2.9   | -3    | -2   | -3    | -2    |
| -2.5   | -3    | -2   | -2    | -2    |
| -2.1   | -3    | -2   | -2    | -2    |
| 2.1    | 2     | 3    | 2     | 2     |
| 2.5    | 2     | 3    | 3     | 2     |
| 2.9    | 2     | 3    | 3     | 2     |

# Relationships

## Builds Upon
- **math-object** — part of the Math namespace

## Enables
- Integer conversion from floats
- Array index calculations

## Related
- **converting-to-number** — rounding is often done after type conversion

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `Math.round(-2.5)` to be `-3`
  **Correction**: `Math.round()` rounds .5 toward +infinity, so `Math.round(-2.5)` is `-2`.

# Common Confusions

- **Confusion**: Thinking `Math.floor()` and `Math.trunc()` are the same
  **Clarification**: They differ for negative numbers: `Math.floor(-2.1)` is `-3` but `Math.trunc(-2.1)` is `-2`.

# Source Reference

Chapter 19: Math, Section 19.3, lines 190-454.

# Verification Notes

- Definition source: direct (complete rounding table provided)
- Confidence rationale: Exhaustive examples with positive and negative inputs
- Cross-reference status: verified
