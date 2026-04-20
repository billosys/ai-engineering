---
# === CORE IDENTIFICATION ===
concept: Property Definition
slug: property-definition

# === CLASSIFICATION ===
category: object-model
subcategory: definition
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Properties: assignment vs. definition"
chapter_number: 12
section: "12.1.2 Definition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "definition"
  - "defining a property"
  - "Object.defineProperty semantics"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-descriptor
  - property-attributes
  - object-define-property
extends: []
related: []
contrasts_with:
  - property-assignment

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does property assignment differ from property definition?"
  - "How do I define a property with specific attributes using Object.defineProperty()?"
---

# Quick Definition

Property definition uses `Object.defineProperty()` to create or change an own property with explicitly specified attributes. It ignores inherited setters and can set arbitrary property attributes.

# Core Definition

As described in "Deep JavaScript" Ch 12, definition via `Object.defineProperty(obj, propKey, propDesc)` "works differently depending on what the property looks like:
- Changing properties: If an own property with key `propKey` exists, defining changes its property attributes as specified by the property descriptor `propDesc` (if possible).
- Creating properties: Otherwise, defining creates an own property with the attributes specified by `propDesc` (if possible)."

"The main purpose of definition is to create an own property (even if there is an inherited setter, which it ignores) and to change property attributes."

# Prerequisites

- **Property Descriptor** — definition operates via descriptors
- **Property Attributes** — definition explicitly sets attributes
- **Object.defineProperty()** — the primary method for definition

# Key Properties

1. Creates or changes OWN properties only
2. Ignores inherited setters entirely
3. Can set arbitrary attributes (writable, enumerable, configurable)
4. When creating: omitted boolean attributes default to `false`
5. When changing: omitted attributes leave current values unchanged
6. Validates changes against `configurable` attribute
7. Main purpose: creating own properties and changing attributes

# Construction / Recognition

## To Construct/Create:
1. `Object.defineProperty(obj, 'prop', { value: 42 })`
2. `Object.defineProperties(obj, { prop: { value: 42 } })`

## To Identify/Recognize:
1. Uses `Object.defineProperty()` or `Object.defineProperties()`
2. Object literal properties also use definition semantics
3. Public class fields use definition semantics

# Context & Application

Definition is used when you need to: create properties with specific attributes (especially non-default ones), bypass inherited setters, convert between data and accessor properties, or change property attributes.

# Examples

**Example 1** (Ch 12): Definition ignores inherited setters:
```js
let setterWasCalled = false;
const proto = {
  get prop() { return 'protoGetter'; },
  set prop(x) { setterWasCalled = true; },
};
const obj = Object.create(proto);
Object.defineProperty(obj, 'prop', { value: 'objData' });
assert.equal(setterWasCalled, false);
assert.equal(obj.prop, 'objData');
```

# Relationships

## Builds Upon
- **property-descriptor** — definition operates via descriptors
- **object-define-property** — the primary method

## Enables
- Creating properties with non-default attributes
- Overriding inherited accessors with own data properties

## Related
- None

## Contrasts With
- **property-assignment** — assignment invokes setters and creates all-true-attribute properties

# Common Errors

- **Error**: Using definition when you intend to trigger a setter.
  **Correction**: Definition ignores setters. Use assignment (`=`) to trigger setters.

# Common Confusions

- **Confusion**: Thinking object literal properties use assignment.
  **Clarification**: Object literal properties use definition (they do not trigger inherited setters). Only the `=` operator uses assignment.

# Source Reference

Chapter 12: Properties: assignment vs. definition, Section 12.1.2, lines 95-117.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with two-case breakdown.
- Cross-reference status: verified
