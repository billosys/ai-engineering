---
# === CORE IDENTIFICATION ===
concept: Primitive Constructor Functions
slug: primitive-constructor-functions

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
section: "14.8.1 Constructor functions associated with primitive types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - primitive type constructors
  - Boolean/Number/String/Symbol functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-values
  - constructor-functions
extends:
  - constructor-functions
related:
  - explicit-type-conversion
  - wrapper-objects
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are primitive values vs. objects in JavaScript?"
---

# Quick Definition

Each primitive type (except `undefined` and `null`) has an associated constructor function -- `Boolean`, `Number`, `String`, `Symbol` -- which serves triple duty as a type converter, prototype provider, and namespace for utility functions.

# Core Definition

"Each primitive type (except for the types `undefined` and `null`) has an associated *constructor function*." (Ch. 14, &sect;14.8.1). For example, `Number` serves four roles: as a conversion function (`Number('123')` returns `123`), as a prototype provider (`Number.prototype` provides methods for numbers), as a namespace for utility functions (`Number.isInteger()`), and as a class for wrapper objects (which should be avoided).

# Prerequisites

- **primitive-values** -- the types these constructors are associated with
- **constructor-functions** -- these are specialized constructor functions

# Key Properties

1. `Boolean`: associated with booleans
2. `Number`: associated with numbers
3. `String`: associated with strings
4. `Symbol`: associated with symbols
5. `undefined` and `null` have no associated constructors
6. Each plays multiple roles: converter, prototype, namespace, class

# Construction / Recognition

```js
// As converter:
Number('123')           // 123

// As prototype provider:
(123).toString          // Number.prototype.toString

// As namespace:
Number.isInteger(123)   // true
```

# Context & Application

These functions are used throughout JavaScript for type conversion, accessing methods on primitives, and utility functions.

# Examples

From the source text (Ch. 14, &sect;14.8.1):
```js
// Conversion
assert.equal(Number('123'), 123);

// Prototype
assert.equal((123).toString, Number.prototype.toString);

// Namespace
assert.equal(Number.isInteger(123), true);
```

# Relationships

## Builds Upon
- **primitive-values** -- associated with primitive types
- **constructor-functions** -- these are constructor functions

## Enables
- **explicit-type-conversion** -- constructors serve as converters
- **wrapper-objects** -- new-invocation creates wrappers

## Related
- No additional

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `new Number(123)` thinking it creates a number.
  **Correction**: `new Number(123)` creates a wrapper object, not a number. Use `Number('123')` without `new`.

# Common Confusions

- **Confusion**: Thinking primitives can't have methods because they're not objects.
  **Clarification**: Primitives access methods via `Number.prototype`, `String.prototype`, etc. -- JavaScript transparently wraps primitives to provide property access.

# Source Reference

Chapter 14: Values, Section 14.8.1, lines 663-701.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: All four roles explicitly described for Number
- Cross-reference status: verified
