---
# === CORE IDENTIFICATION ===
concept: Getters and Setters in Classes
slug: getters-setters-in-classes

# === CLASSIFICATION ===
category: classes
subcategory: class syntax
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Classes"
chapter_number: 9
pdf_page: 249
section: "9.3.2 Getters, Setters, and other Method Forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "accessor methods"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-keyword-syntax
extends: []
related:
  - private-fields
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define computed properties that look like fields?"
---

# Quick Definition

Getter and setter methods can be defined in class bodies using the `get` and `set` keywords, creating properties that look like fields but execute code when accessed or assigned.

# Core Definition

"Within a class body, you can define getter and setter methods just as you can in object literals. The only difference is that in class bodies, you don't put a comma after the getter or setter." All shorthand method syntaxes allowed in object literals are also allowed in class bodies, including generators and computed-name methods. (Flanagan, p. 249-250)

# Prerequisites

- **class-keyword-syntax** — Must understand class syntax

# Key Properties

1. Use `get` and `set` keywords before method name
2. No commas between methods in class bodies
3. Accessed like properties, not called like methods
4. Can be used to provide read-only access (getter without setter)
5. Works with private fields for encapsulation

# Construction / Recognition

```javascript
class C {
    get propertyName() { return this._value; }
    set propertyName(v) { this._value = v; }
}
```

# Context & Application

Used for computed properties, validation on assignment, and providing read-only access to internal state.

# Examples

```javascript
class Complex {
    constructor(real, imaginary) {
        this.r = real;
        this.i = imaginary;
    }
    get real() { return this.r; }
    get imaginary() { return this.i; }
    get magnitude() { return Math.hypot(this.r, this.i); }
}
let c = new Complex(2, 3);
c.magnitude  // => Math.hypot(2,3); used like a property
```
(Flanagan, p. 252, Example 9-4)

# Relationships

## Builds Upon
- **class-keyword-syntax** — Part of class syntax

## Enables
- Computed properties and validation

## Related
- **private-fields** — Getters often provide read-only access to private fields

## Contrasts With
- None specific

# Common Errors

- **Error**: Calling a getter as a method with parentheses.
  **Correction**: Getters are accessed like properties: `obj.prop`, not `obj.prop()`.

# Common Confusions

- **Confusion**: Getters and setters are just regular methods.
  **Clarification**: They are accessed with property syntax, not method call syntax.

# Source Reference

Chapter 9: Classes, Section 9.3.2, pages 249-250.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
