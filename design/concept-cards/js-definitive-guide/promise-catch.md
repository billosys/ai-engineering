---
concept: Promise.catch() and .finally()
slug: promise-catch
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 373
section: "13.2.4 More on Promises and Errors"
extraction_confidence: high
aliases:
  - ".catch()"
  - ".finally()"
  - "Promise error handling"
prerequisites:
  - promise-chaining
extends: []
related:
  - promise-then
contrasts_with: []
answers_questions:
  - "How do I handle errors in a Promise chain?"
---

# Quick Definition

The `.catch()` method (shorthand for `.then(null, handler)`) handles rejected Promises by catching errors that "trickle down the chain," while `.finally()` (ES2018) runs cleanup code regardless of fulfillment or rejection.

# Core Definition

"The .catch() method of a Promise is simply a shorthand way to call .then() with null as the first argument and an error-handling callback as the second argument" (p. 373). Errors propagate down the chain until a `.catch()` handles them. "Once an error has been passed to a .catch() callback, it stops propagating" (p. 376). `.finally()` callbacks run when the Promise settles, receive no arguments, and their return value is ignored.

# Prerequisites

- **promise-chaining** — catch/finally are used in Promise chains

# Key Properties

1. `.catch(handler)` === `.then(null, handler)`
2. Catches errors from any earlier stage in the chain
3. If catch handler returns normally, error stops propagating
4. `.catch()` can appear mid-chain for recoverable errors
5. `.finally()` runs on both fulfillment and rejection; no arguments passed
6. `.finally()` return value is ignored; it passes through the previous value

# Construction / Recognition

```js
fetch("/api/data")
    .then(response => response.json())
    .then(data => process(data))
    .catch(e => handleError(e))
    .finally(() => hideSpinner());

// Mid-chain error recovery:
startOp()
    .then(doStageTwo)
    .catch(recoverFromStageTwoError)
    .then(doStageThree)
    .catch(logErrors);
```

# Context & Application

Ending every Promise chain with `.catch()` is essential for proper error handling. Mid-chain `.catch()` enables recovery from specific errors while continuing the chain.

# Examples

From the source text (p. 375-377): Mid-chain recovery: `queryDatabase().catch(e => wait(500).then(queryDatabase)).then(displayTable).catch(displayDatabaseError)` retries on first failure. If `recoverFromStageTwoError()` returns normally, `doStageThree()` runs with its return value.

# Relationships

## Builds Upon
- **Promise Chaining** — catch/finally are chain operators

## Related
- **Promise.then()** — catch is shorthand for then(null, handler)

# Common Errors

- **Error**: Using `.then(handler, errorHandler)` instead of `.catch()` at the end.
  **Correction**: The two-argument form of `.then()` won't catch errors thrown by `handler` itself. Use `.catch()` at the end to catch all errors in the chain.

# Common Confusions

- **Confusion**: Thinking `.finally()` can change the resolved value.
  **Clarification**: `.finally()` return value is ignored. The Promise resolves/rejects with the same value as the previous Promise, unless `.finally()` throws.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.4, pages 373-378.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
