---
concept: Object.getPrototypeOf() and Object.setPrototypeOf()
slug: object-get-set-prototype-of
category: metaprogramming
subcategory: prototypes
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 403
section: "14.3 The prototype Attribute"
extraction_confidence: high
aliases:
  - "prototype manipulation"
  - "__proto__"
prerequisites: []
extends: []
related:
  - reflect-api
contrasts_with: []
answers_questions: []
---

# Quick Definition

Methods for querying and changing an object's prototype at runtime: `Object.getPrototypeOf()` returns the prototype, and `Object.setPrototypeOf()` changes it (though changing prototypes is strongly discouraged for performance reasons).

# Core Definition

"You can query the prototype of any object by passing that object to Object.getPrototypeOf()" (p. 403). `Object.setPrototypeOf()` changes the prototype but "any code that uses the altered objects may run much slower than it would normally" (p. 404) because JavaScript engines optimize based on fixed prototypes. The deprecated `__proto__` property provides an alternative.

# Prerequisites

This is a foundational concept with no prerequisites within this source beyond basic prototype knowledge.

# Key Properties

1. `Object.getPrototypeOf(obj)` — returns the prototype or null
2. `Object.setPrototypeOf(obj, proto)` — changes the prototype (performance cost)
3. `isPrototypeOf()` — checks if an object is in another's prototype chain
4. `__proto__` — deprecated but widely supported alternative
5. Setting prototype on non-extensible objects throws TypeError

# Construction / Recognition

```js
Object.getPrototypeOf({})   // => Object.prototype
Object.getPrototypeOf([])   // => Array.prototype
let o = {x: 1}; let p = {y: 2};
Object.setPrototypeOf(o, p);
o.y  // => 2: o now inherits from p
```

# Context & Application

Querying prototypes is useful for reflection and debugging. Setting prototypes at runtime is rare and discouraged — use Object.create() to set prototypes at creation time instead.

# Examples

From the source text (p. 403-404): `Object.getPrototypeOf(()=>{})` returns `Function.prototype`. Changing an array's prototype: `Object.setPrototypeOf(a, p); a.join` becomes `undefined`.

# Relationships

## Related
- **Reflect API** — Reflect.getPrototypeOf/setPrototypeOf provide similar functionality

# Common Errors

- **Error**: Using setPrototypeOf() in performance-critical code.
  **Correction**: Avoid setPrototypeOf() in production code. Use Object.create() to set prototypes at object creation time.

# Common Confusions

- **Confusion**: Thinking `__proto__` is the same as the prototype property of constructor functions.
  **Clarification**: `__proto__` refers to an object's prototype (inheritance chain). `Constructor.prototype` is the object that becomes the prototype of instances created with `new Constructor()`.

# Source Reference

Chapter 14: Metaprogramming, Section 14.3, pages 403-404.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
