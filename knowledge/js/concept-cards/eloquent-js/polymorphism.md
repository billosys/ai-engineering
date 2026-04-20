---
# === CORE IDENTIFICATION ===
concept: Polymorphism
slug: polymorphism

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: design-principles
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "Polymorphism"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - polymorphic code

# === TYPED RELATIONSHIPS ===
prerequisites:
  - interface
  - method
  - prototype
extends: []
related:
  - iterator-protocol
  - overriding-derived-properties
  - inheritance
contrasts_with:
  - encapsulation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is polymorphism?"
  - "How can different types work with the same code?"
---

# Quick Definition
Polymorphism is a technique where code is written to work with values of different shapes, as long as they support the expected interface.

# Core Definition
Haverbeke defines: "This technique is called *polymorphism*. Polymorphic code can work with values of different shapes, as long as they support the interface it expects." (Ch 6, "Polymorphism")

# Prerequisites
- **Interfaces**: Polymorphism requires objects to share a common interface
- **Methods**: Objects must implement expected methods
- **Prototypes**: Different types can provide their own implementations via prototypes

# Key Properties
1. Code written for an interface works with any object supporting that interface
2. Different types can provide their own implementations of the same method
3. `for/of` loops are polymorphic (work with any iterable)
4. `String()` conversion is polymorphic (calls `toString` on any object)

# Construction / Recognition
Polymorphism is present whenever code operates on objects through a shared interface rather than checking specific types.

# Context & Application
Polymorphism is one of the three pillars of OOP. The chapter summary states: "More than one type may implement the same interface. Code written to use an interface automatically knows how to work with any number of different objects that provide the interface."

# Examples
```javascript
Rabbit.prototype.toString = function() {
  return `a ${this.type} rabbit`;
};

console.log(String(killerRabbit));
// -> a killer rabbit
```

Array-like polymorphism:
```javascript
Array.prototype.forEach.call({
  length: 2,
  0: "A",
  1: "B"
}, elt => console.log(elt));
// -> A
// -> B
```
(Ch 6, "Polymorphism", lines 621-660)

# Relationships
## Builds Upon
- interface, method, prototype
## Enables
- iterator-protocol, reusable code across types
## Related
- overriding-derived-properties, inheritance
## Contrasts With
- encapsulation (hides details; polymorphism varies behavior across types)

# Common Errors
- **Error**: Checking object types explicitly instead of relying on interfaces
  **Correction**: Write code that depends on interfaces, not specific types; let polymorphism handle different implementations

# Common Confusions
- **Confusion**: Polymorphism requires inheritance
  **Clarification**: Any objects that share an interface are polymorphic, regardless of inheritance relationships

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Polymorphism", lines 610-660.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with clear examples
- Cross-reference status: verified against chapter summary
