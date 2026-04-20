---
concept: Fixed-Layout vs Dictionary Objects
slug: fixed-layout-vs-dictionary-objects
category: objects
subcategory: usage-patterns
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.2.1 The two ways of using objects"
extraction_confidence: high
aliases:
  - "object usage patterns"
  - "record vs map"
prerequisites:
  - object-literal
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What are the two main ways objects are used in JavaScript?"
---

# Quick Definition

Objects are used in two ways: as fixed-layout objects (like records, with known properties of different types) or as dictionary objects (like lookup tables, with dynamic keys and same-type values).

# Core Definition

As described in "Exploring JavaScript" Ch. 30, there are two ways of using objects. Fixed-layout objects work like database records: fixed number of properties with known keys and different value types. Dictionary objects work like lookup tables: variable number of properties with unknown keys and same value types. Both can be mixed. Maps are usually better dictionaries than objects.

# Prerequisites

- Object literal

# Key Properties

1. Fixed-layout: known keys, different value types, static structure.
2. Dictionary: unknown keys, same value types, dynamic structure.
3. The two uses can be mixed.
4. Maps are generally better than objects for dictionary use.

# Construction / Recognition

```js
// Fixed-layout
const person = { name: 'Jane', age: 30 };

// Dictionary
const translations = { ['hello']: 'hola', ['goodbye']: 'adios' };
```

# Context & Application

Knowing which pattern you're using helps choose appropriate APIs: `Object.keys()` for dictionaries, direct property access for fixed-layout.

# Examples

From the source text (Ch. 30, section 30.2.1):

```js
const fixedLayoutObject = { product: 'carrot', quantity: 4 };
const dictionaryObject = { ['one']: 1, ['two']: 2 };
```

# Relationships

## Builds Upon
- **Object Literal** -- both patterns use object literals

# Source Reference

Chapter 30: Objects, Section 30.2.1, lines 313-372.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit taxonomy
- Cross-reference status: verified
