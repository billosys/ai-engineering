---
# === CORE IDENTIFICATION ===
concept: Object.create
slug: object-create

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: object-creation
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "Prototypes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - prototype
extends: []
related:
  - prototype-chain
  - class-declaration
  - constructor
contrasts_with:
  - class-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create an object with a specific prototype?"
---

# Quick Definition
`Object.create` is a method that creates a new object with a specified prototype, allowing direct control over the prototype chain without using constructors or classes.

# Core Definition
Haverbeke states: "You can use `Object.create` to create an object with a specific prototype." (Ch 6, "Prototypes") This is the most direct way to establish prototype relationships.

# Prerequisites
- **Objects**: The result is a new object
- **Prototypes**: You must understand prototypes to use this meaningfully

# Key Properties
1. Takes a prototype object as its first argument
2. Returns a new object linked to that prototype
3. Passing `null` creates an object with no prototype (useful for maps)
4. Pre-dates the `class` syntax as a way to set up prototype relationships

# Construction / Recognition
```javascript
let protoRabbit = {
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
};
let blackRabbit = Object.create(protoRabbit);
blackRabbit.type = "black";
```

# Context & Application
`Object.create` is useful for creating objects with specific prototypes without the ceremony of class declarations. Passing `null` creates prototype-free objects safe for use as maps.

# Examples
```javascript
let protoRabbit = {
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
};
let blackRabbit = Object.create(protoRabbit);
blackRabbit.type = "black";
blackRabbit.speak("I am fear and darkness");
// -> The black rabbit says 'I am fear and darkness'

// Creating a prototype-free object for use as a map
console.log("toString" in Object.create(null));
// -> false
```
(Ch 6, "Prototypes", lines 239-249, and "Maps", lines 556-563)

# Relationships
## Builds Upon
- prototype, object
## Enables
- prototype-chain
## Related
- class-declaration, constructor
## Contrasts With
- class-declaration (provides more structure for creating types)

# Common Errors
- **Error**: Using `Object.create` when a class would be more appropriate
  **Correction**: For types with constructors and methods, prefer `class` syntax; use `Object.create` for simple prototype delegation or prototype-free objects

# Common Confusions
- **Confusion**: `Object.create(proto)` copies properties from proto
  **Clarification**: It creates a link; the new object delegates to the prototype, it doesn't copy its properties

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Prototypes", lines 236-249.

# Verification Notes
- Definition source: direct
- Confidence rationale: Directly demonstrated with code examples
- Cross-reference status: verified
