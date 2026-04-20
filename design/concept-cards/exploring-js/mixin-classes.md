---
concept: Mixin Classes
slug: mixin-classes
category: classes
subcategory: inheritance
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.8 Mixin classes (advanced)"
extraction_confidence: high
aliases:
  - "mixin"
  - "mixin pattern"
prerequisites:
  - subclassing
extends: []
related:
  - class-declaration
contrasts_with: []
answers_questions:
  - "How can I compose behavior from multiple sources?"
---

# Quick Definition

A mixin class is a function that takes a superclass as input and returns a subclass with additional behavior, enabling composition of features without deep inheritance hierarchies.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, JavaScript only supports single inheritance. Mixin classes work around this by using functions that take a superclass and return a subclass: `const MixinB = (Sup) => class extends Sup { ... }`. Multiple mixins can be chained: `class C extends MixinB(MixinA(SuperClass)) {}`.

# Prerequisites

- Subclassing

# Key Properties

1. A function that returns a class extending its parameter.
2. Enables multiple inheritance-like behavior.
3. Can be chained for multiple mixins.
4. Avoids deep inheritance hierarchies.

# Construction / Recognition

```js
const Named = (Sup) => class extends Sup {
  name = '(Unnamed)';
  toString() { return `Name: ${this.name}`; }
};
class Person extends Named(Object) {}
```

# Context & Application

Used to add cross-cutting functionality (e.g., serialization, event handling, naming) to multiple class hierarchies.

# Examples

From the source text (Ch. 31, section 31.8.1) -- conceptual pattern:

```js
const Named = (Sup) => class extends Sup {
  name = '(Unnamed)';
};
class Employee extends Named(Person) {}
```

# Relationships

## Builds Upon
- **Subclassing** -- mixins use `extends` dynamically

# Source Reference

Chapter 31: Classes, Section 31.8, lines ~2700-2750.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit pattern description
- Cross-reference status: verified
