---
# === CORE IDENTIFICATION ===
concept: Abstract Classes
slug: abstract-classes

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
pdf_page: 261
section: "9.5.4 Class Hierarchies and Abstract Classes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "base classes"
  - "incomplete classes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subclassing-with-extends
  - class-keyword-syntax
extends: []
related:
  - delegation-vs-inheritance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can JavaScript have abstract classes like Java?"
---

# Quick Definition

Abstract classes in JavaScript are classes with incomplete implementations (methods that throw errors) that serve as superclasses for concrete subclasses. JavaScript has no formal `abstract` keyword; the pattern is implemented by convention.

# Core Definition

The text "defines lots of subclasses, but it also demonstrates how you can define abstract classes -- classes that do not include a complete implementation -- to serve as a common superclass for a group of related subclasses. An abstract superclass can define a partial implementation that all subclasses inherit and share. The subclasses, then, only need to define their own unique behavior by implementing the abstract methods defined -- but not implemented -- by the superclass. Note that JavaScript does not have any formal definition of abstract methods or abstract classes." (Flanagan, p. 261)

# Prerequisites

- **subclassing-with-extends** — Abstract classes are used with extends
- **class-keyword-syntax** — Must understand class syntax

# Key Properties

1. No formal `abstract` keyword in JavaScript
2. Abstract methods throw Error when called directly
3. Concrete subclasses implement the abstract methods
4. Abstract superclass can implement concrete methods based on abstract ones
5. Convention-based pattern

# Construction / Recognition

```javascript
class AbstractSet {
    has(x) { throw new Error("Abstract method"); }
}
class ConcreteSet extends AbstractSet {
    has(x) { /* actual implementation */ }
}
```

# Context & Application

Used to define class hierarchies where a common interface is shared but implementations vary. Example 9-8 shows AbstractSet, AbstractEnumerableSet, and AbstractWritableSet.

# Examples

```javascript
class AbstractSet {
    has(x) { throw new Error("Abstract method"); }
}

class AbstractEnumerableSet extends AbstractSet {
    get size() { throw new Error("Abstract method"); }
    [Symbol.iterator]() { throw new Error("Abstract method"); }
    isEmpty() { return this.size === 0; }  // concrete method using abstract
    toString() { return `{${Array.from(this).join(", ")}}`; }
}

class SingletonSet extends AbstractEnumerableSet {
    constructor(member) { super(); this.member = member; }
    has(x) { return x === this.member; }
    get size() { return 1; }
    *[Symbol.iterator]() { yield this.member; }
}
```
(Flanagan, p. 261-263, Example 9-8)

# Relationships

## Builds Upon
- **subclassing-with-extends** — Abstract classes use extends hierarchy
- **class-keyword-syntax** — Built with class syntax

## Enables
- Separating interface from implementation
- Class hierarchies with shared behavior

## Related
- **delegation-vs-inheritance** — Alternative design approach

## Contrasts With
- None specific

# Common Errors

- **Error**: Instantiating an abstract class directly and expecting it to work.
  **Correction**: Abstract classes have unimplemented methods that will throw errors. Only instantiate concrete subclasses.

# Common Confusions

- **Confusion**: JavaScript has formal abstract class support.
  **Clarification**: There is no `abstract` keyword. The pattern is purely conventional, using methods that throw Error.

# Source Reference

Chapter 9: Classes, Section 9.5.4, pages 261-263.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with extensive Example 9-8
- Uncertainties: None
- Cross-reference status: Verified
