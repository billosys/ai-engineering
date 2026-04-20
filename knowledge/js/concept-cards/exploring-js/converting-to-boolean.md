---
# === CORE IDENTIFICATION ===
concept: Converting to Boolean
slug: converting-to-boolean

# === CLASSIFICATION ===
category: primitive-types
subcategory: booleans
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Booleans"
chapter_number: 17
pdf_page: null
section: "Converting to boolean"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "boolean conversion"
  - "Boolean()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean-type
extends: []
related:
  - falsy-and-truthy-values
  - converting-to-number
  - converting-to-string
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

Values can be converted to boolean using `Boolean(x)` (recommended), `x ? true : false`, or `!!x`, following a well-defined table of which values become `false` and which become `true`.

# Core Definition

Three ways to convert a value to boolean: `Boolean(x)` (most descriptive, recommended), the conditional operator `x ? true : false`, and double negation `!!x`. The conversion rules are: `undefined`, `null`, `false`, `0`, `NaN`, `0n`, and `''` convert to `false`; all other values (including all objects) convert to `true` (Ch. 17, Section 17.1).

# Prerequisites

- **boolean-type** -- understanding the target type

# Key Properties

1. `undefined` -> `false`
2. `null` -> `false`
3. `false` -> `false` (no change)
4. `0` and `NaN` -> `false`; other numbers -> `true`
5. `0n` -> `false`; other bigints -> `true`
6. `''` -> `false`; other strings -> `true`
7. All symbols -> `true`
8. All objects -> `true` (always)

# Construction / Recognition

```js
Boolean(0)         // false
Boolean('')        // false
Boolean('abc')     // true
Boolean([])        // true (objects are always truthy)
!!null             // false
```

# Context & Application

Boolean conversion happens implicitly in `if` conditions, `while` conditions, and other boolean contexts. `Boolean()` is preferred for explicit conversion because of its descriptive name.

# Examples

From the source text:

```js
> Boolean('abc')
true
> Boolean([])
true
> Boolean({})
true
```

# Relationships

## Builds Upon
- **boolean-type** — the target type of conversion

## Enables
- **falsy-and-truthy-values** — the classification of values by their boolean conversion

## Related
- **converting-to-number** — another type conversion function
- **converting-to-string** — another type conversion function

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `Boolean([])` to be `false` because arrays can be empty
  **Correction**: All objects are truthy, including empty arrays and empty objects.

# Common Confusions

- **Confusion**: Thinking `Boolean('false')` returns `false`
  **Clarification**: Any non-empty string is truthy, including the string `'false'`.

# Source Reference

Chapter 17: Booleans, Section 17.1, lines 53-237.

# Verification Notes

- Definition source: direct (conversion table provided)
- Confidence rationale: Complete conversion table in source
- Cross-reference status: verified
