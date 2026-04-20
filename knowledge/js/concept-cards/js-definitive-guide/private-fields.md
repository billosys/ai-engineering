---
# === CORE IDENTIFICATION ===
concept: Private Fields (#field)
slug: private-fields

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
  - "hash-prefixed fields"
  - "private class fields"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-keyword-syntax
  - public-class-fields
extends: []
related:
  - closure-based-private-state
  - getters-setters-in-classes
contrasts_with:
  - public-class-fields
  - closure-based-private-state

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with private fields in JavaScript?"
---

# Quick Definition

Private fields use the `#` prefix in their names and are only accessible within the class body, providing true encapsulation that is invisible and inaccessible to external code.

# Core Definition

"If you use the instance field initialization syntax to define a field whose name begins with # (which is not normally a legal character in JavaScript identifiers), that field will be usable (with the # prefix) within the class body but will be invisible and inaccessible (and therefore immutable) to any code outside of the class body." "Private fields must be declared using this new field syntax before they can be used. You can't just write this.#size = 0; in the constructor of a class unless you include a 'declaration' of the field directly in the class body." (Flanagan, p. 251)

# Prerequisites

- **class-keyword-syntax** — Must understand class syntax
- **public-class-fields** — Private fields use same syntax with # prefix

# Key Properties

1. Name begins with `#` (e.g., `#size`)
2. Must be declared in the class body before use
3. Only accessible within the class body
4. Invisible and inaccessible from outside
5. Can be combined with a getter for read-only access
6. The `#` is part of the name (always used with it)

# Construction / Recognition

```javascript
class Buffer {
    #size = 0;
    get size() { return this.#size; }
}
```

# Context & Application

Provides true encapsulation in JavaScript classes, replacing the closure-based privacy pattern with native syntax.

# Examples

```javascript
class Buffer {
    #size = 0;
    get size() { return this.#size; }
}

let b = new Buffer();
b.size      // => 0 (via getter)
b.#size     // SyntaxError: private field not accessible outside class
```
(Flanagan, p. 251)

# Relationships

## Builds Upon
- **class-keyword-syntax** — Part of class syntax
- **public-class-fields** — Same declaration syntax with # prefix

## Enables
- True encapsulation in classes

## Related
- **closure-based-private-state** — Pre-ES6 alternative for private state
- **getters-setters-in-classes** — Often used together for read-only access

## Contrasts With
- **public-class-fields** — Public fields are accessible from outside; private are not
- **closure-based-private-state** — Different mechanism (# syntax vs. function scope)

# Common Errors

- **Error**: Using `this.#field` in the constructor without declaring the field in the class body.
  **Correction**: Private fields must be declared in the class body before they can be used, even in the constructor.

# Common Confusions

- **Confusion**: The `#` is just a naming convention like `_` for private properties.
  **Clarification**: The `#` provides true privacy enforced by the language. External code gets a SyntaxError, not just a convention violation.

# Source Reference

Chapter 9: Classes, Section 9.3.3, page 251.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: Feature was being standardized at time of writing
- Cross-reference status: Verified
