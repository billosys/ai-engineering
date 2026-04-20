---
# === CORE IDENTIFICATION ===
concept: Recursive Deep Copying of Instances
slug: recursive-deep-copying

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
extraction_confidence: high

# === VARIANTS ===
aliases:
  - deep clone
  - recursive instance copying

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - clone-method
extends: []
related:
  - static-from-factory
  - shallow-vs-deep-cloning
contrasts_with:
  - shallow-vs-deep-cloning

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement the .clone() pattern for class instances?"
---

# Quick Definition

Recursive deep copying means that when cloning an instance, any compound (object-valued) properties are themselves cloned by calling their `.clone()` or `.from()` method, ensuring no shared references between original and copy.

# Core Definition

As highlighted in "Deep JavaScript" (Ch 15, Section 15.1, line A): "compound instance property values must also be cloned, recursively." When a `ColorPoint` has a `color` property that is a `Color` instance, the `.clone()` method must call `this.color.clone()` rather than simply copying the reference. The same principle applies to `.from()` factories: `Color.from(other.color)`.

# Prerequisites

- **JavaScript classes** — Object composition.
- **`.clone()` method** or **static `.from()` factory** — The mechanism used for each level of copying.

# Key Properties

1. Each object in the graph must have its own **copy mechanism** (`.clone()` or `.from()`).
2. Only **primitive** properties can be copied directly.
3. **Object-valued** properties must be recursively copied.
4. Without recursive copying, modifications to nested objects **affect both** original and copy.
5. The recursion follows the **object composition graph**.

# Construction / Recognition

## To Construct/Create:
1. In `.clone()` or `.from()`, identify all object-valued properties.
2. Call `.clone()` or `.from()` on each object-valued property.
3. Pass the cloned values (not the originals) to the constructor.

## To Identify/Recognize:
1. A `.clone()` or `.from()` method that calls `.clone()` / `.from()` on nested objects.
2. The copy operation traverses the entire object graph.

# Context & Application

Recursive deep copying is essential whenever class instances contain other class instances as properties. Without it, a "copy" shares nested objects with the original, and mutations to one affect the other.

# Examples

**Example 1** (Ch 15): Recursive cloning in `.clone()`:
```js
class ColorPoint extends Point {
  constructor(x, y, color) {
    super(x, y);
    this.color = color;
  }
  clone() {
    return new ColorPoint(
      this.x, this.y, this.color.clone()); // recursive!
  }
}
```

**Example 2** (Ch 15): Recursive copying in `.from()`:
```js
class ColorPoint extends Point {
  static from(other) {
    return new ColorPoint(
      other.x, other.y, Color.from(other.color)); // recursive!
  }
}
```

# Relationships

## Builds Upon
- **`.clone()` method** — The instance-based mechanism that recurses.
- **Static `.from()` factory** — The static mechanism that recurses.

## Enables
- **True independence** — Original and copy share no mutable state.

## Related
- **Shallow vs. deep cloning** — The distinction this addresses.

## Contrasts With
- **Shallow copying** — Copies only the top-level properties; nested objects are shared.

# Common Errors

- **Error**: Copying an object property by reference instead of cloning it.
  **Correction**: Use `this.color.clone()` or `Color.from(other.color)`, not just `this.color` or `other.color`.

# Common Confusions

- **Confusion**: Thinking `Object.assign()` or spread syntax handles deep copying.
  **Clarification**: Both produce shallow copies. For class instances with nested objects, you need explicit recursive cloning via `.clone()` or `.from()`.

# Source Reference

Chapter 15: Copying instances of classes, Sections 15.1-15.2, lines 7480-7653.

# Verification Notes

- Definition source: direct (explicitly highlighted in source at line A annotations)
- Confidence rationale: Explicitly emphasized as "an important aspect of this technique"
- Cross-reference status: verified in both .clone() and .from() examples
