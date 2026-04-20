---
# === CORE IDENTIFICATION ===
concept: Prototype Objects
slug: prototype-objects

# === CLASSIFICATION ===
category: objects
subcategory: prototypes
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 149
section: "6.2.3 Prototypes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "prototypes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-as-property-collections
  - constructor-functions
extends: []
related:
  - prototype-chain
  - object-create
  - own-vs-inherited-properties
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the prototype chain?"
---

# Quick Definition

Almost every JavaScript object has a second object associated with it called its *prototype*, from which it inherits properties. The prototype is determined by how the object was created.

# Core Definition

"Almost every JavaScript object has a second JavaScript object associated with it. This second object is known as a *prototype*, and the first object inherits properties from the prototype." Objects created by `{}` or `new Object()` use `Object.prototype`. Objects created by `new Constructor()` use `Constructor.prototype`. "Remember: almost all objects have a *prototype*, but only a relatively small number of objects have a prototype property." (Ch. 6, §6.2.3)

# Prerequisites

- **objects-as-property-collections** — Prototypes are objects that provide inherited properties.
- **constructor-functions** — Constructors define the prototype for their instances.

# Key Properties

1. Object literals and `new Object()` objects have `Object.prototype` as their prototype.
2. `new Array()` objects have `Array.prototype`, which inherits from `Object.prototype`.
3. `new Date()` objects have `Date.prototype`, which inherits from `Object.prototype`.
4. `Object.prototype` is one of the rare objects with no prototype (the chain ends here).
5. The distinction between an object's prototype and its `prototype` property is critical.

# Construction / Recognition

The prototype of an object is set at creation time:
- Literal `{}` => `Object.prototype`
- `new Constructor()` => `Constructor.prototype`
- `Object.create(proto)` => `proto`

# Context & Application

Prototypes are the foundation of JavaScript's inheritance system. Methods shared among instances are defined on the prototype, and the prototype chain enables property lookup across the inheritance hierarchy.

# Examples

From the source text (§6.2.3, p. 149):

```js
// Object created by {} inherits from Object.prototype
// Object created by new Array() inherits from Array.prototype
// Array.prototype inherits from Object.prototype
// So a Date object inherits from both Date.prototype and Object.prototype
```

# Relationships

## Builds Upon
- **objects-as-property-collections** — Prototypes are objects
- **constructor-functions** — Constructor's `prototype` property defines instance prototypes

## Enables
- **prototype-chain** — Prototypes link together to form chains
- **own-vs-inherited-properties** — Prototypes are the source of inherited properties

## Related
- **object-create** — Explicitly sets the prototype

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Confusing an object's prototype with its `prototype` property.
  **Correction**: Most objects have a prototype (internal link to another object). Only constructor functions have a `prototype` property that defines the prototype for instances they create.

# Common Confusions

- **Confusion**: Believing every object has a `prototype` property.
  **Clarification**: Almost all objects have a prototype (accessed via `Object.getPrototypeOf()`), but only a small number — primarily constructor functions — have a `prototype` property.

# Source Reference

Chapter 6: Objects, Section 6.2.3, page 149.

# Verification Notes

- Definition source: Direct quote from §6.2.3
- Confidence rationale: High — foundational prototype explanation
- Uncertainties: Prototype manipulation via §14.3 is outside scope
- Cross-reference status: Verified against §6.3.2
