---
# === CORE IDENTIFICATION ===
concept: Enumerating Properties
slug: enumerating-properties

# === CLASSIFICATION ===
category: objects
subcategory: property-operations
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 157
section: "6.6 Enumerating Properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - for-in-loop
  - for-of-loop
  - own-vs-inherited-properties
  - property-attributes
extends: []
related:
  - property-enumeration-order
  - property-existence-testing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from for/in?"
---

# Quick Definition

JavaScript provides multiple ways to enumerate properties: `for/in` (own + inherited enumerable), `Object.keys()` (own enumerable strings), `Object.getOwnPropertyNames()` (all own strings), `Object.getOwnPropertySymbols()` (own Symbols), and `Reflect.ownKeys()` (all own).

# Core Definition

"There are four functions you can use to get an array of property names: Object.keys() returns an array of the names of the enumerable own properties... Object.getOwnPropertyNames() works like Object.keys() but returns an array of the names of non-enumerable own properties as well... Object.getOwnPropertySymbols() returns own properties whose names are Symbols... Reflect.ownKeys() returns all own property names, both enumerable and non-enumerable, and both string and Symbol." (Ch. 6, §6.6)

# Prerequisites

- **for-in-loop** — The traditional way to enumerate properties.
- **for-of-loop** — Modern iteration over arrays returned by Object.keys() etc.
- **own-vs-inherited-properties** — Enumeration methods differ in what they include.
- **property-attributes** — The enumerable attribute controls visibility.

# Key Properties

1. `for/in`: own + inherited enumerable string properties.
2. `Object.keys()`: own enumerable string properties only.
3. `Object.getOwnPropertyNames()`: all own string properties (enumerable + non-enumerable).
4. `Object.getOwnPropertySymbols()`: own Symbol properties.
5. `Reflect.ownKeys()`: all own properties (string + Symbol, enumerable + non-enumerable).
6. `Object.values()` and `Object.entries()` return values and [key, value] pairs respectively.
7. Use `for/of` with `Object.keys()` instead of `for/in` to avoid inherited properties.

# Construction / Recognition

```js
for(let key of Object.keys(obj)) { ... }
for(let val of Object.values(obj)) { ... }
for(let [k, v] of Object.entries(obj)) { ... }
for(let p in obj) { ... }  // includes inherited
```

# Context & Application

Choosing the right enumeration method is crucial for correct behavior. `Object.keys()` with `for/of` is the recommended default. `for/in` is needed when inherited properties should be included.

# Examples

From the source text (§6.6, pp. 157-159):

```js
let o = {x: 1, y: 2, z: 3};
o.propertyIsEnumerable("toString")  // => false: not enumerable
for(let p in o) {
    console.log(p);  // Prints x, y, z, but not toString
}

// Filtering inherited properties in for/in
for(let p in o) {
    if (!o.hasOwnProperty(p)) continue;  // Skip inherited
}

// Modern approach: Object.keys() with for/of
for(let key of Object.keys(o)) {
    console.log(key);  // Only own enumerable string properties
}
```

# Relationships

## Builds Upon
- **for-in-loop** — Traditional enumeration
- **for-of-loop** — Modern iteration over key/value arrays
- **own-vs-inherited-properties** — Core distinction for choosing method
- **property-attributes** — Enumerable attribute controls what's included

## Enables
- **property-enumeration-order** — Order rules apply to all enumeration methods

## Related
- **property-existence-testing** — Complements enumeration

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `for/in` and getting unexpected inherited properties.
  **Correction**: Use `Object.keys()` with `for/of` to enumerate only own enumerable properties.

# Common Confusions

- **Confusion**: Believing `Object.keys()` and `for/in` return the same properties.
  **Clarification**: `Object.keys()` returns only own enumerable string properties. `for/in` also includes inherited enumerable properties and was part of JavaScript since the beginning.

# Source Reference

Chapter 6: Objects, Section 6.6, pages 157-159.

# Verification Notes

- Definition source: Direct quote from §6.6
- Confidence rationale: High — comprehensive comparison of all methods
- Uncertainties: None
- Cross-reference status: Verified against §5.4.5
