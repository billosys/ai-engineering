---
# === CORE IDENTIFICATION ===
concept: instanceof Operator
slug: instanceof-operator

# === CLASSIFICATION ===
category: classes
subcategory: class identity
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Classes"
chapter_number: 9
pdf_page: 243
section: "9.2.1 Constructors, Class Identity, and instanceof"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - constructor-functions
  - classes-and-prototypes
extends: []
related:
  - constructor-property
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I check if an object is an instance of a class?"
  - "How does the prototype chain relate to class inheritance?"
---

# Quick Definition

The `instanceof` operator tests whether an object's prototype chain includes the `prototype` property of a constructor function, checking class membership through prototype inheritance.

# Core Definition

"The expression o instanceof C evaluates to true if o inherits from C.prototype. The inheritance need not be direct: if o inherits from an object that inherits from an object that inherits from C.prototype, the expression will still evaluate to true." Technically, instanceof is "not checking whether r was actually initialized by the Range constructor. Instead, it is checking whether r inherits from Range.prototype." (Flanagan, p. 243-244)

# Prerequisites

- **constructor-functions** — instanceof uses constructor's prototype property
- **classes-and-prototypes** — Must understand prototype chains

# Key Properties

1. Checks prototype chain, not actual constructor used
2. Walks up entire prototype chain (not just direct prototype)
3. Uses the constructor as the right-hand operand
4. Two objects from different constructors with same prototype pass instanceof for both
5. Alternative: `isPrototypeOf()` for constructor-less classes

# Construction / Recognition

```javascript
obj instanceof Constructor  // boolean
```

# Context & Application

Used for type checking and polymorphism in class hierarchies.

# Examples

```javascript
r instanceof Range  // => true: r inherits from Range.prototype

// Prototype sharing quirk:
function Strange() {}
Strange.prototype = Range.prototype;
new Strange() instanceof Range  // => true (same prototype!)

// For constructor-less classes:
range.methods.isPrototypeOf(r)  // => true
```
(Flanagan, p. 243-244)

# Relationships

## Builds Upon
- **constructor-functions** — Uses constructor's prototype property
- **classes-and-prototypes** — Checks prototype chain

## Enables
- Type checking and class membership testing

## Related
- **constructor-property** — Another way to determine class identity

## Contrasts With
- None specific

# Common Errors

- **Error**: Expecting instanceof to check which constructor actually created the object.
  **Correction**: instanceof only checks the prototype chain. Any object inheriting from C.prototype passes `instanceof C`.

# Common Confusions

- **Confusion**: instanceof verifies the constructor that created an object.
  **Clarification**: It verifies prototype chain inheritance, not construction history.

# Source Reference

Chapter 9: Classes, Section 9.2.1, pages 243-244.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with edge cases
- Uncertainties: None
- Cross-reference status: Verified
