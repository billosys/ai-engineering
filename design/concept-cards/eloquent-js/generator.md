---
# === CORE IDENTIFICATION ===
concept: Generator
slug: generator

# === CLASSIFICATION ===
category: asynchronous-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Asynchronous Programming"
chapter_number: 11
pdf_page: null
section: "Generators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - generator function
  - function*

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
extends: []
related:
  - async-function
  - async-iteration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does async/await relate to promises?"
---

# Quick Definition
A generator is a function defined with `function*` that can be paused and resumed, yielding values one at a time through an iterator interface.

# Core Definition
"When you define a function with `function*` (placing an asterisk after the word `function`), it becomes a generator. When you call a generator, it returns an iterator." "Every time you call `next` on the iterator, the function runs until it hits a `yield` expression, which pauses it and causes the yielded value to become the next value produced by the iterator." (Eloquent JavaScript, Ch. 11, lines 689-716)

# Prerequisites
- **Functions**: Understanding function definition and invocation
- Understanding iterators and the iteration protocol

# Key Properties
1. Defined with `function*` syntax
2. Returns an iterator when called
3. Pauses at each `yield` expression
4. Saves local state between yields
5. `yield` can only occur directly in the generator function, not in inner functions
6. Async functions are a special type of generator

# Construction / Recognition
```javascript
function* powers(n) {
  for (let current = n;; current *= n) {
    yield current;
  }
}

for (let power of powers(3)) {
  if (power > 50) break;
  console.log(power);
}
// -> 3
// -> 9
// -> 27
```
(lines 695-708)

# Context & Application
Generators simplify writing iterators and share the pause/resume mechanism with async functions. They are useful for lazy sequences and custom iteration patterns.

# Examples
From the source, implementing an iterator for a Group class:
```javascript
Group.prototype[Symbol.iterator] = function*() {
  for (let i = 0; i < this.members.length; i++) {
    yield this.members[i];
  }
};
```
(lines 725-729)

"An `async` function is a special type of generator. It produces a promise when called, which is resolved when it returns (finishes) and rejected when it throws an exception." (lines 745-747)

# Relationships
## Builds Upon
- Functions and the iterator protocol
## Enables
- Easy iterator creation
- Foundation for async/await mechanism
## Related
- Async functions (special type of generator)
## Contrasts With
- Regular functions (which run to completion)

# Common Errors
- **Error**: Using `yield` inside a nested function within the generator
  **Correction**: "Such `yield` expressions may occur only directly in the generator function itself and not in an inner function you define inside of it." (lines 738-740)

# Common Confusions
- **Confusion**: Generators are the same as async functions
  **Clarification**: Generators yield values through an iterator; async functions yield promises. "These are similar, but without the promises." (lines 685-686)

# Source Reference
Chapter 11: Asynchronous Programming, Section "Generators", lines 680-749 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clear definition with examples
- Cross-reference status: verified
