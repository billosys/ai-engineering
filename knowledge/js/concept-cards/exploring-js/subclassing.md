---
concept: Subclassing
slug: subclassing
category: classes
subcategory: inheritance
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.7 Subclassing"
extraction_confidence: high
aliases:
  - "extends"
  - "class inheritance"
  - "derived class"
prerequisites:
  - class-declaration
  - prototype-chain
extends:
  - class-declaration
related:
  - super-keyword
  - instanceof-operator
contrasts_with: []
answers_questions:
  - "How do I create and use a class with inheritance?"
  - "How does subclassing (extends) interact with the prototype chain?"
---

# Quick Definition

Subclassing via `extends` creates a derived class that inherits both instance methods (via the instance prototype chain) and static members (via the class prototype chain) from a superclass.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, `class Employee extends Person` creates a subclass. The subclass inherits instance methods via the instance prototype chain and static members via the class prototype chain (two linked prototype chains). In the subclass constructor, `super()` must be called before accessing `this` because instances are created in base classes. `super.method()` calls overridden methods. Static public slots are inherited; private slots are not.

# Prerequisites

- Class declaration
- Prototype chain

# Key Properties

1. Syntax: `class Sub extends Super {}`.
2. Creates two prototype chains: instance chain and class chain.
3. `super()` required in derived constructor before `this` access.
4. `super.method()` calls overridden methods.
5. Static public members are inherited by subclasses.
6. Private slots are NOT inherited.
7. Instances are created in base classes, then subclass constructors add slots.
8. Terminology: superclass/base class vs. subclass/derived class.

# Construction / Recognition

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

# Context & Application

Use sparingly -- the author recommends inheritance only when objects truly share behavior. Prefer composition when possible.

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
const jane = new Employee('Jane', 'CTO');
assert.equal(jane.describe(), 'Person named Jane (CTO)');
```

# Relationships

## Builds Upon
- **Class Declaration** -- subclassing extends classes
- **Prototype Chain** -- two prototype chains are created

## Enables
- **instanceof Operator** -- checks the instance prototype chain

## Related
- **Super Keyword** -- `super()` and `super.method()` used in subclasses

# Common Errors

- **Error**: Forgetting to call `super()` in a derived class constructor.
  **Correction**: `super()` must be called before any `this` access in derived constructors.

- **Error**: Trying to access superclass private fields from a subclass.
  **Correction**: Private fields are scoped to the declaring class only. Use WeakMap patterns for protected visibility.

# Common Confusions

- **Confusion**: Thinking a base class with no `extends` is the same as `extends Object`.
  **Clarification**: They differ in the class prototype chain. A base class's prototype is `Function.prototype`, while `extends Object` adds `Object` to the class prototype chain.

# Source Reference

Chapter 31: Classes, Section 31.7, lines 2351-2700.

# Verification Notes

- Definition source: direct
- Confidence rationale: Core concept with detailed internal mechanics
- Cross-reference status: verified
