---
# === CORE IDENTIFICATION ===
concept: Loose Equality Operator (==)
slug: loose-equality-operator

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 97
section: "4.9.1 Equality and Inequality Operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "abstract equality"
  - "equality with type conversion"
  - "== operator"
  - "double equals"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - strict-equality-operator
extends: []
related:
  - addition-operator
contrasts_with:
  - strict-equality-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes == from ===? (operator side)"
---

# Quick Definition

The loose equality operator (`==`) checks whether two values are "equal" using a relaxed definition that allows implicit type conversions before comparison.

# Core Definition

"The equality operator == is like the strict equality operator, but it is less strict. If the values of the two operands are not the same type, it attempts some type conversions and tries the comparison again." The `==` operator is "a legacy feature of JavaScript and is widely considered to be a source of bugs." (Ch. 4, §4.9.1)

# Prerequisites

- **strict-equality-operator** — `==` is defined in terms of `===` with added type coercion rules.

# Key Properties

1. Same-type values are tested for strict equality first.
2. `null == undefined` is `true` (special rule).
3. Number vs. string: the string is converted to a number.
4. Boolean operands: `true` converts to `1`, `false` to `0`, then comparison retries.
5. Object vs. number/string: the object is converted to a primitive via `valueOf()` or `toString()`.
6. All other combinations are not equal.
7. `!=` is the corresponding inequality operator.

# Construction / Recognition

```js
value1 == value2   // Loose equality
value1 != value2   // Loose inequality
```

# Context & Application

The `==` operator is a legacy feature. Modern JavaScript best practice is to always use `===` instead. Understanding `==` is still necessary to read existing code and understand why certain comparisons produce surprising results.

# Examples

From the source text (§4.9.1, pp. 97-98):

```js
"1" == true    // => true
// Evaluation: true -> 1, then "1" -> 1, then 1 === 1

null == undefined  // => true (special case)
null == 0          // => false (null only equals undefined)
"" == 0            // => true (string "" converts to 0)
```

# Relationships

## Builds Upon
- **strict-equality-operator** — `==` falls back to `===` for same-type comparisons

## Enables
- No specific concepts — `==` is a legacy feature

## Related
- **addition-operator** — Both `+` and `==` perform type conversions, but with different rules

## Contrasts With
- **strict-equality-operator** — `===` performs no type conversion; `==` converts types to attempt a match

# Common Errors

- **Error**: Using `==` to compare values without realizing type coercion occurs.
  **Correction**: Use `===` unless you specifically need type-coercing comparison.

- **Error**: Expecting `null == 0` or `null == ""` to be `true`.
  **Correction**: `null` is only `==` to `undefined` and nothing else.

# Common Confusions

- **Confusion**: Believing `==` is simply a "less strict" version of `===` with no surprises.
  **Clarification**: The coercion rules create counterintuitive results like `"1" == true` being `true`, and `"" == 0` being `true`. The source calls `==` "widely considered to be a source of bugs."

# Source Reference

Chapter 4: Expressions and Operators, Section 4.9.1, pages 97-98.

# Verification Notes

- Definition source: Direct quote from §4.9.1
- Confidence rationale: High — detailed coercion rules enumerated
- Uncertainties: Coercion algorithm details are in §3.9.3
- Cross-reference status: Verified
