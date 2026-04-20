---
concept: Well-Known Symbols
slug: well-known-symbols
category: metaprogramming
subcategory: well-known-symbols
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 404
section: "14.4 Well-Known Symbols"
extraction_confidence: high
aliases: []
prerequisites:
  - symbol-iterator
extends: []
related:
  - symbol-to-primitive
  - symbol-to-string-tag
  - symbol-has-instance
  - symbol-species
contrasts_with: []
answers_questions:
  - "What must I understand before learning about the Proxy API?"
---

# Quick Definition

A set of Symbol values stored as properties of the `Symbol()` factory function (like `Symbol.iterator`, `Symbol.toPrimitive`) that allow JavaScript code to control low-level behaviors of objects and classes.

# Core Definition

"These are a set of Symbol values stored as properties of the Symbol() factory function that are used to allow JavaScript code to control certain low-level behaviors of objects and classes" (p. 404). They include Symbol.iterator, Symbol.asyncIterator, Symbol.hasInstance, Symbol.toStringTag, Symbol.species, Symbol.toPrimitive, and Symbol.isConcatSpreadable.

# Prerequisites

- **symbol-iterator** — The most common well-known Symbol

# Key Properties

1. `Symbol.iterator` / `Symbol.asyncIterator` — make objects iterable
2. `Symbol.hasInstance` — customize `instanceof` behavior
3. `Symbol.toStringTag` — customize `Object.prototype.toString()` output
4. `Symbol.species` — control constructor used by derived objects
5. `Symbol.toPrimitive` — control object-to-primitive conversion
6. `Symbol.isConcatSpreadable` — control Array.concat() behavior

# Construction / Recognition

Well-known Symbols are used as computed property names: `[Symbol.toStringTag]`, `[Symbol.toPrimitive]`, etc.

# Context & Application

Enable library and class authors to integrate deeply with JavaScript's built-in mechanisms — making custom objects work with `instanceof`, `for/of`, string conversion, and more. Prior to ES6, this customization was only available to built-in types.

# Examples

From the source text (p. 404-412): Various well-known Symbols demonstrated: making objects iterable (Symbol.iterator), customizing instanceof (Symbol.hasInstance), customizing toString (Symbol.toStringTag), controlling subclass constructor (Symbol.species).

# Relationships

## Builds Upon
- **Symbol.iterator** — The best-known example

## Enables
- **Symbol.toPrimitive** — Object-to-primitive conversion control
- **Symbol.toStringTag** — toString() customization
- **Symbol.hasInstance** — instanceof customization
- **Symbol.species** — Subclass constructor control

# Common Errors

- **Error**: Defining well-known Symbol methods as regular string-named methods.
  **Correction**: Use computed property syntax: `[Symbol.toPrimitive](hint) { ... }`, not `"Symbol.toPrimitive"()`.

# Common Confusions

- **Confusion**: Thinking well-known Symbols are just constants.
  **Clarification**: They are actual Symbol values used as property names, enabling a form of method overloading that doesn't conflict with string-named properties.

# Source Reference

Chapter 14: Metaprogramming, Section 14.4, pages 404-412.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
