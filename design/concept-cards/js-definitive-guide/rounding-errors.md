---
# === CORE IDENTIFICATION ===
concept: Binary Floating-Point Rounding Errors
slug: rounding-errors

# === CLASSIFICATION ===
category: type-system
subcategory: primitive-types
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 47
section: "3.2.4 Binary Floating-Point and Rounding Errors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - floating-point precision
  - IEEE 754 rounding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
  - floating-point-literals
extends: []
related:
  - nan-and-infinity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Binary floating-point representation cannot exactly represent many common decimal fractions (like 0.1), leading to rounding errors that can cause unexpected inequality when comparing computed results.

# Core Definition

"There are infinitely many real numbers, but only a finite number of them (18,437,736,874,454,810,627, to be exact) can be represented exactly by the JavaScript floating-point format." "The IEEE-754 floating-point representation used by JavaScript is a binary representation, which can exactly represent fractions like 1/2, 1/8, and 1/1024. Unfortunately, the fractions we use most commonly (especially when performing financial calculations) are decimal fractions: 1/10, 1/100, and so on. Binary floating-point representations cannot exactly represent numbers as simple as 0.1." (p. 47)

# Prerequisites

- **number-type** — Must understand the Number type uses IEEE 754
- **floating-point-literals** — Must understand how floating-point numbers are written

# Key Properties

1. Only a finite set of real numbers can be represented exactly
2. Decimal fractions like 0.1, 0.2, 0.3 cannot be exactly represented in binary
3. Computed values are very close approximations but not exact
4. Problem is not JavaScript-specific — affects all languages using binary floating-point
5. Workaround: use scaled integers (e.g., cents instead of dollars)

# Construction / Recognition

```javascript
let x = .3 - .2;    // thirty cents minus 20 cents
let y = .2 - .1;    // twenty cents minus 10 cents
x === y              // => false: the two values are not the same!
x === .1             // => false: .3-.2 is not equal to .1
y === .1             // => true: .2-.1 is equal to .1
```

# Context & Application

This is especially important for financial calculations. The recommended approach is to "manipulate monetary values as integer cents rather than fractional dollars" (p. 47).

# Examples

From the source text (p. 47):
```javascript
let x = .3 - .2;    // thirty cents minus 20 cents
let y = .2 - .1;    // twenty cents minus 10 cents
x === y              // => false: the two values are not the same!
x === .1             // => false: .3-.2 is not equal to .1
y === .1             // => true: .2-.1 is equal to .1
```

# Relationships

## Builds Upon
- **number-type** — Rounding errors are inherent to the IEEE 754 format
- **floating-point-literals** — Affects decimal literal computation

## Enables
- Understanding of when to use BigInt or scaled integers

## Related
- **nan-and-infinity** — Other numeric edge cases

## Contrasts With
- None within this source

# Common Errors

- **Error**: Comparing floating-point arithmetic results for exact equality.
  **Correction**: Use tolerance-based comparison or work with scaled integers for financial calculations.

# Common Confusions

- **Confusion**: JavaScript's floating-point is broken.
  **Clarification**: This is not a JavaScript bug — it "affects any programming language that uses binary floating-point numbers." The values are adequate for almost any purpose; the problem only arises when comparing for exact equality (p. 47).

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.2.4, page 47.

# Verification Notes

- Definition source: Direct quotes from p. 47
- Confidence rationale: High — clearly explained
- Uncertainties: None
- Cross-reference status: Verified
