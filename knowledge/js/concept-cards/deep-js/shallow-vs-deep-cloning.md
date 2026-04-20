---
# === CORE IDENTIFICATION ===
concept: Shallow vs. Deep Cloning of Instances
slug: shallow-vs-deep-cloning

# === CLASSIFICATION ===
category: class-patterns
subcategory: cloning
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Copying instances of classes: .clone() vs. copy constructors"
chapter_number: 15
section: "15.1 .clone() methods"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - shallow copy vs deep copy
  - reference copy vs value copy

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
extends: []
related:
  - recursive-deep-copying
  - clone-method
  - static-from-factory
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement the .clone() pattern for class instances?"
---

# Quick Definition

Shallow cloning copies only top-level property values (sharing references to nested objects), while deep cloning recursively copies all nested objects so that original and copy are fully independent.

# Core Definition

Implied in "Deep JavaScript" (Ch 15, Section 15.1): The `.clone()` examples demonstrate deep copying by recursively cloning compound properties (`this.color.clone()`). A shallow copy would simply assign `this.color` directly, resulting in both original and clone sharing the same `Color` instance. The distinction is critical for maintaining independence between original and copy.

# Prerequisites

- **JavaScript classes** — Object composition and reference semantics.

# Key Properties

1. **Shallow clone**: copies primitive values and references to objects.
2. **Deep clone**: copies primitive values and recursively clones referenced objects.
3. Shallow clones are **faster** but share nested state.
4. Deep clones are **safer** but require every nested class to support cloning.
5. Modifications to shared nested objects in a shallow clone **affect the original**.

# Construction / Recognition

## To Construct/Create:
1. **Shallow**: `new Point(this.x, this.y)` — primitives are copied by value automatically.
2. **Deep**: `new ColorPoint(this.x, this.y, this.color.clone())` — objects are cloned recursively.

## To Identify/Recognize:
1. **Shallow**: Object-valued properties are assigned directly.
2. **Deep**: Object-valued properties have `.clone()` or `.from()` called on them.

# Context & Application

The distinction is implicit but fundamental in Chapter 15. For instances with only primitive properties (like `Point` with `x` and `y`), shallow and deep cloning are equivalent. The distinction matters when instances contain object-valued properties (like `ColorPoint` containing a `Color`).

# Examples

**Example 1** (Ch 15): Deep cloning (correct):
```js
clone() {
  return new ColorPoint(
    this.x, this.y, this.color.clone()); // deep: color is cloned
}
```

**Example 2** (inferred): Shallow cloning (problematic):
```js
clone() {
  return new ColorPoint(
    this.x, this.y, this.color); // shallow: color is shared!
}
```

# Relationships

## Builds Upon
- **Reference semantics** — Objects are passed by reference in JavaScript.

## Enables
- **Instance independence** — Deep cloning ensures no shared mutable state.

## Related
- **Recursive deep copying** — The technique for achieving deep clones.

## Contrasts With
- **Structural sharing** — Immutable data structures can safely share references.

# Common Errors

- **Error**: Assuming a clone is deep when it only copies top-level properties.
  **Correction**: Check whether all object-valued properties are recursively cloned.

# Common Confusions

- **Confusion**: Thinking spread syntax (`{...obj}`) produces a deep copy.
  **Clarification**: Spread syntax produces a shallow copy. Nested objects are shared by reference.

# Source Reference

Chapter 15: Copying instances of classes, Section 15.1, lines 7480-7567.

# Verification Notes

- Definition source: synthesized (distinction is demonstrated but not explicitly named in source)
- Confidence rationale: The recursive cloning is explicitly shown; the terminology "shallow vs. deep" is standard
- Cross-reference status: consistent with Chapter 7 (copying objects and arrays)
