---
# === CORE IDENTIFICATION ===
concept: Property Enumeration Order
slug: property-enumeration-order

# === CLASSIFICATION ===
category: objects
subcategory: property-operations
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 158
section: "6.6.1 Property Enumeration Order"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerating-properties
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from for/in?"
---

# Quick Definition

ES6 formally defines property enumeration order: non-negative integer string names first (in numeric order), then other string names in insertion order, then Symbol names in insertion order.

# Core Definition

"ES6 formally defines the order in which the own properties of an object are enumerated." Properties are listed: "String properties whose names are non-negative integers are listed first, in numeric order from smallest to largest... all remaining properties with string names are listed in the order in which they were added to the object... properties whose names are Symbol objects are listed in the order in which they were added." (Ch. 6, §6.6.1)

# Prerequisites

- **enumerating-properties** — Order rules apply to all enumeration methods.

# Key Properties

1. Integer-indexed string properties come first, in ascending numeric order.
2. Other string properties follow, in insertion order.
3. Symbol properties come last, in insertion order.
4. `for/in` order is less tightly specified but implementations typically follow the same rules, traveling up the prototype chain.
5. A property already enumerated (or non-enumerable with the same name) is not re-enumerated.

# Construction / Recognition

The order is deterministic and consistent across `Object.keys()`, `Object.getOwnPropertyNames()`, `Object.getOwnPropertySymbols()`, `Reflect.ownKeys()`, and `JSON.stringify()`.

# Context & Application

Understanding enumeration order matters when object property order is significant, such as when serializing to JSON or when relying on property iteration order in algorithms.

# Examples

From the source text (§6.6.1, pp. 158-159):

```js
// Integer-like keys are enumerated first in numeric order
let o = { b: 2, a: 1, 2: "two", 1: "one" };
Object.keys(o)  // => ["1", "2", "b", "a"]
// "1" and "2" come first (numeric order), then "b" and "a" (insertion order)
```

# Relationships

## Builds Upon
- **enumerating-properties** — Order rules apply to enumeration methods

## Enables
- Predictable iteration behavior for algorithms that depend on order

## Related
- No additional related concepts

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Assuming properties are always enumerated in insertion order.
  **Correction**: Integer-like string keys are sorted numerically first, before other string keys.

# Common Confusions

- **Confusion**: Believing `for/in` has the same strictly defined order as `Object.keys()`.
  **Clarification**: `for/in` order is less tightly specified by the standard, though implementations typically follow the same rules.

# Source Reference

Chapter 6: Objects, Section 6.6.1, pages 158-159.

# Verification Notes

- Definition source: Direct quote from §6.6.1
- Confidence rationale: High — formal order clearly specified
- Uncertainties: None
- Cross-reference status: Verified
