---
# === CORE IDENTIFICATION ===
concept: Symbol Type
slug: symbol-type

# === CLASSIFICATION ===
category: type-system
subcategory: primitive-types
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 58
section: "3.6 Symbols"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Symbol
  - symbol primitive

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-vs-object-types
  - object-type-overview
extends: []
related:
  - global-object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Symbol in JavaScript?"
---

# Quick Definition

A Symbol is an ES6 primitive type that serves as a unique, non-string property name for objects, created by calling `Symbol()` which never returns the same value twice.

# Core Definition

"Symbols were introduced in ES6 to serve as non-string property names." "The Symbol type does not have a literal syntax. To obtain a Symbol value, you call the Symbol() function. This function never returns the same value twice, even when called with the same argument. This means that if you call Symbol() to obtain a Symbol value, you can safely use that value as a property name to add a new property to an object and do not need to worry that you might be overwriting an existing property with the same name." (pp. 58-59)

# Prerequisites

- **primitive-vs-object-types** — Symbol is a primitive type
- **object-type-overview** — Symbols are used as object property names

# Key Properties

1. No literal syntax — created via `Symbol()` function
2. Every call to `Symbol()` returns a unique value
3. Optional string argument for description: `Symbol("desc")`
4. Used as non-string property names on objects
5. `typeof` returns `"symbol"`
6. `Symbol.for("key")` returns a shared Symbol from a global registry
7. `Symbol.for()` always returns the same Symbol for the same string argument
8. `Symbol.keyFor(sym)` retrieves the string key for a registered Symbol
9. Well-known Symbols: `Symbol.iterator` for making objects iterable
10. `toString()` is the only interesting method on Symbol instances

# Construction / Recognition

```javascript
let symname = Symbol("propname");
typeof symname                      // => "symbol"

let o = {};
o[symname] = 2;                     // Define a property with a Symbol name
o[symname]                          // => 2: access the symbol-named property

// Global registry
let s = Symbol.for("shared");
let t = Symbol.for("shared");
s === t                             // => true
Symbol.keyFor(t)                    // => "shared"
```

# Context & Application

Symbols are primarily used as a language extension mechanism. ES6 used `Symbol.iterator` to add iteration support to objects without risking name collisions with existing string property names. Libraries and frameworks use Symbols to add "hidden" properties that won't conflict with user code.

# Examples

From the source text (pp. 58-60):
```javascript
let strname = "string name";
let symname = Symbol("propname");
typeof strname             // => "string"
typeof symname             // => "symbol"
let o = {};
o[strname] = 1;            // Define a property with a string name
o[symname] = 2;            // Define a property with a Symbol name
o[strname]                 // => 1
o[symname]                 // => 2

let s = Symbol("sym_x");
s.toString()               // => "Symbol(sym_x)"

// Global Symbol registry
let s = Symbol.for("shared");
let t = Symbol.for("shared");
s === t                    // => true
s.toString()               // => "Symbol(shared)"
Symbol.keyFor(t)           // => "shared"
```

# Relationships

## Builds Upon
- **primitive-vs-object-types** — Symbol is a primitive type
- **object-type-overview** — Symbols serve as property names on objects

## Enables
- Language extension mechanisms (Symbol.iterator for iteration)
- Collision-free property naming

## Related
- **global-object** — Well-known Symbols are global

## Contrasts With
- String property names — Symbols are guaranteed unique; strings can collide

# Common Errors

- **Error**: Calling `new Symbol()` with the `new` keyword.
  **Correction**: `Symbol()` is a function, not a constructor — do not use `new`.

# Common Confusions

- **Confusion**: `Symbol("x") === Symbol("x")` is true because the descriptions match.
  **Clarification**: Every call to `Symbol()` returns a unique value regardless of the description. Use `Symbol.for("x")` if you need shared Symbols.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.6, pages 58-60.

# Verification Notes

- Definition source: Direct quotes from pp. 58-59
- Confidence rationale: High — clearly defined with examples
- Uncertainties: None
- Cross-reference status: Verified
