---
# === CORE IDENTIFICATION ===
concept: Destructuring
slug: destructuring

# === CLASSIFICATION ===
category: data-structures
subcategory: syntax
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Destructuring"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - destructuring assignment
  - destructuring binding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - object
  - binding
extends: []
related:
  - parameters
  - rest-parameters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Destructuring is a syntax that allows you to "look inside" an array or object value when creating bindings, extracting individual elements or properties directly into named bindings.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 1229-1232 of 04-data-structures-objects-and-arrays.md): "This also works for bindings created with `let`, `var`, or `const`. If you know that the value you are binding is an array, you can use square brackets to 'look inside' of the value, binding its contents." And (lines 1235-1236): "A similar trick works for objects, using braces instead of square brackets."

# Prerequisites

- **array**: Array destructuring uses square brackets.
- **object**: Object destructuring uses curly braces.
- **binding**: Destructuring creates bindings from parts of a value.

# Key Properties

1. **Array destructuring**: `let [a, b, c] = [1, 2, 3]` binds by position.
2. **Object destructuring**: `let {name} = {name: "Faraji", age: 23}` binds by property name.
3. Works in `let`, `var`, `const` declarations and function parameters.
4. Destructuring `null` or `undefined` causes an error.

# Construction / Recognition

## To Construct/Create:
```javascript
// Array destructuring
let [n00, n01, n10, n11] = [76, 9, 4, 1];

// Object destructuring
let {name} = {name: "Faraji", age: 23};

// In function parameters
function phi([n00, n01, n10, n11]) {
  return (n11 * n00 - n10 * n01) / Math.sqrt(...);
}
```

## To Identify/Recognize:
- Square brackets or curly braces on the left side of an assignment or in a parameter list.

# Context & Application

Destructuring makes code more readable when working with functions that return arrays or objects, and when function parameters are complex data structures. It is used extensively with `reduce` in Ch 5 (e.g., `([from, to])` in characterCount).

# Examples

**Example 1** (Ch 4, lines 1220-1226 of 04-data-structures-objects-and-arrays.md) -- array destructuring in parameters:
```javascript
function phi([n00, n01, n10, n11]) {
  return (n11 * n00 - n10 * n01) /
    Math.sqrt((n10 + n11) * (n00 + n01) *
              (n01 + n11) * (n00 + n10));
}
```

**Example 2** (Ch 4, lines 1238-1242) -- object destructuring:
```javascript
let {name} = {name: "Faraji", age: 23};
console.log(name);
// → Faraji
```

# Relationships

## Builds Upon
- **array** -- Array destructuring extracts elements by position.
- **object** -- Object destructuring extracts properties by name.
- **binding** -- Destructuring creates bindings.

## Enables
- Cleaner function parameter handling.
- More readable data extraction.

## Related
- **parameters** -- Destructuring can be used in function parameters.
- **rest-parameters** -- Can be combined with destructuring.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Destructuring `null` or `undefined`.
  **Correction**: "If you try to destructure `null` or `undefined`, you get an error, much as you would if you directly try to access a property of those values."

# Common Confusions

- **Confusion**: Object destructuring variable names must match property names.
  **Clarification**: By default, yes. But you can rename: `let {name: n} = obj` binds `obj.name` to `n`.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Destructuring", lines 1197-1247 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 1229-1236)
- Confidence rationale: Explicit dedicated section
- Cross-reference status: verified against Ch 5 usage
