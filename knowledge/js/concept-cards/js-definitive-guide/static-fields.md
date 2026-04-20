---
# === CORE IDENTIFICATION ===
concept: Static Fields
slug: static-fields

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
pdf_page: 251
section: "9.3.3 Public, Private, and Static Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "class-level fields"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-keyword-syntax
  - static-methods
extends: []
related:
  - public-class-fields
  - private-fields
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define class-level constants or shared data?"
---

# Quick Definition

Static fields are declared with the `static` keyword before a field declaration, creating properties on the constructor function rather than on instances.

# Core Definition

"A related proposal seeks to standardize the use of the static keyword for fields. If you add static before a public or private field declaration, those fields will be created as properties of the constructor function instead of properties of instances." Static fields can also be private with `#`. Without the field syntax, static fields must be defined outside the class body: `ClassName.fieldName = value;` (Flanagan, p. 251-252)

# Prerequisites

- **class-keyword-syntax** — Must understand class syntax
- **static-methods** — Same `static` keyword mechanism

# Key Properties

1. `static fieldName = value;` in class body
2. Property of the constructor, not instances
3. Can be public or private (`static #field`)
4. Without field syntax, defined as: `ClassName.field = value` after class

# Construction / Recognition

```javascript
class Range {
    static integerRangePattern = /^\((\d+)\.\.\.(\d+)\)$/;
}
// Or without field syntax:
Complex.ZERO = new Complex(0,0);
```

# Context & Application

Used for class-level constants, configuration, and shared data.

# Examples

```javascript
// With field syntax:
class Range {
    static integerRangePattern = /^\((\d+)\.\.\.(\d+)\)$/;
}

// Without field syntax (works in all environments):
Complex.ZERO = new Complex(0,0);
Complex.ONE = new Complex(1,0);
Complex.I = new Complex(0,1);
```
(Flanagan, p. 251-253)

# Relationships

## Builds Upon
- **class-keyword-syntax** — Part of class syntax
- **static-methods** — Same mechanism for methods

## Enables
- Class-level constants and configuration

## Related
- **public-class-fields** — Instance field equivalent
- **private-fields** — Can be combined with static

## Contrasts With
- None specific

# Common Errors

- **Error**: Accessing static fields on instances.
  **Correction**: Static fields are on the constructor/class, not on instances.

# Common Confusions

- **Confusion**: Static fields are shared mutable state among instances.
  **Clarification**: Static fields are on the class itself. Instances don't directly see them (must access via ClassName.field).

# Source Reference

Chapter 9: Classes, Section 9.3.3, pages 251-252.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: Feature was being standardized at time of writing
- Cross-reference status: Verified
