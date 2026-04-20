---
concept: Class Declaration
slug: class-declaration
category: classes
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.2 The essentials of classes"
extraction_confidence: high
aliases:
  - "class"
  - "class definition"
  - "class statement"
prerequisites:
  - prototype-chain
  - object-literal
extends: []
related:
  - class-expression
  - constructor-method
  - subclassing
contrasts_with: []
answers_questions:
  - "What is a class in JavaScript?"
  - "How do I create and use a class with inheritance?"
  - "What must I know before learning about classes and inheritance?"
---

# Quick Definition

A JavaScript class (ES6) is a compact syntax for creating constructor functions that set up prototype chains, serving as factories for objects with shared behavior.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, classes are basically a compact syntax for setting up prototype chains. Under the hood, they are unconventional but should feel familiar to OOP programmers. A class creates two connected objects: the class itself (holding static members and `.prototype`) and the prototype object (holding instance methods). Each instance's prototype is `ClassName.prototype`. Classes are functions (`typeof` returns `'function'`).

# Prerequisites

- Prototype chain (classes are built on prototypes)
- Object literal (alternative for one-off objects)

# Key Properties

1. Introduced in ES6.
2. A class is actually a function (the constructor).
3. Creates two objects: the class and `Class.prototype`.
4. Instance methods live on `Class.prototype`.
5. Static members live on the class itself.
6. `this` inside methods/constructor refers to the instance.
7. Classes cannot be function-called (only `new`).
8. Classes are not hoisted like function declarations.

# Construction / Recognition

```js
class Person {
  #firstName;
  constructor(firstName) {
    this.#firstName = firstName;
  }
  describe() {
    return `Person named ${this.#firstName}`;
  }
  static extractNames(persons) {
    return persons.map(p => p.#firstName);
  }
}
```

# Context & Application

Use classes when creating multiple objects with shared behavior. For one-off objects, use object literals. The author recommends using inheritance sparingly and keeping core functionality in prototype methods.

# Examples

From the source text (Ch. 31, section 31.1):

```js
class Person {
  constructor(firstName) {
    this.firstName = firstName;
  }
  describe() {
    return 'Person named ' + this.firstName;
  }
}
const tarzan = new Person('Tarzan');
assert.equal(tarzan.describe(), 'Person named Tarzan');
```

# Relationships

## Builds Upon
- **Prototype Chain** -- classes set up prototype chains for instances

## Enables
- **Subclassing** -- classes support `extends` for inheritance
- **Constructor Method** -- the initialization entry point
- **Instance Fields** -- declared properties on instances

## Related
- **Class Expression** -- anonymous and named class expressions

# Common Errors

- **Error**: Trying to call a class as a function without `new`.
  **Correction**: Classes can only be invoked with `new`. Use static factory methods for alternative construction.

# Common Confusions

- **Confusion**: Thinking class methods are stored on instances.
  **Clarification**: Methods are stored on `Class.prototype` and inherited by instances through the prototype chain.

# Source Reference

Chapter 31: Classes, Section 31.2-31.3, lines 159-1258.

# Verification Notes

- Definition source: direct
- Confidence rationale: Core concept with extensive coverage
- Cross-reference status: verified
