---
# === CORE IDENTIFICATION ===
concept: Property Access
slug: property-access

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
  - dot notation
  - bracket notation
  - member access

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property
  - expression
extends: []
related:
  - optional-chaining
  - object
  - array
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create and manipulate an array?"
---

# Quick Definition

Properties in JavaScript are accessed in two ways: dot notation (`value.x`) uses the literal property name, while bracket notation (`value[x]`) evaluates the expression inside to determine the property name.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 161-170 of 04-data-structures-objects-and-arrays.md): "The two main ways to access properties in JavaScript are with a dot and with square brackets. Both `value.x` and `value[x]` access a property on `value` -- but not necessarily the same property. The difference is in how `x` is interpreted. When using a dot, the word after the dot is the literal name of the property. When using square brackets, the expression between the brackets is *evaluated* to get the property name."

# Prerequisites

- **property**: Property access retrieves properties from values.
- **expression**: Bracket notation evaluates an expression to determine the property name.

# Key Properties

1. **Dot notation** (`value.x`): the word after the dot is the literal property name.
2. **Bracket notation** (`value[x]`): the expression is evaluated and converted to a string.
3. Dot notation works only with names that look like valid binding names.
4. For names like "2" or "John Doe", bracket notation is required.
5. Array elements must use bracket notation since their names are numbers.

# Construction / Recognition

## To Construct/Create:
```javascript
value.color     // dot notation
value["color"]  // bracket notation
value[i]        // computed property name
```

## To Identify/Recognize:
- A dot followed by a name, or square brackets after a value expression.

# Context & Application

Property access is one of the most common operations in JavaScript. Understanding the difference between dot and bracket notation is essential for working with objects and arrays.

# Examples

**Example 1** (Ch 4, lines 161-170 of 04-data-structures-objects-and-arrays.md):
"Whereas `value.x` fetches the property of `value` named 'x', `value[x]` takes the value of the variable named `x` and uses that, converted to a string, as the property name."

**Example 2** (Ch 4, lines 176-181):
"If you want to access a property named *2* or *John Doe*, you must use square brackets: `value[2]` or `value["John Doe"]`."

# Relationships

## Builds Upon
- **property** -- Accessing properties requires understanding what they are.
- **expression** -- Bracket notation uses expressions.

## Enables
- **optional-chaining** -- Safe property access when values may be null.

## Related
- **object** -- Objects are accessed via property access.
- **array** -- Array elements use bracket notation with numeric indices.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using dot notation with numeric property names (`arr.0`).
  **Correction**: Use bracket notation for numeric properties: `arr[0]`.

# Common Confusions

- **Confusion**: `value.x` and `value[x]` always access the same property.
  **Clarification**: `value.x` accesses the property literally named "x", while `value[x]` evaluates the variable `x` and uses its value as the property name.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Properties", lines 160-192 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 161-170)
- Confidence rationale: Explicit detailed explanation
- Cross-reference status: verified within chapter
