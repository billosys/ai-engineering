---
# === CORE IDENTIFICATION ===
concept: Instance Copying Techniques
slug: instance-copying-techniques

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - class instance copying
  - object copying patterns

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
extends: []
related:
  - clone-method
  - copy-constructor
  - static-from-factory
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement the .clone() pattern for class instances?"
---

# Quick Definition

Instance copying techniques are the approaches available in JavaScript for creating copies of class instances, including `.clone()` methods, copy constructors, and static `.from()` factory methods.

# Core Definition

As introduced in "Deep JavaScript" (Ch 15): "In this chapter, we look at two techniques for implementing copying for class instances: `.clone()` methods" and "so-called copy constructors, constructors that receive another instance of the current class and use it to initialize the current instance." The author recommends `.clone()` methods and static `.from()` factories over copy constructors for JavaScript.

# Prerequisites

- **JavaScript classes** — Class syntax and construction.

# Key Properties

1. Three approaches: **`.clone()`**, **copy constructor**, **static `.from()`**.
2. `.clone()` is an **instance method** — polymorphic, can be overridden by subclasses.
3. Copy constructors are **inelegant** in JavaScript due to lack of static overloading.
4. Static `.from()` is the **recommended alternative** to copy constructors.
5. All three require **recursive copying** for compound properties.

# Construction / Recognition

## To Construct/Create:
1. Choose between `.clone()` (instance method) and `.from()` (static method).
2. Implement the chosen method on each class that needs copying.
3. Handle compound properties recursively.

## To Identify/Recognize:
1. A class with a `.clone()` method, a copy-capable constructor, or a `.from()` static method.
2. The method creates a new instance from an existing one.

# Context & Application

Chapter 15 compares these approaches to help developers choose the right pattern. The `.clone()` method is simple and widely understood. The `.from()` static factory is more idiomatic for JavaScript. Copy constructors are included for completeness but are not recommended.

# Examples

**Example 1** (Ch 15): Three approaches compared:
```js
// .clone() method
const copy1 = original.clone();

// Copy constructor (not recommended)
const copy2 = new Point(original);

// Static .from() factory (recommended)
const copy3 = Point.from(original);
```

# Relationships

## Builds Upon
- **JavaScript classes** — The class system being extended with copying capabilities.

## Enables
- **Immutable data patterns** — Copying enables non-destructive updates.
- **State snapshots** — Save the state of an object at a point in time.

## Related
- **`.clone()` method** — Instance-based approach.
- **Copy constructor** — Constructor-based approach (not recommended).
- **Static `.from()` factory** — Static method approach (recommended).

## Contrasts With
- **Object.assign() / spread** — Generic shallow copy, not class-aware.
- **structuredClone()** — Built-in deep clone, but not class-aware.

# Common Errors

- **Error**: Using `Object.assign({}, instance)` to copy a class instance.
  **Correction**: `Object.assign` creates a plain object, not an instance of the class. Prototype chain and private fields are lost.

# Common Confusions

- **Confusion**: Thinking `.clone()` and `.from()` serve different purposes.
  **Clarification**: Both create copies. `.clone()` is called on the instance; `.from()` is called on the class. Choose based on your API preferences.

# Source Reference

Chapter 15: Copying instances of classes: .clone() vs. copy constructors, lines 7480-7663.

# Verification Notes

- Definition source: direct (from chapter introduction)
- Confidence rationale: Chapter-level overview with explicit technique comparison
- Cross-reference status: verified across Sections 15.1 and 15.2
