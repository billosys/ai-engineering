---
concept: Private Methods and Accessors
slug: private-methods-and-accessors
category: classes
subcategory: prototype-members
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.4.2 Private methods and accessors"
extraction_confidence: high
aliases:
  - "private methods"
  - "#method()"
prerequisites:
  - public-and-private-slots
  - class-declaration
extends: []
related:
  - instance-private-fields
contrasts_with: []
answers_questions:
  - "How do I create private methods in a class?"
---

# Quick Definition

Private methods and accessors (ES2022) use the `#` prefix and are stored in instance slots (not on the prototype), but are shared between all instances of the class.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, private methods and accessors are an interesting mix of prototype and instance members. They are stored in slots on instances (not on `.prototype` objects) because private slots are not inherited. However, the actual method function is shared between instances -- like prototype public methods. Private methods can only be accessed inside the class body.

# Prerequisites

- Public and private slots
- Class declaration

# Key Properties

1. Introduced in ES2022.
2. Stored in instance slots, but function is shared.
3. Not on `.prototype` (private slots aren't inherited).
4. Only accessible inside the declaring class.
5. Supports getters, setters, generators, and async methods.

# Construction / Recognition

```js
class MyClass {
  #privateMethod() { return 'private'; }
  get #accessor() { return 'getter'; }
  callPrivate() { return this.#privateMethod(); }
}
```

# Context & Application

Use for internal implementation details that should not be part of the public API.

# Examples

From the source text (Ch. 31, section 31.4.2):

```js
class PrivateMethodClass {
  #privateMethod() { return 'privateMethod'; }
  get #privateAccessor() { return 'privateGetter'; }
  callPrivateMembers() {
    assert.equal(this.#privateMethod(), 'privateMethod');
    assert.equal(this.#privateAccessor, 'privateGetter');
  }
}
```

# Relationships

## Builds Upon
- **Public and Private Slots** -- private methods create private slots

## Related
- **Instance Private Fields** -- both are private slot types

# Source Reference

Chapter 31: Classes, Section 31.4.2, lines 1388-1478.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit storage semantics explained
- Cross-reference status: verified
