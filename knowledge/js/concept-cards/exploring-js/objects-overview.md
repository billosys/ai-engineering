---
# === CORE IDENTIFICATION ===
concept: Objects
slug: objects-overview

# === CLASSIFICATION ===
category: types-values
subcategory: objects
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.6 Objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - object type

# === TYPED RELATIONSHIPS ===
prerequisites:
  - specification-types
extends: []
related:
  - objects-are-mutable
  - objects-passed-by-identity
  - objects-compared-by-identity
contrasts_with:
  - primitive-values

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are primitive values vs. objects in JavaScript?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Objects are compound pieces of data that are mutable by default, passed by identity (not copied), and compared by identity (not content). They are created via object literals `{}` and array literals `[]`.

# Core Definition

"All other values are *objects*." (Ch. 14, &sect;14.4). Objects are compound data with three key properties: "They are *passed by identity*: when objects are assigned to variables or passed to functions, their *identities* (think pointers) are copied. They are *compared by identity*: when comparing two objects, their identities are compared." (Ch. 14, &sect;14.4). Objects are mutable by default and created via object literals or array literals.

# Prerequisites

- **specification-types** -- objects are one of the eight spec types

# Key Properties

1. Compound pieces of data
2. Mutable by default
3. Passed by identity (think pointers/references)
4. Compared by identity (not content)
5. Created via object literals `{}` and array literals `[]`
6. Properties (key-value entries) can be changed, added, and removed
7. Virtually all objects are instances of `Object`

# Construction / Recognition

```js
const obj = { first: 'Jane', last: 'Doe' };  // object literal
const fruits = ['strawberry', 'apple'];       // array literal
```

# Context & Application

Objects are the primary data structure in JavaScript. Understanding their pass-by-identity and compare-by-identity behavior is critical.

# Examples

From the source text (Ch. 14, &sect;14.6):
```js
// Object literal
const obj = {
  first: 'Jane',
  last: 'Doe',
};

// Array literal
const fruits = ['strawberry', 'apple'];
```

# Relationships

## Builds Upon
- **specification-types** -- objects are the eighth spec type

## Enables
- **objects-are-mutable** -- default mutability
- **objects-passed-by-identity** -- identity-based passing
- **objects-compared-by-identity** -- identity-based comparison

## Related
- No additional

## Contrasts With
- **primitive-values** -- primitives are immutable, passed/compared by value

# Common Errors

- **Error**: Comparing objects with `===` expecting content comparison.
  **Correction**: `===` compares identity for objects. Use `assert.deepEqual()` or manual comparison for content.

# Common Confusions

- **Confusion**: Thinking assigning an object to a new variable copies the object.
  **Clarification**: Assignment copies the identity (reference), not the object. Both variables point to the same object.

# Source Reference

Chapter 14: Values, Section 14.6, lines 216-251.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Comprehensive with three key properties
- Cross-reference status: verified
