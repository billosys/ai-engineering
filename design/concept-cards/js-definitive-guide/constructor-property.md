---
# === CORE IDENTIFICATION ===
concept: constructor Property
slug: constructor-property

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
pdf_page: 245
section: "9.2.2 The constructor Property"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - constructor-functions
extends: []
related:
  - instanceof-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the constructor property relate to prototypes?"
---

# Quick Definition

Every regular function automatically has a `prototype` property whose value is an object with a non-enumerable `constructor` property pointing back to the function itself. Instances inherit this `constructor` reference.

# Core Definition

"Every regular JavaScript function automatically has a prototype property. The value of this property is an object that has a single, non-enumerable constructor property. The value of the constructor property is the function object." This means "objects typically inherit a constructor property that refers to their constructor" and "this constructor property gives the class of an object." (Flanagan, p. 245-246)

# Prerequisites

- **constructor-functions** — Must understand how constructors and prototypes work

# Key Properties

1. `F.prototype.constructor === F` for any regular function F
2. Instances inherit the `constructor` property from their prototype
3. Non-enumerable by default
4. Can be lost when overwriting the prototype object (must be re-added explicitly)
5. Provides back-reference from instances to their constructor

# Construction / Recognition

```javascript
let F = function() {};
let p = F.prototype;
let c = p.constructor;
c === F  // => true: F.prototype.constructor === F
```

# Context & Application

The constructor property allows determining the class of an object. When overwriting a prototype, remember to restore the constructor property.

# Examples

```javascript
let F = function() {};
let p = F.prototype;
let c = p.constructor;
c === F  // => true

let o = new F();
o.constructor === F  // => true

// Must restore constructor when overwriting prototype:
Range.prototype = {
    constructor: Range,  // explicitly set back-reference
    /* method definitions */
};
```
(Flanagan, p. 245-246)

# Relationships

## Builds Upon
- **constructor-functions** — Constructor property is a feature of constructor patterns

## Enables
- Class identity detection via `obj.constructor`

## Related
- **instanceof-operator** — Another way to check class membership

## Contrasts With
- None specific

# Common Errors

- **Error**: Overwriting the prototype object without restoring the constructor property.
  **Correction**: When replacing a prototype, explicitly include `constructor: ConstructorName`.

# Common Confusions

- **Confusion**: The constructor property is reliable for class detection.
  **Clarification**: It can be lost when prototypes are overwritten and is not always present.

# Source Reference

Chapter 9: Classes, Section 9.2.2, pages 245-246.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with figure reference
- Uncertainties: None
- Cross-reference status: Verified
