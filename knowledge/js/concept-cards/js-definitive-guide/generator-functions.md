---
concept: Generator Functions
slug: generator-functions
category: iterators-generators
subcategory: generators
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 349
section: "12.3 Generators"
extraction_confidence: high
aliases:
  - "function*"
  - "generator"
prerequisites:
  - iterator-protocol
extends: []
related:
  - yield-keyword
  - yield-star-delegation
  - generator-return-throw
contrasts_with: []
answers_questions:
  - "What is a generator function?"
  - "What must I understand before learning about generators?"
---

# Quick Definition

Functions declared with `function*` syntax that return generator objects — iterators whose values are produced lazily by `yield` expressions, pausing and resuming execution between each value.

# Core Definition

"A *generator* is a kind of iterator defined with powerful new ES6 syntax" (p. 349). "A generator function is syntactically like a regular JavaScript function but is defined with the keyword function* rather than function. When you invoke a generator function, it does not actually execute the function body, but instead returns a generator object. This generator object is an iterator" (p. 349). Calling `next()` runs the body until a `yield` statement.

# Prerequisites

- **iterator-protocol** — Generators produce iterators

# Key Properties

1. Defined with `function*` (statement, expression, or method shorthand `*method()`)
2. Invoking returns a generator object (does not execute the body)
3. `next()` runs the body until the next `yield`
4. The yielded value becomes `next().value`
5. Generator objects are both iterators and iterables
6. Cannot be defined with arrow function syntax

# Construction / Recognition

```js
function* oneDigitPrimes() {
    yield 2; yield 3; yield 5; yield 7;
}
let primes = oneDigitPrimes();
primes.next().value  // => 2
[...oneDigitPrimes()]  // => [2,3,5,7]

// Expression form:
const seq = function*(from, to) { for(let i = from; i <= to; i++) yield i; };

// Method shorthand:
let o = { *g() { for(let key of Object.keys(this)) yield key; } };
```

# Context & Application

Generators dramatically simplify creating custom iterators. Instead of manually implementing `next()` and managing state, you write sequential code with `yield` statements.

# Examples

From the source text (p. 349-351): `function* oneDigitPrimes()` yields 2, 3, 5, 7. Generator as class method: `*[Symbol.iterator]() { for(let x = Math.ceil(this.from); x <= this.to; x++) yield x; }` replaces a complex manual iterator.

# Relationships

## Builds Upon
- **Iterator Protocol** — Generators implement the iterator protocol

## Enables
- **Yield Keyword** — The mechanism for producing values
- **Yield* Delegation** — Delegating to sub-iterables
- **Generator return/throw** — Flow control methods
- **Async Generators** — The async version

## Related
- **Lazy Evaluation** — Generators are inherently lazy

# Common Errors

- **Error**: Using `yield` inside an arrow function nested within a generator.
  **Correction**: `yield` can only appear directly within a `function*` body. Arrow functions inside generators cannot use `yield`.

# Common Confusions

- **Confusion**: Expecting the generator function body to run when called.
  **Clarification**: Calling a generator function returns a generator object without executing any code. Code runs only when `next()` is called.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.3, pages 349-352.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — core chapter topic
- Uncertainties: None
- Cross-reference status: Verified
