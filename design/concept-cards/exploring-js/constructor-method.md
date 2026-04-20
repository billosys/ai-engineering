---
concept: Constructor Method
slug: constructor-method
category: classes
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.2.1 A class for persons"
extraction_confidence: high
aliases:
  - "constructor"
  - "constructor()"
prerequisites:
  - class-declaration
extends: []
related:
  - this-keyword
contrasts_with: []
answers_questions:
  - "How do I initialize class instances?"
---

# Quick Definition

The `constructor()` method is a special class method called automatically after instance creation, where `this` refers to the new instance.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, `.constructor()` is called after the creation of a new instance. Inside it, `this` refers to that instance. It initializes instance properties and private fields. In derived classes (subclasses), `super()` must be called before accessing `this`. The constructor can be omitted, in which case a default is provided.

# Prerequisites

- Class declaration

# Key Properties

1. Called automatically by `new`.
2. `this` refers to the newly created instance.
3. In derived classes, `super()` must be called before accessing `this`.
4. Can be omitted (default constructor provided).
5. Creates instance properties via `this.prop = value`.

# Construction / Recognition

```js
class Person {
  constructor(name) {
    this.name = name;
  }
}
```

# Context & Application

The entry point for initializing new instances. Must call `super()` first in subclasses.

# Examples

From the source text (Ch. 31, section 31.2.1):

```js
class Person {
  #firstName;
  constructor(firstName) {
    this.#firstName = firstName;
  }
}
const jane = new Person('Jane');
```

# Relationships

## Builds Upon
- **Class Declaration** -- constructor is defined inside a class

## Related
- **The this Keyword** -- `this` refers to the new instance

# Common Errors

- **Error**: Accessing `this` before calling `super()` in a derived class.
  **Correction**: Always call `super()` first in subclass constructors.

# Source Reference

Chapter 31: Classes, Section 31.2.1, lines 295-385.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with rules
- Cross-reference status: verified
