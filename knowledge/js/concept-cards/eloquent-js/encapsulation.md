---
# === CORE IDENTIFICATION ===
concept: Encapsulation
slug: encapsulation

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
section: "Abstract Data Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - information hiding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - abstract-data-type
extends: []
related:
  - interface
  - private-property
  - class-declaration
contrasts_with:
  - polymorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is encapsulation in object-oriented programming?"
  - "Why should internal details be hidden from external code?"
---

# Quick Definition
Encapsulation is the practice of separating an object's interface from its internal implementation, treating details beyond the interface as internal to the type and of no concern to the rest of the program.

# Core Definition
Haverbeke defines encapsulation within the context of abstract data types: "Each abstract data type has an *interface*, the collection of operations that external code can perform on it. Any details beyond that interface are *encapsulated*, treated as internal to the type and of no concern to the rest of the program." (Ch 6, "Abstract Data Types")

# Prerequisites
- **Objects**: Encapsulation applies to object-based data types
- **Abstract data types**: Encapsulation is a property of well-designed ADTs

# Key Properties
1. Separates public interface from private implementation
2. Protects internal state from external modification
3. Allows implementation changes without affecting external code
4. Reduces coupling between program components

# Construction / Recognition
In JavaScript, encapsulation is achieved through private properties (prefixed with `#`), closures, or conventions. A well-encapsulated object exposes only the methods and properties needed by external code.

# Context & Application
Encapsulation is one of the three pillars of OOP alongside polymorphism and inheritance. The chapter summary states: "One useful thing to do with objects is to specify an interface for them and tell everybody that they are supposed to talk to your object only through that interface. The rest of the details that make up your object are now *encapsulated*, hidden behind the interface."

# Examples
```javascript
class RandomSource {
  #max;
  constructor(max) {
    this.#max = max;
  }
  getNumber() {
    return Math.floor(Math.random() * this.#max);
  }
}
```
The `#max` field is encapsulated; only `getNumber()` is the public interface. (Ch 6, "Private Properties")

# Relationships
## Builds Upon
- object, abstract-data-type
## Enables
- private-property, interface
## Related
- class-declaration, module
## Contrasts With
- polymorphism (separates code via interfaces, while encapsulation hides details)

# Common Errors
- **Error**: Exposing all properties as public for convenience
  **Correction**: Define a clear interface and use private properties to hide implementation details

# Common Confusions
- **Confusion**: Encapsulation means using private fields exclusively
  **Clarification**: Encapsulation is the principle of separating interface from implementation; private fields are one mechanism, but conventions and closures also achieve encapsulation

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Abstract Data Types", lines 78-82, and "Private Properties", lines 396-451.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined term with clear examples in source
- Cross-reference status: verified against chapter summary
