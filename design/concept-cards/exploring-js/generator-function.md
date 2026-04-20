---
concept: Generator Function
slug: generator-function
category: iteration
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous generators (advanced)"
chapter_number: 33
pdf_page: null
section: "33.1 What are synchronous generators?"
extraction_confidence: high
aliases:
  - "generator"
  - "function*"
  - "generator function declaration"
prerequisites:
  - iteration-protocol
  - iterator-interface
extends: []
related:
  - yield-operator
  - yield-star-operator
contrasts_with: []
answers_questions:
  - "What is a generator function?"
  - "What is needed to understand generator functions?"
---

# Quick Definition

A generator function (declared with `function*`) is a special function that returns an iterator, producing values lazily via the `yield` operator and pausing execution between each yielded value.

# Core Definition

Synchronous generators are special versions of function definitions and method definitions that always return synchronous iterators (which are iterable). They are marked with an asterisk (`*`): `function*` for declarations/expressions, `*` as a method modifier. Calling a generator function does not execute its body; instead, it returns an iterator. The body executes incrementally via `.next()` calls, pausing at each `yield`.

# Prerequisites

- **iteration-protocol** -- generators produce iterators
- **iterator-interface** -- the returned object follows this interface

# Key Properties

1. Introduced in ES2015 (ES6)
2. Declared with `function*` or `*` method modifier
3. Calling returns an iterator without executing the body
4. `yield` pauses execution and returns a value
5. The returned iterator is also iterable (iterable iterator)
6. Supports four declaration forms: function declaration, function expression, object method, class method

# Construction / Recognition

```js
// Generator function declaration
function* genFunc1() { /*...*/ }

// Generator function expression
const genFunc2 = function* () { /*...*/ };

// Generator method in object literal
const obj = { * generatorMethod() { } };

// Generator method in class
class MyClass { * generatorMethod() { } }
```

# Context & Application

Generators are used to implement custom iterators, create lazy sequences, transform iterables, and reuse traversal logic. They are fundamental for any scenario requiring on-demand value production.

# Examples

```js
function* createIterator() {
  yield 'a';
  yield 'b';
}

Array.from(createIterator()); // ['a', 'b']

for (const x of createIterator()) {
  console.log(x);
}
// Output: a, b
```

(Chapter 33, Section 33.1.1, lines 84-115)

# Relationships

## Builds Upon
- **iteration-protocol** -- generators produce protocol-compliant iterators
- **iterator-interface** -- the return value implements Iterator

## Enables
- **yield-operator** -- the mechanism for producing values
- **yield-star-operator** -- delegation to other generators/iterables
- Lazy data processing pipelines

## Related
- **iterable-iterator** -- generator objects are iterable iterators

## Contrasts With
- None at this scope

# Common Errors

- **Error**: Expecting the generator body to execute when calling the function.
  **Correction**: Calling a generator function only creates an iterator. The body runs incrementally via `.next()`.

# Common Confusions

- **Confusion**: `yield` works like `return`.
  **Clarification**: Like `return`, `yield` exits and returns a value. Unlike `return`, execution resumes directly after the `yield` on the next `.next()` call.

# Source Reference

Chapter 33: Synchronous generators (advanced), Section 33.1, lines 45-115.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with all four declaration forms
- Cross-reference status: verified
