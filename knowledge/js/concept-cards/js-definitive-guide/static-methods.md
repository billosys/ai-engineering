---
# === CORE IDENTIFICATION ===
concept: Static Methods
slug: static-methods

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
section: "9.3.1 Static Methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "class methods"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-keyword-syntax
extends: []
related:
  - static-fields
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define methods on the class itself rather than on instances?"
---

# Quick Definition

Static methods are defined with the `static` keyword and become properties of the constructor function rather than the prototype, invoked through the class name rather than instances.

# Core Definition

"You can define a static method within a class body by prefixing the method declaration with the static keyword. Static methods are defined as properties of the constructor function rather than properties of the prototype object." They are "invoked using the name of the class/constructor" and "it almost never makes sense to use the this keyword in a static method." (Flanagan, p. 249)

# Prerequisites

- **class-keyword-syntax** — Must understand class syntax

# Key Properties

1. Prefixed with `static` keyword in class body
2. Property of the constructor function, not the prototype
3. Called on the class, not on instances
4. `this` is rarely useful in static methods
5. Inherited by subclasses (with extends)

# Construction / Recognition

```javascript
class Range {
    static parse(s) {
        let matches = s.match(/^\((\d+)\.\.\.(\d+)\)$/);
        if (!matches) throw new TypeError(`Cannot parse Range from "${s}".`);
        return new Range(parseInt(matches[1]), parseInt(matches[2]));
    }
}
```

# Context & Application

Used for factory methods, utility functions, and methods that operate on the class level rather than instance level.

# Examples

```javascript
class Range {
    static parse(s) {
        let matches = s.match(/^\((\d+)\.\.\.(\d+)\)$/);
        if (!matches) throw new TypeError(`Cannot parse Range from "${s}".`);
        return new Range(parseInt(matches[1]), parseInt(matches[2]));
    }
}
let r = Range.parse('(1...10)');  // Returns a new Range object
r.parse('(1...10)');              // TypeError: r.parse is not a function
```
(Flanagan, p. 249)

# Relationships

## Builds Upon
- **class-keyword-syntax** — Static methods are part of class syntax

## Enables
- Factory methods and class-level utilities

## Related
- **static-fields** — Static properties (data) on the class

## Contrasts With
- None specific (contrasts with instance methods)

# Common Errors

- **Error**: Calling a static method on an instance.
  **Correction**: Static methods are properties of the class, not instances. Call `Range.parse()`, not `r.parse()`.

# Common Confusions

- **Confusion**: `this` in a static method refers to an instance.
  **Clarification**: In a static method, `this` refers to the constructor function (the class itself), not any instance.

# Source Reference

Chapter 9: Classes, Section 9.3.1, page 249.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
