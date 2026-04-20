---
# === CORE IDENTIFICATION ===
concept: Comparison Operators
slug: comparison-operators

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 98
section: "4.9.2 Comparison Operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "relational operators"
  - "ordering operators"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - operator-precedence
extends: []
related:
  - strict-equality-operator
  - addition-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes == from ===? (operator side)"
---

# Quick Definition

The comparison operators (`<`, `>`, `<=`, `>=`) test the relative order of two values, performing string comparison when both operands are strings and numeric comparison otherwise.

# Core Definition

"The comparison operators test the relative order (numerical or alphabetical) of their two operands." They favor numeric comparison: "Comparison and conversion occur as follows: if, after any required object-to-primitive conversion, both operands are strings, the two strings are compared... If, after object-to-primitive conversion, at least one operand is not a string, both operands are converted to numbers and compared numerically." (Ch. 4, §4.9.2)

# Prerequisites

- **primary-expressions** — Comparison operators take two expression operands.
- **operator-precedence** — Comparison operators have specific precedence (lower than arithmetic, higher than equality).

# Key Properties

1. String comparison uses 16-bit Unicode value order (case-sensitive; "Zoo" < "aardvark").
2. If at least one operand is not a string, both are converted to numbers.
3. Any comparison involving NaN returns `false`.
4. BigInt values can be compared with regular numbers.
5. `<=` is "not greater than" and `>=` is "not less than" — they do not use `==` or `===`.
6. Objects are converted to primitives via `valueOf()` first, then `toString()`.

# Construction / Recognition

```js
a < b    // Less than
a > b    // Greater than
a <= b   // Less than or equal
a >= b   // Greater than or equal
```

# Context & Application

Comparison operators are used extensively in conditionals and loop conditions. The different treatment of strings vs. numbers (compared to the `+` operator) is an important asymmetry to understand.

# Examples

From the source text (§4.9.2, pp. 98-100):

```js
11 < 3       // => false: numeric comparison
"11" < "3"   // => true: string comparison (Unicode order)
"11" < 3     // => false: numeric comparison, "11" converted to 11
"one" < 3    // => false: numeric comparison, "one" converted to NaN
```

Contrast with `+`:
```js
"1" + 2      // => "12": + favors strings
"11" < 3     // => false: < favors numbers
```

# Relationships

## Builds Upon
- **operator-precedence** — Comparison operators have defined precedence

## Enables
- **if-else-statement** — Comparisons are the primary condition expressions
- **while-loop** — Loop conditions typically use comparisons

## Related
- **strict-equality-operator** — Tests equality rather than ordering
- **addition-operator** — `+` favors strings; comparisons favor numbers

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Comparing strings that should be compared numerically: `"11" < "3"` is `true`.
  **Correction**: Convert to numbers first if numeric comparison is intended.

# Common Confusions

- **Confusion**: Assuming `<=` is the same as `< || ==`.
  **Clarification**: `<=` is defined as "not greater than." When NaN is involved, all four comparisons return `false`.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.9.2, pages 98-100.

# Verification Notes

- Definition source: Direct quote from §4.9.2
- Confidence rationale: High — detailed type conversion rules provided
- Uncertainties: None
- Cross-reference status: Verified
