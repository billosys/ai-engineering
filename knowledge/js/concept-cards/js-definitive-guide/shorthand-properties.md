---
# === CORE IDENTIFICATION ===
concept: Shorthand Properties
slug: shorthand-properties

# === CLASSIFICATION ===
category: objects
subcategory: extended-literal-syntax
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 163
section: "6.10.1 Shorthand Properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "property value shorthand"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-literals
extends:
  - object-literals
related:
  - computed-property-names
  - shorthand-methods
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

In ES6+, when a property name matches a variable name, you can omit the colon and value: `{x, y}` is equivalent to `{x: x, y: y}`.

# Core Definition

"In ES6 and later, you can drop the colon and one copy of the identifier and end up with much simpler code." When variable names match desired property names, the shorthand `{ x, y }` creates properties named `x` and `y` with the values of the variables `x` and `y`. (Ch. 6, §6.10.1)

# Prerequisites

- **object-literals** — Shorthand properties extend object literal syntax.

# Key Properties

1. `{x, y}` is equivalent to `{x: x, y: y}`.
2. Only works when the variable name matches the desired property name.
3. Can be mixed with regular name:value pairs.

# Construction / Recognition

```js
let x = 1, y = 2;
let o = { x, y };   // Same as { x: x, y: y }
o.x + o.y           // => 3
```

# Context & Application

Shorthand properties reduce boilerplate when constructing objects from variables, which is extremely common in function return values and module exports.

# Examples

From the source text (§6.10.1, pp. 163-164):

```js
// Without shorthand:
let x = 1, y = 2;
let o = { x: x, y: y };

// With shorthand (ES6):
let o = { x, y };
o.x + o.y   // => 3
```

# Relationships

## Builds Upon
- **object-literals** — Extends basic object literal syntax

## Enables
- Concise object construction from variables

## Related
- **computed-property-names** — Another ES6 literal extension
- **shorthand-methods** — Another ES6 literal extension

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using shorthand when the variable is not defined.
  **Correction**: The variable must be in scope. `{ x }` requires a variable `x` to exist.

# Common Confusions

- **Confusion**: None significant.
  **Clarification**: Shorthand is purely syntactic sugar — no semantic difference from the explicit form.

# Source Reference

Chapter 6: Objects, Section 6.10.1, pages 163-164.

# Verification Notes

- Definition source: Direct quote from §6.10.1
- Confidence rationale: High — simple, clearly defined
- Uncertainties: None
- Cross-reference status: Verified
