---
# === CORE IDENTIFICATION ===
concept: "Static .from() Factory"
slug: static-from-factory

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
section: "15.2 Static factory methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - static copy factory
  - ".from() copy method"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - static-factory-method
extends:
  - static-factory-method
related:
  - clone-method
  - recursive-deep-copying
contrasts_with:
  - copy-constructor
  - clone-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement the .clone() pattern for class instances?"
---

# Quick Definition

A static `.from()` factory is a class method that creates a new instance by copying properties from an existing instance, serving as JavaScript's idiomatic alternative to copy constructors.

# Core Definition

As described in "Deep JavaScript" (Ch 15, Section 15.2): "Static factory methods are an alternative to constructors and work better in this case because we can directly invoke the desired functionality." Each class defines a `static from(other)` method that creates a new instance from an existing one. The pattern follows the convention established by `Array.from()`.

# Prerequisites

- **JavaScript classes** — Static method syntax.
- **Static factory method** — The general pattern this specializes.

# Key Properties

1. Uses the naming convention `.from()` to signal "create from an existing object."
2. The method is **static** — called on the class, not an instance.
3. Compound properties must be **copied recursively** — e.g., `Color.from(other.color)`.
4. More idiomatic in JavaScript than copy constructors.
5. Constructor stays simple; copying logic is in the static method.

# Construction / Recognition

## To Construct/Create:
1. Define `static from(other)` on the class.
2. Return `new ClassName(other.prop1, other.prop2, ...)`.
3. For object properties, call `OtherClass.from(other.prop)` recursively.

## To Identify/Recognize:
1. A `static from()` method on a class.
2. The method accepts an instance and returns a new instance with copied properties.

# Context & Application

This is the author's recommended approach for copying class instances in JavaScript. It avoids the constructor overloading problems of copy constructors and provides a clear, explicit API. The `.from()` naming convention is well-established in JavaScript (e.g., `Array.from()`, `Object.fromEntries()`).

# Examples

**Example 1** (Ch 15): Static `.from()` with recursive copying:
```js
class Point {
  constructor(x, y) { this.x = x; this.y = y; }
  static from(other) {
    return new Point(other.x, other.y);
  }
}
class Color {
  constructor(name) { this.name = name; }
  static from(other) {
    return new Color(other.name);
  }
}
class ColorPoint extends Point {
  constructor(x, y, color) { super(x, y); this.color = color; }
  static from(other) {
    return new ColorPoint(
      other.x, other.y, Color.from(other.color)); // recursive
  }
}

const original = new ColorPoint(-1, 4, new Color('red'));
const copy = ColorPoint.from(original);
assert.deepEqual(copy, original);
```

# Relationships

## Builds Upon
- **Static factory method** — `.from()` is a specific application of the factory method pattern.

## Enables
- **Recursive deep copying** — Composed objects are copied via their own `.from()`.

## Related
- **`.clone()` method** — Instance-based alternative.
- **`Array.from()`** — Built-in that establishes the `.from()` naming convention.

## Contrasts With
- **Copy constructor** — Runtime overloading; less idiomatic in JavaScript.
- **`.clone()` method** — Instance method vs. static method; `.from()` is called on the class.

# Common Errors

- **Error**: Forgetting to recursively copy compound properties.
  **Correction**: Object-valued properties need `OtherClass.from(other.prop)`, not just `other.prop`.

# Common Confusions

- **Confusion**: Thinking `.from()` and `.clone()` are interchangeable.
  **Clarification**: `.from()` is called on the class (`Point.from(other)`), while `.clone()` is called on the instance (`point.clone()`). `.from()` can accept objects that aren't instances of the class.

# Source Reference

Chapter 15: Copying instances of classes, Section 15.2, lines 7607-7653.

# Verification Notes

- Definition source: direct (from source code and explanation)
- Confidence rationale: Explicitly presented as recommended alternative with complete examples
- Cross-reference status: verified against `.clone()` approach in Section 15.1
