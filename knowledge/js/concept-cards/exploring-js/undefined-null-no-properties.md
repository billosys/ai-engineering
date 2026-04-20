---
# === CORE IDENTIFICATION ===
concept: Undefined and Null Have No Properties
slug: undefined-null-no-properties

# === CLASSIFICATION ===
category: primitive-types
subcategory: non-values
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The non-values undefined and null"
chapter_number: 16
pdf_page: null
section: "undefined and null don't have properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - undefined-value
  - null-value
extends: []
related:
  - optional-chaining
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is `undefined` and how does it differ from `null`?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

`undefined` and `null` are the only two JavaScript values that throw a `TypeError` when you attempt to read a property from them.

# Core Definition

"undefined and null are the only two JavaScript values where we get an exception if we try to read a property." All other values, including other primitives like `true` and `{}`, return `undefined` for missing properties rather than throwing (Ch. 16, Section 16.5).

# Prerequisites

- **undefined-value** -- one of the two propertyless values
- **null-value** -- one of the two propertyless values

# Key Properties

1. `undefined.prop` throws `TypeError: Cannot read properties of undefined`
2. `null.prop` throws `TypeError: Cannot read properties of null`
3. All other values (including `true`, `{}`, `0`) silently return `undefined` for missing properties

# Construction / Recognition

```js
> getProp(undefined)
TypeError: Cannot read properties of undefined (reading 'prop')
> getProp(null)
TypeError: Cannot read properties of null (reading 'prop')
> getProp(true)
undefined
> getProp({})
undefined
```

# Context & Application

This is one of the most common runtime errors in JavaScript. Optional chaining (`?.`) was introduced to safely access properties that might be on `undefined` or `null`.

# Examples

From the source text:

```js
function getProp(x) {
  return x.prop;
}
> getProp(undefined)
TypeError: Cannot read properties of undefined (reading 'prop')
> getProp(null)
TypeError: Cannot read properties of null (reading 'prop')
> getProp(true)
undefined
> getProp({})
undefined
```

# Relationships

## Builds Upon
- **undefined-value** — one of the propertyless values
- **null-value** — one of the propertyless values

## Enables
- Understanding why optional chaining (`?.`) exists

## Related
- **optional-chaining** — safe property access for potentially nullish values

## Contrasts With
- None

# Common Errors

- **Error**: Accessing nested properties without null checks: `obj.a.b.c`
  **Correction**: Use optional chaining: `obj?.a?.b?.c`

# Common Confusions

- **Confusion**: Thinking all primitives throw when accessing properties
  **Clarification**: Only `undefined` and `null` throw. Other primitives silently return `undefined` for missing properties (they are temporarily wrapped in objects).

# Source Reference

Chapter 16: The non-values undefined and null, Section 16.5, lines 449-478.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit statement with clear examples
- Cross-reference status: verified
