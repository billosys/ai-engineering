---
concept: Symbol.iterator
slug: symbol-iterator
category: iterators-generators
subcategory: iterator-protocol
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 345
section: "12.1 How Iterators Work"
extraction_confidence: high
aliases:
  - "[Symbol.iterator]"
prerequisites:
  - iterator-protocol
extends: []
related:
  - iterable-vs-iterator
  - custom-iterable-objects
  - well-known-symbols
contrasts_with: []
answers_questions:
  - "How do I make an object iterable with `Symbol.iterator`?"
  - "How does `for/of` relate to the iterator protocol?"
---

# Quick Definition

The well-known Symbol used as a method name on objects to make them iterable — when an object has a `[Symbol.iterator]()` method, it can be used with `for/of` loops, spread syntax, and destructuring.

# Core Definition

"The tricky thing about this is that the iterator method of an iterable object does not have a conventional name but uses the Symbol `Symbol.iterator` as its name" (p. 345). Any object with a `[Symbol.iterator]()` method that returns an iterator is considered iterable by the language.

# Prerequisites

- **iterator-protocol** — Symbol.iterator is the mechanism that implements the iterable side of the protocol

# Key Properties

1. A well-known Symbol — not a string property name
2. The method must return an iterator object (with a `next()` method)
3. Used by `for/of`, spread `...`, destructuring, `Array.from()`, `Set()`, `Map()`, etc.
4. The method is called each time iteration begins

# Construction / Recognition

```js
class Range {
    constructor(from, to) { this.from = from; this.to = to; }
    [Symbol.iterator]() {
        let next = Math.ceil(this.from);
        let last = this.to;
        return {
            next() { return (next <= last) ? { value: next++ } : { done: true }; },
            [Symbol.iterator]() { return this; }
        };
    }
}
for(let x of new Range(1,10)) console.log(x);
```

# Context & Application

Implementing `[Symbol.iterator]()` is how you make any class or object work with `for/of` and the spread operator. This is the most commonly used well-known Symbol.

# Examples

From the source text (p. 346-348): The Range class example above. Also: `[...new Range(-2,2)]` returns `[-2, -1, 0, 1, 2]`. Lazy iteration with a `words()` function that returns an iterable iterator for tokenizing strings without allocating the entire array.

# Relationships

## Builds Upon
- **Iterator Protocol** — Symbol.iterator is the key to the iterable side of the protocol

## Enables
- **Custom Iterable Objects** — Implementing this symbol makes objects iterable
- **for/of Loop** — The primary consumer of iterables

## Related
- **Well-Known Symbols** — Symbol.iterator is one of several well-known Symbols

# Common Errors

- **Error**: Using a string `"Symbol.iterator"` instead of the actual Symbol.
  **Correction**: Use the computed property syntax: `[Symbol.iterator]()`, not `"Symbol.iterator"()`.

# Common Confusions

- **Confusion**: Thinking `Symbol.iterator` makes an object an iterator.
  **Clarification**: `Symbol.iterator` makes an object *iterable* (it can produce iterators). The iterator itself is the object returned by the method, which must have `next()`.

# Source Reference

Chapter 12: Iterators and Generators, Sections 12.1-12.2, pages 345-349.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
