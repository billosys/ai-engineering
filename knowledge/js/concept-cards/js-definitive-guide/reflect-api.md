---
concept: Reflect API
slug: reflect-api
category: metaprogramming
subcategory: reflect
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 414
section: "14.6 The Reflect API"
extraction_confidence: high
aliases:
  - "Reflect object"
prerequisites:
  - property-descriptors
extends: []
related:
  - proxy-objects
contrasts_with: []
answers_questions: []
---

# Quick Definition

A built-in object providing functions that mirror JavaScript's fundamental operations (property access, function calls, object creation) in a unified namespace, with a one-to-one correspondence to Proxy handler methods.

# Core Definition

"The Reflect object is not a class; like the Math object, its properties simply define a collection of related functions" (p. 414). These functions "map one-to-one with the set of Proxy handler methods" (p. 414), making Reflect essential for implementing Proxy handlers that delegate to default behavior.

# Prerequisites

- **property-descriptors** — Reflect includes property descriptor operations

# Key Properties

1. `Reflect.get(o, name)` — like `o[name]`
2. `Reflect.set(o, name, value)` — like `o[name] = value`
3. `Reflect.has(o, name)` — like `name in o`
4. `Reflect.deleteProperty(o, name)` — like `delete o[name]`
5. `Reflect.defineProperty()` — returns boolean (unlike Object.defineProperty)
6. `Reflect.ownKeys(o)` — all own property names (strings + symbols)
7. `Reflect.apply(f, o, args)` — like `f.apply(o, args)`
8. `Reflect.construct(c, args)` — like `new c(...args)`

# Construction / Recognition

```js
let value = Reflect.get(target, property, receiver);
Reflect.set(target, prop, value, receiver);
Reflect.ownKeys(target);
```

# Context & Application

Primarily used inside Proxy handler methods to delegate to default behavior after performing custom logic (logging, validation, etc.).

# Examples

From the source text (p. 414-416): Functions like `Reflect.defineProperty()` return boolean instead of throwing (unlike `Object.defineProperty()`). `Reflect.ownKeys()` combines `Object.getOwnPropertyNames()` and `Object.getOwnPropertySymbols()`.

# Relationships

## Related
- **Proxy Objects** — Reflect methods map 1:1 to Proxy traps, enabling delegation

# Common Errors

- **Error**: Using Reflect.get/set without the receiver argument when needed for accessor properties.
  **Correction**: Pass the receiver when working with accessor properties to ensure the getter/setter runs with the correct `this`.

# Common Confusions

- **Confusion**: Thinking Reflect provides new capabilities beyond existing operators/methods.
  **Clarification**: Reflect mostly duplicates existing functionality but with consistent return types (booleans instead of throwing) and a clean namespace matching Proxy traps.

# Source Reference

Chapter 14: Metaprogramming, Section 14.6, pages 414-416.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
