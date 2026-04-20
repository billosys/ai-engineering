---
concept: Symbol.species
slug: symbol-species
category: metaprogramming
subcategory: well-known-symbols
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 407
section: "14.4.4 Symbol.species"
extraction_confidence: high
aliases: []
prerequisites:
  - well-known-symbols
extends: []
related: []
contrasts_with: []
answers_questions: []
---

# Quick Definition

A well-known Symbol that allows subclasses to control which constructor is used when inherited methods (like `Array.map()`) create new instances, defaulting to the subclass constructor but overridable.

# Core Definition

Array methods like `map()`, `filter()`, `slice()`, `concat()`, and `splice()` "invoke new this.constructor[Symbol.species]() to create the new array" (p. 407). By default, `Array[Symbol.species]` is a getter that returns `this`, so subclass constructors create subclass instances. Override to return `Array` if you want base class instances.

# Prerequisites

- **well-known-symbols** — Symbol.species is a well-known Symbol

# Key Properties

1. Controls which constructor is used by methods that create new instances
2. Default: getter returns `this` (subclass methods return subclass instances)
3. Can be overridden with a static getter
4. Used by Array, TypedArray, ArrayBuffer, Map, Set, RegExp, and Promise
5. `Array[Symbol.species]` is a read-only accessor — must use defineProperty or static getter to override

# Construction / Recognition

```js
class EZArray extends Array {
    static get [Symbol.species]() { return Array; }
    get first() { return this[0]; }
    get last() { return this[this.length-1]; }
}
let e = new EZArray(1,2,3);
let f = e.map(x => x - 1);
f.last  // => undefined: f is a regular Array, not EZArray
```

# Context & Application

Important when subclassing built-in types. Controls whether methods like `map()` return instances of the subclass or the base class.

# Examples

From the source text (p. 407-408): Without Symbol.species override, `EZArray.map()` returns EZArray instances with the custom `last` getter. With the override, it returns plain Arrays.

# Relationships

## Builds Upon
- **Well-Known Symbols** — One of the well-known Symbols

# Common Errors

- **Error**: Trying to set Symbol.species with assignment: `EZArray[Symbol.species] = Array`.
  **Correction**: The inherited property is a read-only accessor. Use `static get [Symbol.species]() { return Array; }` in the class definition.

# Common Confusions

- **Confusion**: Thinking Symbol.species affects the constructor called with `new`.
  **Clarification**: Symbol.species only affects methods that create derived objects (like map, filter, slice). It does not affect `new SubClass()`.

# Source Reference

Chapter 14: Metaprogramming, Section 14.4.4, pages 407-408.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
