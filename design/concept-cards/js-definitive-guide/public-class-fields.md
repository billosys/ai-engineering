---
# === CORE IDENTIFICATION ===
concept: Public Class Fields
slug: public-class-fields

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
pdf_page: 250
section: "9.3.3 Public, Private, and Static Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "instance fields"
  - "class field declarations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-keyword-syntax
extends: []
related:
  - private-fields
  - static-fields
contrasts_with:
  - private-fields

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare instance properties in a class body?"
---

# Quick Definition

Public class fields allow declaring instance properties directly in the class body with initializer syntax (`name = value;`), making the class state visible at the top of the definition rather than buried in the constructor.

# Core Definition

"With the new instance field syntax, you could instead write" field declarations directly in the class body using `name = value;` syntax. "The field initialization code has moved out of the constructor and now appears directly in the class body. (That code is still run as part of the constructor, of course.)" Fields can be declared without initializers (defaulting to undefined). You "still must use this. to refer to these fields" on the right-hand side. (Flanagan, p. 250-251)

# Prerequisites

- **class-keyword-syntax** — Must understand class syntax

# Key Properties

1. Declared directly in class body: `fieldName = value;`
2. Uses `=` and `;` (not `:` and `,` like object literals)
3. Initialized as part of constructor execution
4. `this.` prefix removed from left side, still needed on right
5. Can declare without initializer (defaults to undefined)

# Construction / Recognition

```javascript
class Buffer {
    size = 0;
    capacity = 4096;
    buffer = new Uint8Array(this.capacity);
}
```

# Context & Application

Makes class structure immediately visible by declaring fields at the top. Widely used in React and modern JavaScript.

# Examples

```javascript
// Before (constructor-based):
class Buffer {
    constructor() {
        this.size = 0;
        this.capacity = 4096;
        this.buffer = new Uint8Array(this.capacity);
    }
}

// After (field declarations):
class Buffer {
    size = 0;
    capacity = 4096;
    buffer = new Uint8Array(this.capacity);
}
```
(Flanagan, p. 250)

# Relationships

## Builds Upon
- **class-keyword-syntax** — Extension of class syntax

## Enables
- Clear documentation of class state at the top of the definition

## Related
- **private-fields** — Private version with `#` prefix
- **static-fields** — Static version with `static` keyword

## Contrasts With
- **private-fields** — Public fields are accessible from outside; private fields are not

# Common Errors

- **Error**: Using colon instead of equals for field initialization.
  **Correction**: Class fields use `=` and `;`: `size = 0;`, not `size: 0,`.

# Common Confusions

- **Confusion**: Class bodies with fields are object literals.
  **Clarification**: Class bodies use different syntax (= and ; vs : and ,) and are not object literals.

# Source Reference

Chapter 9: Classes, Section 9.3.3, pages 250-251.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with before/after examples
- Uncertainties: Feature was being standardized at time of writing
- Cross-reference status: Verified
