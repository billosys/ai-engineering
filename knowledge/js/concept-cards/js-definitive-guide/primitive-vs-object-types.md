---
# === CORE IDENTIFICATION ===
concept: Primitive vs Object Types
slug: primitive-vs-object-types

# === CLASSIFICATION ===
category: type-system
subcategory: type-categories
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 40
section: "3.1 Overview and Definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - value types vs reference types

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-system-overview
extends:
  - type-system-overview
related:
  - primitive-immutability-vs-object-mutability
  - number-type
  - string-type
  - boolean-type
  - symbol-type
  - null-vs-undefined
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

JavaScript types divide into two categories: primitive types (number, string, boolean, null, undefined, symbol, bigint) which are immutable and compared by value, and object types (objects, arrays, functions) which are mutable and compared by reference.

# Core Definition

"JavaScript types can be divided into two categories: primitive types and object types." Primitive types include "numbers, strings of text (known as strings), and Boolean truth values (known as booleans)," plus null, undefined, and Symbol. "Any JavaScript value that is not a number, a string, a boolean, a symbol, null, or undefined is an object." Objects include "an unordered collection of named values" as well as arrays, functions, Sets, Maps, RegExps, Dates, and Errors. (pp. 40-41)

# Prerequisites

- **type-system-overview** — Must understand the type system at a high level

# Key Properties

1. Primitive types: Number, String, Boolean, null, undefined, Symbol, BigInt
2. Object types: Object, Array, Function, Set, Map, RegExp, Date, Error
3. Primitives are immutable; objects are mutable
4. Primitives are compared by value; objects are compared by reference
5. Functions and classes are specialized objects
6. null and undefined are the only values that cannot have methods invoked on them

# Construction / Recognition

Primitive values:
```javascript
42, "hello", true, null, undefined, Symbol("x"), 123n
```

Object values:
```javascript
{x: 1}, [1,2,3], function(){}, new Date(), /regex/
```

# Context & Application

This distinction is fundamental to understanding JavaScript. It affects how values are compared, copied, and passed to functions. Primitives are always copied by value; objects are always referenced.

# Examples

From the source text (p. 40-41):
```javascript
// Primitives
let n = 42;          // Number
let s = "hello";     // String
let b = true;        // Boolean
let x = null;        // null
let y = undefined;   // undefined
let sym = Symbol();  // Symbol

// Objects
let obj = {x: 1};   // Object
let arr = [1,2,3];   // Array (specialized object)
let fn = function(){}; // Function (specialized object)
```

# Relationships

## Builds Upon
- **type-system-overview** — This is the fundamental type categorization

## Enables
- **primitive-immutability-vs-object-mutability** — The core behavioral difference
- **type-coercion** — Conversion between types
- **strict-vs-loose-equality** — Equality behavior differs by category

## Related
- All individual type cards (number-type, string-type, etc.)

## Contrasts With
- The two categories contrast with each other by design

# Common Errors

- **Error**: Expecting object comparison by value.
  **Correction**: `{x:1} === {x:1}` is `false` — objects are compared by reference, not by the values of their properties.

# Common Confusions

- **Confusion**: Strings are objects because they have methods like `.toUpperCase()`.
  **Clarification**: Strings are primitives. They "behave as if they have methods" via temporary wrapper objects, but they are immutable primitive values (p. 42).

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.1, pages 40-42.

# Verification Notes

- Definition source: Direct quotes from pp. 40-41
- Confidence rationale: High — clearly and thoroughly defined
- Uncertainties: None
- Cross-reference status: Verified
