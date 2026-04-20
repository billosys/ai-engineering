---
# === CORE IDENTIFICATION ===
concept: Augmenting Prototypes (Monkey-Patching)
slug: augmenting-prototypes

# === CLASSIFICATION ===
category: classes
subcategory: prototypes
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Classes"
chapter_number: 9
pdf_page: 253
section: "9.4 Adding Methods to Existing Classes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "monkey-patching"
  - "prototype augmentation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classes-and-prototypes
  - constructor-functions
extends: []
related:
  - class-keyword-syntax
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can I add methods to existing classes after they are defined?"
---

# Quick Definition

JavaScript's dynamic prototype system allows adding new methods to any class at any time by assigning to the constructor's prototype, even for built-in classes -- though modifying built-in prototypes is generally discouraged.

# Core Definition

"JavaScript's prototype-based inheritance mechanism is dynamic: an object inherits properties from its prototype, even if the properties of the prototype change after the object is created. This means that we can augment JavaScript classes simply by adding new methods to their prototype objects." "Adding methods to the prototypes of built-in types like this is generally considered to be a bad idea because it will cause confusion and compatibility problems in the future." (Flanagan, p. 253-254)

# Prerequisites

- **classes-and-prototypes** — Must understand prototype inheritance
- **constructor-functions** — Prototypes are properties of constructors

# Key Properties

1. Prototype modifications are visible to all existing and future instances
2. Works for user-defined and built-in classes
3. Modifying built-in prototypes (e.g., Object.prototype) is bad practice
4. Can cause compatibility problems with future language versions
5. Adding to Object.prototype makes properties visible to for/in loops

# Construction / Recognition

```javascript
Complex.prototype.conj = function() { return new Complex(this.r, -this.i); };
```

# Context & Application

Used for polyfilling missing features in older environments. Generally avoided for built-in types to prevent conflicts.

# Examples

```javascript
// Adding method to user class:
Complex.prototype.conj = function() { return new Complex(this.r, -this.i); };

// Polyfilling a built-in (only if not already defined):
if (!String.prototype.startsWith) {
    String.prototype.startsWith = function(s) {
        return this.indexOf(s) === 0;
    };
}
```
(Flanagan, p. 253-254)

# Relationships

## Builds Upon
- **classes-and-prototypes** — Exploits dynamic prototype inheritance
- **constructor-functions** — Modifies Constructor.prototype

## Enables
- Polyfilling missing methods
- Extending existing classes

## Related
- **class-keyword-syntax** — Subclassing is often preferred over monkey-patching

## Contrasts With
- None specific

# Common Errors

- **Error**: Adding methods to Object.prototype without making them non-enumerable.
  **Correction**: Use Object.defineProperty() to make added properties non-enumerable, or avoid modifying Object.prototype entirely.

# Common Confusions

- **Confusion**: Modifying built-in prototypes is a good way to add utility methods.
  **Clarification**: It is "generally considered to be a bad idea" because it can cause conflicts with future JavaScript versions.

# Source Reference

Chapter 9: Classes, Section 9.4, pages 253-254.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with warning
- Uncertainties: None
- Cross-reference status: Verified
