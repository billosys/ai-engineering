---
# === CORE IDENTIFICATION ===
concept: Interface
slug: interface

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
  - object interface
  - public API

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - abstract-data-type
extends: []
related:
  - encapsulation
  - polymorphism
  - method
contrasts_with:
  - private-property

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an interface in object-oriented programming?"
  - "What distinguishes a method from a function?"
---

# Quick Definition
An interface is the collection of operations (methods and properties) that external code can perform on an abstract data type, defining how other code interacts with it.

# Core Definition
Haverbeke states: "Each abstract data type has an *interface*, the collection of operations that external code can perform on it. Any details beyond that interface are *encapsulated*, treated as internal to the type and of no concern to the rest of the program." (Ch 6, "Abstract Data Types")

# Prerequisites
- **Objects**: Interfaces are defined on objects
- **Abstract data types**: Interfaces are the public face of ADTs

# Key Properties
1. Defines the publicly accessible methods and properties
2. Serves as a contract between the type and its users
3. Enables polymorphism when multiple types share the same interface
4. Module interfaces have much in common with object interfaces (Ch 10)

# Construction / Recognition
An interface is recognized as the set of public methods and properties a type exposes. In JavaScript, there's no formal `interface` keyword; interfaces are implicit contracts.

# Context & Application
Interfaces are central to polymorphism: "When a piece of code is written to work with objects that have a certain interface---in this case, a `toString` method---any kind of object that happens to support this interface can be plugged into the code and will be able to work with it." (Ch 6, "Polymorphism")

# Examples
The iterator interface requires a `next` method returning `{value, done}`:
```javascript
let okIterator = "OK"[Symbol.iterator]();
console.log(okIterator.next());
// -> {value: "O", done: false}
console.log(okIterator.next());
// -> {value: "K", done: false}
console.log(okIterator.next());
// -> {value: undefined, done: true}
```
(Ch 6, "The iterator interface")

# Relationships
## Builds Upon
- object, abstract-data-type
## Enables
- polymorphism, iterator-protocol
## Related
- encapsulation, method, module
## Contrasts With
- private-property (internal, not part of interface)

# Common Errors
- **Error**: Assuming JavaScript has a formal interface mechanism
  **Correction**: JavaScript interfaces are implicit; they're conventions about what methods/properties an object should have

# Common Confusions
- **Confusion**: An interface is the same as a class
  **Clarification**: An interface describes what operations are available; a class is an implementation that provides those operations

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Abstract Data Types", lines 78-92, and "Polymorphism", lines 610-660.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined and used throughout chapter
- Cross-reference status: verified against Ch 10 module interfaces
