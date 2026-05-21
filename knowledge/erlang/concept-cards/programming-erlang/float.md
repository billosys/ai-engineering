---
# === CORE IDENTIFICATION ===
concept: Float
slug: float

# === CLASSIFICATION ===
category: data-types
subcategory: primitive-types
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Floating-Point Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - floating-point number

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - term
contrasts_with:
  - integer

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a float in Erlang?"
  - "How does float division differ from integer division?"
---

# Quick Definition

A float is an Erlang floating-point number, internally a 64-bit IEEE 754 value. Dividing two integers with `/` produces a float, and floats carry the usual rounding and precision limitations.

# Core Definition

Erlang floating-point numbers are written with a decimal point, e.g. `3.0`. "When you divide two integers with `/`, the result is automatically converted to a floating-point number; thus, `5/3` evaluates to `1.6666666666666667`" (Chapter 3, "Floating-Point Numbers"). Even an exact division such as `4/2` produces the float `2.0` rather than the integer `2`. "Internally, Erlang uses 64-bit IEEE 754-1985 floats, so programs using floats will have the same kind of rounding or precision problems associated with floats that you would get in a language like C." A trailing `.` ends an expression and is not a decimal point — "If I had wanted a floating-point number here, I'd have written `3.0`."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A float is written with a decimal point (e.g., `3.0`, `1.82`).
2. Internally a 64-bit IEEE 754-1985 floating-point value.
3. Subject to the same rounding and precision problems as C floats.
4. The `/` operator on two integers always yields a float.
5. Even `4/2` yields the float `2.0`, not the integer `2`.
6. A trailing `.` (end of expression) is not a decimal point.

# Construction / Recognition

## To Write a Float:
1. Include a decimal point, e.g. `3.0` or `1.82`.

## To Produce a Float by Division:
1. Use `/` on numbers; the result is automatically a float.

## To Recognize It:
1. A number containing a decimal point.

# Context & Application

- **Typical contexts**: Measurements and computed ratios — heights, areas, temperatures.
- **Common applications**: `area({circle, Radius}) -> 3.14159 * Radius * Radius` (Chapter 4); temperature conversions.
- **Historical/stylistic notes**: Armstrong warns floats carry C-like precision issues, so exact arithmetic should use integers.

# Examples

**Example 1** (Chapter 3, "Floating-Point Numbers"): `5/3.` evaluates to `1.6666666666666667`.

**Example 2** (Chapter 3, "Floating-Point Numbers"): `4/2.` evaluates to `2.0` — "Even though `4` is exactly divisible by `2`, the result is a floating-point number and not an integer."

# Relationships

## Builds Upon
- This is a foundational data type and does not build upon another card in this source.

## Enables
- Used wherever non-integer numeric values are needed.

## Related
- **Term** — A float is a primitive term.

## Contrasts With
- **Integer** — Integers are arbitrary-sized and exact; floats are 64-bit IEEE 754 with rounding error. The `/` operator yields a float; `div`/`rem` yield integers.

# Common Errors

- **Error**: Using `/` when an integer result is required.
  **Correction**: `/` always produces a float; use `div` for integer division.

- **Error**: Mistaking a trailing `.` for a decimal point.
  **Correction**: The dot that ends an expression is punctuation; to write a float, include a digit after the point (`3.0`).

# Common Confusions

- **Confusion**: Believing float arithmetic in Erlang is exact.
  **Clarification**: Floats are 64-bit IEEE 754 values and have the same rounding/precision problems as in C.

- **Confusion**: Expecting `4/2` to be the integer `2`.
  **Clarification**: `/` converts to a float; `4/2` is `2.0`.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, section "Floating-Point Numbers." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 3, "Floating-Point Numbers."
- Confidence rationale: HIGH — float representation and division behavior explicitly stated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
