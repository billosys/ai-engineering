---
concept: Generator return() and throw() Methods
slug: generator-return-throw
category: iterators-generators
subcategory: generators
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 355
section: "12.4.3 The return() and throw() Methods of a Generator"
extraction_confidence: high
aliases: []
prerequisites:
  - generator-functions
  - sending-values-to-generators
extends: []
related:
  - iterator-protocol
contrasts_with: []
answers_questions: []
---

# Quick Definition

Methods on generator objects that force the generator to return a value or throw an exception at the point where it is paused, enabling cleanup via try/finally and external flow control.

# Core Definition

"Calling these methods on a generator causes it to return a value or throw an exception as if the next statement in the generator was a return or throw" (p. 355). `return()` triggers the generator's finally blocks for cleanup. `throw()` causes an exception inside the generator that can be caught with try/catch to alter behavior.

# Prerequisites

- **generator-functions** — These methods exist on generator objects
- **sending-values-to-generators** — Understanding bidirectional communication

# Key Properties

1. `return(value)` — forces generator to return, triggering finally blocks
2. `throw(error)` — causes exception at paused yield; catchable inside generator
3. Used by for/of when loop exits early (break/return/exception) — calls `return()`
4. With yield*, return/throw propagate to the delegated iterator

# Construction / Recognition

```js
function* gen() {
    try {
        yield 1; yield 2; yield 3;
    } finally {
        console.log("cleanup");  // Runs when return() is called
    }
}
let g = gen();
g.next();     // {value: 1, done: false}
g.return(99); // Logs "cleanup", returns {value: 99, done: true}
```

# Context & Application

`return()` is used for resource cleanup (closing files, releasing connections) when iteration ends early. `throw()` provides a mechanism for external code to signal errors or reset a generator.

# Examples

From the source text (p. 355-356): When a for/of loop exits early via break, the interpreter calls `return()` on the iterator, giving generators a chance to clean up via try/finally. `throw()` can be used to reset a counter generator by throwing a catchable exception.

# Relationships

## Builds Upon
- **Generator Functions** — These are methods on generator objects

## Related
- **Iterator Protocol** — `return()` is part of the optional iterator cleanup protocol

# Common Errors

- **Error**: Expecting custom `return()` method to be defined on generators.
  **Correction**: Generators have a built-in `return()` method. Use try/finally inside the generator for cleanup, not a custom `return()`.

# Common Confusions

- **Confusion**: Thinking `throw()` always terminates the generator.
  **Clarification**: If the generator has a try/catch around the yield, the exception is caught and the generator can continue running.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.4.3, pages 355-357.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
