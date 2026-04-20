---
concept: Custom Iterable Objects
slug: custom-iterable-objects
category: iterators-generators
subcategory: iterator-protocol
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 346
section: "12.2 Implementing Iterable Objects"
extraction_confidence: high
aliases: []
prerequisites:
  - iterator-protocol
  - symbol-iterator
extends: []
related:
  - generator-functions
  - lazy-evaluation-iterators
contrasts_with: []
answers_questions:
  - "How do I make an object iterable with `Symbol.iterator`?"
---

# Quick Definition

User-defined objects made iterable by implementing a `[Symbol.iterator]()` method that returns an iterator with a `next()` method, enabling use with `for/of`, spread, and destructuring.

# Core Definition

"In order to make a class iterable, you must implement a method whose name is the Symbol `Symbol.iterator`. That method must return an iterator object that has a next() method. And the next() method must return an iteration result object that has a value property and/or a boolean done property" (p. 346). Iterable functions like `map()` and `filter()` can also be created as iterator-returning functions.

# Prerequisites

- **iterator-protocol** — Must understand the three-part protocol
- **symbol-iterator** — Must know how to use Symbol.iterator

# Key Properties

1. Implement `[Symbol.iterator]()` to return an iterator
2. Each call should return an independent iterator with fresh state
3. Can also create standalone iterable-returning functions (like `map()`, `filter()`)
4. Iterators may implement `return()` for cleanup when iteration ends early
5. Using generators simplifies implementation significantly

# Construction / Recognition

The Range class from Example 12-1 (p. 346-348) and iterable `map()` / `filter()` functions (p. 347-348).

# Context & Application

Making classes iterable is a best practice whenever they represent collections or sequences. Iterable APIs integrate naturally with JavaScript's iteration infrastructure.

# Examples

From the source text (p. 347-348): An iterable `map()` function: `[...map(new Range(1,4), x => x*x)]` returns `[1, 4, 9, 16]`. An iterable `filter()` function: `[...filter(new Range(1,10), x => x % 2 === 0)]` returns `[2,4,6,8,10]`.

# Relationships

## Builds Upon
- **Iterator Protocol** — Custom iterables implement the protocol
- **Symbol.iterator** — The method name used to make objects iterable

## Related
- **Generator Functions** — A much simpler way to implement iterables
- **Lazy Evaluation** — Custom iterables enable deferred computation

# Common Errors

- **Error**: Returning the same iterator object from multiple `[Symbol.iterator]()` calls, causing iterations to share state.
  **Correction**: Each call to `[Symbol.iterator]()` should return a new iterator with independent state.

# Common Confusions

- **Confusion**: Thinking you always need to manually implement `next()`.
  **Clarification**: Generator functions (`function*`) provide a much simpler way to create iterables — see section 12.3.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.2, pages 346-349.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
