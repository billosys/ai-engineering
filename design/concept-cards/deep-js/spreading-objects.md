---
# === CORE IDENTIFICATION ===
concept: Spreading Into Object Literals
slug: spreading-objects

# === CLASSIFICATION ===
category: data-management
subcategory: copying
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Copying objects and Arrays"
chapter_number: 7
section: "Copying plain objects and Arrays via spreading"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "object spread"
  - "spread syntax for objects"
  - "{...obj}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shallow-copy
extends: []
related:
  - spreading-arrays
  - object-assign
  - property-descriptor-copying
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do shallow copies relate to deep copies?"
  - "What distinguishes shallow copying from deep copying?"
---

# Quick Definition

Object spreading (`{...obj}`) creates a shallow copy of an object's own enumerable properties into a new object literal.

# Core Definition

As described in "Deep JavaScript" Ch 7, Section 7.2.1, spreading into object literals (`{...originalObject}`) is the primary way to shallow-copy objects in JavaScript. It copies only own, enumerable properties; the copy's properties are always writable and configurable data properties regardless of the original's property attributes. Prototypes, non-enumerable properties, getters/setters, and special internal slots are not faithfully preserved.

# Prerequisites

- **Shallow copy** -- spreading produces a shallow copy

# Key Properties

1. Only copies own (non-inherited) properties.
2. Only copies enumerable properties.
3. Property attributes are not preserved: copies are always writable and configurable.
4. Getters are invoked and their return values are stored (not the getter itself).
5. The prototype is not copied.
6. Built-in objects with internal slots (Date, RegExp) are not fully copied.
7. The copy is always shallow.

# Construction / Recognition

## To Construct/Create:
1. `const copy = {...original};`

## To Identify/Recognize:
1. The `{...x}` syntax in an object literal context.

# Context & Application

Object spreading is the most common and concise way to shallow-copy objects in modern JavaScript. It is used extensively in non-destructive updating patterns (e.g., `{...obj, key: newValue}`).

# Examples

**Example 1** (Ch 7): Basic object copy:
```js
const copyOfObject = {...originalObject};
```

**Example 2** (Ch 7): Prototype is not preserved:
```js
class MyClass {}
const original = new MyClass();
assert.equal(original instanceof MyClass, true);

const copy = {...original};
assert.equal(copy instanceof MyClass, false);
```

**Example 3** (Ch 7): Fix by setting prototype:
```js
const copy = {
  __proto__: Object.getPrototypeOf(original),
  ...original,
};
assert.equal(copy instanceof MyClass, true);
```

**Example 4** (Ch 7): Getters are not preserved:
```js
const original = {
  get myGetter() { return 123 },
  set mySetter(x) {},
};
assert.deepEqual({...original}, {
  myGetter: 123,        // not a getter anymore!
  mySetter: undefined,
});
```

# Relationships

## Builds Upon
- **Shallow copy** -- spreading is a mechanism for shallow copying

## Enables
- **Non-destructive update** -- `{...obj, key: value}` pattern for non-destructive object updates

## Related
- **Spreading arrays** -- the array equivalent: `[...arr]`
- **Object.assign()** -- an alternative shallow copy mechanism

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Expecting spreading to copy getters/setters as accessors.
  **Correction**: Spreading invokes getters and stores their values. Use `Object.getOwnPropertyDescriptors()` + `Object.defineProperties()` to copy accessor properties faithfully.

# Common Confusions

- **Confusion**: Spreading copies all properties of an object.
  **Clarification**: It only copies own, enumerable properties. Inherited and non-enumerable properties are excluded.

# Source Reference

Chapter 7: "Copying objects and Arrays", Section 7.2.1, lines 3158-3270.

# Verification Notes

- Definition source: direct
- Confidence rationale: Detailed discussion with multiple limitations enumerated in source.
- Cross-reference status: verified against Ch 7 section 7.2.1
