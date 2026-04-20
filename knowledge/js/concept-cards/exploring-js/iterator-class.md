---
concept: Iterator Class
slug: iterator-class
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.7 Class Iterator and iterator helper methods"
extraction_confidence: high
aliases:
  - "Iterator"
  - "Iterator API"
prerequisites:
  - iterator-interface
extends:
  - iterator-interface
related:
  - iterator-helper-methods
  - iterator-from
contrasts_with: []
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

The `Iterator` class (ES2025) provides a globally accessible prototype for all built-in iterators and exposes helper methods like `.map()`, `.filter()`, `.take()`, `.drop()`, and `.toArray()` on `Iterator.prototype`.

# Core Definition

ECMAScript 2025 introduces a class `Iterator` where `Iterator.prototype` refers to `%IteratorPrototype%` (the common prototype of all built-in iterators). The class provides `Iterator.from(iterable)` for creating API iterators, and `Iterator.prototype` contains helper methods inherited by all iterators.

# Prerequisites

- **iterator-interface** -- the Iterator class formalizes the existing interface

# Key Properties

1. Introduced in ES2025
2. `Iterator.prototype` is the prototype of all built-in iterators
3. Provides `Iterator.from()` static method
4. Provides helper methods: `.map()`, `.filter()`, `.flatMap()`, `.reduce()`, `.find()`, `.some()`, `.every()`, `.forEach()`, `.drop()`, `.take()`, `.toArray()`
5. Distinguishes "API iterators" (instances of Iterator) from "legacy iterators"

# Construction / Recognition

```js
const iter = Iterator.from(['a', 'b']);
iter instanceof Iterator; // true

// Generator objects are also instances
function* gen() {}
gen() instanceof Iterator; // true
```

# Context & Application

The Iterator class unifies the iterator ecosystem by providing a common prototype with useful methods, eliminating the need to convert to arrays for operations like filtering and mapping.

# Examples

```js
['a', 'b', 'c'].values().map(x => `=${x}=`).toArray();
// ['=a=', '=b=', '=c=']

['a', 'b', 'c'].values().drop(1).toArray();
// ['b', 'c']

['a', 'b', 'c'].values().take(2).toArray();
// ['a', 'b']
```

(Chapter 32, Section 32.7, lines 711-798)

# Relationships

## Builds Upon
- **iterator-interface** -- formalizes the interface as a class

## Enables
- **iterator-helper-methods** -- methods on Iterator.prototype

## Related
- **iterator-from** -- static method for creating API iterators

## Contrasts With
- None

# Common Errors

- **Error**: Assuming older library iterators automatically have helper methods.
  **Correction**: Legacy iterators may not be instances of Iterator. Use `Iterator.from()` to wrap them.

# Common Confusions

- **Confusion**: `Iterator` existed before ES2025.
  **Clarification**: Before ES2025, `%IteratorPrototype%` existed internally but was not globally accessible as `Iterator`.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.7, lines 711-798.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2025 marker
- Cross-reference status: verified
