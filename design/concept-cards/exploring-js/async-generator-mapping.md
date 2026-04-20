---
concept: Mapping Over Async Iterables
slug: async-generator-mapping
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Asynchronous iteration"
chapter_number: 45
pdf_page: null
section: "45.2.5 Example: mapping over asynchronous iterables"
extraction_confidence: high
aliases:
  - async iterable map
  - mapAsync
prerequisites:
  - async-generator
  - for-await-of
extends: []
related:
  - async-iterable-to-array
contrasts_with: []
answers_questions:
  - "How do synchronous and asynchronous iteration protocols differ?"
---

# Quick Definition

Async generators can transform async iterables using the same patterns as sync generators: an `async function*` takes an async iterable, iterates with `for-await-of`, and `yield`s transformed values, creating composable stream-processing pipelines.

# Core Definition

"Exploring JavaScript" Ch. 45 shows that async mapping mirrors sync mapping: "Note how similar the sync implementation and the async implementation are. The only two differences are the async in line A and the await in line B." This demonstrates that going from sync to async iteration only requires adding `async` and `await`.

# Prerequisites

- **Async generator** -- produces the transformed iterable
- **for-await-of** -- iterates input

# Key Properties

1. Pattern mirrors synchronous generator mapping
2. Only differences from sync: add `async` and `await`
3. Creates composable transformation pipelines
4. Lazy: values produced on demand

# Construction / Recognition

Sync:
```js
function* mapSync(iterable, func) {
  let index = 0;
  for (const x of iterable) { yield func(x, index); index++; }
}
```

Async:
```js
async function* mapAsync(asyncIterable, func) {
  let index = 0;
  for await (const x of asyncIterable) { yield func(x, index); index++; }
}
```

(Ch. 45, Section 45.2.5, lines 448-471)

# Context & Application

Enables functional-style data processing over async data sources (streams, APIs, etc.) with composable transformations.

# Examples

```js
const mapped = mapAsync(createAsyncIterable(), s => s.repeat(3));
assert.deepEqual(await asyncIterableToArray(mapped), ['aaa', 'bbb']);
```

(Ch. 45, Section 45.2.5, lines 490-494)

# Relationships

## Builds Upon
- **Async generator** -- the transformation mechanism
- **for-await-of** -- consumes the input

## Related
- **Async iterable to Array** -- collects the output

# Common Errors

- **Error**: Forgetting `await` in `for await` when transforming async iterables
  **Correction**: Must use `for await` with async iterables, not plain `for`

# Common Confusions

- **Confusion**: Async mapping requires complex new patterns
  **Clarification**: The pattern is nearly identical to sync mapping -- just add `async` and `await`

# Source Reference

Chapter 45: Asynchronous iteration, Section 45.2.5, lines 442-498.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit comparison between sync and async versions
- Cross-reference status: verified
