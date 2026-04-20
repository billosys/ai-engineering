---
# === CORE IDENTIFICATION ===
concept: Floating-Point Literals
slug: floating-point-literals

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: literals
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 44
section: "3.2.2 Floating-Point Literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - decimal literals
  - real number literals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
  - literals
extends:
  - literals
related:
  - integer-literals
  - rounding-errors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Floating-point literals represent real numbers using decimal point notation or exponential notation, following the syntax `[digits][.digits][(E|e)[(+|-)]digits]`.

# Core Definition

"Floating-point literals can have a decimal point; they use the traditional syntax for real numbers. A real value is represented as the integral part of the number, followed by a decimal point and the fractional part of the number." They "may also be represented using exponential notation: a real number followed by the letter e (or E), followed by an optional plus or minus sign, followed by an integer exponent." The syntax is: `[digits][.digits][(E|e)[(+|-)]digits]`. (p. 44)

# Prerequisites

- **number-type** — Floating-point literals produce Number values
- **literals** — Floating-point literals are a type of literal

# Key Properties

1. Syntax: `[digits][.digits][(E|e)[(+|-)]digits]`
2. Can use decimal point notation: `3.14`
3. Can use exponential notation: `6.02e23`
4. Can start with a decimal point: `.333333`
5. Underscores allowed as separators: `0.123_456_789`
6. Subject to binary floating-point rounding errors

# Construction / Recognition

```javascript
3.14
2345.6789
.333333333333333333
6.02e23             // 6.02 x 10^23
1.4738223E-32       // 1.4738223 x 10^-32
0.123_456_789       // underscore separator in fractional part
```

# Context & Application

Floating-point literals are used for any numeric value that requires a decimal component or very large/small values expressed in scientific notation.

# Examples

From the source text (p. 44):
```javascript
3.14
2345.6789
.333333333333333333
6.02e23             // 6.02 x 10^23
1.4738223E-32       // 1.4738223 x 10^-32
```

With separators (p. 44):
```javascript
let fraction = 0.123_456_789;  // Works in the fractional part, too.
```

# Relationships

## Builds Upon
- **number-type** — Floating-point literals produce Number values
- **literals** — A specific kind of literal

## Enables
- **rounding-errors** — Floating-point representation leads to rounding issues

## Related
- **integer-literals** — The other format for numeric literals

## Contrasts With
- None within this source

# Common Errors

- **Error**: Expecting exact decimal arithmetic with floating-point.
  **Correction**: Binary floating-point cannot exactly represent many decimal fractions; `.3 - .2 !== .1` (p. 47).

# Common Confusions

- **Confusion**: `.` always means a decimal point in JavaScript.
  **Clarification**: A `.` after a number is a decimal point; after a variable or object, it's property access. Context determines meaning.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.2.2, page 44.

# Verification Notes

- Definition source: Direct quote from p. 44
- Confidence rationale: High — clearly defined with syntax
- Uncertainties: None
- Cross-reference status: Verified
