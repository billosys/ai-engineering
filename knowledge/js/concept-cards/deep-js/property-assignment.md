---
# === CORE IDENTIFICATION ===
concept: Property Assignment
slug: property-assignment

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
section: "12.1.1 Assignment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "assignment"
  - "property write"
  - "obj.prop = value"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-attributes
  - data-property
  - accessor-property
  - prototype-internal-slot
extends: []
related:
  - assignment-calls-setters
  - inherited-read-only-prevents-assignment
contrasts_with:
  - property-definition

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does property assignment differ from property definition?"
  - "What must I understand before learning about property assignment vs. definition?"
---

# Quick Definition

Property assignment uses the `=` operator (`obj.prop = value`) to create or change properties. Its behavior depends on the existing property landscape: it changes own data properties, invokes inherited setters, or creates new own data properties.

# Core Definition

As described in "Deep JavaScript" Ch 12, assignment via `obj.prop = value` "works differently depending on what `.prop` looks like:
- Changing properties: If there is an own data property `.prop`, assignment changes its value to `value`.
- Invoking setters: If there is an own or inherited setter for `.prop`, assignment invokes that setter.
- Creating properties: If there is no own data property `.prop` and no own or inherited setter for it, assignment creates a new own data property."

"The main purpose of assignment is making changes. That's why it supports setters."

# Prerequisites

- **Property Attributes** — assignment creates properties with specific attribute values
- **Data Property** — assignment changes or creates data properties
- **Accessor Property** — assignment invokes setters
- **[[Prototype]] Internal Slot** — assignment traverses the prototype chain

# Key Properties

1. Uses the `=` operator
2. Creates new own data properties with `writable: true, enumerable: true, configurable: true`
3. Invokes inherited setters (does not bypass them)
4. Does not change properties in prototypes (creates own property instead)
5. Blocked by inherited non-writable properties
6. Main purpose: making changes

# Construction / Recognition

## To Construct/Create:
1. `obj.prop = value` — standard assignment
2. `[obj.prop] = [value]` — destructuring assignment

## To Identify/Recognize:
1. Uses `=` operator with a property access on the left side

# Context & Application

Assignment is the most common way to create and change properties in everyday JavaScript. Understanding its three-case behavior is critical for understanding prototype-based inheritance and the distinction from definition.

# Examples

**Example 1** (Ch 12): Assignment does not change prototype properties:
```js
const proto = { prop: 'a' };
const obj = Object.create(proto);
obj.prop = 'b';
assert.equal(obj.prop, 'b');       // Own property created
assert.equal(proto.prop, 'a');      // Prototype unchanged
assert.deepEqual(Object.keys(obj), ['prop']);
```

# Relationships

## Builds Upon
- **property-attributes** — assignment creates properties with all-true boolean attributes
- **prototype-internal-slot** — assignment traverses the prototype chain

## Enables
- **assignment-calls-setters** — key behavior of assignment
- **inherited-read-only-prevents-assignment** — a pitfall of assignment

## Related
- **property-assignment-operator-semantics** — the `=` operator always uses assignment

## Contrasts With
- **property-definition** — definition ignores setters and can set arbitrary attributes

# Common Errors

- **Error**: Expecting assignment to change a property in a prototype object.
  **Correction**: Assignment creates a new own property on the target object, shadowing the prototype property.

# Common Confusions

- **Confusion**: Thinking assignment and definition are the same thing.
  **Clarification**: Assignment invokes setters and creates properties with all-true attributes; definition ignores setters and defaults to all-false attributes.

# Source Reference

Chapter 12: Properties: assignment vs. definition, Section 12.1.1, lines 69-93.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with three-case breakdown.
- Cross-reference status: verified
