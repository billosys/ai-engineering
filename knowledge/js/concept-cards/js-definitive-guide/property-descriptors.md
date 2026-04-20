---
concept: Property Descriptors
slug: property-descriptors
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
  - "property attributes"
prerequisites: []
extends: []
related:
  - object-define-property
  - object-freeze
contrasts_with: []
answers_questions:
  - "How do property descriptors relate to `Object.freeze()`?"
  - "How do I use `Object.defineProperty()` to control property behavior?"
  - "What must I understand before learning about the Proxy API?"
---

# Quick Definition

Objects representing the four attributes of a property — `value`/`writable`/`enumerable`/`configurable` for data properties, or `get`/`set`/`enumerable`/`configurable` for accessor properties — queried with `Object.getOwnPropertyDescriptor()`.

# Core Definition

"The JavaScript methods for querying and setting the attributes of a property use an object called a *property descriptor*" (p. 397). Data properties have value, writable, enumerable, and configurable attributes. Accessor properties have get, set, enumerable, and configurable. Properties created by assignment are writable, enumerable, and configurable by default.

# Prerequisites

This is a foundational concept with no prerequisites within this source beyond basic object knowledge.

# Key Properties

1. **writable** — whether the value can be changed
2. **enumerable** — whether the property appears in for/in and Object.keys()
3. **configurable** — whether the property can be deleted or its attributes changed
4. Accessor descriptors use **get/set** instead of value/writable
5. Queried with `Object.getOwnPropertyDescriptor(obj, name)`
6. Only works for own properties (not inherited)

# Construction / Recognition

```js
Object.getOwnPropertyDescriptor({x: 1}, "x");
// => {value: 1, writable: true, enumerable: true, configurable: true}

const random = { get octet() { return Math.floor(Math.random()*256); } };
Object.getOwnPropertyDescriptor(random, "octet");
// => {get: /*func*/, set: undefined, enumerable: true, configurable: true}
```

# Context & Application

Essential for library authors who need to add non-enumerable methods to prototypes, create read-only properties, or lock down objects. Forms the foundation for Object.freeze/seal.

# Examples

From the source text (p. 397-398): Regular property `{x:1}` has all attributes true. Accessor property has get/set instead of value/writable. `Object.getOwnPropertyDescriptor({}, "toString")` returns undefined because toString is inherited.

# Relationships

## Enables
- **Object.defineProperty()** — Sets property descriptors
- **Object.freeze()** — Makes all properties non-writable and non-configurable

## Related
- **Object.freeze/seal** — Built on property attribute manipulation

# Common Errors

- **Error**: Trying to get descriptors of inherited properties with getOwnPropertyDescriptor.
  **Correction**: This method only works for own properties. Traverse the prototype chain manually for inherited properties.

# Common Confusions

- **Confusion**: Thinking all properties have a value attribute.
  **Clarification**: Accessor properties have get/set instead of value/writable. A property cannot be both a data property and an accessor property.

# Source Reference

Chapter 14: Metaprogramming, Section 14.1, pages 397-401.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
