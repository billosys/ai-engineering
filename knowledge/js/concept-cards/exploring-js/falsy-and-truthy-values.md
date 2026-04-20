---
# === CORE IDENTIFICATION ===
concept: Falsy and Truthy Values
slug: falsy-and-truthy-values

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
section: "Falsy and truthy values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "truthiness"
  - "falsiness"
  - "truthy"
  - "falsy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - converting-to-boolean
extends: []
related:
  - truthiness-based-existence-checks
  - nullish-coalescing-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

A value is "truthy" if it converts to `true` when coerced to boolean; it is "falsy" if it converts to `false`. There are exactly eight falsy values; everything else is truthy.

# Core Definition

"A value is called *truthy* if it is `true` when converted to boolean. A value is called *falsy* if it is `false` when converted to boolean." The exhaustive list of falsy values is: `undefined`, `null`, `false`, `0`, `NaN`, `0n`, and `''`. All other values (including all objects) are truthy (Ch. 17, Section 17.2).

# Prerequisites

- **converting-to-boolean** -- falsy/truthy is defined in terms of boolean conversion

# Key Properties

1. Exhaustive falsy list: `undefined`, `null`, `false`, `0`, `NaN`, `0n`, `''`
2. All objects are truthy (including `[]`, `{}`, `new Boolean(false)`)
3. All symbols are truthy
4. Any non-empty string is truthy
5. Any non-zero, non-NaN number is truthy

# Construction / Recognition

```js
if (value) {
  // value is truthy
}
if (!value) {
  // value is falsy
}
```

In boolean contexts, JavaScript uses `Boolean(value)`:
```js
if (value) {} // equivalent to: if (Boolean(value) === true) {}
```

# Context & Application

Truthy/falsy checks are pervasive in JavaScript for conditional logic, existence checks, and default values. Understanding the complete list of falsy values is essential to avoid bugs when using boolean contexts.

# Examples

From the source text:

```js
if (x) {
  // x is truthy
}
if (!x) {
  // x is falsy
}
const result = x ? 'truthy' : 'falsy';
```

Falsy values are: `undefined, null, false, 0, NaN, 0n, ''`

# Relationships

## Builds Upon
- **converting-to-boolean** — truthy/falsy is defined by boolean conversion

## Enables
- **truthiness-based-existence-checks** — using truthiness to check if values exist
- **logical-and-operator** — short-circuits on falsy values
- **logical-or-operator** — short-circuits on truthy values

## Related
- **nullish-coalescing-operator** — distinguishes nullish from falsy

## Contrasts With
- None

# Common Errors

- **Error**: Treating `0` or `''` as "not existing" via a truthiness check
  **Correction**: `0` and `''` are falsy but may be valid values. Use `=== undefined` or `??` for existence checks when these values are meaningful.

# Common Confusions

- **Confusion**: Thinking empty arrays `[]` or empty objects `{}` are falsy
  **Clarification**: All objects are truthy, regardless of content. `Boolean([])` is `true`.

# Source Reference

Chapter 17: Booleans, Section 17.2, lines 238-299.

# Verification Notes

- Definition source: direct (explicit definition with exhaustive list)
- Confidence rationale: Complete falsy list provided
- Cross-reference status: verified
