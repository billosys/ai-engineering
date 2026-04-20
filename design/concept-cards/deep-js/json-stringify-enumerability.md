---
# === CORE IDENTIFICATION ===
concept: JSON.stringify() and Enumerability
slug: json-stringify-enumerability

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
section: "13.3.4 Hiding own properties from JSON.stringify()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
extends: []
related:
  - object-keys
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
---

# Quick Definition

`JSON.stringify()` only includes enumerable own properties with string keys in its output. Non-enumerable properties and symbol-keyed properties are excluded from serialization.

# Core Definition

As described in "Deep JavaScript" Ch 13, "`JSON.stringify()` [ES5] only stringifies enumerable own properties with string keys." The book also notes an alternative to enumerability for controlling serialization: "an object can implement the method `.toJSON()` and `JSON.stringify()` stringifies whatever that method returns, instead of the object itself."

# Prerequisites

- **Enumerability** — determines which properties are serialized

# Key Properties

1. Only serializes enumerable own string-keyed properties
2. Non-enumerable properties are excluded
3. Symbol-keyed properties are excluded
4. Inherited properties are excluded
5. Alternative control mechanism: `.toJSON()` method

# Construction / Recognition

## To Construct/Create:
1. `JSON.stringify(obj)` — serializes enumerable own string-keyed properties

## To Identify/Recognize:
1. JSON output missing certain properties may be due to enumerability

# Context & Application

Making properties non-enumerable is one way to exclude them from JSON serialization, but the `.toJSON()` method provides a cleaner alternative with more control.

# Examples

**Example 1** (Ch 13):
```js
> JSON.stringify(obj)
'{"objEnumStringKey":"objEnumStringKeyValue"}'
```

**Example 2** (Ch 13): Using `.toJSON()` as alternative:
```js
class Point {
  constructor(x, y) { this.x = x; this.y = y; }
  toJSON() { return [this.x, this.y]; }
}
assert.equal(
  JSON.stringify(new Point(8, -3)),
  '[8,-3]');
```

# Relationships

## Builds Upon
- **enumerability** — controls which properties are serialized

## Enables
- Control over JSON serialization output

## Related
- **object-keys** — similar enumerability filtering

## Contrasts With
- None

# Common Errors

- **Error**: Expecting symbol-keyed properties to appear in JSON output.
  **Correction**: `JSON.stringify()` only processes string keys.

# Common Confusions

- **Confusion**: Thinking non-enumerability is the best way to control JSON output.
  **Clarification**: The `.toJSON()` method is a cleaner alternative that gives full control over the serialization format.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.1, lines 165-171. Section 13.3.4, lines 665-702.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in operations table with alternative approach.
- Cross-reference status: verified
