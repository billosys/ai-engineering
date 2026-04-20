---
concept: Symbol.hasInstance
slug: symbol-has-instance
category: metaprogramming
subcategory: well-known-symbols
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 405
section: "14.4.2 Symbol.hasInstance"
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

A well-known Symbol that customizes the `instanceof` operator, allowing objects to define a `[Symbol.hasInstance]()` method that determines whether a value is an "instance" of that type.

# Core Definition

"In ES6, if the righthand side of instanceof is any object with a [Symbol.hasInstance] method, then that method is invoked with the lefthand side value as its argument, and the return value of the method, converted to a boolean, becomes the value of the instanceof operator" (p. 405).

# Prerequisites

- **well-known-symbols** — Symbol.hasInstance is a well-known Symbol

# Key Properties

1. Overrides the default `instanceof` behavior
2. Method receives the left-hand value as argument
3. Return value is coerced to boolean
4. Enables "type checking" with non-class objects

# Construction / Recognition

```js
let uint8 = {
    [Symbol.hasInstance](x) {
        return Number.isInteger(x) && x >= 0 && x <= 255;
    }
};
128 instanceof uint8    // => true
256 instanceof uint8    // => false
Math.PI instanceof uint8  // => false
```

# Context & Application

Enables custom type-checking predicates that work with the `instanceof` syntax. Useful for defining pseudotypes or value constraints.

# Examples

From the source text (p. 405): A `uint8` "type" object that checks if a value is an integer between 0-255 using Symbol.hasInstance.

# Relationships

## Builds Upon
- **Well-Known Symbols** — One of the well-known Symbols

# Common Errors

- **Error**: Using Symbol.hasInstance on a class without understanding it overrides prototype chain checking.
  **Correction**: When defined, Symbol.hasInstance completely replaces the default prototype-based instanceof check.

# Common Confusions

- **Confusion**: Thinking Symbol.hasInstance is commonly used.
  **Clarification**: The text notes this is "clever but confusing" and suggests a regular `isUint8()` function would be clearer.

# Source Reference

Chapter 14: Metaprogramming, Section 14.4.2, page 405.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
