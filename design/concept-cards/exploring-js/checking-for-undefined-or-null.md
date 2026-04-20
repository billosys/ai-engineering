---
# === CORE IDENTIFICATION ===
concept: Checking for Undefined or Null
slug: checking-for-undefined-or-null

# === CLASSIFICATION ===
category: primitive-types
subcategory: non-values
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The non-values undefined and null"
chapter_number: 16
pdf_page: null
section: "Checking for undefined or null"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - undefined-value
  - null-value
  - falsy-and-truthy-values
extends: []
related:
  - nullish-coalescing-operator
  - truthiness-based-existence-checks
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is `undefined` and how does it differ from `null`?"
  - "What distinguishes `null` from `undefined`?"
---

# Quick Definition

To check for `undefined` or `null`, use strict equality (`=== undefined`, `=== null`) for precision, or truthiness/falsiness checks for convenience (with the caveat that they also match other falsy values).

# Core Definition

Precise checks: `x === null` or `x === undefined`. To check if `x` has a value: `x !== undefined && x !== null`. Truthy shorthand: `if (x)` checks for non-nullish but also excludes `false`, `0`, `NaN`, `0n`, `''`. Falsy shorthand: `if (!x)` checks for nullish but also matches other falsy values (Ch. 16, Section 16.3).

# Prerequisites

- **undefined-value** -- one of the values being checked for
- **null-value** -- the other value being checked for
- **falsy-and-truthy-values** -- truthiness-based alternatives

# Key Properties

1. `x === null` checks for null specifically
2. `x === undefined` checks for undefined specifically
3. `x !== undefined && x !== null` checks that x has a value
4. `if (x)` is imprecise: also excludes `false`, `0`, `NaN`, `0n`, `''`
5. `if (!x)` is imprecise: also matches other falsy values

# Construction / Recognition

```js
// Precise checks
if (x === null) ···
if (x === undefined) ···

// Check if x has a value
if (x !== undefined && x !== null) { ··· }

// Imprecise but common
if (x) { ··· }  // truthy?
if (!x) { ··· } // falsy?
```

# Context & Application

Choose between precise and imprecise checks based on your needs. For APIs where `0` or `''` are valid values, use strict equality or `??`.

# Examples

From the source text:

```js
if (x !== undefined && x !== null) {
  // x has a value
}
if (x) { // truthy?
  // x is neither: undefined, null, false, 0, NaN, 0n, ''
}
if (x === undefined || x === null) {
  // x is undefined or null
}
if (!x) { // falsy?
  // x is: undefined, null, false, 0, NaN, 0n, ''
}
```

# Relationships

## Builds Upon
- **undefined-value** — checking for undefined
- **null-value** — checking for null
- **falsy-and-truthy-values** — imprecise alternative checks

## Enables
- Defensive programming patterns

## Related
- **nullish-coalescing-operator** — `??` provides defaults for nullish values
- **truthiness-based-existence-checks** — related pattern

## Contrasts With
- None

# Common Errors

- **Error**: Using `if (!x)` when `x` could legitimately be `0` or `''`
  **Correction**: Use `x === undefined || x === null` or `x == null` for nullish-only checks.

# Common Confusions

- **Confusion**: Thinking `if (x)` only fails for `undefined` and `null`
  **Clarification**: It fails for all seven falsy values: `undefined`, `null`, `false`, `0`, `NaN`, `0n`, `''`.

# Source Reference

Chapter 16: The non-values undefined and null, Section 16.3, lines 151-188.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete pattern set provided
- Cross-reference status: verified
