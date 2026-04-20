---
# === CORE IDENTIFICATION ===
concept: In Operator
slug: in-operator

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
  - string
extends: []
related:
  - object-keys
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The binary `in` operator checks whether an object has a property with a given name, returning `true` or `false`.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 350-356 of 04-data-structures-objects-and-arrays.md): "The binary `in` operator, when applied to a string and an object, tells you whether that object has a property with that name. The difference between setting a property to `undefined` and actually deleting it is that in the first case, the object still *has* the property (it just doesn't have a very interesting value), whereas in the second case, the property is no longer present and `in` will return `false`."

# Prerequisites

- **object**: The `in` operator checks object properties.
- **property**: Tests for property existence.
- **string**: The left operand is a string (property name).

# Key Properties

1. Syntax: `"propertyName" in object`.
2. Returns `true` if the property exists on the object (even if its value is `undefined`).
3. Returns `false` if the property has been deleted or never existed.
4. Checks the prototype chain (not just own properties).

# Construction / Recognition

## To Construct/Create:
```javascript
console.log("left" in anObject);
console.log("right" in anObject);
```

## To Identify/Recognize:
- `string in object` expression.

# Context & Application

The `in` operator is useful for checking whether a property exists, especially when the property's value might legitimately be `undefined`.

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
- **object** -- Checks object properties.
- **property** -- Tests for property existence.

## Enables
- Distinguishing between missing properties and properties set to `undefined`.

## Related
- **object-keys** -- Another way to inspect object properties.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using `object.prop !== undefined` to check for property existence.
  **Correction**: A property can exist with the value `undefined`. Use `in` for reliable existence checks.

# Common Confusions

- **Confusion**: `in` only checks own properties.
  **Clarification**: `in` also checks the prototype chain. Use `Object.hasOwn()` for own-only checks.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Objects", lines 349-356 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 350-356)
- Confidence rationale: Explicit description with example
- Cross-reference status: verified within chapter
