---
concept: for/await Loop
slug: for-await-loop
category: async-programming
subcategory: async-iteration
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 387
section: "13.4.1 The for/await Loop"
extraction_confidence: high
aliases:
  - "for await...of"
prerequisites:
  - async-functions
  - async-iterators
extends: []
related:
  - iterator-protocol
contrasts_with: []
answers_questions:
  - "What must I understand before learning about async iteration?"
---

# Quick Definition

A loop syntax (`for await (const x of iterable)`) that awaits each value from an asynchronous iterable, running the loop body once for each resolved value, and can only be used inside async functions.

# Core Definition

"Asynchronous iterators are like the iterators described in Chapter 12, but they are Promise-based and are meant to be used with a new form of the for/of loop: for/await" (p. 388). The loop gets a Promise from the iterator, waits for it to fulfill, assigns the value to the loop variable, runs the body, then repeats.

# Prerequisites

- **async-functions** — for/await can only appear inside async functions
- **async-iterators** — The primary target of for/await loops

# Key Properties

1. Can only be used inside `async` functions
2. Works with both async iterables (Symbol.asyncIterator) and regular iterables
3. Prefers Symbol.asyncIterator if available, falls back to Symbol.iterator
4. Awaits each value from the iterator
5. ES2018 feature

# Construction / Recognition

```js
const fs = require("fs");
async function parseFile(filename) {
    let stream = fs.createReadStream(filename, { encoding: "utf-8"});
    for await (let chunk of stream) {
        parseChunk(chunk);
    }
}
```

# Context & Application

Used to process streams of asynchronous data with simple loop syntax. Essential for Node readable streams, real-time data feeds, and any async event sequence.

# Examples

From the source text (p. 387-389): Reading Node streams: `for await (let chunk of stream) { parseChunk(chunk); }`. Also works with regular arrays of Promises: `for await (const response of promises) { handle(response); }`.

# Relationships

## Builds Upon
- **Async Functions** — for/await requires async context
- **Async Iterators** — The primary data source for for/await

## Related
- **Iterator Protocol** — for/await also works with sync iterables

# Common Errors

- **Error**: Using for/await outside of an async function.
  **Correction**: The containing function must be declared `async`.

# Common Confusions

- **Confusion**: Thinking for/await processes items in parallel.
  **Clarification**: for/await is sequential — it waits for each Promise to fulfill before starting the next iteration.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.4.1, pages 387-389.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
