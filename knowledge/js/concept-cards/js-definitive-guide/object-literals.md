---
# === CORE IDENTIFICATION ===
concept: Object Literals
slug: object-literals

# === CLASSIFICATION ===
category: objects
subcategory: object-creation
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 148
section: "6.2.1 Object Literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "object initializer syntax"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-as-property-collections
extends:
  - object-and-array-initializers
related:
  - shorthand-properties
  - computed-property-names
  - spread-operator-in-object-literals
  - shorthand-methods
contrasts_with:
  - constructor-functions
  - object-create

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the prototype chain?"
---

# Quick Definition

An object literal is a comma-separated list of colon-separated name:value pairs enclosed in curly braces. It creates and initializes a new, distinct object each time it is evaluated.

# Core Definition

"The easiest way to create an object is to include an object literal in your JavaScript code. In its simplest form, an *object literal* is a comma-separated list of colon-separated name:value pairs, enclosed within curly braces." Each evaluation creates a new and distinct object. All objects created by object literals share the same prototype: `Object.prototype`. (Ch. 6, §6.2.1)

# Prerequisites

- **objects-as-property-collections** — Object literals create objects with properties.

# Key Properties

1. Property names can be identifiers, string literals, or (in ES6+) computed expressions.
2. Property values are any JavaScript expression, evaluated each time.
3. Trailing commas are legal.
4. Each evaluation creates a new, distinct object.
5. All objects from literals inherit from `Object.prototype`.
6. ES6+ adds shorthand properties, computed names, spread, and shorthand methods.

# Construction / Recognition

```js
let empty = {};
let point = { x: 0, y: 0 };
let book = {
    "main title": "JavaScript",
    for: "all audiences",
    author: { firstname: "David", surname: "Flanagan" }
};
```

# Context & Application

Object literals are the most common way to create objects in JavaScript. They are used for configuration objects, data structures, and ad-hoc groupings of related values.

# Examples

From the source text (§6.2.1, pp. 148-149):

```js
let empty = {};
let point = { x: 0, y: 0 };
let p2 = { x: point.x, y: point.y+1 };
let book = {
    "main title": "JavaScript",
    "sub-title": "The Definitive Guide",
    for: "all audiences",
    author: {
        firstname: "David",
        surname: "Flanagan"
    }
};
```

# Relationships

## Builds Upon
- **objects-as-property-collections** — Literals create objects with named properties
- **object-and-array-initializers** — Object literals are the object form of initializers

## Enables
- **shorthand-properties** — ES6 shorthand syntax for object literals
- **computed-property-names** — ES6 computed names in object literals
- **spread-operator-in-object-literals** — ES2018 spread syntax
- **shorthand-methods** — ES6 method shorthand

## Related
- All extended object literal syntax features

## Contrasts With
- **constructor-functions** — Alternative object creation via `new`
- **object-create** — Alternative object creation with explicit prototype

# Common Errors

- **Error**: Expecting two object literals to create the same object.
  **Correction**: Each evaluation creates a new, distinct object. Two literals with identical content produce different objects.

# Common Confusions

- **Confusion**: Believing reserved words cannot be used as property names.
  **Clarification**: As of ES5, reserved words like `for` can be used as unquoted property names in object literals.

# Source Reference

Chapter 6: Objects, Section 6.2.1, pages 148-149.

# Verification Notes

- Definition source: Direct quote from §6.2.1
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
