---
# === CORE IDENTIFICATION ===
concept: Objects as Property Collections
slug: objects-as-property-collections

# === CLASSIFICATION ===
category: objects
subcategory: object-fundamentals
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 146
section: "6.1 Introduction to Objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "JavaScript objects"
  - "object fundamentals"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - property-attributes
  - own-vs-inherited-properties
  - prototype-objects
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the prototype chain?"
  - "What distinguishes shallow copy from deep copy of objects?"
---

# Quick Definition

A JavaScript object is an unordered collection of properties, each with a name (string or Symbol) and a value. Objects also inherit properties from a prototype, and are mutable, manipulated by reference.

# Core Definition

"An object is a composite value: it aggregates multiple values (primitive values or other objects) and allows you to store and retrieve those values by name. An object is an unordered collection of *properties*, each of which has a name and a value... In addition to maintaining its own set of properties, a JavaScript object also inherits the properties of another object, known as its 'prototype.'" Objects are "dynamic — properties can usually be added and deleted" and are "mutable and manipulated by reference rather than by value." (Ch. 6, §6.1)

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Properties are name-value pairs; names are strings or Symbols.
2. Objects map strings to values — often called hash, hashtable, dictionary, or associative array.
3. Objects inherit properties from a prototype (prototypal inheritance).
4. Objects are mutable and manipulated by reference: `let y = x` copies the reference, not the object.
5. Any value that is not a string, number, Symbol, boolean, null, or undefined is an object.
6. Properties can be dynamically added and deleted.

# Construction / Recognition

An object is any non-primitive value in JavaScript, including arrays, functions, Date, Map, Set, RegExp, etc.

# Context & Application

Objects are JavaScript's most fundamental datatype. They are used to represent structured data, serve as hash maps, hold methods, implement classes, and more.

# Examples

From the source text (§6.1, pp. 146-147):

```js
// Objects are mutable and manipulated by reference
let x = { a: 1 };
let y = x;        // y holds a reference to the same object
y.a = 2;          // Modification through y is visible through x
x.a               // => 2
```

# Relationships

## Builds Upon
- No prerequisites — this is the foundational object concept

## Enables
- **property-attributes** — Each property has writable, enumerable, configurable attributes
- **own-vs-inherited-properties** — Properties are either own or inherited
- **prototype-objects** — Objects inherit from prototypes

## Related
- All other object-related concepts build on this foundation

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Expecting assignment to copy an object's contents.
  **Correction**: `let y = x` copies the reference. Use `Object.assign()` or spread for a shallow copy.

# Common Confusions

- **Confusion**: Believing strings, numbers, and booleans are objects.
  **Clarification**: They are primitives, but "can behave like immutable objects" due to auto-boxing.

# Source Reference

Chapter 6: Objects, Section 6.1, pages 146-148.

# Verification Notes

- Definition source: Direct quote from §6.1
- Confidence rationale: High — foundational section with clear definitions
- Uncertainties: None
- Cross-reference status: Verified
