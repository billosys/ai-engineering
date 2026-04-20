---
# === CORE IDENTIFICATION ===
concept: Addition Operator Coercion
slug: addition-operator-coercion

# === CLASSIFICATION ===
category: type-system
subcategory: type-coercion
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Type coercion in JavaScript"
chapter_number: 2
section: "2.5.1 Addition operator (+)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "plus operator coercion"
  - "Addition()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
  - to-primitive
  - to-string
  - to-numeric
extends: []
related:
  - abstract-equality-comparison
  - to-primitive
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

The addition operator (`+`) coerces both operands to primitives, then either concatenates strings (if either operand is a string) or adds numbers.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.5.1): The addition operator first converts both operands to primitives via `ToPrimitive()` with the default hint. "If one of the results is a string, both are converted to strings and concatenated. Otherwise, both operands are converted to numeric values and added." If the numeric types differ (e.g., number and bigint), a `TypeError` is thrown.

# Prerequisites

- **ToPrimitive** — Both operands are converted to primitives first.
- **ToString** — Used when one operand is a string.
- **ToNumeric** — Used when neither operand is a string.
- **Type coercion** — The `+` operator is a primary example of coercion.

# Key Properties

1. Both operands are converted to primitives via `ToPrimitive()` with default hint.
2. If either primitive is a string, both are converted to strings and concatenated.
3. Otherwise, both are converted to numeric values and added.
4. Mixing number and bigint throws `TypeError`.
5. The default hint means objects use `valueOf()` first (except Date which uses `toString()` first).

# Construction / Recognition

## To Construct/Create:
1. Use the `+` operator between two values.

## To Identify/Recognize:
1. The `+` operator with non-numeric or mixed-type operands triggers coercion.

# Context & Application

The `+` operator is the most common source of unexpected coercion in JavaScript. Because it serves dual purpose (addition and concatenation), accidentally mixing types can produce surprising results. Understanding its algorithm explains why `[] + []` produces `""` and `{} + []` can produce different results depending on context.

# Examples

**Example 1** (Ch 2): The algorithm in JavaScript form:
```js
function Addition(leftHandSide, rightHandSide) {
  let lprim = ToPrimitive(leftHandSide);
  let rprim = ToPrimitive(rightHandSide);
  if (TypeOf(lprim) === 'string' || TypeOf(rprim) === 'string') {
    return ToString(lprim) + ToString(rprim);
  }
  let lnum = ToNumeric(lprim);
  let rnum = ToNumeric(rprim);
  if (TypeOf(lnum) !== TypeOf(rnum)) {
    throw new TypeError();
  }
  let T = Type(lnum);
  return T.add(lnum, rnum);
}
```

**Example 2** (Ch 2): Date + number produces string (because Date's ToPrimitive prefers strings for default hint):
```js
const d = new Date('2222-03-27');
assert.equal(
  123 + d,
  '123Wed Mar 27 2222 01:00:00 GMT+0100'
    + ' (Central European Standard Time)');
```

# Relationships

## Builds Upon
- **ToPrimitive** — Both operands go through ToPrimitive with default hint.
- **ToString** — Used for string concatenation path.
- **ToNumeric** — Used for numeric addition path.

## Enables
- **String concatenation** — `+` is the primary string concatenation operator.
- **Numeric addition** — `+` performs numeric addition when both operands are numeric.

## Related
- **Abstract equality comparison** — Also uses ToPrimitive with default hint.

## Contrasts With
- None in the immediate taxonomy.

# Common Errors

- **Error**: Expecting `'3' + 2` to produce `5`.
  **Correction**: Since one operand is a string, the result is `'32'` (string concatenation).

- **Error**: Expecting `[] + []` to produce an empty array.
  **Correction**: Arrays are converted to primitives (empty strings), so `[] + []` produces `""`.

# Common Confusions

- **Confusion**: The `+` operator always adds numbers.
  **Clarification**: The `+` operator first converts to primitives. If either result is a string, it concatenates. Only if neither is a string does it perform numeric addition.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.5.1, lines 918-949.

# Verification Notes

- Definition source: direct (algorithm quoted from source)
- Confidence rationale: Full algorithm provided with explanation
- Cross-reference status: verified
