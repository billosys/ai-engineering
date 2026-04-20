---
concept: Infinite Sequences with Generators
slug: infinite-sequences
category: iterators-generators
subcategory: generators
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 351
section: "12.3.1 Generator Examples"
extraction_confidence: high
aliases: []
prerequisites:
  - generator-functions
  - lazy-evaluation-iterators
extends: []
related: []
contrasts_with: []
answers_questions: []
---

# Quick Definition

Generator functions with infinite loops that yield values forever, useful with `take()` or bounded `for/of` loops for computing sequences like Fibonacci numbers without allocating infinite storage.

# Core Definition

Generators can define infinite sequences because values are computed lazily. The `fibonacciSequence()` generator uses `for(;;)` and "yields values forever without returning" (p. 351). These generators must be consumed carefully — using them with spread `...` will crash the program.

# Prerequisites

- **generator-functions** — Infinite sequences are implemented as generators
- **lazy-evaluation-iterators** — Laziness makes infinite sequences practical

# Key Properties

1. Use infinite loops (`for(;;)`, `while(true)`) with yield
2. Must be consumed with bounded iteration (for/of with break, or take())
3. Spread `[...]` on an infinite generator crashes the program
4. Compose well with utility generators like `take(n, iterable)`

# Construction / Recognition

```js
function* fibonacciSequence() {
    let x = 0, y = 1;
    for(;;) { yield y; [x, y] = [y, x+y]; }
}
function* take(n, iterable) {
    let it = iterable[Symbol.iterator]();
    while(n-- > 0) { let next = it.next(); if (next.done) return; else yield next.value; }
}
[...take(5, fibonacciSequence())]  // => [1, 1, 2, 3, 5]
```

# Context & Application

Modeling mathematical sequences, generating test data, and creating lazy pipelines where the consumer determines how many values to process.

# Examples

From the source text (p. 351-352): Fibonacci generator consumed with a bounded for/of: `function fibonacci(n) { for(let f of fibonacciSequence()) { if (n-- <= 0) return f; } }; fibonacci(20)` returns 10946.

# Relationships

## Builds Upon
- **Generator Functions** — Infinite sequences are generators
- **Lazy Evaluation** — Lazy evaluation makes infinite sequences possible

# Common Errors

- **Error**: Using `[...infiniteGenerator()]` or `Array.from(infiniteGenerator())`.
  **Correction**: Never spread or convert an infinite generator to an array. Use `take()` or a bounded loop.

# Common Confusions

- **Confusion**: Thinking generators detect and prevent infinite iteration.
  **Clarification**: Generators have no built-in protection against infinite iteration. It is the consumer's responsibility to limit consumption.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.3.1, pages 351-352.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
