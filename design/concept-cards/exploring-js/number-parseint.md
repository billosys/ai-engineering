---
# === CORE IDENTIFICATION ===
concept: Number.parseInt() and Number.parseFloat()
slug: number-parseint

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
section: "Global functions for numbers"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "parseInt()"
  - "parseFloat()"
  - "Number.parseFloat()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
  - converting-to-number
extends: []
related:
  - nan-value
contrasts_with:
  - converting-to-number

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

`Number.parseInt(str, radix)` parses a string to an integer in a given radix, stopping at the first unparsable character. `Number.parseFloat(str)` parses a string to a floating point number. Both have quirks compared to `Number()`.

# Core Definition

`Number.parseInt()` parses a string from left to right, stopping at the first character that is not valid for the given radix. It can parse partial strings: `parseInt('123abc')` returns `123`. `Number.parseFloat()` similarly parses until failure. The author recommends `Number()` instead because of its more predictable behavior: `Number('123abc')` returns `NaN` (Ch. 18, Section 18.4 and 18.11.1).

# Prerequisites

- **number-type** -- produces number values
- **converting-to-number** -- `Number()` is the recommended alternative

# Key Properties

1. `parseInt('123abc')` returns `123` (partial parsing)
2. `Number('123abc')` returns `NaN` (complete parsing)
3. `parseInt()` accepts a radix: `parseInt('FF', 16)` returns `255`
4. Neither function supports numeric separators
5. `parseFloat()` has quirks and should be avoided
6. `Number.parseInt === parseInt` (global and Number versions are identical)

# Construction / Recognition

```js
> Number.parseInt('123abc')
123
> Number('123abc')
NaN
> Number.parseInt('FF', 16)
255
```

# Context & Application

Use `parseInt()` only when you need partial string parsing or a specific radix. For general numeric conversion, prefer `Number()`.

# Examples

From the source text:

```js
> Number('123_456')
NaN
> Number.parseInt('123_456')
123   // stops at underscore

> Number.parseInt('123')
123
```

# Relationships

## Builds Upon
- **number-type** — produces numbers
- **converting-to-number** — alternative approach

## Enables
- Parsing strings with mixed content

## Related
- **nan-value** — returned for completely unparsable input

## Contrasts With
- **converting-to-number** — `Number()` requires the entire string to be numeric

# Common Errors

- **Error**: Omitting the radix parameter: `parseInt('010')` may give unexpected results
  **Correction**: Always specify the radix: `parseInt('010', 10)` for decimal.

# Common Confusions

- **Confusion**: Thinking `parseInt()` and `Number()` are interchangeable
  **Clarification**: `parseInt('123abc')` returns `123`; `Number('123abc')` returns `NaN`.

# Source Reference

Chapter 18: Numbers, Sections 18.4 and 18.11.1, lines 789-801.

# Verification Notes

- Definition source: synthesized from multiple sections
- Confidence rationale: Behavior described but full API reference is in quick reference section
- Cross-reference status: verified
