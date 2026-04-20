---
# === CORE IDENTIFICATION ===
concept: Symbol Type
slug: symbol-type

# === CLASSIFICATION ===
category: primitive-types
subcategory: symbols
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Symbols"
chapter_number: 24
pdf_page: null
section: "Symbols are primitive values with unique identities"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "symbol"
  - "Symbol()"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - symbol-descriptions
  - symbols-as-constants
  - symbols-as-property-keys
  - publicly-known-symbols
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Symbol and when would you use one?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Symbols are primitive values created via the `Symbol()` factory function that have unique identities -- each symbol is different from every other symbol, even with the same description. Introduced in ES6.

# Core Definition

"Symbols are primitive values that are created via the factory function `Symbol()`." The optional parameter provides a description for debugging. Unlike other primitives, symbols have unique identities and are not compared by value: `Symbol() === Symbol()` is `false`. They can be used as property keys in objects. `typeof` returns `'symbol'` (Ch. 24, Section 24.1).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Created via `Symbol()` factory function (not `new Symbol()`) (ES6)
2. `typeof` returns `'symbol'`
3. Unique identity: `Symbol() === Symbol()` is `false`
4. Optional description parameter (for debugging)
5. Can be used as object property keys
6. Compared by identity, not value (like objects, unlike other primitives)

# Construction / Recognition

```js
const sym = Symbol('mySymbol');
typeof sym // 'symbol'
Symbol() === Symbol() // false

const obj = { [sym]: 123 };
```

# Context & Application

Symbols have two main use cases: (1) as values for constants that need unique identities, and (2) as unique property keys that cannot clash with string keys.

# Examples

From the source text:

```js
const mySymbol = Symbol('mySymbol');
assert.equal(typeof mySymbol, 'symbol');

// Unique identities
const sym1 = Symbol();
const sym2 = Symbol();
assert.equal(sym1 === sym2, false);

// Unlike strings which compare by value
const str1 = 'abc';
const str2 = 'abc';
assert.equal(str1 === str2, true); // strings compared by value

// Used as property keys
const obj = { [sym1]: 123 };
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **symbols-as-constants** — symbols as unique constant values
- **symbols-as-property-keys** — symbols as clash-free property keys
- **publicly-known-symbols** — ECMAScript-defined symbols

## Related
- **symbol-descriptions** — debugging descriptions
- **converting-symbols** — conversion rules

## Contrasts With
- None

# Common Errors

- **Error**: Using `new Symbol()` to create a symbol
  **Correction**: `Symbol()` is a factory function, not a constructor. `new Symbol()` throws `TypeError`.

# Common Confusions

- **Confusion**: Thinking symbols with the same description are equal
  **Clarification**: `Symbol('foo') === Symbol('foo')` is `false`. The description is only for debugging.

# Source Reference

Chapter 24: Symbols, Section 24.1, lines 34-103.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with identity comparison examples
- Cross-reference status: verified
