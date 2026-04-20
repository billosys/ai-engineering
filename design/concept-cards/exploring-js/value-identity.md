---
# === CORE IDENTIFICATION ===
concept: Value Identity
slug: value-identity

# === CLASSIFICATION ===
category: types-values
subcategory: type-system
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.6.5 Identity in the ECMAScript specification (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - object identity
  - reference identity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-values
  - objects-overview
extends: []
related:
  - objects-compared-by-identity
  - objects-passed-by-identity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

The ECMAScript specification distinguishes values *without identity* (primitives, equal if contents match) from values *with identity* (objects and non-registered symbols, each unique and only equal to itself).

# Core Definition

The spec defines (Ch. 14, &sect;14.6.5): "*Values without identity* are equal to other values without identity if all of their innate characteristics are the same." They can be described by their characteristics. "*Each value with identity* is unique and therefore only equal to itself." Values with identity have "an additional unguessable, unchangeable, universally-unique characteristic called identity." At the language level: objects and `Symbol()` have identity; primitives and `Symbol.for()` do not.

# Prerequisites

- **primitive-values** -- values without identity
- **objects-overview** -- values with identity

# Key Properties

1. Values without identity: primitives, `Symbol.for()` symbols
2. Values with identity: objects, `Symbol()` symbols
3. Values with identity are unique -- only equal to themselves
4. Mutable values with identity can have characteristics changed in-place
5. Identity is indescribable -- cannot be recreated, only passed

# Construction / Recognition

```js
// Without identity (equal by content):
123 === 123      // true

// With identity (unique):
{} === {}        // false (different identities)
Symbol() === Symbol()  // false (different identities)
```

# Context & Application

The identity concept formalizes why objects are compared by reference and primitives by value.

# Examples

From the source text (Ch. 14, &sect;14.6.5):
- Values with identity: objects, `Symbol()` created symbols
- Values without identity: primitive values, `Symbol.for()` symbols

# Relationships

## Builds Upon
- **primitive-values** -- primitives lack identity
- **objects-overview** -- objects have identity

## Enables
- Understanding comparison semantics

## Related
- **objects-compared-by-identity** -- practical implication
- **objects-passed-by-identity** -- practical implication

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Thinking all symbols have identity.
  **Correction**: `Symbol.for()` creates symbols without identity (registered symbols are shared).

# Common Confusions

- **Confusion**: Thinking "identity" means "name" or "variable."
  **Clarification**: Identity is an intrinsic property of the value itself -- a unique, opaque characteristic.

# Source Reference

Chapter 14: Values, Section 14.6.5, lines 365-394.

# Verification Notes

- Definition source: direct from source (ECMAScript specification terms)
- Confidence rationale: Explicit spec-based definition
- Cross-reference status: verified
