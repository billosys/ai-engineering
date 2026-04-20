---
concept: Object.defineProperty()
slug: object-define-property
category: metaprogramming
subcategory: property-attributes
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 398
section: "14.1 Property Attributes"
extraction_confidence: high
aliases:
  - "Object.defineProperties()"
prerequisites:
  - property-descriptors
extends: []
related:
  - object-freeze
  - proxy-objects
contrasts_with: []
answers_questions:
  - "How do I use `Object.defineProperty()` to control property behavior?"
---

# Quick Definition

A method that creates or modifies a property on an object with explicit control over its attributes (writable, enumerable, configurable, value/get/set), unlike simple assignment which always creates writable, enumerable, configurable properties.

# Core Definition

"To set the attributes of a property or to create a new property with the specified attributes, call Object.defineProperty(), passing the object to be modified, the name of the property to be created or altered, and the property descriptor object" (p. 398). Omitted attributes default to false/undefined for new properties. `Object.defineProperties()` sets multiple properties at once.

# Prerequisites

- **property-descriptors** — Understanding the descriptor object structure

# Key Properties

1. Creates new properties or modifies existing own properties
2. Omitted attributes default to false/undefined for new properties
3. For existing properties, omitted attributes are left unchanged
4. Throws TypeError if operation violates configurable constraints
5. `Object.defineProperties()` for batch operations
6. Returns the modified object

# Construction / Recognition

```js
let o = {};
Object.defineProperty(o, "x", {
    value: 1, writable: true, enumerable: false, configurable: true
});
o.x  // => 1
Object.keys(o)  // => [] (not enumerable)

Object.defineProperty(o, "x", { writable: false });  // Make read-only
o.x = 2;  // Fails silently (or TypeError in strict mode)
```

# Context & Application

Used by library authors to add non-enumerable methods to prototypes (like built-in methods), create read-only properties, and build property-level access control.

# Examples

From the source text (p. 398-401): Creating non-enumerable property, making it read-only, then changing from data to accessor property. `Object.defineProperties()` for creating multiple properties at once with a point object having x, y (data) and r (accessor).

# Relationships

## Builds Upon
- **Property Descriptors** — defineProperty uses descriptor objects

## Enables
- **Object.freeze/seal** — Built on defineProperty concepts
- **Proxy Objects** — Proxy traps intercept defineProperty operations

# Common Errors

- **Error**: Trying to change a non-configurable property's attributes (other than value of writable property).
  **Correction**: Non-configurable properties have restricted attribute changes. Only writable→non-writable and value changes (if writable) are allowed.

# Common Confusions

- **Confusion**: Thinking `Object.defineProperty()` works on inherited properties.
  **Clarification**: It only creates or modifies *own* properties. It will not alter inherited properties.

# Source Reference

Chapter 14: Metaprogramming, Section 14.1, pages 398-401.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
