---
# === CORE IDENTIFICATION ===
concept: DefineProperty Semantics
slug: define-property-semantics

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
section: "12.2.2 Defining a property"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ValidateAndApplyPropertyDescriptor"
  - "definition algorithm"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-definition
  - configurable-attribute
extends: []
related:
  - property-assignment
contrasts_with:
  - assignment-operator-semantics

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does property assignment differ from property definition?"
  - "How do I define a property with specific attributes using Object.defineProperty()?"
---

# Quick Definition

The definition algorithm (`ValidateAndApplyPropertyDescriptor`) either creates a new own property or modifies an existing own property's attributes, subject to validation rules based on the `configurable` attribute.

# Core Definition

As described in "Deep JavaScript" Ch 12, the definition algorithm (`ValidateAndApplyPropertyDescriptor(O, P, extensible, Desc, current)`) works as follows:
- If the property does not exist: create it if the object is extensible
- If the descriptor has no fields: succeed (no changes needed)
- If `current.[[Configurable]]` is `false`: most changes are disallowed
- Validate whether the change from `current` to `Desc` is legal
- For non-configurable data properties: `writable` can go from `true` to `false` but not back
- If validation passes: apply the changes and return `true`

"Some callers ignore the result. Others, such as `Object.defineProperty()`, throw an exception if the result is `false`."

# Prerequisites

- **Property Definition** — this is the underlying algorithm
- **Configurable Attribute** — the algorithm checks configurable extensively

# Key Properties

1. Only operates on own properties (no prototype traversal)
2. Validates all changes against `configurable` attribute
3. Can create new properties (if extensible)
4. Can change property kind (data <-> accessor) if configurable
5. Non-configurable + non-writable: only exact-same-value changes allowed
6. Non-configurable but writable: value changes and writable->false changes allowed
7. Returns boolean success; `Object.defineProperty()` throws on failure

# Construction / Recognition

## To Construct/Create:
1. `Object.defineProperty(obj, key, desc)` invokes this algorithm
2. `Object.defineProperties()` and `Object.create()` also invoke it

## To Identify/Recognize:
1. Any operation that creates/changes properties via descriptors

# Context & Application

Understanding the definition algorithm explains why certain attribute changes are rejected, why non-configurable properties are locked down, and the special exception that allows `writable` to change from `true` to `false` on non-configurable properties.

# Examples

**Example 1** (Ch 12): Definition can override inherited read-only properties:
```js
const proto = Object.defineProperty(
  {}, 'prop', { value: 'protoValue', writable: false });
const obj = Object.create(proto);
// Assignment fails:
assert.throws(() => obj.prop = 'objValue');
// But definition works:
Object.defineProperty(obj, 'prop', { value: 'objValue' });
assert.equal(obj.prop, 'objValue');
```

# Relationships

## Builds Upon
- **property-definition** — this is the spec algorithm behind definition
- **configurable-attribute** — central to the validation logic

## Enables
- Understanding why certain `Object.defineProperty()` calls throw TypeError

## Related
- None

## Contrasts With
- **assignment-operator-semantics** — the parallel algorithm for assignment

# Common Errors

- **Error**: Trying to change `enumerable` on a non-configurable property.
  **Correction**: Non-configurable properties reject changes to all attributes except `value` (and `writable` from true to false).

# Common Confusions

- **Confusion**: Thinking definition always succeeds.
  **Clarification**: Definition can fail if the property is non-configurable and the requested change is not allowed. `Object.defineProperty()` throws a TypeError on failure.

# Source Reference

Chapter 12: Properties: assignment vs. definition, Section 12.2.2, lines 254-353.

# Verification Notes

- Definition source: direct (summarized from spec algorithm description)
- Confidence rationale: Detailed walkthrough of the specification algorithm.
- Cross-reference status: verified
