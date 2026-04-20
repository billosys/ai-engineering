---
# === CORE IDENTIFICATION ===
concept: Primitives Are Immutable
slug: primitives-are-immutable

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
section: "14.5.1 Primitives are immutable"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-values
extends:
  - primitive-values
related:
  - objects-are-mutable
  - const-immutability
contrasts_with:
  - objects-are-mutable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Primitive values are immutable: you cannot change, add, or remove their properties. Attempting to modify a property of a primitive throws a TypeError in strict mode.

# Core Definition

"We can't change, add, or remove properties of primitives." (Ch. 14, &sect;14.5.1). Attempting to assign to a read-only property of a primitive (like `str.length`) throws a `TypeError`.

# Prerequisites

- **primitive-values** -- immutability is a property of primitives

# Key Properties

1. Cannot change existing properties
2. Cannot add new properties
3. Cannot remove properties
4. Attempting modification throws TypeError in strict mode
5. This applies to all seven primitive types

# Construction / Recognition

```js
const str = 'abc';
assert.equal(str.length, 3);
assert.throws(
  () => { str.length = 1 },
  /^TypeError: Cannot assign to read only property 'length'/
);
```

# Context & Application

Immutability of primitives means they are always safe to share between variables, functions, and scopes without risk of unintended modification.

# Examples

From the source text (Ch. 14, &sect;14.5.1):
```js
const str = 'abc';
assert.equal(str.length, 3);
assert.throws(
  () => { str.length = 1 },
  /^TypeError: Cannot assign to read only property 'length'/
);
```

# Relationships

## Builds Upon
- **primitive-values** -- this is a defining property of primitives

## Enables
- Safe value sharing

## Related
- **const-immutability** -- const immutability is about bindings, not values

## Contrasts With
- **objects-are-mutable** -- objects can be modified freely

# Common Errors

- **Error**: Trying to modify string characters via index assignment.
  **Correction**: Strings are immutable; create a new string instead.

# Common Confusions

- **Confusion**: Confusing primitive immutability with `const` immutability.
  **Clarification**: Primitives are inherently immutable (the value itself). `const` makes the binding immutable (the variable assignment).

# Source Reference

Chapter 14: Values, Section 14.5.1, lines 155-167.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with code demonstration
- Cross-reference status: verified
