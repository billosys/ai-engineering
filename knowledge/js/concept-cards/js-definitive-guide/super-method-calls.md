---
# === CORE IDENTIFICATION ===
concept: super.method() Calls
slug: super-method-calls

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
aliases:
  - "superclass method invocation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subclassing-with-extends
  - super-in-constructors
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I call an overridden method from the superclass?"
---

# Quick Definition

`super.method()` in a subclass calls the overridden version of a method from the superclass, allowing subclasses to extend rather than replace superclass behavior.

# Core Definition

"In this context, super works much like the this keyword does: it refers to the current object but allows access to overridden methods defined in the superclass." A subclass method that overrides a superclass method "is not required to invoke the superclass method. If it does use super to invoke the overridden method, it can do that at the beginning or the middle or the end of the overriding method." (Flanagan, p. 258-259)

# Prerequisites

- **subclassing-with-extends** — Must understand class inheritance
- **super-in-constructors** — Understanding super keyword usage

# Key Properties

1. `super.method(args)` calls the superclass version
2. Not required -- overriding methods may or may not call super
3. Can be called at any point in the overriding method
4. `super` refers to the current object but accesses superclass methods

# Construction / Recognition

```javascript
class TypedMap extends Map {
    set(key, value) {
        // Subclass validation...
        return super.set(key, value);  // Delegate to superclass
    }
}
```

# Context & Application

Used when a subclass needs to add behavior around (before/after/instead of) the superclass's implementation.

# Examples

```javascript
class TypedMap extends Map {
    set(key, value) {
        if (this.keyType && typeof key !== this.keyType) {
            throw new TypeError(`${key} is not of type ${this.keyType}`);
        }
        if (this.valueType && typeof value !== this.valueType) {
            throw new TypeError(`${value} is not of type ${this.valueType}`);
        }
        return super.set(key, value);  // Invoke superclass set()
    }
}
```
(Flanagan, p. 257-258, Example 9-6)

# Relationships

## Builds Upon
- **subclassing-with-extends** — Used within subclass methods
- **super-in-constructors** — Same keyword, different context

## Enables
- Extending superclass behavior without replacing it

## Related
- None specific

## Contrasts With
- None specific

# Common Errors

- **Error**: Forgetting to return the value of super.method() when the superclass method returns a value.
  **Correction**: If the superclass method returns a value (like Map.set() for chaining), use `return super.set(...)`.

# Common Confusions

- **Confusion**: super.method() must be called in overriding methods.
  **Clarification**: It is optional. An overriding method can completely replace the superclass implementation.

# Source Reference

Chapter 9: Classes, Section 9.5.2, pages 258-259.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with example
- Uncertainties: None
- Cross-reference status: Verified
