---
# === CORE IDENTIFICATION ===
concept: Prototype Chain and Assignment
slug: prototype-chain-and-assignment

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
section: "12.3.2 The assignment operator does not change properties in prototypes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "property shadowing"
  - "overriding inherited properties"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-assignment
  - prototype-internal-slot
extends: []
related:
  - inherited-read-only-prevents-assignment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does property assignment differ from property definition?"
---

# Quick Definition

The assignment operator never modifies properties in prototypes. When assigning to a property that exists only in a prototype, assignment creates a new own property on the target object, shadowing the prototype property.

# Core Definition

As described in "Deep JavaScript" Ch 12, "We can't (destructively) change `proto.prop` by assigning to `obj.prop`. Doing so creates a new own property." The rationale: "Prototypes can have properties whose values are shared by all of their descendants. If we want to change such a property in only one descendant, we must do so non-destructively, via overriding. Then the change does not affect the other descendants."

# Prerequisites

- **Property Assignment** — this describes assignment's behavior with prototypes
- **[[Prototype]] Internal Slot** — the prototype chain is central

# Key Properties

1. Assignment never modifies a property in a prototype
2. Instead, it creates a new own property on the target object
3. The new own property shadows the prototype property
4. The prototype's property remains unchanged
5. This is by design — prototypal sharing requires non-destructive updates

# Construction / Recognition

## To Construct/Create:
1. `const proto = { prop: 'a' }; const obj = Object.create(proto); obj.prop = 'b';`
2. Now `obj` has its own `prop` that shadows `proto.prop`

## To Identify/Recognize:
1. After assignment, `Object.keys(obj)` includes the key
2. The prototype's value is unchanged

# Context & Application

This behavior is fundamental to JavaScript's prototype-based inheritance. It explains why assigning to an inherited property does not break other objects that share the same prototype.

# Examples

**Example 1** (Ch 12):
```js
const proto = { prop: 'a' };
const obj = Object.create(proto);
assert.deepEqual(Object.keys(obj), []);
obj.prop = 'b';
assert.equal(obj.prop, 'b');
assert.deepEqual(Object.keys(obj), ['prop']); // own property created
assert.equal(proto.prop, 'a');                  // prototype unchanged
```

# Relationships

## Builds Upon
- **property-assignment** — this is a behavior of assignment
- **prototype-internal-slot** — the prototype chain determines inheritance

## Enables
- Understanding of prototype-based inheritance patterns

## Related
- **inherited-read-only-prevents-assignment** — related prototype chain interaction

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `obj.prop = value` to change the prototype's `prop`.
  **Correction**: Assignment always creates or changes own properties on the target, never prototype properties.

# Common Confusions

- **Confusion**: Thinking you need a special API to "override" a prototype property.
  **Clarification**: Simple assignment automatically creates an own property that shadows the prototype property.

# Source Reference

Chapter 12: Properties: assignment vs. definition, Section 12.3.2, lines 389-424.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated with examples and rationale.
- Cross-reference status: verified
