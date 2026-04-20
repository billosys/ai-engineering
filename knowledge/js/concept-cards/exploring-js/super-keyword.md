---
concept: Super Keyword
slug: super-keyword
category: classes
subcategory: inheritance
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.7.1 Defining subclasses via `extends`"
extraction_confidence: high
aliases:
  - "super()"
  - "super.method()"
prerequisites:
  - subclassing
extends: []
related:
  - constructor-method
contrasts_with: []
answers_questions:
  - "How do I call the parent class constructor or methods?"
---

# Quick Definition

`super()` calls the superclass constructor in a derived class, and `super.method()` calls an overridden method from the superclass.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, `super` has two forms: `super()` in constructors calls the parent constructor (mandatory before accessing `this` in derived classes), and `super.method()` in methods invokes the overridden parent method. Instances are created in the base class, so `super()` must complete before the derived class can add its own slots.

# Prerequisites

- Subclassing

# Key Properties

1. `super()` -- calls superclass constructor (required in derived constructors).
2. `super.method()` -- calls overridden method from parent.
3. Must be called before `this` in derived constructors.
4. If constructor is omitted in a subclass, `super(...args)` is called automatically.

# Construction / Recognition

```js
class Sub extends Super {
  constructor(a, b) {
    super(a);        // call parent constructor
    this.b = b;
  }
  method() {
    return super.method() + ' extended';  // call parent method
  }
}
```

# Context & Application

Essential for class inheritance. Use `super()` for initialization chaining and `super.method()` for extending rather than replacing parent behavior.

# Examples

From the source text (Ch. 31, section 31.7.1):

```js
class Employee extends Person {
  constructor(firstName, title) {
    super(firstName);
    this.title = title;
  }
  describe() {
    return super.describe() + ` (${this.title})`;
  }
}
```

# Relationships

## Builds Upon
- **Subclassing** -- `super` is used within subclasses

## Related
- **Constructor Method** -- `super()` chains to the parent constructor

# Common Errors

- **Error**: Accessing `this` before `super()` in a derived constructor.
  **Correction**: Call `super()` first; the instance doesn't exist until then.

# Source Reference

Chapter 31: Classes, Section 31.7.1, lines 2362-2434.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit rules and examples
- Cross-reference status: verified
