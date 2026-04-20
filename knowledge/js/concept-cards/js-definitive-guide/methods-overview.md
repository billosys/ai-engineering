---
# === CORE IDENTIFICATION ===
concept: Methods Overview
slug: methods-overview

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
pdf_page: 25
section: "1.3 A Tour of JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - first-class-functions
  - object-type-overview
extends:
  - first-class-functions
related:
  - type-system-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

A method is a function that is stored as a property of an object and invoked on that object, using `this` to refer to the object on which it is called.

# Core Definition

As introduced in Chapter 1: "When functions are assigned to the properties of an object, we call them 'methods.' All JavaScript objects (including arrays) have methods." Chapter 3 adds: "Technically, it is only JavaScript objects that have methods. But numbers, strings, boolean, and symbol values behave as if they have methods. In JavaScript, null and undefined are the only values that methods cannot be invoked on." (pp. 25, 41-42)

# Prerequisites

- **first-class-functions** — Methods are functions stored as properties
- **object-type-overview** — Methods are properties of objects

# Key Properties

1. Methods are functions assigned to object properties
2. The `this` keyword refers to the object on which the method is invoked
3. All objects (including arrays) have methods
4. Primitives (except null/undefined) behave as if they have methods
5. Only null and undefined cannot have methods invoked on them

# Construction / Recognition

```javascript
let a = [];
a.push(1, 2, 3);      // push() is a method of array objects
a.reverse();           // reverse() is another array method

// Custom method
points.dist = function() {
    let p1 = this[0];
    let p2 = this[1];
    let a = p2.x - p1.x;
    let b = p2.y - p1.y;
    return Math.sqrt(a*a + b*b);
};
```

# Context & Application

Methods are the primary way to interact with objects in JavaScript. The object-oriented style means "rather than having globally defined functions to operate on values of various types, the types themselves define methods for working with values" (p. 41).

# Examples

From the source text (p. 25):
```javascript
let a = [];
a.push(1, 2, 3);   // The push() method adds elements to an array
a.reverse();        // Another method: reverse the order of elements

points.dist = function() {
    let p1 = this[0];
    let p2 = this[1];
    let a = p2.x - p1.x;
    let b = p2.y - p1.y;
    return Math.sqrt(a*a + b*b);
};
points.dist()       // => Math.sqrt(2)
```

From Chapter 3 (p. 41):
```javascript
a.sort();   // The object-oriented version of sort(a).
```

# Relationships

## Builds Upon
- **first-class-functions** — Methods are functions used as object properties
- **object-type-overview** — Methods are defined on objects

## Enables
- Object-oriented programming patterns (covered in Chapter 9)

## Related
- **type-system-overview** — Primitives behave as if they have methods

## Contrasts With
- Standalone functions — methods are bound to objects via `this`

# Common Errors

- **Error**: Trying to call a method on null or undefined.
  **Correction**: "null and undefined are the only values that methods cannot be invoked on" — this causes a TypeError (p. 58).

# Common Confusions

- **Confusion**: Primitive values like strings and numbers don't have methods.
  **Clarification**: They behave as if they have methods (via temporary wrapper objects), so `"hello".toUpperCase()` works.

# Source Reference

Chapter 1: Introduction to JavaScript, Section 1.3, pages 25-26. Chapter 3, Section 3.1, pages 41-42.

# Verification Notes

- Definition source: Direct quotes from pp. 25, 41-42
- Confidence rationale: High — clearly introduced with examples
- Uncertainties: Full method treatment deferred to Chapter 9
- Cross-reference status: Verified across Ch 1 and Ch 3
