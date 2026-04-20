---
# === CORE IDENTIFICATION ===
concept: Spreading and Enumerability
slug: spreading-enumerability

# === CLASSIFICATION ===
category: object-model
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Enumerability of properties"
chapter_number: 13
section: "13.1.1 Operations that only consider enumerable properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "object spread"
  - "{...x}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
extends: []
related:
  - object-assign-enumerability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
---

# Quick Definition

Spreading into object literals (`{...x}`) only copies own enumerable properties, including both string and symbol keys. Non-enumerable and inherited properties are excluded.

# Core Definition

As described in "Deep JavaScript" Ch 13, "Spreading into object literals [ES2018] only considers own enumerable properties (with string keys or symbol keys)."

# Prerequisites

- **Enumerability** — determines which properties are spread

# Key Properties

1. Only copies own enumerable properties
2. Includes both string and symbol keys
3. Does not include inherited properties
4. Similar behavior to `Object.assign()`
5. Introduced in ES2018

# Construction / Recognition

## To Construct/Create:
1. `const copy = {...obj}`

## To Identify/Recognize:
1. The `...` syntax inside object literals

# Context & Application

Object spreading is a concise syntax for shallow copying objects, following the same enumerability rules as `Object.assign()`.

# Examples

**Example 1** (Ch 13):
```js
const copy = {...obj};
Reflect.ownKeys(copy); // [ 'objEnumStringKey', objEnumSymbolKey ]
```

# Relationships

## Builds Upon
- **enumerability** — filters by enumerable attribute

## Enables
- Concise object copying

## Related
- **object-assign-enumerability** — similar behavior

## Contrasts With
- None

# Common Errors

- **Error**: Expecting spreading to copy non-enumerable properties.
  **Correction**: Only enumerable own properties are spread.

# Common Confusions

- **Confusion**: Thinking spreading copies accessor properties faithfully.
  **Clarification**: Like `Object.assign()`, spreading reads getters and writes data properties.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.1, lines 147-154.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in the operations table.
- Cross-reference status: verified
