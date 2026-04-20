---
concept: Static Members
slug: static-members
category: classes
subcategory: static
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.6 Static members of classes"
extraction_confidence: high
aliases:
  - "static methods"
  - "static fields"
  - "static keyword"
prerequisites:
  - class-declaration
extends: []
related:
  - static-factory-methods
  - static-initialization-blocks
contrasts_with: []
answers_questions:
  - "How do I add methods or data to the class itself?"
---

# Quick Definition

Static members belong to the class itself (not instances), declared with the `static` keyword, and include methods, fields, accessors, and private slots.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, static members are properties of the class object itself, not of instances. They include static methods, accessors (since ES1), static public fields (ES2022), static private members (ES2022), and static initialization blocks (ES2022). Static public slots are inherited by subclasses through the class prototype chain.

# Prerequisites

- Class declaration

# Key Properties

1. Belong to the class, not instances.
2. `static` keyword prefix for all static members.
3. Static public members are inherited by subclasses.
4. Static private members are NOT inherited (private slots don't inherit).
5. Access via class name, not `this` (for private static members).
6. Static initialization blocks (ES2022) run when the class is created.

# Construction / Recognition

```js
class MyClass {
  static staticMethod() { return 'hello'; }
  static staticField = 42;
  static #privateStatic = 'secret';
  static { /* initialization block */ }
}
```

# Context & Application

Used for utility methods, factory methods, constants, and configuration. The author suggests external functions and variables are often better alternatives, except for operations needing private slot access.

# Examples

From the source text (Ch. 31, section 31.6.1):

```js
class StaticClass {
  static staticMethod() { return 'staticMethod'; }
  static get staticAccessor() { return 'getter'; }
}
assert.equal(StaticClass.staticMethod(), 'staticMethod');
```

# Relationships

## Related
- **Static Factory Methods** -- common use case for static methods

# Common Errors

- **Error**: Using `this` to access static private fields in a method inherited by a subclass.
  **Correction**: Use the class name directly (e.g., `SuperClass.#field`) because `this` in a static method points to the receiver class, which may be a subclass without the private slot.

# Source Reference

Chapter 31: Classes, Section 31.6, lines 1816-2076.

# Verification Notes

- Definition source: direct
- Confidence rationale: Comprehensive coverage of all static member types
- Cross-reference status: verified
