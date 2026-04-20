---
# === CORE IDENTIFICATION ===
concept: Computed Property Names
slug: computed-property-names

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
pdf_page: 164
section: "6.10.2 Computed Property Names"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "dynamic property names"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-literals
  - property-access-expressions
extends:
  - object-literals
related:
  - symbols-as-property-names
  - shorthand-properties
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

ES6 computed property names allow using arbitrary expressions as property names in object literals by enclosing the expression in square brackets: `{ [expression]: value }`.

# Core Definition

"It is much simpler to set up an object like this with an ES6 feature known as *computed properties* that lets you take the square brackets from the preceding code and move them directly into the object literal... the square brackets delimit an arbitrary JavaScript expression. That expression is evaluated, and the resulting value (converted to a string, if necessary) is used as the property name." (Ch. 6, §6.10.2)

# Prerequisites

- **object-literals** — Computed names extend object literal syntax.
- **property-access-expressions** — Bracket notation is the same concept applied to literals.

# Key Properties

1. Expression is evaluated at object creation time.
2. Result is converted to a string (if necessary) and used as property name.
3. Enables using constants, function return values, or Symbol values as property names.
4. Can be combined with shorthand methods.

# Construction / Recognition

```js
const NAME = "p1";
let o = {
    [NAME]: 1,
    [computePropertyName()]: 2
};
```

# Context & Application

Computed properties are useful when property names come from constants, library values, or Symbol-based protocols. They eliminate the need to create an object and add properties in separate steps.

# Examples

From the source text (§6.10.2, pp. 164-165):

```js
const PROPERTY_NAME = "p1";
function computePropertyName() { return "p" + 2; }

// Without computed properties (pre-ES6):
let o = {};
o[PROPERTY_NAME] = 1;
o[computePropertyName()] = 2;

// With computed properties (ES6):
let p = {
    [PROPERTY_NAME]: 1,
    [computePropertyName()]: 2
};
p.p1 + p.p2   // => 3
```

# Relationships

## Builds Upon
- **object-literals** — Extends literal syntax
- **property-access-expressions** — Same bracket notation concept

## Enables
- **symbols-as-property-names** — Symbols as property names require computed syntax

## Related
- **shorthand-properties** — Another ES6 literal extension

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Forgetting that the expression result is converted to a string.
  **Correction**: If the expression yields a non-string, non-Symbol value, it is converted to a string.

# Common Confusions

- **Confusion**: None significant.
  **Clarification**: Computed property names are purely syntactic sugar for creating objects with dynamic keys.

# Source Reference

Chapter 6: Objects, Section 6.10.2, pages 164-165.

# Verification Notes

- Definition source: Direct quote from §6.10.2
- Confidence rationale: High — clear examples
- Uncertainties: None
- Cross-reference status: Verified
