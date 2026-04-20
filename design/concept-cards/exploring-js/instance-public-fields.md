---
concept: Instance Public Fields
slug: instance-public-fields
category: classes
subcategory: instance-members
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.5.1 Instance public fields"
extraction_confidence: high
aliases:
  - "public fields"
  - "class fields"
prerequisites:
  - class-declaration
extends: []
related:
  - instance-private-fields
contrasts_with:
  - instance-private-fields
answers_questions:
  - "How do I declare properties on class instances?"
---

# Quick Definition

Instance public fields (ES2022) declare and optionally initialize properties on each instance, either via field declarations in the class body or `this.prop` in the constructor.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, instance public fields can be created in two ways: via field declarations in the class body (`prop = value;`) or via `this.prop = value` in the constructor. Field declarations don't need to be re-declared elsewhere. In base classes, fields execute immediately before the constructor. In derived classes, fields execute immediately after `super()`. Instance properties are relatively common in JavaScript.

# Prerequisites

- Class declaration

# Key Properties

1. Introduced as formal syntax in ES2022.
2. Two creation methods: field declaration or `this.prop` in constructor.
3. Constructor-created properties don't need prior declaration.
4. Fields execute before constructor (base) or after `super()` (derived).
5. `this` in field initializers refers to the new instance.

# Construction / Recognition

```js
class MyClass {
  instanceField = 0;         // field declaration
  constructor(value) {
    this.property = value;    // constructor assignment
  }
}
```

# Context & Application

Used for all public instance data. More common in JavaScript than in languages like Java where most instance state is private.

# Examples

From the source text (Ch. 31, section 31.5.1):

```js
class InstPublicClass {
  instancePublicField = 0;
  constructor(value) {
    this.property = value;
  }
}
const inst = new InstPublicClass('arg');
assert.deepEqual(Reflect.ownKeys(inst), ['instancePublicField', 'property']);
```

# Relationships

## Contrasts With
- **Instance Private Fields** -- private fields use `#` prefix and are not visible outside

# Source Reference

Chapter 31: Classes, Section 31.5.1, lines 1492-1602.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with execution order
- Cross-reference status: verified
