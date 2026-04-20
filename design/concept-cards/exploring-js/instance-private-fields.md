---
concept: Instance Private Fields
slug: instance-private-fields
category: classes
subcategory: instance-members
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.5.2 Instance private fields"
extraction_confidence: high
aliases:
  - "private fields"
  - "#field"
prerequisites:
  - public-and-private-slots
extends: []
related:
  - instance-public-fields
contrasts_with:
  - instance-public-fields
answers_questions:
  - "How do I store truly private data in class instances?"
---

# Quick Definition

Instance private fields (ES2022) are declared with `#` prefix in the class body and can only be accessed inside the declaring class, providing true encapsulation.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, instance private fields use the `#` prefix and must be declared in the class body before use. They can only be accessed inside the class that declares them. They are not visible to `Reflect.ownKeys()` and cannot be accessed from subclasses. The `in` operator can check for their existence: `#field in obj`.

# Prerequisites

- Public and private slots

# Key Properties

1. Introduced in ES2022.
2. Must be declared in the class body: `#field;` or `#field = value;`.
3. Only accessible inside the declaring class.
4. Not accessible in subclasses.
5. Not visible to `Reflect.ownKeys()`.
6. Same `#name` in different classes never clash.

# Construction / Recognition

```js
class Person {
  #name;
  constructor(name) { this.#name = name; }
  getName() { return this.#name; }
}
```

# Context & Application

Use for data that must be truly encapsulated. Before ES2022, WeakMaps or naming conventions were used instead.

# Examples

From the source text (Ch. 31, section 31.5.2):

```js
class InstPrivateClass {
  #privateField1 = 'private field 1';
  #privateField2;
  constructor(value) { this.#privateField2 = value; }
}
const inst = new InstPrivateClass('arg');
assert.deepEqual(Reflect.ownKeys(inst), []);
```

# Relationships

## Contrasts With
- **Instance Public Fields** -- public fields are visible properties; private fields are hidden slots

# Common Errors

- **Error**: Using `this.#field` without declaring `#field` in the class body.
  **Correction**: All private fields must be declared in the class body before use.

# Source Reference

Chapter 31: Classes, Section 31.5.2, lines 1604-1641.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with visibility rules
- Cross-reference status: verified
