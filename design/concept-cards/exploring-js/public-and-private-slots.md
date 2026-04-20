---
concept: Public and Private Slots
slug: public-and-private-slots
category: classes
subcategory: encapsulation
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.2.4 Public slots (properties) vs. private slots"
extraction_confidence: high
aliases:
  - "private fields"
  - "private slots"
  - "#private"
prerequisites:
  - class-declaration
extends: []
related:
  - instance-public-fields
  - instance-private-fields
contrasts_with: []
answers_questions:
  - "How does JavaScript encapsulate data in classes?"
---

# Quick Definition

Objects have public slots (properties, accessible everywhere) and private slots (ES2022, prefixed with `#`, accessible only inside the declaring class).

# Core Definition

As described in "Exploring JavaScript" Ch. 31, objects can have public slots (properties) and private slots (ES2022). Private slots use the `#` prefix and must be declared in the class body before use. They can only be accessed inside the class that declares them -- not even in subclasses. Properties and private slots are stored separately, have different key types (string/symbol vs private names), and follow different inheritance rules (properties are inherited, private slots are not). Private slots can only be created via classes.

# Prerequisites

- Class declaration

# Key Properties

1. Private slots introduced in ES2022.
2. Private identifiers start with `#` (e.g., `#name`).
3. Must be declared in the class body before use.
4. Not accessible outside the class (not even in subclasses).
5. Not inherited through prototype chain.
6. Private names are unique per class (same `#name` in different classes never clash).
7. `in` operator can check for private slots: `#name in obj`.

# Construction / Recognition

```js
class MyClass {
  #privateField = 1;
  publicProperty = 2;
  getValues() {
    return [this.#privateField, this.publicProperty];
  }
}
```

# Context & Application

Use private fields for data that should not be accessible from outside the class. Use public properties for data that needs to be shared.

# Examples

From the source text (Ch. 31, section 31.2.4):

```js
class MyClass {
  #instancePrivateField = 1;
  instanceProperty = 2;
}
const inst = new MyClass();
assert.deepEqual(Reflect.ownKeys(inst), ['instanceProperty']);
```

# Relationships

## Enables
- **Instance Private Fields** -- private data on instances
- **Instance Public Fields** -- public data on instances

# Common Errors

- **Error**: Trying to access a private field from a subclass.
  **Correction**: Private fields are class-scoped, not accessible in subclasses. Use protected patterns (WeakMaps) if needed.

# Common Confusions

- **Confusion**: Thinking private fields are like properties with access restrictions.
  **Clarification**: Private slots and properties are fundamentally different: stored separately, different key types, different inheritance behavior.

# Source Reference

Chapter 31: Classes, Section 31.2.4-31.2.5, lines 439-634.

# Verification Notes

- Definition source: direct
- Confidence rationale: Thorough treatment of the distinction
- Cross-reference status: verified
