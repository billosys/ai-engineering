---
concept: Accessor Property Descriptors
slug: accessor-property-descriptors
category: metaprogramming
subcategory: property-attributes
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 397
section: "14.1 Property Attributes"
extraction_confidence: high
aliases:
  - "getter/setter descriptors"
prerequisites:
  - property-descriptors
extends: []
related:
  - object-define-property
contrasts_with: []
answers_questions:
  - "How do I use `Object.defineProperty()` to control property behavior?"
---

# Quick Definition

Property descriptors for accessor properties that use `get` and `set` function attributes instead of `value` and `writable`, enabling computed properties, validation, and side effects on property access.

# Core Definition

"Accessor properties don't have a *value* attribute or a *writable* attribute: their writability is determined by the presence or absence of a setter. So the four attributes of an accessor property are *get*, *set*, *enumerable*, and *configurable*" (p. 397). A property cannot be both a data property and an accessor property simultaneously.

# Prerequisites

- **property-descriptors** — Accessor descriptors are a variant of property descriptors

# Key Properties

1. `get` — function called when property is read (no arguments)
2. `set` — function called when property is written (receives new value)
3. `enumerable` — whether the property appears in for/in
4. `configurable` — whether the property can be deleted or reconfigured
5. No `value` or `writable` attributes
6. Can convert data property to accessor and vice versa (if configurable)

# Construction / Recognition

```js
Object.defineProperty(o, "x", {
    get: function() { return 0; },
    enumerable: true,
    configurable: true
});

// Or using Object.defineProperties:
let p = Object.defineProperties({}, {
    x: { value: 1, writable: true, enumerable: true, configurable: true },
    r: {
        get() { return Math.sqrt(this.x*this.x + this.y*this.y); },
        enumerable: true, configurable: true
    }
});
```

# Context & Application

Used to create computed properties, implement validation on assignment, log property access, and maintain backward compatibility when changing from data to computed properties.

# Examples

From the source text (p. 398-399): Converting a data property to an accessor: `Object.defineProperty(o, "x", { get: function() { return 0; } })` changes x from value 2 to always returning 0. The `assignDescriptors` example (p. 400-401) shows that `Object.assign()` copies getter return values, not the getter functions themselves.

# Relationships

## Builds Upon
- **Property Descriptors** — Accessor descriptors are one of two descriptor types

## Related
- **Object.defineProperty()** — The method used to create accessor properties programmatically

# Common Errors

- **Error**: Including both `value` and `get` in a property descriptor.
  **Correction**: A descriptor must be either a data descriptor (value/writable) or an accessor descriptor (get/set), never both. Mixing them throws TypeError.

# Common Confusions

- **Confusion**: Thinking `Object.assign()` copies getter functions.
  **Clarification**: `Object.assign()` invokes getters and copies the returned values as data properties. To copy the getter itself, use `Object.getOwnPropertyDescriptor()` and `Object.defineProperty()`.

# Source Reference

Chapter 14: Metaprogramming, Section 14.1, pages 397-401.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
