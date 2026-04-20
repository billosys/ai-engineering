---
concept: Iterator return() Method
slug: iterator-return-method
category: iterators-generators
subcategory: iterator-protocol
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 349
section: "12.2.1 Closing an Iterator: The Return Method"
extraction_confidence: high
aliases:
  - "iterator cleanup"
  - "closing iterators"
prerequisites:
  - iterator-protocol
extends: []
related:
  - generator-return-throw
contrasts_with: []
answers_questions: []
---

# Quick Definition

An optional method on iterator objects that is called when iteration ends early (via `break`, `return`, or exception in a `for/of` loop), giving the iterator a chance to release resources like open files or network connections.

# Core Definition

"If iteration stops before next() has returned an iteration result with the done property set to true... then the interpreter will check to see if the iterator object has a return() method. If this method exists, the interpreter will invoke it with no arguments, giving the iterator the chance to close files, release memory, and otherwise clean up after itself" (p. 349).

# Prerequisites

- **iterator-protocol** — return() is an optional part of the iterator protocol

# Key Properties

1. Optional method on iterator objects
2. Called automatically by for/of when loop exits early (break, return, throw)
3. Called automatically during destructuring when not all values are consumed
4. Must return an iterator result object (properties are ignored)
5. For generators, triggers finally blocks in try/finally
6. Returning a non-object value is an error

# Construction / Recognition

```js
// Iterator with cleanup:
function createIterator(resource) {
    return {
        next() { /* ... */ },
        return() {
            resource.close();
            return { done: true };
        }
    };
}
```

# Context & Application

Important for iterators that manage resources (file handles, database connections, network sockets). Ensures cleanup happens even when iteration is interrupted.

# Examples

From the source text (p. 349): The hypothetical words-in-a-file iterator needs to close its file handle even if iteration ends early via break.

# Relationships

## Builds Upon
- **Iterator Protocol** — return() is an optional part of the protocol

## Related
- **Generator return/throw** — Generator return() triggers finally blocks

# Common Errors

- **Error**: Forgetting to implement return() on iterators that manage resources.
  **Correction**: Always implement return() for iterators that open files, connections, or acquire resources.

# Common Confusions

- **Confusion**: Thinking return() is required for all iterators.
  **Clarification**: return() is optional. Only implement it when cleanup is needed for early termination.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.2.1, page 349.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
