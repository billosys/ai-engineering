---
# === CORE IDENTIFICATION ===
concept: Shorthand Properties
slug: shorthand-properties

# === CLASSIFICATION ===
category: data-structures
subcategory: syntax
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "The lycanthrope's log"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - property shorthand
  - shorthand notation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - property
  - binding
extends: []
related:
  - destructuring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

When a property name in an object literal isn't followed by a value, JavaScript uses the value from the binding with the same name as both the property name and value.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 501-506 of 04-data-structures-objects-and-arrays.md): "Note that the object added to the journal looks a little odd. Instead of declaring properties like `events: events`, it just gives a property name: `events`. This is shorthand that means the same thing -- if a property name in brace notation isn't followed by a value, its value is taken from the binding with the same name."

# Prerequisites

- **object**: Shorthand properties are used in object literals.
- **property**: This is a syntax shortcut for property definitions.
- **binding**: The value comes from a binding with the same name.

# Key Properties

1. `{events}` is equivalent to `{events: events}`.
2. Works when the property name matches a binding name in scope.
3. Can be mixed with regular property definitions.

# Construction / Recognition

## To Construct/Create:
```javascript
function addEntry(events, squirrel) {
  journal.push({events, squirrel});
}
```

## To Identify/Recognize:
- A single identifier inside an object literal without a colon and value.

# Context & Application

Shorthand properties reduce redundancy when creating objects from existing bindings. This is very common in modern JavaScript.

# Examples

**Example 1** (Ch 4, lines 492-497 of 04-data-structures-objects-and-arrays.md):
```javascript
let journal = [];
function addEntry(events, squirrel) {
  journal.push({events, squirrel});
}
```
This is equivalent to `journal.push({events: events, squirrel: squirrel})`.

# Relationships

## Builds Upon
- **object** -- Used in object literal syntax.
- **binding** -- Value comes from same-named binding.

## Enables
- More concise object creation.

## Related
- **destructuring** -- The inverse operation (extracting from objects).

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using shorthand when the binding name doesn't match the desired property name.
  **Correction**: Shorthand only works when binding name and property name are identical.

# Common Confusions

- **Confusion**: Shorthand properties are a different kind of property.
  **Clarification**: It is purely syntactic sugar. `{x}` is exactly `{x: x}`.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "The lycanthrope's log", lines 500-506 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 501-506)
- Confidence rationale: Explicit explanation of shorthand
- Cross-reference status: verified within chapter
