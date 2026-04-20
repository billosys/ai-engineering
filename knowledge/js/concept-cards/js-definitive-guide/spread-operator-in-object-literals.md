---
# === CORE IDENTIFICATION ===
concept: Spread Operator in Object Literals
slug: spread-operator-in-object-literals

# === CLASSIFICATION ===
category: objects
subcategory: extended-literal-syntax
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 165
section: "6.10.4 Spread Operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "object spread"
  - "... in object literals"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-literals
  - own-vs-inherited-properties
extends:
  - object-literals
related:
  - object-assign
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes shallow copy from deep copy of objects?"
---

# Quick Definition

The spread operator `...` in object literals (ES2018) copies the own properties of an existing object into a new object literal. Later properties override earlier ones with the same name.

# Core Definition

"In ES2018 and later, you can copy the properties of an existing object into a new object using the 'spread operator' ... inside an object literal." It "only spreads the own properties of an object, not any inherited ones." It is not a true operator — "it is a special-case syntax available only within object literals." (Ch. 6, §6.10.4)

# Prerequisites

- **object-literals** — Spread extends object literal syntax.
- **own-vs-inherited-properties** — Only own properties are spread.

# Key Properties

1. Only spreads own properties, not inherited ones.
2. Later properties override earlier ones: `{...o, x: 2}` overrides `o.x` with `2`.
3. Not a true operator — special syntax only available in object literals.
4. Spreading `n` properties is O(n) — using `...` in loops can create O(n^2) algorithms.
5. Equivalent to `Object.assign({}, obj)` for copying.

# Construction / Recognition

```js
let copy = { ...original };
let merged = { ...defaults, ...overrides };
```

# Context & Application

Object spread is used for shallow copying, merging objects, and the defaults-with-overrides pattern. It is more concise than `Object.assign()`.

# Examples

From the source text (§6.10.4, pp. 165-166):

```js
let position = { x: 0, y: 0 };
let dimensions = { width: 100, height: 75 };
let rect = { ...position, ...dimensions };
rect.x + rect.y + rect.width + rect.height  // => 175

// Override behavior
let o = { x: 1 };
let p = { x: 0, ...o };
p.x   // => 1: value from o overrides initial value
let q = { ...o, x: 2 };
q.x   // => 2: the value 2 overrides the value from o

// Does NOT spread inherited properties
let o = Object.create({x: 1});
let p = { ...o };
p.x   // => undefined
```

# Relationships

## Builds Upon
- **object-literals** — Extends literal syntax
- **own-vs-inherited-properties** — Only own properties spread

## Enables
- Concise shallow copy and merge patterns

## Related
- **object-assign** — `Object.assign({}, obj)` achieves the same result

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `...` in a loop to accumulate into a large object.
  **Correction**: This creates an O(n^2) algorithm. Use `Object.assign()` or mutation for accumulation.

# Common Confusions

- **Confusion**: Expecting spread to copy inherited properties.
  **Clarification**: Spread only copies own properties. `Object.create({x:1})` spread produces `{}`.

# Source Reference

Chapter 6: Objects, Section 6.10.4, pages 165-166.

# Verification Notes

- Definition source: Direct quote from §6.10.4
- Confidence rationale: High — clear with override and inheritance examples
- Uncertainties: None
- Cross-reference status: Verified
