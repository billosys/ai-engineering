---
# === CORE IDENTIFICATION ===
concept: Type System Overview
slug: type-system-overview

# === CLASSIFICATION ===
category: type-system
subcategory: type-categories
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
  - JavaScript types
  - JS type system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
extends: []
related:
  - primitive-vs-object-types
  - type-coercion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

JavaScript has a dynamic type system with two categories of types — primitive types (numbers, strings, booleans, null, undefined, Symbols) and object types (objects, arrays, functions) — where variables are untyped but values always have a type.

# Core Definition

As introduced in Chapter 1 and detailed in Chapter 3: "JavaScript types can be divided into two categories: primitive types and object types. JavaScript's primitive types include numbers, strings of text (known as strings), and Boolean truth values (known as booleans)." Special primitive values include null, undefined, and Symbol. "Any JavaScript value that is not a number, a string, a boolean, a symbol, null, or undefined is an object." (pp. 40-41)

# Prerequisites

- **javascript-language-overview** — Must understand the language to understand its type system

# Key Properties

1. Two categories: primitive types and object types
2. Primitive types: Number, String, Boolean, null, undefined, Symbol, BigInt
3. Object types: Object, Array, Function, Set, Map, RegExp, Date, Error, etc.
4. Variables are untyped; values are typed
5. JavaScript liberally converts values between types (type coercion)
6. The language performs automatic garbage collection

# Construction / Recognition

Types are recognized by their values and can be inspected with the `typeof` operator:
```javascript
typeof 42          // "number"
typeof "hello"     // "string"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // "object" (historical quirk)
typeof Symbol()    // "symbol"
typeof {}          // "object"
```

# Context & Application

Understanding the type system is fundamental to writing correct JavaScript. The dynamic, coercive type system is one of JavaScript's most distinctive features and a common source of both power and bugs.

# Examples

From the source text (p. 22):
```javascript
x = 1;           // Numbers.
x = 0.01;        // Numbers can be integers or reals.
x = "hello world"; // Strings of text in quotation marks.
x = true;         // A Boolean value.
x = null;         // Null is a special value that means "no value."
x = undefined;    // Undefined is another special value like null.
```

# Relationships

## Builds Upon
- **javascript-language-overview** — The type system is a core feature of the language

## Enables
- **primitive-vs-object-types** — Detailed distinction between the two type categories
- **type-coercion** — How values convert between types
- **number-type** — Detailed Number type
- **string-type** — Detailed String type
- **boolean-type** — Detailed Boolean type

## Related
- **type-coercion** — JavaScript's liberal value conversion rules

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming `typeof null` returns `"null"`.
  **Correction**: `typeof null` returns `"object"` — a historical bug that can never be fixed for backward compatibility.

# Common Confusions

- **Confusion**: JavaScript has no type system because variables are untyped.
  **Clarification**: JavaScript values always have types; it is the variables that are untyped.

# Source Reference

Chapter 1: Introduction to JavaScript, Section 1.3, page 22. Chapter 3: Types, Values, and Variables, Section 3.1, pages 40-42.

# Verification Notes

- Definition source: Direct quotes from pp. 40-41
- Confidence rationale: High — clearly defined in the source
- Uncertainties: None
- Cross-reference status: Verified across Ch 1 and Ch 3
