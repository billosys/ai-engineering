---
# === CORE IDENTIFICATION ===
concept: Delegation Instead of Inheritance
slug: delegation-vs-inheritance

# === CLASSIFICATION ===
category: classes
subcategory: design patterns
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Classes"
chapter_number: 9
pdf_page: 259
section: "9.5.3 Delegation Instead of Inheritance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "composition over inheritance"
  - "wrapping"
  - "object composition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subclassing-with-extends
  - class-keyword-syntax
extends: []
related:
  - factory-function-pattern
contrasts_with:
  - subclassing-with-extends

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use composition instead of class inheritance?"
---

# Quick Definition

Delegation (composition) creates a class that wraps an instance of another class and forwards method calls to it, rather than subclassing. This follows the principle "favor composition over inheritance."

# Core Definition

"If you want to write a class that shares the behavior of some other class, you can try to inherit that behavior by creating a subclass. But it is often easier and more flexible to get that desired behavior into your class by having your class create an instance of the other class and simply delegating to that instance as needed." "This delegation approach is often called 'composition,' and it is an oft-quoted maxim of object-oriented programming that one should 'favor composition over inheritance.'" (Flanagan, p. 259)

# Prerequisites

- **subclassing-with-extends** — Must understand inheritance to see the alternative
- **class-keyword-syntax** — Delegation uses class syntax too

# Key Properties

1. Class creates and holds an instance of another class
2. Methods delegate to the held instance
3. No formal inheritance relationship (no instanceof)
4. More flexible than inheritance
5. Decouples the implementation from the interface

# Construction / Recognition

```javascript
class Histogram {
    constructor() { this.map = new Map(); }
    count(key) { return this.map.get(key) || 0; }
    has(key) { return this.count(key) > 0; }
    add(key) { this.map.set(key, this.count(key) + 1); }
    // ... delegates to this.map
}
```

# Context & Application

Preferred when you want similar behavior without tight coupling. A Histogram is like a Set but uses Map internally -- composition is simpler than subclassing.

# Examples

```javascript
class Histogram {
    constructor() { this.map = new Map(); }
    count(key) { return this.map.get(key) || 0; }
    has(key) { return this.count(key) > 0; }
    get size() { return this.map.size; }
    add(key) { this.map.set(key, this.count(key) + 1); }
    delete(key) {
        let count = this.count(key);
        if (count === 1) this.map.delete(key);
        else if (count > 1) this.map.set(key, count - 1);
    }
    [Symbol.iterator]() { return this.map.keys(); }
    keys() { return this.map.keys(); }
    values() { return this.map.values(); }
    entries() { return this.map.entries(); }
}
```
(Flanagan, p. 259-260, Example 9-7)

# Relationships

## Builds Upon
- **subclassing-with-extends** — Understanding inheritance clarifies when delegation is better
- **class-keyword-syntax** — Delegation uses class syntax

## Enables
- Flexible, loosely-coupled class design

## Related
- **factory-function-pattern** — Another non-inheritance approach to class creation

## Contrasts With
- **subclassing-with-extends** — Inheritance creates tight coupling; delegation is looser

# Common Errors

- **Error**: Always reaching for `extends` when composition would be simpler.
  **Correction**: Consider whether you truly need an is-a relationship or just need to use another class's behavior.

# Common Confusions

- **Confusion**: Delegation requires an inheritance relationship.
  **Clarification**: Delegation creates no formal inheritance. The delegating class is not an instance of the delegated-to class.

# Source Reference

Chapter 9: Classes, Section 9.5.3, pages 259-260.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with complete example
- Uncertainties: None
- Cross-reference status: Verified
