---
# === CORE IDENTIFICATION ===
concept: Integer Division
slug: integer-division

# === CLASSIFICATION ===
category: language-mechanics
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "% is a remainder operator, not a modulo operator (bonus)"
chapter_number: 6
section: "The equations behind remainder and modulo"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "div operator"
  - "integer quotient"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - remainder-operator
  - modulo-operator
  - truncating-division
  - floor-division
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the remainder operator and the modulo operator?"
---

# Quick Definition

Integer division (`div`) divides two numbers and produces an integer quotient, discarding any fractional part according to a specific rounding strategy.

# Core Definition

As described in "Deep JavaScript" Ch 6, integer division is the operation that computes the quotient in the equations `dividend = (divisor * quotient) + remainder` and `|remainder| < |divisor|`. The key insight is that the choice of how to round the quotient to an integer determines whether you get remainder or modulo: truncating toward zero yields remainder, flooring toward negative infinity yields modulo.

# Prerequisites

- **Division** -- basic arithmetic division of numbers

# Key Properties

1. Produces an integer quotient from two operands.
2. The rounding strategy determines the associated remainder/modulo operation.
3. `Math.trunc()`-based integer division pairs with remainder.
4. `Math.floor()`-based integer division pairs with modulo.
5. Other strategies (e.g., `Math.ceil()`, `Math.round()`) produce yet other operations.

# Construction / Recognition

## To Construct/Create:
1. Perform floating-point division: `dividend / divisor`.
2. Apply a rounding function to get an integer: `Math.trunc()` for remainder-style, `Math.floor()` for modulo-style.

## To Identify/Recognize:
1. The result is always an integer.
2. The associated remainder satisfies `dividend = (divisor * quotient) + remainder`.

# Context & Application

Integer division is the foundation for both remainder and modulo operations. JavaScript does not have a dedicated integer division operator, but it can be implemented using `Math.trunc()` or `Math.floor()` on the result of regular division.

# Examples

**Example 1** (Ch 6): The defining equations:
```
dividend = (divisor * quotient) + remainder
|remainder| < |divisor|
remainder = dividend - (divisor * quotient)
quotient = dividend div divisor
```

**Example 2** (Ch 6): Two different integer divisions for -2 / 3:
```
Truncating: Math.trunc(-2/3) = 0   -> remainder = -2 - (3*0)  = -2
Flooring:   Math.floor(-2/3) = -1  -> remainder = -2 - (3*-1) =  1
```

# Relationships

## Builds Upon
- **Division** -- integer division is division with rounding to integer

## Enables
- **Remainder operator** -- remainder is defined as `dividend - (divisor * trunc_quotient)`
- **Modulo operator** -- modulo is defined as `dividend - (divisor * floor_quotient)`

## Related
- **Truncating division** -- one form of integer division
- **Floor division** -- another form of integer division

## Contrasts With
(none)

# Common Errors

- **Error**: Assuming there is only one way to do integer division.
  **Correction**: There are multiple rounding strategies (trunc, floor, ceil, round), each producing a different operation when paired with the remainder equation.

# Common Confusions

- **Confusion**: Integer division always means the same thing across languages.
  **Clarification**: Different languages choose different rounding strategies. JavaScript's `%` uses truncating division; Python's `%` uses floor division.

# Source Reference

Chapter 6: "% is a remainder operator, not a modulo operator (bonus)", Section 6.5, lines 2812-2898.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit equations and multiple rounding strategies discussed in source.
- Cross-reference status: verified against Ch 6 section 6.5
