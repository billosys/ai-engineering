---
# === CORE IDENTIFICATION ===
concept: Property Descriptor Copying
slug: property-descriptor-copying

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
section: "Shallow copying via Object.getOwnPropertyDescriptors() and Object.defineProperties() (optional)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "faithful property copying"
  - "descriptor-based copying"
  - "copyAllOwnProperties"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shallow-copy
  - spreading-objects
extends:
  - spreading-objects
related:
  - object-assign
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do shallow copies relate to deep copies?"
---

# Quick Definition

Combining `Object.getOwnPropertyDescriptors()` with `Object.defineProperties()` creates a shallow copy that faithfully preserves all property attributes, including getters, setters, non-enumerable properties, and read-only flags.

# Core Definition

As described in "Deep JavaScript" Ch 7, Section 7.2.3, this approach eliminates two issues of spreading: (1) all property attributes (`writable`, `configurable`, `enumerable`, accessor descriptors) are preserved, and (2) non-enumerable properties are copied. The pattern is `Object.defineProperties({}, Object.getOwnPropertyDescriptors(original))`.

# Prerequisites

- **Shallow copy** -- this is still a shallow copy, just more faithful
- **Spreading objects** -- understanding the limitations this approach addresses

# Key Properties

1. Copies all own properties (enumerable AND non-enumerable).
2. Preserves property attributes: `writable`, `configurable`, `enumerable`.
3. Preserves getters and setters as accessor properties (not their invoked values).
4. Still a shallow copy -- nested values are shared.
5. Uses definition (not assignment), so inherited setters are not invoked.

# Construction / Recognition

## To Construct/Create:
1. ```js
   function copyAllOwnProperties(original) {
     return Object.defineProperties(
       {}, Object.getOwnPropertyDescriptors(original));
   }
   ```

## To Identify/Recognize:
1. The combination of `Object.getOwnPropertyDescriptors()` and `Object.defineProperties()`.

# Context & Application

Use this approach when you need to preserve property attributes faithfully -- for example, when copying objects with getters/setters, read-only properties, or non-enumerable properties. It is more verbose than spreading but more correct.

# Examples

**Example 1** (Ch 7): Copying getters and setters faithfully:
```js
const original = {
  get myGetter() { return 123 },
  set mySetter(x) {},
};
assert.deepEqual(copyAllOwnProperties(original), original);
```

**Example 2** (Ch 7): Copying non-enumerable properties:
```js
const arr = ['a', 'b'];
assert.equal({}.hasOwnProperty.call(arr, 'length'), true);

const copy = copyAllOwnProperties(arr);
assert.equal({}.hasOwnProperty.call(copy, 'length'), true);
```

# Relationships

## Builds Upon
- **Spreading objects** -- this approach fixes limitations of spreading

## Enables
- **Faithful object cloning** -- needed when property attributes matter

## Related
- **Object.assign()** -- another copying approach, but uses assignment

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Forgetting to pass an empty object `{}` as the first argument to `Object.defineProperties()`.
  **Correction**: The first argument is the target object to define properties on.

# Common Confusions

- **Confusion**: This approach performs deep copying.
  **Clarification**: It is still shallow. Only the property descriptors (attributes) are faithfully copied; nested object values remain shared references.

# Source Reference

Chapter 7: "Copying objects and Arrays", Section 7.2.3, lines 3158-3360.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit implementation and comparison with spreading provided.
- Cross-reference status: verified against Ch 7 section 7.2.3
