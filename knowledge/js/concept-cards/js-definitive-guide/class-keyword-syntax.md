---
# === CORE IDENTIFICATION ===
concept: class Keyword Syntax
slug: class-keyword-syntax

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
pdf_page: 246
section: "9.3 Classes with the class Keyword"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ES6 classes"
  - "class declaration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - constructor-functions
  - classes-and-prototypes
extends: []
related:
  - static-methods
  - getters-setters-in-classes
  - public-class-fields
  - private-fields
contrasts_with:
  - constructor-functions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with private fields in JavaScript?"
  - "What must I understand before learning about class inheritance with extends?"
---

# Quick Definition

The ES6 `class` keyword provides a cleaner syntax for defining prototype-based classes, using `constructor` for initialization and shorthand method syntax, but is fundamentally syntactic sugar over the existing constructor/prototype mechanism.

# Core Definition

"ES6 introduced a brand-new syntax (including a class keyword) that makes it even easier to create classes." "It is important to understand that the classes defined in Examples 9-2 and 9-3 work in exactly the same way." "The new class syntax is clean and convenient but is best thought of as 'syntactic sugar' for the more fundamental class definition mechanism." Class declarations are NOT hoisted. All code within class bodies is implicitly in strict mode. (Flanagan, p. 246-248)

# Prerequisites

- **constructor-functions** — Class syntax is sugar over constructor pattern
- **classes-and-prototypes** — Must understand prototype-based inheritance

# Key Properties

1. `class` keyword followed by name and body in curly braces
2. `constructor` method defines the initialization function
3. Methods use shorthand syntax (no commas between them)
4. Not hoisted (unlike function declarations)
5. Implicitly in strict mode
6. If no constructor is defined, an empty one is implicit
7. Can have expression form: `let C = class { ... }`

# Construction / Recognition

```javascript
class Range {
    constructor(from, to) {
        this.from = from;
        this.to = to;
    }
    includes(x) { return this.from <= x && x <= this.to; }
    toString() { return `(${this.from}...${this.to})`; }
}
```

# Context & Application

The standard modern way to define classes in JavaScript. Understanding the underlying prototype mechanism helps debug and optimize.

# Examples

```javascript
class Range {
    constructor(from, to) {
        this.from = from;
        this.to = to;
    }
    includes(x) { return this.from <= x && x <= this.to; }
    *[Symbol.iterator]() {
        for (let x = Math.ceil(this.from); x <= this.to; x++) yield x;
    }
    toString() { return `(${this.from}...${this.to})`; }
}
let r = new Range(1,3);
r.includes(2)   // => true
r.toString()     // => "(1...3)"
[...r]           // => [1, 2, 3]

// Expression form:
let Square = class { constructor(x) { this.area = x * x; } };
new Square(3).area  // => 9
```
(Flanagan, p. 246-248, Example 9-3)

# Relationships

## Builds Upon
- **constructor-functions** — class syntax is sugar over constructors
- **classes-and-prototypes** — Same prototype mechanism underneath

## Enables
- **static-methods** — Defined with `static` keyword
- **getters-setters-in-classes** — Getter/setter syntax in class bodies
- **public-class-fields** — Field declarations in class bodies
- **private-fields** — Private fields with `#` prefix
- **subclassing-with-extends** — extends keyword for inheritance

## Related
- None specific

## Contrasts With
- **constructor-functions** — Older syntax, same semantics

# Common Errors

- **Error**: Using commas between methods in a class body (like object literals).
  **Correction**: Class bodies do not use commas between methods.

# Common Confusions

- **Confusion**: Class declarations are hoisted like function declarations.
  **Clarification**: Class declarations are NOT hoisted. You cannot instantiate a class before it is declared.

# Source Reference

Chapter 9: Classes, Section 9.3, pages 246-249.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Core concept, thoroughly documented
- Uncertainties: None
- Cross-reference status: Verified
