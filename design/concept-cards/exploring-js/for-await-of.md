---
concept: for-await-of Loop
slug: for-await-of
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Asynchronous iteration"
chapter_number: 45
pdf_page: null
section: "45.1.3 Using async iteration via for-await-of"
extraction_confidence: high
aliases:
  - for await of
  - async for loop
prerequisites:
  - async-iteration-protocol
  - async-function
extends:
  - for-await-of-loop
related:
  - async-generator
contrasts_with:
  - for-of-loop
answers_questions:
  - "How do synchronous and asynchronous iteration protocols differ?"
  - "What must I understand before working with async iteration?"
---

# Quick Definition

`for-await-of` is an asynchronous version of the `for-of` loop that can iterate over async iterables, sync iterables, and sync iterables of Promises, unwrapping each value asynchronously within an async function or async generator.

# Core Definition

"Exploring JavaScript" Ch. 45: "The asynchronous iteration protocol is not meant to be used directly. One of the language constructs that supports it is the for-await-of loop, which is an asynchronous version of the for-of loop." It is introduced in ES2018 and "can be used in async functions and async generators."

# Prerequisites

- **Async iteration protocol** -- `for-await-of` consumes async iterables
- **Async function** -- `for-await-of` can only be used in async contexts

# Key Properties

1. Introduced in ES2018
2. Works with async iterables (primary use)
3. Also works with sync iterables (convenience)
4. Also works with sync iterables of Promises (unwraps them)
5. Can only be used in async functions and async generators

# Construction / Recognition

```js
for await (const x of syncToAsyncIterable(['a', 'b'])) {
  console.log(x);
}
// Output: a, b

// Also works with sync iterables:
for await (const x of ['a', 'b']) { console.log(x); }

// And sync iterables of Promises:
const arr = [Promise.resolve('a'), Promise.resolve('b')];
for await (const x of arr) { console.log(x); }
```

(Ch. 45, Section 45.1.3, lines 187-241)

# Context & Application

Primary way to consume async iterables such as Node.js streams, paginated APIs, or any data source that produces values over time.

# Examples

Reading from a Node.js stream:
```js
async function main(inputFilePath) {
  const readStream = fs.createReadStream(inputFilePath,
    { encoding: 'utf-8', highWaterMark: 1024 });
  for await (const chunk of readStream) {
    console.log('>>> ' + chunk);
  }
}
```

(Ch. 45, Section 45.3.2, lines 546-554)

# Relationships

## Builds Upon
- **Async iteration protocol** -- the protocol it consumes

## Related
- **Async generator** -- produces values that `for-await-of` consumes

## Contrasts With
- **for-of loop** -- sync version; `for-await-of` is the async version

# Common Errors

- **Error**: Using `for-await-of` outside an async function
  **Correction**: Wrap in an async function or use top-level await in a module

# Common Confusions

- **Confusion**: `for-await-of` only works with async iterables
  **Clarification**: It also accepts sync iterables and sync iterables of Promises

# Source Reference

Chapter 45: Asynchronous iteration, Section 45.1.3, lines 187-257.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with multiple examples
- Cross-reference status: verified
