---
# === CORE IDENTIFICATION ===
concept: Converting to Number
slug: converting-to-number

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
section: "Converting to number"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Number()"
  - "numeric conversion"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - converting-to-boolean
  - converting-to-string
  - nan-value
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

Values are converted to numbers using `Number(value)` (recommended), unary `+value`, or `parseFloat(value)` (has quirks), following a well-defined conversion table.

# Core Definition

`Number(value)` converts values to numbers: `undefined` becomes `NaN`, `null` becomes `0`, booleans become `0`/`1`, strings are parsed (empty string becomes `0`, unparsable strings become `NaN`), bigints are converted directly, symbols throw `TypeError`, and objects are configurable via `.valueOf()` (Ch. 18, Section 18.4).

# Prerequisites

- **number-type** -- the target type of conversion

# Key Properties

1. `undefined` -> `NaN`
2. `null` -> `0`
3. `false` -> `0`, `true` -> `1`
4. `''` -> `0`, other strings parsed as numbers
5. Unparsable strings -> `NaN`
6. Symbols -> `TypeError`
7. `+value` is equivalent to `Number(value)`
8. `parseFloat()` has quirks and should be avoided

# Construction / Recognition

```js
Number(123.45)          // 123.45
Number('')              // 0
Number('\n 123.45 \t')  // 123.45 (ignores whitespace)
Number('xyz')           // NaN
Number(-123n)           // -123
```

# Context & Application

Numeric conversion is essential for processing user input, parsing data, and handling mixed-type operations. `Number()` is recommended over `parseFloat()` because of its predictable behavior.

# Examples

From the source text:

```js
assert.equal(Number(123.45), 123.45);
assert.equal(Number(''), 0);
assert.equal(Number('\n 123.45 \t'), 123.45);
assert.equal(Number('xyz'), NaN);
assert.equal(Number(-123n), -123);

// Objects configurable via valueOf()
> Number({ valueOf() { return 123 } })
123
```

# Relationships

## Builds Upon
- **number-type** — target type

## Enables
- Processing string input as numbers
- **nan-value** — unparsable inputs produce NaN

## Related
- **converting-to-boolean** — another conversion function
- **converting-to-string** — another conversion function

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `Number(undefined)` to be `0`
  **Correction**: `Number(undefined)` is `NaN`. Only `Number(null)` is `0`.

- **Error**: Expecting `Number('')` to be `NaN`
  **Correction**: `Number('')` is `0`. Empty strings are treated as zero.

# Common Confusions

- **Confusion**: Thinking `Number()` and `parseInt()` behave the same
  **Clarification**: `Number('123abc')` is `NaN`; `parseInt('123abc')` is `123`. `Number()` requires the entire string to be a number.

# Source Reference

Chapter 18: Numbers, Section 18.4, lines 789-965.

# Verification Notes

- Definition source: direct (conversion table provided)
- Confidence rationale: Complete conversion table in source
- Cross-reference status: verified
