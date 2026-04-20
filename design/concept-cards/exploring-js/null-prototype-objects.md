---
concept: Null Prototype Objects
slug: null-prototype-objects
category: objects
subcategory: creation
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.9.11 Objects with `null` prototypes make good dictionaries and lookup tables"
extraction_confidence: high
aliases:
  - "prototype-less objects"
  - "dictionary objects with null prototype"
prerequisites:
  - prototype-chain
  - object-create
extends: []
related:
  - fixed-layout-vs-dictionary-objects
contrasts_with: []
answers_questions:
  - "How do I create a clean dictionary object without inherited properties?"
---

# Quick Definition

Objects with `null` prototypes (`Object.create(null)`) have no inherited properties, making them clean dictionaries/lookup tables without unexpected inherited keys like `toString` or `constructor`.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, objects with `null` prototypes make good dictionaries and lookup tables because they have no inherited properties that could interfere with arbitrary key lookups. They are created via `Object.create(null)` or `{__proto__: null}`.

# Prerequisites

- Prototype chain
- Object.create()

# Key Properties

1. Created via `Object.create(null)` or `{__proto__: null}`.
2. No inherited properties (no `.toString`, `.hasOwnProperty`, etc.).
3. Not instances of `Object` (`instanceof Object` is `false`).
4. Clean for use as dictionaries/lookup tables.
5. Cannot use `Object.prototype` methods directly (use direct method calls).

# Construction / Recognition

```js
const dict = Object.create(null);
dict['key'] = 'value';
```

# Context & Application

Use when objects serve as pure key-value stores and you want to avoid key collisions with inherited properties.

# Examples

```js
const dict = Object.create(null);
dict.toString = 'my value'; // no collision with Object.prototype.toString
assert.equal(dict.toString, 'my value');
```

# Relationships

## Builds Upon
- **Prototype Chain** -- explicitly breaks the chain
- **Object.create()** -- primary creation method

# Source Reference

Chapter 30: Objects, Section 30.9.11.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit recommendation
- Cross-reference status: verified
