---
# === CORE IDENTIFICATION ===
concept: Primitive Immutability vs Object Mutability
slug: primitive-immutability-vs-object-mutability

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
pdf_page: 60
section: "3.8 Immutable Primitive Values and Mutable Object References"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - value types vs reference types
  - by value vs by reference

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-vs-object-types
extends:
  - primitive-vs-object-types
related:
  - string-type
  - strict-vs-loose-equality
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

Primitive values (numbers, strings, booleans, null, undefined, symbols) are immutable and compared by value, while objects (including arrays and functions) are mutable and compared by reference — two objects are equal only if they refer to the same underlying object.

# Core Definition

"Primitives are immutable: there is no way to change (or 'mutate') a primitive value." "All string methods that appear to return a modified string are, in fact, returning a new string value." "Primitives are also compared by value: two values are the same only if they have the same value." Objects are different: "they are mutable—their values can change." "Objects are not compared by value: two distinct objects are not equal even if they have the same properties and values." Objects are "sometimes called reference types" and "are compared by reference: two object values are the same if and only if they refer to the same underlying object." (pp. 60-62)

# Prerequisites

- **primitive-vs-object-types** — Must understand the distinction between primitive and object types

# Key Properties

1. Primitives are immutable — cannot be changed in place
2. Strings are immutable despite looking like character arrays
3. Primitives are compared by value
4. Objects are mutable — properties and elements can be changed
5. Objects are compared by reference
6. Assigning an object to a variable copies the reference, not the object
7. To copy an object/array, you must explicitly copy properties/elements
8. `Array.from()` (ES6) creates a shallow copy of an array

# Construction / Recognition

```javascript
// Primitives: immutable, compared by value
let s = "hello";
s.toUpperCase();    // Returns "HELLO", doesn't change s
s                   // => "hello": unchanged

// Objects: mutable, compared by reference
let o = {x: 1};
o.x = 2;            // Mutate the object
let p = {x: 2};
o === p              // => false: different objects even with same properties

let a = [];
let b = a;           // b and a refer to the SAME array
b[0] = 1;
a[0]                 // => 1: change visible through both references
a === b              // => true: same underlying object
```

# Context & Application

This distinction is fundamental to understanding JavaScript behavior when passing values to functions, comparing values, and working with data structures. It is essential background for understanding closures, which capture variable references.

# Examples

From the source text (pp. 60-62):
```javascript
// String immutability
let s = "hello";
s.toUpperCase();    // Returns "HELLO", but doesn't alter s
s                   // => "hello": the original string has not changed

// Object mutability
let o = { x: 1 };
o.x = 2;             // Mutate it
o.y = 3;             // Add new property

// Object comparison by reference
let o = {x: 1}, p = {x: 1};
o === p               // => false: distinct objects are never equal

// Shared references
let a = [];
let b = a;
b[0] = 1;
a[0]                  // => 1: change visible through a
a === b               // => true: same object

// Copying arrays
let a = ["a","b","c"];
let b = [];
for(let i = 0; i < a.length; i++) { b[i] = a[i]; }
let c = Array.from(b);    // ES6 copy
```

# Relationships

## Builds Upon
- **primitive-vs-object-types** — Extends the type categorization with behavioral differences

## Enables
- Understanding function argument passing behavior
- Understanding closures (variables capture references)
- **strict-vs-loose-equality** — Object equality is reference-based

## Related
- **string-type** — Strings are immutable despite appearing array-like

## Contrasts With
- None — this card IS the contrast between the two categories

# Common Errors

- **Error**: Expecting `let b = a` to copy an array.
  **Correction**: This copies the reference, not the array. Both `a` and `b` point to the same array. Use `Array.from(a)` or `[...a]` to copy.

- **Error**: Comparing arrays for equality: `[1,2,3] === [1,2,3]`.
  **Correction**: This is `false` — two distinct arrays are never equal. Compare elements individually.

# Common Confusions

- **Confusion**: `const` makes objects immutable.
  **Clarification**: `const` prevents reassignment of the variable binding, but the object itself remains mutable. `const o = {x: 1}; o.x = 2;` is legal.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.8, pages 60-62.

# Verification Notes

- Definition source: Direct quotes from pp. 60-62
- Confidence rationale: High — thoroughly explained with examples
- Uncertainties: None
- Cross-reference status: Verified
