---
concept: Object.create()
slug: object-create
category: objects
subcategory: creation
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.8.3 Tips for working with prototypes"
extraction_confidence: high
aliases:
  - "Object.create"
prerequisites:
  - prototype-chain
extends: []
related:
  - object-literal
contrasts_with: []
answers_questions:
  - "How do I create an object with a specific prototype?"
---

# Quick Definition

`Object.create(proto)` creates a new object with `proto` as its prototype, enabling explicit prototype chain construction.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, `Object.create(proto)` is the recommended way to create objects with a specific prototype. Passing `null` creates a prototype-less object (useful for dictionaries without inherited properties). The recommended ways to manage prototypes are: `Object.create()` for creation, `Object.getPrototypeOf()` for reading, and `Object.setPrototypeOf()` for mutation (use sparingly).

# Prerequisites

- Prototype chain

# Key Properties

1. Creates a new empty object with the given prototype.
2. `Object.create(null)` creates a prototype-less object.
3. Preferred over `__proto__` for programmatic prototype setting.
4. `Object.setPrototypeOf()` exists but may harm performance.

# Construction / Recognition

```js
const proto = { greet() { return 'hello'; } };
const obj = Object.create(proto);
obj.greet(); // 'hello' (inherited)
```

# Context & Application

Used for creating objects with specific prototype chains, dictionary objects without inherited properties, and implementing prototype-based patterns.

# Examples

From the source text (Ch. 30, section 30.8.3):

```js
const obj1 = {__proto__: null};
const obj2 = Object.create(null);
assert.equal(Object.getPrototypeOf(obj2), null);
```

# Relationships

## Builds Upon
- **Prototype Chain** -- explicitly sets up prototype relationships

# Source Reference

Chapter 30: Objects, Section 30.8.3, lines 1983-2043.

# Verification Notes

- Definition source: direct
- Confidence rationale: Recommended approach documented
- Cross-reference status: verified
