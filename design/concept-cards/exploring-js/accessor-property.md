---
concept: Accessor Property
slug: accessor-property
category: objects
subcategory: properties
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.3.6 Object literals: accessors"
extraction_confidence: high
aliases:
  - "getter"
  - "setter"
  - "get/set"
prerequisites:
  - method-definition
extends: []
related:
  - object-literal
contrasts_with: []
answers_questions:
  - "How do I create computed or validated properties?"
---

# Quick Definition

An accessor is a pair of getter (`get`) and/or setter (`set`) methods that are invoked transparently when a property is read or written.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, accessors are methods invoked by accessing a property. A getter is prefixed with `get` and invoked by reading the property. A setter is prefixed with `set` and invoked by writing to the property. Accessors enable encapsulation: starting with a normal property and later switching to an accessor without breaking existing code.

# Prerequisites

- Method definition

# Key Properties

1. Getter: `get name() { return value; }` -- invoked by reading.
2. Setter: `set name(value) { ... }` -- invoked by writing.
3. An accessor can have just a getter, just a setter, or both.
4. Transparent: callers use property syntax, not method calls.
5. Enable encapsulation and computed properties.

# Construction / Recognition

```js
const obj = {
  first: 'Jane',
  last: 'Doe',
  get full() { return `${this.first} ${this.last}`; },
  set full(name) {
    const parts = name.split(' ');
    this.first = parts[0];
    this.last = parts[1];
  },
};
```

# Context & Application

Used for computed properties, validation, lazy initialization, and read-only properties (getter-only).

# Examples

From the source text (Ch. 30, section 30.3.6.1-30.3.6.2):

```js
const jane = {
  first: 'Jane', last: 'Doe',
  get full() { return `${this.first} ${this.last}`; },
};
assert.equal(jane.full, 'Jane Doe');
```

# Relationships

## Builds Upon
- **Method Definition** -- accessors are special methods

# Common Errors

- **Error**: Trying to write to a getter-only accessor.
  **Correction**: A getter-only accessor throws a TypeError on write in strict mode.

# Source Reference

Chapter 30: Objects, Section 30.3.6, lines 531-617.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with both getter and setter
- Cross-reference status: verified
