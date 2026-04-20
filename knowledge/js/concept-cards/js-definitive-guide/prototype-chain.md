---
# === CORE IDENTIFICATION ===
concept: Prototype Chain
slug: prototype-chain

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
section: "6.2.3 Prototypes, 6.3.2 Inheritance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "prototype chain lookup"
  - "prototypal inheritance chain"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - prototype-objects
  - own-vs-inherited-properties
extends:
  - prototype-objects
related:
  - instanceof-operator
  - object-create
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the prototype chain?"
---

# Quick Definition

The prototype chain is the linked series of prototype objects from an object up to `Object.prototype` (which has a null prototype). Property lookup traverses this chain from the object upward until the property is found or the chain ends.

# Core Definition

"This linked series of prototype objects is known as a *prototype chain*." When querying a property: "If o does not have an own property with that name, the prototype object of o is queried for the property x. If the prototype object does not have an own property by that name, but has a prototype itself, the query is performed on the prototype of the prototype. This continues until the property x is found or until an object with a null prototype is searched." (Ch. 6, §6.2.3, §6.3.2)

# Prerequisites

- **prototype-objects** — The chain is formed by prototype links between objects.
- **own-vs-inherited-properties** — The chain determines what is inherited.

# Key Properties

1. Property reads traverse the chain upward until found or chain ends (returning `undefined`).
2. Property writes always create/modify own properties — never modify the prototype chain.
3. `Object.prototype` is at the top of most chains and has a null prototype.
4. The `instanceof` operator works by searching the prototype chain.
5. Overriding: setting a property with the same name as an inherited property creates an own property that hides the inherited one.

# Construction / Recognition

```js
let o = {};                      // o -> Object.prototype -> null
let p = Object.create(o);       // p -> o -> Object.prototype -> null
let q = Object.create(p);       // q -> p -> o -> Object.prototype -> null
```

# Context & Application

The prototype chain is JavaScript's inheritance mechanism. It enables method sharing across instances, class hierarchies, and the `instanceof` operator. Understanding it is essential for Ch. 9 (Classes).

# Examples

From the source text (§6.3.2, pp. 152-153):

```js
let o = {};                    // inherits from Object.prototype
o.x = 1;                      // own property x
let p = Object.create(o);     // inherits from o and Object.prototype
p.y = 2;                      // own property y
let q = Object.create(p);     // inherits from p, o, Object.prototype
q.z = 3;                      // own property z
let f = q.toString();          // toString inherited from Object.prototype
q.x + q.y                     // => 3: x inherited from o, y from p

// Assignment creates own property, does not modify prototype
let unitcircle = { r: 1 };
let c = Object.create(unitcircle);
c.r = 2;                      // own property hides inherited one
unitcircle.r                   // => 1: prototype unaffected
```

# Relationships

## Builds Upon
- **prototype-objects** — Individual prototypes form the links in the chain
- **own-vs-inherited-properties** — The chain determines inheritance

## Enables
- **instanceof-operator** — Searches the prototype chain for the constructor's prototype
- Class-based inheritance patterns (Ch. 9)

## Related
- **object-create** — Creates objects with explicit prototype chain links

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Expecting property assignment to modify a prototype object.
  **Correction**: "Inheritance occurs when querying properties but not when setting them." Assignment always creates/sets an own property on the target object.

# Common Confusions

- **Confusion**: Believing the prototype chain is created at property-access time.
  **Clarification**: The chain is determined at object creation time. It is traversed at property read time.

# Source Reference

Chapter 6: Objects, Sections 6.2.3 (p. 149) and 6.3.2 (pp. 152-154).

# Verification Notes

- Definition source: Direct quotes from §6.2.3 and §6.3.2
- Confidence rationale: High — core concept with extensive examples
- Uncertainties: None
- Cross-reference status: Verified against §4.9.4 (instanceof)
