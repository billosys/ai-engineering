---
concept: Sequential vs Parallel Await
slug: sequential-vs-parallel-await
category: async-programming
subcategory: async-await
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 387
section: "13.3.3 Awaiting Multiple Promises"
extraction_confidence: high
aliases: []
prerequisites:
  - await-expressions
  - promise-all
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How does `async/await` relate to Promises?"
---

# Quick Definition

The distinction between sequentially awaiting independent Promises (which wastes time) and using `Promise.all()` with `await` to run them concurrently, which is critical for performance.

# Core Definition

Sequential awaits like `let v1 = await getJSON(url1); let v2 = await getJSON(url2)` are "unnecessarily sequential: the fetch of the second URL will not begin until the first fetch is complete" (p. 387). For independent operations, use `let [v1, v2] = await Promise.all([getJSON(url1), getJSON(url2)])`.

# Prerequisites

- **await-expressions** — Understanding how await works
- **promise-all** — Using Promise.all() for concurrent execution

# Key Properties

1. Sequential await: each operation waits for the previous to complete
2. Parallel await: start all operations, await the combined result
3. Use `Promise.all()` when operations are independent
4. Use sequential await when later operations depend on earlier results
5. Destructuring works with await: `let [v1, v2] = await Promise.all([...])`

# Construction / Recognition

Sequential (wrong for independent ops):
```js
let value1 = await getJSON(url1);
let value2 = await getJSON(url2);  // Doesn't start until url1 completes
```

Parallel (correct):
```js
let [value1, value2] = await Promise.all([getJSON(url1), getJSON(url2)]);
```

# Context & Application

A common performance pitfall with async/await. Always consider whether awaited operations are independent and can run in parallel.

# Examples

From the source text (p. 387-388): Two independent getJSON calls should use `Promise.all()` instead of sequential await, potentially halving the total wait time.

# Relationships

## Builds Upon
- **Await Expressions** — Sequential/parallel distinction applies to await
- **Promise.all()** — The mechanism for parallel awaiting

# Common Errors

- **Error**: Sequentially awaiting independent fetches, doubling response time.
  **Correction**: Use `await Promise.all([...])` for independent operations.

# Common Confusions

- **Confusion**: Thinking `Promise.all()` is only for `.then()` chains and not usable with await.
  **Clarification**: `await Promise.all([...])` is the idiomatic way to run parallel operations in async functions.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.3.3, pages 387-388.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
