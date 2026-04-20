---
# === CORE IDENTIFICATION ===
concept: Getters and Setters
slug: getters-and-setters

# === CLASSIFICATION ===
category: objects
subcategory: extended-literal-syntax
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 167
section: "6.10.6 Property Getters and Setters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "accessor properties"
  - "get/set methods"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-literals
  - shorthand-methods
  - property-attributes
extends: []
related:
  - prototype-chain
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do property descriptors relate to Object.freeze()?"
---

# Quick Definition

Accessor properties use `get` and `set` methods instead of a single value. Reading the property invokes the getter; assigning to it invokes the setter. A property with only a getter is read-only.

# Core Definition

"JavaScript also supports *accessor properties*, which do not have a single value but instead have one or two accessor methods: a *getter* and/or a *setter*. When a program queries the value of an accessor property, JavaScript invokes the getter method. When a program sets the value of an accessor property, JavaScript invokes the setter method." (Ch. 6, §6.10.6)

# Prerequisites

- **object-literals** — Accessor properties are defined in object literals.
- **shorthand-methods** — Accessor syntax builds on method syntax.
- **property-attributes** — Accessor properties are an alternative to data properties.

# Key Properties

1. Getter-only: read-only property; reading returns the getter's return value.
2. Setter-only: write-only property; reading returns `undefined`.
3. Both getter and setter: read/write property.
4. Accessor properties are inherited, just like data properties.
5. `this` inside getters/setters refers to the object on which the property is accessed.
6. Introduced in ES5 (not an ES6 extension).

# Construction / Recognition

```js
let o = {
    dataProp: value,
    get accessorProp() { return this.dataProp; },
    set accessorProp(value) { this.dataProp = value; }
};
```

# Context & Application

Getters and setters are used to provide computed properties, validation on assignment, lazy initialization, logging, and providing multiple API views of the same underlying data (e.g., Cartesian and polar coordinates).

# Examples

From the source text (§6.10.6, pp. 167-170):

```js
let p = {
    x: 1.0,
    y: 1.0,
    get r() { return Math.hypot(this.x, this.y); },
    set r(newvalue) {
        let oldvalue = Math.hypot(this.x, this.y);
        let ratio = newvalue/oldvalue;
        this.x *= ratio;
        this.y *= ratio;
    },
    get theta() { return Math.atan2(this.y, this.x); }
};
p.r       // => Math.SQRT2
p.theta   // => Math.PI / 4

// Inherited accessor properties
let q = Object.create(p);
q.x = 3; q.y = 4;
q.r       // => 5 (inherited getter works)

// Serial number generator
const serialnum = {
    _n: 0,
    get next() { return this._n++; },
    set next(n) {
        if (n > this._n) this._n = n;
        else throw new Error("serial number can only be set to a larger value");
    }
};
serialnum.next = 10;
serialnum.next   // => 10
serialnum.next   // => 11
```

# Relationships

## Builds Upon
- **object-literals** — Defined in object literal syntax
- **shorthand-methods** — Similar syntax with `get`/`set` prefix
- **property-attributes** — Accessor properties have different attributes than data properties

## Enables
- Computed properties, validation, lazy evaluation

## Related
- **prototype-chain** — Accessor properties are inherited like data properties

## Contrasts With
- No direct contrast (data properties vs. accessor properties is implicit)

# Common Errors

- **Error**: Defining a getter and a data property with the same name.
  **Correction**: A property is either a data property or an accessor property, not both.

# Common Confusions

- **Confusion**: Believing accessor properties can have a `value` attribute.
  **Clarification**: Accessor properties have `get`, `set`, `enumerable`, and `configurable` attributes — not `value` or `writable`.

# Source Reference

Chapter 6: Objects, Section 6.10.6, pages 167-170.

# Verification Notes

- Definition source: Direct quote from §6.10.6
- Confidence rationale: High — extensive examples with multiple use cases
- Uncertainties: None
- Cross-reference status: Verified
