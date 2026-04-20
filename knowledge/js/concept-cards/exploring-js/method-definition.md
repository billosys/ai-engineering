---
concept: Method Definition
slug: method-definition
category: objects
subcategory: methods
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.3.5 Object literals: methods"
extraction_confidence: high
aliases:
  - "method shorthand"
  - "shorthand method"
prerequisites:
  - object-literal
  - this-keyword
extends: []
related:
  - accessor-property
contrasts_with: []
answers_questions:
  - "How do I define methods on objects?"
---

# Quick Definition

A method is a property whose value is a function, defined with shorthand syntax `name() {}` in object literals and class bodies, receiving the object as `this`.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, methods are properties whose values are functions. During a method call `obj.method()`, `obj` is the receiver and is assigned to `this`. Methods are internally stored as function values. The shorthand syntax `says(text) {}` is preferred over `says: function(text) {}`.

# Prerequisites

- Object literal
- The `this` keyword

# Key Properties

1. Methods are properties whose values are functions.
2. `this` refers to the receiver of the method call.
3. Shorthand syntax: `name() {}` (preferred).
4. Full syntax: `name: function() {}` (equivalent but verbose).

# Construction / Recognition

```js
const jane = {
  first: 'Jane',
  says(text) {
    return `${this.first} says "${text}"`;
  },
};
```

# Context & Application

Used to add behavior to objects. The receiver becomes `this` inside the method, enabling access to the object's other properties.

# Examples

From the source text (Ch. 30, section 30.3.5):

```js
const jane = {
  first: 'Jane',
  says(text) {
    return `${this.first} says "${text}"`;
  },
};
assert.equal(jane.says('hello'), 'Jane says "hello"');
```

# Relationships

## Builds Upon
- **Object Literal** -- methods are defined inside object literals
- **The this Keyword** -- methods use `this` to access the receiver

# Common Errors

- **Error**: Extracting a method and calling it as a function, losing `this`.
  **Correction**: Use `.bind()` or an arrow wrapper when extracting methods.

# Source Reference

Chapter 30: Objects, Section 30.3.5, lines 496-518.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with example
- Cross-reference status: verified
