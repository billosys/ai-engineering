---
# === CORE IDENTIFICATION ===
concept: ".clone() Method"
slug: clone-method

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
  - clone pattern
  - instance cloning

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
extends: []
related:
  - static-from-factory
  - recursive-deep-copying
  - copy-constructor
contrasts_with:
  - copy-constructor
  - static-from-factory

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement the .clone() pattern for class instances?"
---

# Quick Definition

The `.clone()` method is an instance method that returns a deep copy of the current object by constructing a new instance of the same class with copied property values.

# Core Definition

As described in "Deep JavaScript" (Ch 15, Section 15.1): "This technique introduces one method `.clone()` per class whose instances are to be copied. It returns a deep copy of `this`." Each class implements its own `.clone()` method that calls its constructor with the current instance's property values. For compound properties, `.clone()` must be called recursively.

# Prerequisites

- **JavaScript classes** — Constructor and method syntax.

# Key Properties

1. Each class implements its **own `.clone()` method**.
2. The method returns `new ClassName(this.prop1, this.prop2, ...)`.
3. Compound (object) properties must be **cloned recursively** — `this.color.clone()`.
4. The caller invokes `.clone()` on an existing instance.
5. Produces a **deep copy** when recursive cloning is used correctly.

# Construction / Recognition

## To Construct/Create:
1. Define a `.clone()` method on the class.
2. In `.clone()`, return a new instance of the class using `new`.
3. Pass the current instance's properties to the constructor.
4. For object-valued properties, call `.clone()` on them recursively.

## To Identify/Recognize:
1. An instance method named `.clone()` (or similar).
2. The method calls `new` on its own class.
3. Properties are copied from `this` to the new instance.

# Context & Application

The `.clone()` pattern is a common approach to instance copying in object-oriented JavaScript. It places the copying logic on the instance itself, making it polymorphic — subclasses can override `.clone()` with their own logic. It is one of two approaches covered in Chapter 15 (the other being static factory methods).

# Examples

**Example 1** (Ch 15): Clone with recursive copying:
```js
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  clone() {
    return new Point(this.x, this.y);
  }
}
class Color {
  constructor(name) {
    this.name = name;
  }
  clone() {
    return new Color(this.name);
  }
}
class ColorPoint extends Point {
  constructor(x, y, color) {
    super(x, y);
    this.color = color;
  }
  clone() {
    return new ColorPoint(
      this.x, this.y, this.color.clone()); // recursive
  }
}
```

# Relationships

## Builds Upon
- **JavaScript classes** — Constructor called within `.clone()`.

## Enables
- **Recursive deep copying** — Compound properties are cloned recursively.
- **Polymorphic copying** — Subclasses override `.clone()` for custom behavior.

## Related
- **Static `.from()` factory** — An alternative approach to copying.

## Contrasts With
- **Copy constructor** — Puts copying logic in the constructor; less idiomatic in JavaScript.
- **Static `.from()` factory** — Puts copying logic in a static method rather than an instance method.

# Common Errors

- **Error**: Forgetting to recursively clone compound properties.
  **Correction**: Object-valued properties must have `.clone()` called on them; otherwise you get a shallow copy with shared references.

# Common Confusions

- **Confusion**: Thinking `.clone()` is a built-in JavaScript method.
  **Clarification**: `.clone()` is a user-defined method. JavaScript has no built-in clone mechanism for class instances.

# Source Reference

Chapter 15: Copying instances of classes, Section 15.1, lines 7480-7567.

# Verification Notes

- Definition source: direct (from source explanation and code)
- Confidence rationale: Explicitly defined technique with complete code examples
- Cross-reference status: verified against Section 15.2 alternative
