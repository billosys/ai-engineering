---
concept: Yield Keyword
slug: yield-keyword
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
  - "yield expression"
prerequisites:
  - generator-functions
extends: []
related:
  - yield-star-delegation
  - sending-values-to-generators
contrasts_with: []
answers_questions:
  - "What is a generator function?"
---

# Quick Definition

The `yield` keyword used inside generator functions to pause execution and produce a value to the caller, resuming when `next()` is called again.

# Core Definition

"yield is new in ES6 and is something like a return statement. The value of the yield statement becomes the value returned by the next() call on the iterator" (p. 349). yield is also an expression — it can receive a value passed via `next(value)`, where the argument becomes the value of the yield expression when execution resumes.

# Prerequisites

- **generator-functions** — yield can only appear inside generator functions

# Key Properties

1. Pauses generator execution and produces a value
2. The yielded value becomes `next().value` for the caller
3. As an expression, yield receives the argument of the *next* `next()` call
4. Can only be used directly in `function*` bodies (not nested arrow functions)
5. `yield` without a value produces `undefined`

# Construction / Recognition

```js
function* range(from, to) {
    for(let i = from; i <= to; i++) yield i;
}
```

# Context & Application

yield is the fundamental mechanism for generators to produce sequences of values lazily. It also enables bidirectional communication between generator and caller.

# Examples

From the source text (p. 349-350): `function* oneDigitPrimes() { yield 2; yield 3; yield 5; yield 7; }`. Each `next()` call runs until the next `yield` and returns the yielded value. After the last `yield`, the next `next()` returns `{done: true}`.

# Relationships

## Builds Upon
- **Generator Functions** — yield is only valid inside generators

## Enables
- **Sending Values to Generators** — yield as an expression receives values from `next()`
- **Yield* Delegation** — Extending yield to delegate to sub-iterables

# Common Errors

- **Error**: Using `yield` inside a `forEach()` callback within a generator.
  **Correction**: yield cannot appear in nested non-generator functions. Use a `for/of` loop instead.

# Common Confusions

- **Confusion**: Thinking yield works like return and terminates the function.
  **Clarification**: yield pauses the function; it does not terminate it. Execution resumes from the yield point on the next `next()` call.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.3, pages 349-350.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
