---
# === CORE IDENTIFICATION ===
concept: Property
slug: property

# === CLASSIFICATION ===
category: data-structures
subcategory: core-concepts
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - properties
  - object property

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
  - string
extends: []
related:
  - property-access
  - method
  - object
  - array
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

A property is a named attribute of a value, accessed with dot notation or bracket notation. Almost all JavaScript values have properties, with the exceptions of `null` and `undefined`.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 142-148 of 04-data-structures-objects-and-arrays.md): "We've seen a few expressions like `myString.length` (to get the length of a string) and `Math.max` (the maximum function) in past chapters. These expressions access a *property* of some value." Further (lines 151-153): "Almost all JavaScript values have properties. The exceptions are `null` and `undefined`. If you try to access a property on one of these nonvalues, you get an error."

# Prerequisites

- **value**: Properties belong to values.
- **string**: Property names are strings.

# Key Properties

1. Almost all values in JavaScript have properties (`null` and `undefined` do not).
2. Property names are strings.
3. Accessing a property on `null` or `undefined` causes a TypeError.
4. Array elements are stored as properties with numeric names.
5. Properties can hold any value, including functions (methods).

# Construction / Recognition

## To Construct/Create:
```javascript
let obj = {x: 0, y: 0, z: 2};
```

## To Identify/Recognize:
- Any named attribute accessed via dot or bracket notation on a value.

# Context & Application

Properties are the fundamental mechanism for accessing data and behavior on JavaScript values. Understanding properties is necessary for working with objects, arrays, strings, and the built-in `Math` object.

# Examples

**Example 1** (Ch 4, lines 155-158 of 04-data-structures-objects-and-arrays.md):
```javascript
null.length;
// → TypeError: null has no properties
```

**Example 2** (Ch 4, lines 191-192 of 04-data-structures-objects-and-arrays.md):
"Just like strings, arrays have a `length` property that tells us how many elements the array has."

# Relationships

## Builds Upon
- **value** -- Properties belong to values.

## Enables
- **property-access** -- Two ways to access properties.
- **method** -- Properties that hold functions.

## Related
- **object** -- Objects are collections of properties.
- **array** -- Array elements are properties with numeric names.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Accessing a property on `null` or `undefined`.
  **Correction**: Always check for `null`/`undefined` before property access, or use optional chaining (`?.`).

# Common Confusions

- **Confusion**: Only objects have properties.
  **Clarification**: Almost all values have properties -- strings have `.length`, numbers have methods via their prototype.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Properties", lines 139-192 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 142-148)
- Confidence rationale: Explicit definition with italicized term "property"
- Cross-reference status: verified within chapter
