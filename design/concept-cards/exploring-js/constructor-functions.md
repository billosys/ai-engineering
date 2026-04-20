---
# === CORE IDENTIFICATION ===
concept: Classes and Constructor Functions
slug: constructor-functions

# === CLASSIFICATION ===
category: types-values
subcategory: type-system
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.8 Classes and constructor functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - classes
  - constructors

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-overview
  - specification-types
extends: []
related:
  - instanceof-operator
  - wrapper-objects
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are primitive values vs. objects in JavaScript?"
---

# Quick Definition

Constructor functions (and their ES6 syntactic sugar, classes) are JavaScript's factories for creating objects. They partition the single `object` spec type into subtypes, providing more types than the specification's eight.

# Core Definition

"JavaScript's original factories for objects are *constructor functions*: ordinary functions that return 'instances' of themselves if we invoke them via the `new` operator." (Ch. 14, &sect;14.8). ^ES6^: "ES6 introduced *classes*, which are mainly better syntax for constructor functions." Classes partition the `object` type into subtypes: "they give us more types than the limited 7 ones of the specification."

# Prerequisites

- **objects-overview** -- constructor functions create objects
- **specification-types** -- classes subdivide the object type

# Key Properties

1. Constructor functions are the original object factories
2. ^ES6^: Classes are syntactic sugar for constructor functions
3. Classes create subtypes of `object`
4. `new` operator invokes a constructor
5. Each primitive type (except undefined/null) has an associated constructor: Boolean, Number, String, Symbol

# Construction / Recognition

```js
class Person {
  constructor(name) {
    this.name = name;
  }
}
const jane = new Person('Jane');
assert.equal(jane instanceof Person, true);
```

# Context & Application

Classes are the modern way to create object types. The associated constructors for primitives serve as type conversion functions and namespace objects.

# Examples

From the source text (Ch. 14, &sect;14.8.1):
```js
// Number as conversion function:
assert.equal(Number('123'), 123);

// Number.prototype provides methods:
assert.equal((123).toString, Number.prototype.toString);

// Number as namespace:
assert.equal(Number.isInteger(123), true);
```

# Relationships

## Builds Upon
- **objects-overview** -- constructors create objects
- **specification-types** -- classes subdivide object type

## Enables
- **instanceof-operator** -- instanceof checks constructor/class
- **wrapper-objects** -- new-invoking primitive constructors

## Related
- No additional

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `new` with primitive constructors to create values.
  **Correction**: `new Number(123)` creates a wrapper object, not a number. Use `Number('123')` without `new` for conversion.

# Common Confusions

- **Confusion**: Thinking classes and constructor functions are fundamentally different.
  **Clarification**: Classes are syntactic sugar for constructor functions; they use the same prototype-based mechanism.

# Source Reference

Chapter 14: Values, Section 14.8, lines 646-701.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with multiple roles described
- Cross-reference status: verified
