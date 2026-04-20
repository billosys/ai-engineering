---
# === CORE IDENTIFICATION ===
concept: Iterator Protocol
slug: iterator-protocol

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: protocols
tier: advanced

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "The iterator interface"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - iterable protocol
  - iterator interface

# === TYPED RELATIONSHIPS ===
prerequisites:
  - interface
  - symbol
  - method
  - object
extends: []
related:
  - polymorphism
  - for-loop
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do for/of loops work with custom objects?"
  - "What makes an object iterable?"
---

# Quick Definition
The iterator protocol is a two-part interface: an iterable object must have a method named `Symbol.iterator` that returns an iterator object with a `next` method producing `{value, done}` results.

# Core Definition
Haverbeke explains: "The object given to a `for`/`of` loop is expected to be *iterable*. This means it has a method named with the `Symbol.iterator` symbol. When called, that method should return an object that provides a second interface, *iterator*. This is the actual thing that iterates. It has a `next` method that returns the next result. That result should be an object with a `value` property that provides the next value, if there is one, and a `done` property, which should be true when there are no more results and false otherwise." (Ch 6, "The iterator interface")

# Prerequisites
- **Interfaces**: The protocol defines a specific interface contract
- **Symbols**: Uses `Symbol.iterator` to avoid naming conflicts
- **Methods**: Both iterable and iterator require specific methods
- **Objects**: Results are `{value, done}` objects

# Key Properties
1. Iterable: has a `[Symbol.iterator]()` method returning an iterator
2. Iterator: has a `next()` method returning `{value, done}`
3. `next`, `value`, and `done` are plain string property names
4. Only `Symbol.iterator` is an actual symbol
5. Works with `for/of`, spread syntax (`...`), and destructuring

# Construction / Recognition
```javascript
class ListIterator {
  constructor(list) { this.list = list; }
  next() {
    if (this.list == null) return {done: true};
    let value = this.list.value;
    this.list = this.list.rest;
    return {value, done: false};
  }
}
List.prototype[Symbol.iterator] = function() {
  return new ListIterator(this);
};
```

# Context & Application
The iterator protocol enables polymorphic iteration. Any object implementing it can be used with `for/of` loops, spread syntax, and destructuring.

# Examples
```javascript
let okIterator = "OK"[Symbol.iterator]();
console.log(okIterator.next());
// -> {value: "O", done: false}
console.log(okIterator.next());
// -> {value: "K", done: false}
console.log(okIterator.next());
// -> {value: undefined, done: true}

// Using for/of with a custom iterable
let list = List.fromArray([1, 2, 3]);
for (let element of list) {
  console.log(element);
}
// -> 1
// -> 2
// -> 3

// Spread syntax works with any iterable
console.log([..."PCI"]);
// -> ["P", "C", "I"]
```
(Ch 6, "The iterator interface", lines 827-958)

# Relationships
## Builds Upon
- interface, symbol, method
## Enables
- for/of loops on custom objects, spread syntax, destructuring
## Related
- polymorphism, for-loop
## Contrasts With
- N/A

# Common Errors
- **Error**: Returning just a value from `next()` instead of a `{value, done}` object
  **Correction**: `next()` must always return an object with `value` and `done` properties

# Common Confusions
- **Confusion**: The iterable and the iterator are the same object
  **Clarification**: The iterable has `[Symbol.iterator]()` which returns a separate iterator object with `next()`

# Source Reference
Chapter 6: The Secret Life of Objects, Section "The iterator interface", lines 827-958.

# Verification Notes
- Definition source: direct
- Confidence rationale: Extensively explained with full implementation example
- Cross-reference status: verified
