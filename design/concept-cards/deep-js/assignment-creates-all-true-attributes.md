---
# === CORE IDENTIFICATION ===
concept: Assignment Creates All-True Attributes
slug: assignment-creates-all-true-attributes

# === CLASSIFICATION ===
category: object-model
subcategory: assignment
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Properties: assignment vs. definition"
chapter_number: 12
section: "12.3.1 Only definition allows us to create a property with arbitrary attributes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-assignment
  - property-attributes
extends: []
related:
  - property-definition
  - descriptor-defaults-on-creation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does property assignment differ from property definition?"
---

# Quick Definition

When assignment creates a new own property, it always sets `writable`, `enumerable`, and `configurable` to `true`. There is no way to create a property with different attributes using assignment alone.

# Core Definition

As described in "Deep JavaScript" Ch 12, "If we create an own property via assignment, it always creates properties whose attributes `writable`, `enumerable`, and `configurable` are all `true`." "Therefore, if we want to specify arbitrary attributes, we must use definition. And while we can create getters and setters inside object literals, we can't add them later via assignment. Here, too, we need definition."

# Prerequisites

- **Property Assignment** — describes a specific behavior of assignment
- **Property Attributes** — the attributes that are set

# Key Properties

1. New properties created by assignment always have: `writable: true, enumerable: true, configurable: true`
2. Cannot create non-enumerable properties via assignment
3. Cannot create non-writable properties via assignment
4. Cannot create accessor properties via assignment (only data properties)
5. Definition is required for any other attribute combination

# Construction / Recognition

## To Construct/Create:
1. `obj.prop = 'abc'` — creates with all-true attributes

## To Identify/Recognize:
1. Any property created by the `=` operator will have all-true boolean attributes

# Context & Application

This explains why most own properties in everyday code are enumerable, writable, and configurable — they are created via assignment. When non-default attributes are needed, `Object.defineProperty()` must be used.

# Examples

**Example 1** (Ch 12):
```js
const obj = {};
obj.dataProp = 'abc';
assert.deepEqual(
  Object.getOwnPropertyDescriptor(obj, 'dataProp'),
  {
    value: 'abc',
    writable: true,
    enumerable: true,
    configurable: true,
  });
```

# Relationships

## Builds Upon
- **property-assignment** — this is a constraint of assignment
- **property-attributes** — the attributes that are always set to `true`

## Enables
- Understanding why definition is necessary for non-default attributes

## Related
- **property-definition** — the alternative that allows arbitrary attributes
- **descriptor-defaults-on-creation** — definition defaults to all-false, opposite of assignment

## Contrasts With
- None

# Common Errors

- **Error**: Trying to create a non-enumerable property via assignment.
  **Correction**: Use `Object.defineProperty(obj, 'prop', { value: v, enumerable: false })`.

# Common Confusions

- **Confusion**: Thinking definition defaults are the same as assignment defaults.
  **Clarification**: Assignment defaults all boolean attributes to `true`; definition defaults to `false`.

# Source Reference

Chapter 12: Properties: assignment vs. definition, Section 12.3.1, lines 362-387.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly stated with example.
- Cross-reference status: verified
