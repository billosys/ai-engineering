---
concept: Lazy Evaluation with Generators
slug: lazy-evaluation-generators
category: iteration
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous generators (advanced)"
chapter_number: 33
pdf_page: null
section: "33.1.3 Why does yield pause execution?"
extraction_confidence: high
aliases:
  - "lazy iteration"
  - "on-demand evaluation"
prerequisites:
  - generator-function
  - yield-operator
extends: []
related:
  - iterator-helper-methods
contrasts_with: []
answers_questions:
  - "What is needed to understand generator functions?"
---

# Quick Definition

Generators enable lazy evaluation by producing values on demand through yield pausing -- each value is computed only when requested via `.next()`, avoiding the need to precompute entire collections.

# Core Definition

Due to pausing, generators provide many features of coroutines (processes that are multitasked cooperatively). When we ask for the next value of a generator-backed iterator, that value is computed lazily (on demand). This incrementalism means that if a generator reads from a large file, we get the first processed line as soon as one line is read, rather than waiting for all lines.

# Prerequisites

- **generator-function** -- the mechanism for lazy evaluation
- **yield-operator** -- the pause mechanism

# Key Properties

1. Values computed one at a time, only when requested
2. Enables processing of large or infinite data without memory overhead
3. Generator pipelines process incrementally (no intermediate collections)
4. Complements iterator helper methods for incremental processing

# Construction / Recognition

```js
function* numberLines(lineIterable) {
  let lineNumber = 1;
  for (const line of lineIterable) {
    yield lineNumber + ': ' + line;
    lineNumber++;
  }
}
// Each line is processed on demand
```

# Context & Application

Lazy evaluation is critical when dealing with large datasets, streaming data, infinite sequences, or chained transformations where creating intermediate arrays would be wasteful.

# Examples

```js
function* genLines() {
  yield 'A line';
  yield 'Another line';
  yield 'Last line';
}

const numberedLines = numberLines(genLines());
numberedLines.next(); // { value: '1: A line', done: false }
// Only one line from each generator was processed
```

(Chapter 33, Section 33.1.3, lines 219-298)

# Relationships

## Builds Upon
- **generator-function** -- provides the mechanism
- **yield-operator** -- enables pause/resume

## Enables
- Efficient processing of large data
- Generator pipelines

## Related
- **iterator-helper-methods** -- also enable lazy processing chains

## Contrasts With
- None

# Common Errors

- **Error**: Collecting all generator values into an Array unnecessarily.
  **Correction**: Consume values lazily with for-of or iterator methods when the full array is not needed.

# Common Confusions

- **Confusion**: Generators are always faster than Arrays.
  **Clarification**: Generators add overhead per value. They are beneficial for large datasets or when not all values are needed, but for small arrays, direct methods may be simpler and equally fast.

# Source Reference

Chapter 33: Synchronous generators (advanced), Section 33.1.3, lines 219-298.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained with incremental processing example
- Cross-reference status: verified
