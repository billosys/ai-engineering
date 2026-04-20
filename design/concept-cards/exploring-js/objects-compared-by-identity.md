---
# === CORE IDENTIFICATION ===
concept: Objects Compared by Identity
slug: objects-compared-by-identity

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
section: "14.6.3 Objects are compared by identity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - identity comparison
  - reference equality

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-overview
  - objects-passed-by-identity
extends:
  - objects-overview
related:
  - assert-deep-equal
contrasts_with:
  - primitives-compared-by-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Objects are compared by identity: two variables are equal (`===`) only if they reference the same object. Different objects with identical content are not equal.

# Core Definition

"Objects are *compared by identity*: two variables are only equal if they contain the same object identity. They are not equal if they refer to different objects with the same content." (Ch. 14, &sect;14.6.3).

# Prerequisites

- **objects-overview** -- identity comparison is a key object behavior
- **objects-passed-by-identity** -- understanding identity is prerequisite

# Key Properties

1. `===` compares identity (reference) for objects
2. Same object = same identity = equal
3. Different objects with same content = different identities = not equal
4. `{}` always creates a new object with a new identity

# Construction / Recognition

```js
const obj = {};
assert.equal(obj === obj, true);       // same identity
assert.equal({} === {}, false);        // different identities
```

# Context & Application

Identity comparison explains why `assert.deepEqual()` exists: you need it to compare object contents.

# Examples

From the source text (Ch. 14, &sect;14.6.3):
```js
const obj = {};
assert.equal(obj === obj, true);     // same identity
assert.equal({} === {}, false);      // different identities, same content
```

# Relationships

## Builds Upon
- **objects-overview** -- comparison behavior of objects
- **objects-passed-by-identity** -- identity concept

## Enables
- Understanding why `assert.deepEqual()` is needed

## Related
- **assert-deep-equal** -- content comparison for objects

## Contrasts With
- **primitives-compared-by-value** -- primitives compare content

# Common Errors

- **Error**: Using `===` to compare array or object contents.
  **Correction**: Use `JSON.stringify()`, `assert.deepEqual()`, or manual comparison.

# Common Confusions

- **Confusion**: Expecting `[1,2,3] === [1,2,3]` to be true.
  **Clarification**: Each array literal creates a new object; they have different identities.

# Source Reference

Chapter 14: Values, Section 14.6.3, lines 314-327.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with contrasting examples
- Cross-reference status: verified
