---
# === CORE IDENTIFICATION ===
concept: Symbols as Property Names
slug: symbols-as-property-names

# === CLASSIFICATION ===
category: objects
subcategory: extended-literal-syntax
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 165
section: "6.10.3 Symbols as Property Names"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "symbol properties"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - computed-property-names
extends:
  - computed-property-names
related:
  - enumerating-properties
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from for/in?"
---

# Quick Definition

ES6 Symbols can be used as property names via computed property syntax, providing unique, non-conflicting keys for safe extension of objects. Symbols are not returned by `Object.keys()` or `for/in`.

# Core Definition

"In ES6 and later, property names can be strings or symbols. If you assign a symbol to a variable or constant, then you can use that symbol as a property name using the computed property syntax." Every Symbol is unique: "Symbols are good for creating unique property names." They provide "a safe extension mechanism for JavaScript objects." (Ch. 6, §6.10.3)

# Prerequisites

- **computed-property-names** — Symbols require computed property syntax `[symbol]`.

# Key Properties

1. Every Symbol is unique — two Symbols with the same description are different.
2. Symbols are primitive values, not objects (`Symbol()` is not a constructor).
3. Symbol-named properties are not returned by `Object.keys()` or `for/in`.
4. `Object.getOwnPropertySymbols()` retrieves Symbol properties.
5. The point is not security but safe, conflict-free extension of objects.
6. Well-known symbols like `Symbol.iterator` define protocols.

# Construction / Recognition

```js
const extension = Symbol("my extension symbol");
let o = {
    [extension]: { /* extension data */ }
};
o[extension].x = 0;  // Won't conflict with other properties
```

# Context & Application

Symbols are used to add properties to objects without risking name collisions, especially when extending third-party objects or implementing protocols like iteration (`Symbol.iterator`).

# Examples

From the source text (§6.10.3, pp. 165-166):

```js
const extension = Symbol("my extension symbol");
let o = {
    [extension]: { /* extension data stored in this object */ }
};
o[extension].x = 0;  // This won't conflict with other properties of o
```

# Relationships

## Builds Upon
- **computed-property-names** — Symbols require computed property syntax

## Enables
- Safe object extension patterns
- Protocol implementation (e.g., `Symbol.iterator`)

## Related
- **enumerating-properties** — Symbol properties require `Object.getOwnPropertySymbols()`

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `new Symbol()`.
  **Correction**: `Symbol()` is a factory function, not a constructor. Do not use `new`.

# Common Confusions

- **Confusion**: Believing Symbols provide security.
  **Clarification**: "The point of Symbols is not security." Third-party code can discover Symbols via `Object.getOwnPropertySymbols()`. Symbols prevent accidental conflicts, not deliberate access.

# Source Reference

Chapter 6: Objects, Section 6.10.3, pages 165-166.

# Verification Notes

- Definition source: Direct quote from §6.10.3
- Confidence rationale: High — clear explanation with use case rationale
- Uncertainties: None
- Cross-reference status: Verified
