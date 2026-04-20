---
concept: __proto__ vs .prototype
slug: proto-vs-prototype
category: classes
subcategory: internals
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.3.3 `.__proto__` vs. `.prototype`"
extraction_confidence: high
aliases: []
prerequisites:
  - prototype-chain
  - class-declaration
extends: []
related:
  - subclassing
contrasts_with: []
answers_questions:
  - "What is the difference between __proto__ and .prototype?"
---

# Quick Definition

`.__proto__` is an accessor that gets/sets an object's prototype, while `.prototype` is a property on constructor functions/classes that becomes the prototype of instances created via `new`.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, `Object.prototype.__proto__` is an accessor inherited by most objects that gets and sets the prototype. `SomeClass.prototype` holds the object that becomes the prototype of all instances created via `new SomeClass()`. A better name for `.prototype` would be `.instancePrototype`.

# Prerequisites

- Prototype chain
- Class declaration

# Key Properties

1. `obj.__proto__` === `Object.getPrototypeOf(obj)`.
2. `SomeClass.prototype` is the prototype of instances (not of the class itself).
3. `.__proto__` is deprecated in the spec; use `Object.getPrototypeOf()`.
4. Using `__proto__` in object literals to set prototypes is different from the accessor.

# Construction / Recognition

```js
class SomeClass {}
const inst = new SomeClass();
// inst.__proto__ === SomeClass.prototype
assert.equal(Object.getPrototypeOf(inst), SomeClass.prototype);
```

# Context & Application

Understanding this distinction is essential for debugging prototype chains and understanding how classes work internally.

# Examples

From the source text (Ch. 31, section 31.3.3):

```js
// These are equivalent:
someObj.__proto__
Object.getPrototypeOf(someObj)

// .prototype is about instances:
class SomeClass {}
const inst = new SomeClass();
assert.equal(Object.getPrototypeOf(inst), SomeClass.prototype);
```

# Relationships

## Builds Upon
- **Prototype Chain** -- both concepts relate to prototype chains
- **Class Declaration** -- `.prototype` is set up by class definitions

# Common Confusions

- **Confusion**: Thinking `.prototype` is the prototype of the class/constructor.
  **Clarification**: `.prototype` is the prototype of instances. The prototype of the class itself is `Function.prototype` (for base classes) or the superclass (for derived classes).

# Source Reference

Chapter 31: Classes, Section 31.3.3, lines 986-1023.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit distinction with visual reference
- Cross-reference status: verified
