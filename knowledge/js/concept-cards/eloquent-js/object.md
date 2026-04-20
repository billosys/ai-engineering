---
# === CORE IDENTIFICATION ===
concept: Object
slug: object

# === CLASSIFICATION ===
category: data-structures
subcategory: collections
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
aliases:
  - objects
  - object literal

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
  - string
extends: []
related:
  - property
  - property-access
  - array
  - method
  - mutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arrays relate to objects in JavaScript?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

Objects are arbitrary collections of properties, created using braces as an expression, where each property has a name and a value.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 269-271 of 04-data-structures-objects-and-arrays.md): "Values of the type *object* are arbitrary collections of properties. One way to create an object is by using braces as an expression."

The chapter introduction (lines 36-37) adds: "*Objects* allow us to group values -- including other objects -- to build more complex structures."

# Prerequisites

- **value**: Objects group multiple values.
- **string**: Property names are strings.

# Key Properties

1. Created with braces containing property-value pairs: `{name: "value"}`.
2. Properties are name-value pairs separated by commas.
3. Property names that aren't valid binding names must be quoted.
4. Reading a nonexistent property returns `undefined`.
5. Properties can be added, modified, or deleted after creation.
6. Braces at the start of a statement are a block; in other positions, they describe an object.

# Construction / Recognition

## To Construct/Create:
```javascript
let day1 = {
  squirrel: false,
  events: ["work", "touched tree", "pizza", "running"]
};
```

## To Identify/Recognize:
- Curly braces with key-value pairs (not at the start of a statement).

# Context & Application

Objects are fundamental to JavaScript. They are used for grouping related data, representing entities, and as the basis for more complex data structures. Arrays are a specialized kind of object.

# Examples

**Example 1** (Ch 4, lines 273-285 of 04-data-structures-objects-and-arrays.md):
```javascript
let day1 = {
  squirrel: false,
  events: ["work", "touched tree", "pizza", "running"]
};
console.log(day1.squirrel);
// → false
console.log(day1.wolf);
// → undefined
day1.wolf = false;
console.log(day1.wolf);
// → false
```

**Example 2** (Ch 4, lines 294-299) -- quoted property names:
```javascript
let descriptions = {
  work: "Went to work",
  "touched tree": "Touched a tree"
};
```

# Relationships

## Builds Upon
- **value** -- Objects are a type of value.
- **string** -- Property names are strings.

## Enables
- **property** -- Objects are collections of properties.
- **method** -- Properties that hold functions.
- **mutability** -- Objects are mutable.
- **json** -- JSON is based on JavaScript object notation.

## Related
- **array** -- Arrays are a specialized kind of object.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Writing `n => {prop: n}` in an arrow function expecting an object.
  **Correction**: Braces are interpreted as a function body. Use parentheses: `n => ({prop: n})`.

# Common Confusions

- **Confusion**: Objects and arrays are completely distinct.
  **Clarification**: "Arrays, then, are just a kind of object specialized for storing sequences of things."

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Objects", lines 257-384 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 269-271)
- Confidence rationale: Explicit definition with italicized term "object"
- Cross-reference status: verified against array section
