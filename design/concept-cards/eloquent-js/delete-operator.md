---
# === CORE IDENTIFICATION ===
concept: Delete Operator
slug: delete-operator

# === CLASSIFICATION ===
category: data-structures
subcategory: object-operations
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - property
extends: []
related:
  - in-operator
  - mutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The `delete` operator removes a named property from an object, so the property is no longer present (as opposed to setting it to `undefined`).

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 331-334 of 04-data-structures-objects-and-arrays.md): "The `delete` operator cuts off a tentacle from such an octopus. It is a unary operator that, when applied to an object property, will remove the named property from the object. This is not a common thing to do, but it is possible."

# Prerequisites

- **object**: `delete` operates on object properties.
- **property**: `delete` removes properties.

# Key Properties

1. Syntax: `delete object.property`.
2. Removes the property entirely from the object.
3. After deletion, `"property" in object` returns `false`.
4. Different from setting a property to `undefined` (which keeps the property).

# Construction / Recognition

## To Construct/Create:
```javascript
delete anObject.left;
```

## To Identify/Recognize:
- `delete` keyword followed by a property access expression.

# Context & Application

The `delete` operator is uncommon but useful when you need to truly remove a property (not just set it to undefined). The distinction matters when using the `in` operator.

# Examples

**Example 1** (Ch 4, lines 336-347 of 04-data-structures-objects-and-arrays.md):
```javascript
let anObject = {left: 1, right: 2};
console.log(anObject.left);
// → 1
delete anObject.left;
console.log(anObject.left);
// → undefined
console.log("left" in anObject);
// → false
console.log("right" in anObject);
// → true
```

# Relationships

## Builds Upon
- **object** -- Operates on objects.
- **property** -- Removes properties.

## Enables
- True property removal.

## Related
- **in-operator** -- `in` returns `false` after deletion.
- **mutability** -- Deletion is a mutation.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Expecting `delete` to work on variables or non-property values.
  **Correction**: `delete` only works on object properties, not standalone bindings.

# Common Confusions

- **Confusion**: Setting a property to `undefined` is the same as deleting it.
  **Clarification**: Setting to `undefined` keeps the property (with value `undefined`); `delete` removes it entirely.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Objects", lines 331-347 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 331-334)
- Confidence rationale: Explicit description with example
- Cross-reference status: verified within chapter
