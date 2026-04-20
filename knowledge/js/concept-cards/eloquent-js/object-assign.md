---
# === CORE IDENTIFICATION ===
concept: Object.assign
slug: object-assign

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
  - object-keys
  - spread-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

`Object.assign` copies all properties from one or more source objects into a target object, modifying and returning the target.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 369-370 of 04-data-structures-objects-and-arrays.md): "There's an `Object.assign` function that copies all properties from one object into another."

# Prerequisites

- **object**: `Object.assign` operates on objects.
- **property**: It copies properties between objects.

# Key Properties

1. Copies all enumerable own properties from source(s) to target.
2. Modifies and returns the target object.
3. Later sources overwrite earlier sources for same-named properties.

# Construction / Recognition

## To Construct/Create:
```javascript
Object.assign(targetObject, sourceObject);
```

## To Identify/Recognize:
- `Object.assign(target, source1, source2, ...)` call pattern.

# Context & Application

`Object.assign` is useful for merging objects, adding properties, and creating modified copies. The spread operator (`{...obj}`) provides a similar capability for creating new objects.

# Examples

**Example 1** (Ch 4, lines 372-377 of 04-data-structures-objects-and-arrays.md):
```javascript
let objectA = {a: 1, b: 2};
Object.assign(objectA, {b: 3, c: 4});
console.log(objectA);
// → {a: 1, b: 3, c: 4}
```

# Relationships

## Builds Upon
- **object** -- Operates on objects.
- **property** -- Copies properties.

## Enables
- Object merging and copying patterns.

## Related
- **object-keys** -- Another `Object` utility function.
- **spread-operator** -- Similar but creates a new object.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Expecting `Object.assign` to create a new object.
  **Correction**: `Object.assign` mutates the target. To create a new object, use `Object.assign({}, source)` or spread syntax.

# Common Confusions

- **Confusion**: `Object.assign` performs a deep copy.
  **Clarification**: `Object.assign` performs a shallow copy. Nested objects are copied by reference.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Objects", lines 368-377 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 369-370)
- Confidence rationale: Explicit description with example
- Cross-reference status: verified within chapter
