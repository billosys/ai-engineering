---
concept: Object.freeze(), Object.seal(), Object.preventExtensions()
slug: object-freeze
category: metaprogramming
subcategory: object-protection
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 401
section: "14.2 Object Extensibility"
extraction_confidence: high
aliases:
  - "Object.seal()"
  - "Object.preventExtensions()"
  - "object protection"
  - "frozen object"
  - "sealed object"
prerequisites:
  - property-descriptors
extends: []
related:
  - object-define-property
  - proxy-objects
contrasts_with: []
answers_questions:
  - "How do property descriptors relate to `Object.freeze()`?"
---

# Quick Definition

Three progressive levels of object protection: `preventExtensions()` blocks new properties, `seal()` also makes existing properties non-configurable, and `freeze()` additionally makes all data properties read-only — none are reversible.

# Core Definition

`Object.preventExtensions()` makes an object non-extensible (no new properties). `Object.seal()` adds non-configurability to all own properties. `Object.freeze()` "locks objects down even more tightly. In addition to making the object non-extensible and its properties nonconfigurable, it also makes all of the object's own data properties read-only" (p. 402). None affect prototypes or accessor setter methods.

# Prerequisites

- **property-descriptors** — These methods manipulate property attributes

# Key Properties

1. `preventExtensions()` — no new properties; existing can still be modified/deleted
2. `seal()` — no new properties, existing are non-configurable (but writable ones stay writable)
3. `freeze()` — no new properties, all non-configurable and non-writable
4. None are reversible
5. None affect prototype chain objects
6. Check with `isExtensible()`, `isSealed()`, `isFrozen()`
7. All return the object for chaining

# Construction / Recognition

```js
let o = Object.seal(Object.create(Object.freeze({x: 1}),
    {y: {value: 2, writable: true}}));
```

# Context & Application

Used for defensive programming — preventing third-party code from modifying library objects, protecting shared configuration, and creating truly constant values. "Object.freeze() on those objects to prevent the user's code from modifying them" (p. 403).

# Examples

From the source text (p. 401-403): Nested freezing example. Warning: "frozen objects can interfere with common JavaScript testing strategies" (p. 403).

# Relationships

## Builds Upon
- **Property Descriptors** — These methods manipulate writable/configurable attributes

## Related
- **Object.defineProperty()** — The lower-level mechanism
- **Proxy Objects** — Proxy invariants must respect frozen/sealed state

# Common Errors

- **Error**: Expecting freeze/seal to affect nested objects.
  **Correction**: Freeze/seal are shallow — they only affect the object's own properties. Nested objects remain mutable unless separately frozen.

# Common Confusions

- **Confusion**: Thinking Object.seal() makes properties read-only.
  **Clarification**: seal() makes properties non-configurable and prevents new properties, but writable properties can still be modified. Only freeze() makes data properties read-only.

# Source Reference

Chapter 14: Metaprogramming, Section 14.2, pages 401-403.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
