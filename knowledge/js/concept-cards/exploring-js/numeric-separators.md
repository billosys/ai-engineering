---
# === CORE IDENTIFICATION ===
concept: Numeric Separators
slug: numeric-separators

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
section: "Underscores (_) as separators in number literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "underscore separators"
  - "numeric literal separators"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-literals
extends:
  - number-literals
related:
  - bigint-literals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Since ES2021, underscores (`_`) can be used as visual separators within number literals to improve readability of large numbers, such as `1_335_000`.

# Core Definition

ES2021 allows underscores as separators in number and bigint literals. Restrictions: only between two digits, and at most one underscore in a row. Parsing functions like `Number()` and `Number.parseInt()` do not support separators -- `Number('123_456')` returns `NaN` (Ch. 18, Section 18.2.4).

# Prerequisites

- **number-literals** -- separators are used within number literals

# Key Properties

1. ES2021 feature
2. Only between two digits (not at start/end, not adjacent to `.` or `e`)
3. At most one underscore in a row
4. `Number()`, `Number.parseInt()`, `Number.parseFloat()` do not support separators
5. Works in all bases and in fractions/exponents

# Construction / Recognition

```js
const inhabitantsOfLondon = 1_335_000;
const fileSystemPermission = 0b111_111_000;
const words = 0xFAB_F00D;
const massOfElectronInKg = 9.109_383_56e-31;
```

# Context & Application

Use numeric separators to make large numeric constants more readable. They are purely syntactic sugar with no runtime effect.

# Examples

From the source text:

```js
const inhabitantsOfLondon = 1_335_000;
const distanceEarthSunInKm = 149_600_000;
const fileSystemPermission = 0b111_111_000;
const words = 0xFAB_F00D;
const massOfElectronInKg = 9.109_383_56e-31;

// Parsing functions do NOT support separators
> Number('123_456')
NaN
> Number.parseInt('123_456')
123
```

# Relationships

## Builds Upon
- **number-literals** — extends literal syntax

## Enables
- More readable numeric constants

## Related
- **bigint-literals** — bigints also support underscore separators

## Contrasts With
- None

# Common Errors

- **Error**: Using separators in strings passed to `Number()` or `parseInt()`
  **Correction**: Parsing functions do not support separators. `Number('1_000')` returns `NaN`.

# Common Confusions

- **Confusion**: Thinking separators affect the numeric value
  **Clarification**: Separators are purely visual; `1_000` and `1000` produce identical values.

# Source Reference

Chapter 18: Numbers, Section 18.2.4, lines 196-281.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit rules and restrictions provided
- Cross-reference status: verified
