---
concept: Symbol.toStringTag
slug: symbol-to-string-tag
category: metaprogramming
subcategory: well-known-symbols
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 405
section: "14.4.3 Symbol.toStringTag"
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

A well-known Symbol that customizes the string returned by `Object.prototype.toString()`, allowing custom classes to report a meaningful type string like `"[object Range]"` instead of `"[object Object]"`.

# Core Definition

"In ES6, Object.prototype.toString() looks for a property with the symbolic name Symbol.toStringTag on its argument, and if such a property exists, it uses the property value in its output" (p. 406). This enables a `classof()` utility function that can identify custom types.

# Prerequisites

- **well-known-symbols** — Symbol.toStringTag is a well-known Symbol

# Key Properties

1. Defined as a getter returning a string
2. Customizes `Object.prototype.toString.call(obj)` output
3. Result appears as `"[object YourTag]"`
4. Enables type identification beyond what `typeof` provides

# Construction / Recognition

```js
class Range {
    get [Symbol.toStringTag]() { return "Range"; }
}
let r = new Range(1, 10);
Object.prototype.toString.call(r)  // => "[object Range]"
```

# Context & Application

Useful for debugging and type checking. The `classof()` utility function using `Object.prototype.toString.call(o).slice(8,-1)` can identify types of all values.

# Examples

From the source text (p. 405-406): Built-in types return informative strings: `Array`, `RegExp`, `Function`, `Date`, `Map`, `Set`. Custom class with Symbol.toStringTag returns custom type name.

# Relationships

## Builds Upon
- **Well-Known Symbols** — One of the well-known Symbols

# Common Errors

- **Error**: Implementing Symbol.toStringTag as a data property instead of a getter.
  **Correction**: While it works as a data property, using a getter (`get [Symbol.toStringTag]()`) is the conventional pattern.

# Common Confusions

- **Confusion**: Thinking Symbol.toStringTag changes the behavior of the `typeof` operator.
  **Clarification**: `typeof` is unaffected. Symbol.toStringTag only changes `Object.prototype.toString()` output.

# Source Reference

Chapter 14: Metaprogramming, Section 14.4.3, pages 405-406.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
