---
# === CORE IDENTIFICATION ===
concept: Object.assign() and Enumerability
slug: object-assign-enumerability

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
section: "13.3.2.4 Object.assign()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Object.assign() enumerability"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
  - property-assignment
extends: []
related:
  - object-keys
  - spreading-enumerability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
---

# Quick Definition

`Object.assign()` only copies enumerable own properties (both string and symbol keys) from source objects to the target. It uses "get" to read from sources and "set" (assignment) to write to the target.

# Core Definition

As described in "Deep JavaScript" Ch 13, "`Object.assign()` [ES6] only copies enumerable own properties (with either string keys or symbol keys)." It "uses a 'get' operation to read a value from a source and a 'set' operation to write a value to the target." The book quotes Yehuda Katz: "`Object.assign` would pave the cowpath of all of the `extend()` APIs already in circulation."

`Object.assign()` was designed as an upgrade path from jQuery's `$.extend()` and Prototype's `Object.extend()`, inheriting their convention of skipping non-enumerable properties.

# Prerequisites

- **Enumerability** — determines which properties are copied
- **Property Assignment** — `Object.assign()` uses assignment to write

# Key Properties

1. Only copies enumerable own properties
2. Copies both string and symbol keys
3. Uses get to read (invokes getters on sources)
4. Uses set/assignment to write (invokes setters on target, creates all-true attributes)
5. Converts accessor properties to data properties during copy
6. Does NOT copy inherited properties

# Construction / Recognition

## To Construct/Create:
1. `Object.assign(target, source1, source2, ...)`

## To Identify/Recognize:
1. Copies properties from sources to target

# Context & Application

`Object.assign()` is commonly used for merging objects, but its use of get/set means it cannot faithfully copy accessor properties. For faithful copying, use `Object.defineProperties(target, Object.getOwnPropertyDescriptors(source))`.

# Examples

**Example 1** (Ch 13):
```js
const copy = Object.assign({}, obj);
// Only own enumerable properties (string + symbol) were copied
Reflect.ownKeys(copy); // [ 'objEnumStringKey', objEnumSymbolKey ]
```

# Relationships

## Builds Upon
- **enumerability** — determines which properties are copied
- **property-assignment** — `Object.assign()` uses assignment semantics for writing

## Enables
- Object merging with enumerability filtering

## Related
- **object-keys** — similar filtering behavior
- **spreading-enumerability** — similar behavior with spread syntax

## Contrasts With
- None

# Common Errors

- **Error**: Using `Object.assign()` to copy accessor properties.
  **Correction**: `Object.assign()` reads getters and writes data properties. Use `Object.defineProperties()` + `Object.getOwnPropertyDescriptors()` for faithful copies.

# Common Confusions

- **Confusion**: Thinking `Object.assign()` preserves property descriptors.
  **Clarification**: It always creates data properties with `writable: true, enumerable: true, configurable: true` on the target.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.1, lines 156-163. Section 13.3.2.4, lines 590-612.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly described with historical context and Yehuda Katz quote.
- Cross-reference status: verified against Ch 10 (use cases)
