---
# === CORE IDENTIFICATION ===
concept: Objects Are Mutable
slug: objects-are-mutable

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
section: "14.6.1 Objects are mutable by default"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - mutable objects

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-overview
extends:
  - objects-overview
related:
  - const-immutability
contrasts_with:
  - primitives-are-immutable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Objects are mutable by default: their properties can be freely changed, added, and removed after creation.

# Core Definition

"By default, we can freely change, add, and remove the properties of objects." (Ch. 14, &sect;14.6.1). This applies even to objects held by `const` variables, since `const` only prevents reassignment of the binding, not mutation of the value.

# Prerequisites

- **objects-overview** -- mutability is a property of objects

# Key Properties

1. Properties can be changed (modified)
2. Properties can be added
3. Properties can be removed
4. Mutability persists even with `const` declarations
5. `Object.freeze()` can make objects immutable (not covered in this section)

# Construction / Recognition

```js
const obj = {};
obj.count = 2;     // add a property
obj.count = 3;     // change a property
```

# Context & Application

Object mutability is both powerful and dangerous. It enables in-place updates but can cause bugs when objects are shared.

# Examples

From the source text (Ch. 14, &sect;14.6.1):
```js
const obj = {};
obj.count = 2; // add a property
assert.equal(obj.count, 2);
obj.count = 3; // change a property
assert.equal(obj.count, 3);
```

# Relationships

## Builds Upon
- **objects-overview** -- mutability is a key object property

## Enables
- In-place data modification

## Related
- **const-immutability** -- const doesn't prevent object mutation

## Contrasts With
- **primitives-are-immutable** -- primitives cannot be modified

# Common Errors

- **Error**: Thinking `const obj = {}` prevents modification of `obj`.
  **Correction**: `const` prevents reassignment of `obj`; the object itself is still mutable.

# Common Confusions

- **Confusion**: Confusing `const` immutability with value immutability.
  **Clarification**: `const` makes the binding immutable; `Object.freeze()` makes the value immutable.

# Source Reference

Chapter 14: Values, Section 14.6.1, lines 253-267.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with code demonstration
- Cross-reference status: verified
