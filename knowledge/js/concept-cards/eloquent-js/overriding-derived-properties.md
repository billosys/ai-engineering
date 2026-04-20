---
# === CORE IDENTIFICATION ===
concept: Overriding Derived Properties
slug: overriding-derived-properties

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: inheritance-mechanism
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "Overriding derived properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - property shadowing
  - property overriding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - prototype
  - prototype-chain
extends: []
related:
  - inheritance
  - polymorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens when an object has a property with the same name as one in its prototype?"
---

# Quick Definition
When a property is added to an object that already exists in its prototype, the new property shadows the prototype's version, affecting only that object while leaving the prototype intact.

# Core Definition
Haverbeke explains: "When you add a property to an object, whether it is present in the prototype or not, the property is added to the object *itself*. If there was already a property with the same name in the prototype, this property will no longer affect the object, as it is now hidden behind the object's own property." (Ch 6, "Overriding derived properties")

# Prerequisites
- **Prototypes**: Understanding that properties are looked up through the prototype chain
- **Prototype chain**: The mechanism by which inherited properties are found

# Key Properties
1. Own properties shadow prototype properties of the same name
2. The prototype property remains unchanged
3. Other objects sharing the prototype still see the original value
4. Commonly used to customize behavior of specific instances

# Construction / Recognition
Overriding is detected when an object has its own property that shares a name with a prototype property.

# Context & Application
Overriding is used to express exceptional properties in specific instances while keeping defaults in the prototype. It's also how `Array.prototype.toString` provides a different implementation than `Object.prototype.toString`.

# Examples
```javascript
Rabbit.prototype.teeth = "small";
console.log(killerRabbit.teeth);
// -> small
killerRabbit.teeth = "long, sharp, and bloody";
console.log(killerRabbit.teeth);
// -> long, sharp, and bloody
console.log((new Rabbit("basic")).teeth);
// -> small
console.log(Rabbit.prototype.teeth);
// -> small
```
(Ch 6, "Overriding derived properties", lines 462-473)

# Relationships
## Builds Upon
- prototype, prototype-chain
## Enables
- polymorphism (different objects can override toString differently)
## Related
- inheritance
## Contrasts With
- N/A

# Common Errors
- **Error**: Expecting property assignment to modify the prototype
  **Correction**: Assigning a property always creates it on the object itself, never modifying the prototype

# Common Confusions
- **Confusion**: Overriding a property deletes it from the prototype
  **Clarification**: The prototype property remains; the object's own property simply shadows it during lookup

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Overriding derived properties", lines 453-515.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly explained with clear examples
- Cross-reference status: verified
