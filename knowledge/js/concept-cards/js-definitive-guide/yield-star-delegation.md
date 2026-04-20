---
concept: "yield* Delegation"
slug: yield-star-delegation
category: iterators-generators
subcategory: generators
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 352
section: "12.3.2 yield* and Recursive Generators"
extraction_confidence: high
aliases:
  - "yield delegation"
  - "yield star"
prerequisites:
  - generator-functions
  - yield-keyword
extends: []
related:
  - iterator-protocol
contrasts_with: []
answers_questions: []
---

# Quick Definition

The `yield*` expression that delegates iteration to another iterable, yielding each of its values in sequence, enabling composition of generators and recursive generator patterns.

# Core Definition

"The yield* keyword is like yield except that, rather than yielding a single value, it iterates an iterable object and yields each of the resulting values" (p. 352). It works with any iterable, including other generators, enabling recursive generators for tree traversal and similar patterns.

# Prerequisites

- **generator-functions** — yield* is used within generators
- **yield-keyword** — yield* extends the basic yield concept

# Key Properties

1. `yield*` iterates an iterable and yields each value individually
2. Works with any iterable (arrays, strings, Sets, other generators)
3. Enables recursive generators for tree structures
4. Propagates `return()` and `throw()` to the delegated iterator
5. Cannot be used inside nested arrow functions (same restriction as `yield`)

# Construction / Recognition

```js
function* sequence(...iterables) {
    for(let iterable of iterables) {
        yield* iterable;
    }
}
[...sequence("abc", oneDigitPrimes())]  // => ["a","b","c",2,3,5,7]
```

# Context & Application

Used to compose generators from sub-generators or other iterables. Essential for recursive patterns like tree traversal where each node delegates to its children.

# Examples

From the source text (p. 352-353): Without yield*: nested `for/of` loops with explicit `yield`. With yield*: `yield* iterable` replaces the inner loop. Error case: `iterables.forEach(iterable => yield* iterable)` is a SyntaxError because yield cannot appear in arrow/regular functions nested inside a generator.

# Relationships

## Builds Upon
- **Generator Functions** — yield* is a generator feature
- **Yield Keyword** — yield* extends yield to iterables

## Related
- **Iterator Protocol** — yield* works with any iterable object

# Common Errors

- **Error**: Using yield* inside `forEach()` or `map()`: `iterables.forEach(iterable => yield* iterable)`.
  **Correction**: yield/yield* can only be used directly in generator function bodies. Use a `for/of` loop instead.

# Common Confusions

- **Confusion**: Thinking yield* yields the iterable object itself.
  **Clarification**: yield* iterates the iterable and yields each value individually, not the iterable as a whole.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.3.2, pages 352-353.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
