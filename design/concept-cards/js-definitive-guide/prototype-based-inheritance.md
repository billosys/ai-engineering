---
# === CORE IDENTIFICATION ===
concept: Prototype-Based Inheritance
slug: prototype-based-inheritance

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: language-overview
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Introduction to JavaScript"
chapter_number: 1
pdf_page: 18
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - prototypal inheritance
  - prototype chain

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - type-system-overview
extends: []
related:
  - first-class-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

JavaScript uses prototype-based inheritance (derived from the language Self) rather than classical class-based inheritance, meaning objects inherit directly from other objects through a prototype chain.

# Core Definition

As introduced in Chapter 1: "JavaScript derives its first-class functions from Scheme and its prototype-based inheritance from the little-known language Self." (p. 18) Chapter 1 also shows that JavaScript supports "an object-oriented programming style, but it is significantly different than 'classical' object-oriented programming languages" (p. 27). ES6 introduced `class` syntax, but this is syntactic sugar over the prototype-based system.

# Prerequisites

- **javascript-language-overview** — Must understand the language itself
- **type-system-overview** — Must understand that objects are a fundamental type

# Key Properties

1. Objects inherit directly from other objects (not from classes in the classical sense)
2. Derived from the Self programming language
3. ES6 `class` syntax provides familiar class-based syntax over prototypes
4. Significantly different from classical OOP in Java, C++, etc.

# Construction / Recognition

From Chapter 1 (p. 27), ES6 class syntax:
```javascript
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    distance() {
        return Math.sqrt(this.x * this.x + this.y * this.y);
    }
}
let p = new Point(1, 1);
p.distance()    // => Math.SQRT2
```

# Context & Application

Prototype-based inheritance is fundamental to understanding how JavaScript objects work, how methods are shared, and how the `class` keyword works under the hood. Full treatment is in Chapter 9.

# Examples

From the source text (p. 27):
```javascript
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    distance() {
        return Math.sqrt(this.x * this.x + this.y * this.y);
    }
}
let p = new Point(1, 1);
p.distance()    // => Math.SQRT2
```

# Relationships

## Builds Upon
- **javascript-language-overview** — Prototype-based inheritance is a defining feature
- **type-system-overview** — Inheritance applies to object types

## Enables
- Class-based OOP patterns (covered in Chapter 9)

## Related
- **first-class-functions** — Methods are functions stored as object properties

## Contrasts With
- Classical class-based inheritance (Java, C++) — mentioned but not detailed in Ch 1

# Common Errors

- **Error**: Assuming JavaScript classes work exactly like Java or C++ classes.
  **Correction**: JavaScript's class syntax is syntactic sugar over prototype-based inheritance; the underlying mechanism is fundamentally different.

# Common Confusions

- **Confusion**: ES6 classes replaced prototype-based inheritance.
  **Clarification**: ES6 classes are syntactic sugar; the prototype chain is still the underlying mechanism.

# Source Reference

Chapter 1: Introduction to JavaScript, pages 18, 27.

# Verification Notes

- Definition source: Direct quote from p. 18; class example from p. 27
- Confidence rationale: Medium — briefly introduced in Ch 1; full treatment in Ch 9
- Uncertainties: Detailed prototype mechanics deferred to Chapter 9
- Cross-reference status: Verified within Ch 1
