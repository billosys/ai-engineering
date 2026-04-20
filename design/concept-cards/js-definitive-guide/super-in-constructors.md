---
# === CORE IDENTIFICATION ===
concept: super() in Constructors
slug: super-in-constructors

# === CLASSIFICATION ===
category: classes
subcategory: inheritance
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Classes"
chapter_number: 9
pdf_page: 258
section: "9.5.2 Subclasses with extends and super"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subclassing-with-extends
extends: []
related:
  - super-method-calls
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I call the parent class constructor from a subclass?"
---

# Quick Definition

`super()` in a subclass constructor invokes the superclass constructor. It must be called before using `this`, and if omitted entirely, an implicit constructor calling `super(...args)` is created.

# Core Definition

Rules for super() in constructors: "If you define a class with the extends keyword, then the constructor for your class must use super() to invoke the superclass constructor." "If you don't define a constructor in your subclass, one will be defined automatically for you" that passes all arguments to super(). "You may not use the this keyword in your constructor until after you have invoked the superclass constructor with super(). This enforces a rule that superclasses get to initialize themselves before subclasses do." (Flanagan, p. 258)

# Prerequisites

- **subclassing-with-extends** — super() is used within subclass constructors

# Key Properties

1. Must be called before using `this` in subclass constructors
2. Invokes the superclass constructor
3. If no constructor defined in subclass, implicit one calls super()
4. new.target in the superclass constructor references the subclass constructor
5. Passes arguments to superclass constructor

# Construction / Recognition

```javascript
class Sub extends Super {
    constructor(a, b) {
        super(a);  // Must come before this
        this.b = b;
    }
}
```

# Context & Application

Essential for proper initialization of subclass instances. The superclass must initialize first.

# Examples

```javascript
class TypedMap extends Map {
    constructor(keyType, valueType, entries) {
        // Validate entries...
        super(entries);  // Initialize Map superclass
        this.keyType = keyType;    // Then initialize subclass
        this.valueType = valueType;
    }
}
```
(Flanagan, p. 257-258, Example 9-6)

# Relationships

## Builds Upon
- **subclassing-with-extends** — super() is part of subclassing

## Enables
- Proper superclass initialization in subclasses

## Related
- **super-method-calls** — super.method() for calling overridden methods

## Contrasts With
- None specific

# Common Errors

- **Error**: Using `this` before calling `super()`.
  **Correction**: JavaScript enforces that super() must be called first in subclass constructors.

# Common Confusions

- **Confusion**: super() is optional in subclass constructors.
  **Clarification**: If you define a constructor with extends, super() is required.

# Source Reference

Chapter 9: Classes, Section 9.5.2, page 258.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clear rules enumerated
- Uncertainties: None
- Cross-reference status: Verified
