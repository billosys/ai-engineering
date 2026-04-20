---
concept: Symbol.toPrimitive
slug: symbol-to-primitive
category: metaprogramming
subcategory: well-known-symbols
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 411
section: "14.4.7 Symbol.toPrimitive"
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

A well-known Symbol used as a method name that gives complete control over how an object is converted to a primitive value, receiving a `hint` argument ("string", "number", or "default") indicating the preferred type.

# Core Definition

"In ES6, the well-known Symbol Symbol.toPrimitive allows you to override this default object-to-primitive behavior and gives you complete control over how instances of your own classes will be converted to primitive values" (p. 411). The method receives a hint: "string" (e.g., template literals), "number" (e.g., comparison operators), or "default" (e.g., `+`, `==`).

# Prerequisites

- **well-known-symbols** — Symbol.toPrimitive is a well-known Symbol

# Key Properties

1. Method receives a `hint` string: "string", "number", or "default"
2. Must return a primitive value
3. Overrides the default toString()/valueOf() fallback behavior
4. "string" hint: template literals, string concatenation context
5. "number" hint: arithmetic operators, comparison operators
6. "default" hint: `+`, `==`, `!=` operators

# Construction / Recognition

```js
class MyType {
    [Symbol.toPrimitive](hint) {
        if (hint === "string") return "my string representation";
        if (hint === "number") return 42;
        return true;  // "default" hint
    }
}
```

# Context & Application

Useful for classes that need to behave meaningfully in arithmetic, comparison, or string contexts. Essential for creating sortable/comparable custom objects.

# Examples

From the source text (p. 411-412): Hint is "string" in template literals, "number" with `<`, `>`, `-`, `*` operators, "default" with `+`, `==`, `!=`.

# Relationships

## Builds Upon
- **Well-Known Symbols** — One of the well-known Symbols

# Common Errors

- **Error**: Returning a non-primitive from [Symbol.toPrimitive].
  **Correction**: The method must return a primitive value (string, number, boolean, etc.), not an object.

# Common Confusions

- **Confusion**: Not understanding when "default" vs "number" hint is used.
  **Clarification**: The `+` operator uses "default" (not "number") because it can do both addition and concatenation. Dedicated arithmetic operators like `-` and `*` use "number".

# Source Reference

Chapter 14: Metaprogramming, Section 14.4.7, pages 411-412.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
