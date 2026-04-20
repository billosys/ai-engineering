---
# === CORE IDENTIFICATION ===
concept: for-in Loop
slug: for-in-loop

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
section: "13.3.1 Use case: Hiding properties from the for-in loop"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "for...in"
  - "for-in iteration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
  - enumerable-attribute
extends: []
related:
  - object-keys
contrasts_with:
  - reflect-own-keys

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
---

# Quick Definition

The `for-in` loop traverses all enumerable string-keyed properties of an object, both own and inherited. It is the only built-in operation where enumerability of inherited properties matters.

# Core Definition

As described in "Deep JavaScript" Ch 13, "`for-in` loop [ES1] traverses the keys of own and inherited enumerable string-keyed properties." It is "the only built-in operation where enumerability matters for inherited properties. All other operations only work with own properties."

The reason enumerability was introduced in ECMAScript 1 was "to hide properties that should not be traversed" from `for-in`.

# Prerequisites

- **Enumerability** — `for-in` only sees enumerable properties
- **Enumerable Attribute** — the attribute that controls visibility

# Key Properties

1. Traverses enumerable string-keyed properties
2. Includes both own AND inherited properties (unique among operations)
3. Does not include symbol-keyed properties
4. Was the original motivation for the enumerable attribute
5. Generally should be avoided in favor of `Object.keys()` + `for-of`

# Construction / Recognition

## To Construct/Create:
1. `for (const key in obj) { ... }`

## To Identify/Recognize:
1. The `in` keyword in a `for` loop header

# Context & Application

The book advises against using `for-in` in most cases. For objects, it includes inherited properties which is usually undesired. For arrays, it iterates over all enumerable properties (not just indices). Better alternatives: `Object.keys()` for objects, `for-of` for arrays.

# Examples

**Example 1** (Ch 13):
```js
const propKeys = [];
for (const propKey in obj) {
  propKeys.push(propKey);
}
assert.deepEqual(
  propKeys, ['objEnumStringKey', 'protoEnumStringKey']);
```

**Example 2** (Ch 13): Problem with arrays:
```js
const arr = ['a', 'b'];
arr.nonIndexProp = 'yes';
// for-in sees index properties AND non-index properties:
// ['0', '1', 'nonIndexProp']
```

# Relationships

## Builds Upon
- **enumerability** — only iterates enumerable properties
- **enumerable-attribute** — the gating attribute

## Enables
- Understanding why prototype methods are non-enumerable

## Related
- **object-keys** — the recommended alternative

## Contrasts With
- **reflect-own-keys** — sees all own keys regardless of enumerability

# Common Errors

- **Error**: Using `for-in` to iterate array indices.
  **Correction**: Use `for-of` for array elements or `array.keys()` for indices. `for-in` can include non-index properties.

# Common Confusions

- **Confusion**: Thinking `for-in` only iterates own properties.
  **Clarification**: `for-in` iterates both own and inherited enumerable string-keyed properties. Use `Object.keys()` for own-only.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.1 (line 113), Section 13.3.1, lines 372-491.

# Verification Notes

- Definition source: direct
- Confidence rationale: Extensively covered with caveats and alternatives.
- Cross-reference status: verified
