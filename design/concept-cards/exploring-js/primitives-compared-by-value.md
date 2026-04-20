---
# === CORE IDENTIFICATION ===
concept: Primitives Compared by Value
slug: primitives-compared-by-value

# === CLASSIFICATION ===
category: types-values
subcategory: primitives
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.5.3 Primitives are compared by value"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - compare by value
  - value equality

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-values
extends:
  - primitive-values
related:
  - primitives-passed-by-value
contrasts_with:
  - objects-compared-by-identity

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Primitives are compared by value: two primitive values are equal (`===`) if their contents are the same, regardless of how they were created.

# Core Definition

"Primitives are *compared by value*: when comparing two primitive values, we compare their contents." (Ch. 14, &sect;14.5.3). Two independently created primitive values with the same content are considered equal.

# Prerequisites

- **primitive-values** -- this describes how primitives are compared

# Key Properties

1. `===` compares contents for primitives
2. Two independent primitives with same content are equal
3. Contrasts with objects (compared by identity)

# Construction / Recognition

```js
assert.equal(123 === 123, true);
assert.equal('abc' === 'abc', true);
```

# Context & Application

Value comparison means primitives work intuitively with equality checks. No need for special deep-equal methods.

# Examples

From the source text (Ch. 14, &sect;14.5.3):
```js
assert.equal(123 === 123, true);
assert.equal('abc' === 'abc', true);
```

# Relationships

## Builds Upon
- **primitive-values** -- comparison behavior of primitives

## Enables
- Intuitive equality checks with `===`

## Related
- **primitives-passed-by-value** -- passing and comparing are both value-based

## Contrasts With
- **objects-compared-by-identity** -- objects compare identity, not content

# Common Errors

- **Error**: Expecting `===` to work the same way for objects as for primitives.
  **Correction**: `===` compares identity for objects; use `assert.deepEqual()` for content comparison.

# Common Confusions

- **Confusion**: Wondering why `{} === {}` is false when `123 === 123` is true.
  **Clarification**: Primitives compare by value (content); objects compare by identity (reference).

# Source Reference

Chapter 14: Values, Section 14.5.3, lines 200-211.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with examples
- Cross-reference status: verified
