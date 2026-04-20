---
# === CORE IDENTIFICATION ===
concept: NaN Value
slug: nan-value

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
section: "Error value: NaN"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "NaN"
  - "Not a Number"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - converting-to-number
  - object-is
  - number-isnan
contrasts_with:
  - infinity-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

`NaN` ("Not a Number") is a numeric error value returned when a number cannot be parsed or an arithmetic operation cannot be performed. Despite its name, `typeof NaN` is `'number'`.

# Core Definition

"`NaN` is an abbreviation of 'not a number'. Ironically, JavaScript considers it to be a number." It is returned when: a number cannot be parsed (`Number('$$$')`), an operation cannot be performed (`Math.sqrt(-1)`), or an operand is `NaN` (propagation). The key quirk: `NaN` is not strictly equal to itself (`NaN === NaN` is `false`). Check with `Number.isNaN()` (Ch. 18, Section 18.5.1).

# Prerequisites

- **number-type** -- NaN is a value of the number type

# Key Properties

1. `typeof NaN` is `'number'`
2. `NaN === NaN` is `false` (only value not equal to itself)
3. `NaN` propagates through arithmetic: `NaN - 3` is `NaN`
4. Check with `Number.isNaN(x)`, `Object.is(x, NaN)`, or `x !== x`
5. Some Array methods cannot find NaN: `.indexOf(NaN)` returns `-1`
6. `.includes(NaN)` returns `true`; `.findIndex()` can find NaN

# Construction / Recognition

```js
Number('$$$')     // NaN
Number(undefined) // NaN
Math.sqrt(-1)     // NaN
NaN - 3           // NaN (propagation)
```

Checking:
```js
Number.isNaN(x)    // preferred
Object.is(x, NaN)  // also works
x !== x            // quirky but valid
```

# Context & Application

NaN is a common source of bugs in JavaScript. It propagates silently through calculations, and its self-inequality makes it difficult to detect with `===`. Always use `Number.isNaN()` for checking.

# Examples

From the source text:

```js
> typeof NaN
'number'

> Number('$$$')
NaN
> Number(undefined)
NaN
> Math.log(-1)
NaN
> Math.sqrt(-1)
NaN

// NaN propagates
> NaN - 3
NaN

// Self-inequality
> NaN === NaN
false

// Checking
const x = NaN;
assert.equal(Number.isNaN(x), true);
assert.equal(Object.is(x, NaN), true);
assert.equal(x !== x, true);

// Array methods
> [NaN].indexOf(NaN)
-1
> [NaN].includes(NaN)
true
```

# Relationships

## Builds Upon
- **number-type** — NaN is a number value

## Enables
- Understanding error propagation in numeric computations

## Related
- **converting-to-number** — unparsable conversions produce NaN
- **object-is** — can detect NaN (unlike `===`)
- **number-isnan** — the preferred way to check for NaN

## Contrasts With
- **infinity-value** — the other numeric error value

# Common Errors

- **Error**: Using `x === NaN` to check for NaN
  **Correction**: `NaN === NaN` is `false`. Use `Number.isNaN(x)`.

- **Error**: Using global `isNaN()` instead of `Number.isNaN()`
  **Correction**: `isNaN('abc')` is `true` (coerces to number first). `Number.isNaN('abc')` is `false`.

# Common Confusions

- **Confusion**: Thinking NaN means "not a number type"
  **Clarification**: NaN is of type `number`. It means the result of a numeric operation that failed.

# Source Reference

Chapter 18: Numbers, Section 18.5.1, lines 967-1073.

# Verification Notes

- Definition source: direct
- Confidence rationale: Comprehensive treatment with checking methods
- Cross-reference status: verified against Ch. 15 (Object.is)
