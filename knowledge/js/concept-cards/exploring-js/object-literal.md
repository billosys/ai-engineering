---
concept: Object Literal
slug: object-literal
category: objects
subcategory: creation
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.3.1 Object literals: properties"
extraction_confidence: high
aliases:
  - "object initializer"
  - "{} syntax"
prerequisites: []
extends: []
related:
  - property-value-shorthand
  - method-definition
  - accessor-property
contrasts_with: []
answers_questions:
  - "How do I create an object directly in JavaScript?"
---

# Quick Definition

An object literal is a stand-out JavaScript feature that creates objects directly using `{}` syntax with key-value pairs, without requiring a class.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, object literals are one way of creating fixed-layout objects. They start and end with curly braces `{}` and contain property definitions (key-value entries), methods, and accessors. Property keys must follow variable naming rules (or use quoted/computed keys). Being able to create objects directly without classes is one of the highlights of JavaScript.

# Prerequisites

- Foundational concept with no prerequisites

# Key Properties

1. Creates objects directly without needing a class.
2. Can define properties, methods, getters, and setters.
3. Trailing commas are allowed (since ES5).
4. Reserved words are valid as property keys.
5. Property keys that don't follow identifier rules must be quoted.

# Construction / Recognition

```js
const myObject = {
  myProperty: 1,
  myMethod() { return 2; },
  get myAccessor() { return this.myProperty; },
  set myAccessor(value) { this.myProperty = value; },
};
```

# Context & Application

The most common way to create one-off objects, configuration objects, and data containers. Classes are used when multiple objects with shared behavior are needed.

# Examples

From the source text (Ch. 30, section 30.3.1):

```js
const jane = {
  first: 'Jane',
  last: 'Doe',
};
```

# Relationships

## Enables
- **Property Value Shorthand** -- concise property syntax
- **Method Definition** -- shorthand method syntax
- **Spreading Into Object Literals** -- copying properties

# Source Reference

Chapter 30: Objects, Section 30.3.1, lines 378-416.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition as a stand-out JavaScript feature
- Cross-reference status: verified
