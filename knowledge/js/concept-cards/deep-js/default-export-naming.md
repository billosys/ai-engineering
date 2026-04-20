---
# === CORE IDENTIFICATION ===
concept: Default Export Naming
slug: default-export-naming

# === CLASSIFICATION ===
category: functions
subcategory: naming
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The property .name of functions (bonus)"
chapter_number: 21
section: "21.2.9 Default exports and anonymous constructs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
extends: []
related:
  - function-naming-rules
  - anonymous-function-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

Anonymous functions and classes used as default exports get the `.name` value `'default'`.

# Core Definition

From "Deep JavaScript" (Ch 21.2.9): "All of the following statements set `.name` to `'default'`:" including anonymous function expressions, anonymous class expressions, and arrow functions used as default exports.

# Prerequisites

- **Function .name property** — Default exports have specific naming behavior

# Key Properties

1. Applies to anonymous function expressions, class expressions, and arrow functions
2. Only when used directly as default exports
3. The name is the string `'default'`

# Construction / Recognition

## To Construct/Create:
1. `export default function () {}`
2. `export default (function () {});`
3. `export default class {}`
4. `export default () => {};`

## To Identify/Recognize:
1. `.name === 'default'`

# Context & Application

This ensures that even unnamed default exports have a discoverable name for debugging purposes.

# Examples

**Example 1** (Ch 21):
```js
// All of these set .name to 'default':
export default function () {}
export default (function () {});
export default class {}
export default (class {});
export default () => {};
```

# Relationships

## Builds Upon
- **Function .name property** — A specific naming context

## Related
- **Anonymous function expression** — Default exports name otherwise-anonymous functions

# Common Confusions

- **Confusion**: Default-exported named functions also get the name `'default'`
  **Clarification**: Only anonymous constructs get `'default'`; named constructs keep their explicit name

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.2.9, lines 11437+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: All patterns explicitly listed
- Cross-reference status: verified
