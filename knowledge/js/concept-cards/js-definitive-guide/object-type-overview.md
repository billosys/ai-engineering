---
# === CORE IDENTIFICATION ===
concept: Object Type Overview
slug: object-type-overview

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: language-overview
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Introduction to JavaScript"
chapter_number: 1
pdf_page: 22
section: "1.3 A Tour of JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - objects
  - reference types

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - type-system-overview
extends: []
related:
  - primitive-vs-object-types
  - primitive-immutability-vs-object-mutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

An object in JavaScript is a collection of name/value pairs (properties), and is the fundamental composite data type — arrays, functions, classes, Sets, Maps, RegExps, and Dates are all specialized kinds of objects.

# Core Definition

As introduced in Chapter 1: "An object is a collection of name/value pairs, or a string to value map." Chapter 3 adds: "An object (that is, a member of the type object) is a collection of properties where each property has a name and a value (either a primitive value or another object)." Objects are mutable and compared by reference. (pp. 22, 40-41)

# Prerequisites

- **javascript-language-overview** — Objects are a fundamental language feature
- **type-system-overview** — Objects are one of the two type categories

# Key Properties

1. Unordered collection of named properties (name/value pairs)
2. Properties accessed with dot notation (`.`) or bracket notation (`[]`)
3. New properties can be added by assignment
4. Arrays, functions, RegExps, Dates, etc. are specialized objects
5. Objects are mutable — properties can be changed
6. Objects are compared by reference, not by value
7. Optional chaining (`?.`) for safe property access (ES2020)

# Construction / Recognition

```javascript
let book = {
    topic: "JavaScript",
    edition: 7
};
book.topic          // => "JavaScript"
book["edition"]     // => 7
book.author = "Flanagan";   // Create new property
```

# Context & Application

Objects are JavaScript's most important data type and are used to represent structured data, configurations, records, and more. Arrays and functions are specialized objects, making objects the foundation of nearly all complex JavaScript data structures.

# Examples

From the source text (pp. 22-23):
```javascript
let book = {
    topic: "JavaScript",
    edition: 7
};
book.topic                      // => "JavaScript"
book["edition"]                 // => 7
book.author = "Flanagan";      // Create new properties by assignment
book.contents = {};             // {} is an empty object
book.contents?.ch01?.sect1      // => undefined: optional chaining (ES2020)

let points = [
    {x: 0, y: 0},
    {x: 1, y: 1}
];
```

# Relationships

## Builds Upon
- **type-system-overview** — Objects are one of the two fundamental type categories

## Enables
- **primitive-vs-object-types** — Objects are contrasted with primitives
- **primitive-immutability-vs-object-mutability** — Objects are mutable, primitives are not

## Related
- **primitive-vs-object-types** — The distinction between primitive and object types

## Contrasts With
- Primitive types — objects are mutable and compared by reference

# Common Errors

- **Error**: Comparing two objects with `===` expecting value equality.
  **Correction**: Two distinct objects are never equal even with identical properties — objects are compared by reference, not value.

# Common Confusions

- **Confusion**: Arrays are a separate type from objects.
  **Clarification**: Arrays are a specialized kind of object with numbered indices and special behavior.

# Source Reference

Chapter 1: Introduction to JavaScript, Section 1.3, pages 22-23. Chapter 3, Section 3.1, pages 40-41.

# Verification Notes

- Definition source: Direct quotes from pp. 22, 40-41
- Confidence rationale: High — clearly introduced with examples
- Uncertainties: Full object treatment deferred to Chapter 6
- Cross-reference status: Verified
