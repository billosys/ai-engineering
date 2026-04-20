---
# === CORE IDENTIFICATION ===
concept: new.target
slug: new-target

# === CLASSIFICATION ===
category: functions
subcategory: invocation
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Classes"
chapter_number: 9
pdf_page: 242
section: "9.2 Classes and Constructors - Constructors and new.target"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - constructor-invocation
extends: []
related:
  - constructor-functions
  - subclassing-with-extends
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can a function detect whether it was called with new?"
---

# Quick Definition

`new.target` is a special expression available inside function bodies: it is defined (referencing the constructor) when the function was invoked with `new`, and `undefined` when invoked as a regular function.

# Core Definition

"Within a function body, you can tell whether the function has been invoked as a constructor with the special expression new.target. If the value of that expression is defined, then you know that the function was invoked as a constructor, with the new keyword." In subclass constructors, "new.target is not always a reference to the constructor it is used in: it might also refer to the constructor function of a subclass." (Flanagan, p. 242-243)

# Prerequisites

- **constructor-invocation** — Must understand constructor invocation pattern

# Key Properties

1. Defined inside constructors invoked with `new`
2. `undefined` when function is called without `new`
3. References the actual constructor that was invoked
4. In subclasses, references the subclass constructor, not the superclass

# Construction / Recognition

```javascript
function C() {
    if (!new.target) return new C();
    // initialization code
}
```

# Context & Application

Used to create constructors that work both with and without `new`, and for logging/debugging in class hierarchies.

# Examples

```javascript
function C() {
    if (!new.target) return new C();
    // initialization code goes here
}
// This technique only works for old-style constructors.
// Classes created with class keyword require new.
```
(Flanagan, p. 243)

# Relationships

## Builds Upon
- **constructor-invocation** — new.target detects constructor invocation

## Enables
- Dual-mode constructors (with/without new)

## Related
- **constructor-functions** — Used within constructor functions
- **subclassing-with-extends** — new.target references subclass constructor

## Contrasts With
- None specific

# Common Errors

- **Error**: Using new.target in arrow functions expecting it to reference the constructor.
  **Correction**: Arrow functions inherit new.target from the enclosing function.

# Common Confusions

- **Confusion**: new.target always references the function it appears in.
  **Clarification**: In subclass constructors, new.target references the actual subclass constructor, not the superclass.

# Source Reference

Chapter 9: Classes, Section 9.2, pages 242-243.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly explained
- Uncertainties: None
- Cross-reference status: Verified
