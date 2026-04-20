---
# === CORE IDENTIFICATION ===
concept: Object.getOwnPropertyNames()
slug: object-get-own-property-names

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
section: "13.1.2 Operations that consider both enumerable and non-enumerable properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "getOwnPropertyNames"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
  - property-key
extends: []
related:
  - object-get-own-property-symbols
  - reflect-own-keys
contrasts_with:
  - object-keys

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from Reflect.ownKeys()?"
---

# Quick Definition

`Object.getOwnPropertyNames(obj)` returns an array of all own string-keyed property keys, regardless of enumerability. It includes non-enumerable properties but excludes symbol-keyed properties.

# Core Definition

As described in "Deep JavaScript" Ch 13, "`Object.getOwnPropertyNames()` [ES5] lists the keys of all own string-keyed properties." Its long name follows the naming convention: "operations that don't [ignore non-enumerable] have long names."

# Prerequisites

- **Enumerability** — this operation ignores enumerability
- **Property Key** — returns only string keys

# Key Properties

1. Returns all own string keys (enumerable + non-enumerable)
2. Does not include symbol keys
3. Own properties only
4. Introduced in ES5
5. Long name signals it includes non-enumerable properties

# Construction / Recognition

## To Construct/Create:
1. `Object.getOwnPropertyNames(obj)`

## To Identify/Recognize:
1. Returns an array of strings including non-enumerable own keys

# Context & Application

Useful when you need to see all string-keyed properties including non-enumerable ones, but not symbol-keyed properties.

# Examples

**Example 1** (Ch 13):
```js
> Object.getOwnPropertyNames(obj)
[ 'objEnumStringKey', 'objNonEnumStringKey' ]
```

# Relationships

## Builds Upon
- **enumerability** — ignores this attribute
- **property-key** — returns only string keys

## Enables
- Complete string-key introspection

## Related
- **object-get-own-property-symbols** — the symbol-key counterpart
- **reflect-own-keys** — returns both string + symbol keys

## Contrasts With
- **object-keys** — only enumerable string keys

# Common Errors

- **Error**: Expecting symbol-keyed properties to be included.
  **Correction**: Use `Object.getOwnPropertySymbols()` for symbol keys or `Reflect.ownKeys()` for both.

# Common Confusions

- **Confusion**: Thinking the long method name is just verbose.
  **Clarification**: The naming convention is intentional — long names signal that the operation includes non-enumerable properties.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.2, lines 209-215. Section 13.1.3, lines 283-285.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in the operations table.
- Cross-reference status: verified
