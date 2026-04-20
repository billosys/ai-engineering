---
# === CORE IDENTIFICATION ===
concept: Inherited Read-Only Prevents Assignment
slug: inherited-read-only-prevents-assignment

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
section: "12.3.4 Inherited read-only properties prevent creating own properties via assignment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "override mistake"
  - "inherited non-writable blocks assignment"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-assignment
  - writable-attribute
  - prototype-internal-slot
extends: []
related:
  - property-definition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does property assignment differ from property definition?"
---

# Quick Definition

If an inherited property has `writable: false`, you cannot use assignment to create an own property with the same key on a descendant object. This restriction does not apply to definition — `Object.defineProperty()` can still create the own property.

# Core Definition

As described in "Deep JavaScript" Ch 12, "In any object that inherits the read-only `.prop` from `proto`, we can't use assignment to create an own property with the same key." The rationale: "overriding an inherited property by creating an own property can be seen as non-destructively changing the inherited property. Arguably, if a property is non-writable, we shouldn't be able to do that." This behavior is sometimes called the "override mistake." It also applies to accessor properties without a setter.

# Prerequisites

- **Property Assignment** — this is a behavior of assignment specifically
- **Writable Attribute** — the writable attribute on the inherited property causes the restriction
- **[[Prototype]] Internal Slot** — the property must be inherited via the prototype chain

# Key Properties

1. Any non-writable property in the prototype chain prevents assignment of that key
2. Accessor properties without a setter also block assignment
3. Definition (Object.defineProperty) is NOT affected — it can still create the own property
4. This was introduced in ECMAScript 5.1
5. Known as the "override mistake" in the community
6. An attempt to change this behavior was abandoned because it broke Lodash

# Construction / Recognition

## To Construct/Create:
1. Create a non-writable property in a prototype
2. Create a descendant object
3. Attempt assignment to the same key — it will throw in strict mode

## To Identify/Recognize:
1. TypeError when assigning to a property key that exists as non-writable in the prototype chain

# Context & Application

This pitfall is particularly relevant when deep-freezing the global object or working with frozen prototypes. It is mentioned in both Ch 10 and Ch 12. The workaround is to use `Object.defineProperty()` instead of assignment.

# Examples

**Example 1** (Ch 12):
```js
const proto = Object.defineProperty(
  {}, 'prop', { value: 'protoValue', writable: false });
const obj = Object.create(proto);
// Assignment fails:
assert.throws(
  () => obj.prop = 'objValue',
  /^TypeError: Cannot assign to read only property 'prop'/);
// Definition works:
Object.defineProperty(obj, 'prop', { value: 'objValue' });
assert.equal(obj.prop, 'objValue');
```

**Example 2** (Ch 12): Accessor without setter also blocks:
```js
const proto = {
  get prop() { return 'protoValue'; }
};
const obj = Object.create(proto);
assert.throws(
  () => obj.prop = 'objValue',
  /^TypeError: Cannot set property prop/);
```

# Relationships

## Builds Upon
- **property-assignment** — this is a behavior specific to assignment
- **writable-attribute** — the attribute that triggers the restriction

## Enables
- Understanding why frozen prototypes can cause problems

## Related
- **property-definition** — the workaround (definition bypasses this restriction)

## Contrasts With
- None

# Common Errors

- **Error**: Expecting assignment to create an own property when the same key is non-writable in a prototype.
  **Correction**: Use `Object.defineProperty()` to override inherited non-writable properties.

# Common Confusions

- **Confusion**: Thinking this only applies to `writable: false` data properties.
  **Clarification**: Accessor properties without a setter also prevent assignment in the same way.

# Source Reference

Chapter 12: Properties: assignment vs. definition, Section 12.3.4, lines 486-559. Also Ch 10, Section 10.1.3.1, lines 187-211.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly described as a pitfall with examples and historical context.
- Cross-reference status: verified across Ch 10 and Ch 12
