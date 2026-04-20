---
# === CORE IDENTIFICATION ===
concept: Object.keys
slug: object-keys

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
  - array
extends: []
related:
  - object-assign
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

`Object.keys` is a function that takes an object and returns an array of strings representing the object's own property names.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 359-361 of 04-data-structures-objects-and-arrays.md): "To find out what properties an object has, you can use the `Object.keys` function. Give the function an object and it will return an array of strings -- the object's property names."

# Prerequisites

- **object**: `Object.keys` operates on objects.
- **property**: Returns the names of an object's properties.
- **array**: Returns an array of strings.

# Key Properties

1. Returns an **array of strings** (property names).
2. Returns only the object's own properties.
3. Useful for iterating over an object's properties.

# Construction / Recognition

## To Construct/Create:
```javascript
Object.keys({x: 0, y: 0, z: 2})
```

## To Identify/Recognize:
- `Object.keys(someObject)` call pattern.

# Context & Application

`Object.keys` is essential for inspecting objects, iterating over their properties, and comparing objects. It is referenced in the deep comparison exercise at the end of Ch 4.

# Examples

**Example 1** (Ch 4, lines 363-366 of 04-data-structures-objects-and-arrays.md):
```javascript
console.log(Object.keys({x: 0, y: 0, z: 2}));
// → ["x", "y", "z"]
```

# Relationships

## Builds Upon
- **object** -- Operates on objects.
- **array** -- Returns an array.

## Enables
- Object iteration and comparison patterns.

## Related
- **object-assign** -- `Object.assign` copies properties between objects.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Expecting `Object.keys` to return inherited properties.
  **Correction**: `Object.keys` returns only the object's own properties.

# Common Confusions

- **Confusion**: `Object.keys` returns values.
  **Clarification**: It returns property **names** (strings), not their values.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Objects", lines 358-366 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 359-361)
- Confidence rationale: Explicit function description with example
- Cross-reference status: verified within chapter
