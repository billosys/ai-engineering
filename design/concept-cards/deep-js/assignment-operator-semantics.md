---
# === CORE IDENTIFICATION ===
concept: Assignment Operator Semantics
slug: assignment-operator-semantics

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
section: "12.2.1 Assigning to a property"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "OrdinarySetWithOwnDescriptor"
  - "[[Set]] operation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-assignment
  - prototype-internal-slot
extends: []
related:
  - property-definition
contrasts_with:
  - define-property-semantics

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does property assignment differ from property definition?"
  - "What must I understand before learning about property assignment vs. definition?"
---

# Quick Definition

The assignment operator `=` triggers the spec operation `OrdinarySetWithOwnDescriptor`, which traverses the prototype chain looking for the property. It either changes an existing own data property, invokes a setter, or creates a new own data property on the receiver.

# Core Definition

As described in "Deep JavaScript" Ch 12, the assignment algorithm (`OrdinarySetWithOwnDescriptor(O, P, V, Receiver, ownDesc)`) works as follows:
1. "It traverses the prototype chain of `Receiver` until it finds a property whose key is `P`."
2. If no property found: creates an own data property on `Receiver` with `{[[Writable]]: true, [[Enumerable]]: true, [[Configurable]]: true}`
3. If a data property found: if `[[Writable]]` is `false`, returns `false` (TypeError in strict mode); otherwise, changes the value
4. If an accessor property found: invokes the `[[Set]]` function
5. "Notably, `PutValue()` throws a `TypeError` in strict mode if the result of `.[[Set]]()` is `false`."

# Prerequisites

- **Property Assignment** — this is the underlying algorithm
- **[[Prototype]] Internal Slot** — the algorithm traverses the prototype chain

# Key Properties

1. Traverses the prototype chain from receiver upward
2. Any non-writable property in the chain (own or inherited) prevents assignment
3. Inherited setters are invoked (with `this` set to the receiver)
4. New data properties are created on the receiver (not on the prototype where the search found something)
5. In strict mode, failed assignment throws TypeError
6. Uses `[[DefineOwnProperty]]` internally to change existing property values

# Construction / Recognition

## To Construct/Create:
1. `obj.prop = value` triggers this algorithm
2. Destructuring assignment `[obj.prop] = [value]` also triggers it

## To Identify/Recognize:
1. Any use of `=` with property access on the left side

# Context & Application

Understanding the assignment algorithm explains why inherited non-writable properties prevent creating own properties (the algorithm returns `false` before reaching the "create" step), and why assignment creates properties on the receiver rather than modifying prototype properties.

# Examples

**Example 1** (Ch 12): Assignment does not modify prototype properties:
```js
const proto = { prop: 'a' };
const obj = Object.create(proto);
obj.prop = 'b';
// Created own property on obj, did not change proto.prop
assert.equal(obj.prop, 'b');
assert.equal(proto.prop, 'a');
```

# Relationships

## Builds Upon
- **property-assignment** — this describes the spec-level algorithm
- **prototype-internal-slot** — traversed during the algorithm

## Enables
- **inherited-read-only-prevents-assignment** — explained by the algorithm
- **assignment-calls-setters** — explained by the algorithm

## Related
- None

## Contrasts With
- **define-property-semantics** — the parallel algorithm for definition

# Common Errors

- **Error**: Expecting assignment to modify a prototype property.
  **Correction**: Assignment creates an own property on the receiver, shadowing the prototype property.

# Common Confusions

- **Confusion**: Thinking the prototype chain is only relevant for reads.
  **Clarification**: The prototype chain is traversed during assignment too — inherited setters and inherited non-writable properties affect assignment behavior.

# Source Reference

Chapter 12: Properties: assignment vs. definition, Section 12.2.1, lines 136-251.

# Verification Notes

- Definition source: direct (summarized from spec algorithm description)
- Confidence rationale: Detailed walkthrough of the specification algorithm.
- Cross-reference status: verified
