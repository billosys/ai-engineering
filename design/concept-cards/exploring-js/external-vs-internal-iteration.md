---
concept: External vs. Internal Iteration
slug: external-vs-internal-iteration
category: iteration
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous generators (advanced)"
chapter_number: 33
pdf_page: null
section: "33.3.1 Background: external iteration vs. internal iteration"
extraction_confidence: high
aliases:
  - "pull iteration"
  - "push iteration"
prerequisites:
  - iteration-protocol
  - generator-function
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is needed to understand generator functions?"
---

# Quick Definition

External iteration (pull) uses an iteration protocol where the consumer asks for values one at a time; internal iteration (push) passes a callback to the data source which feeds values to it.

# Core Definition

External iteration (pull): code asks the object for values via an iteration protocol, e.g., the for-of loop. Internal iteration (push): a callback function is passed to a method of the object and the method feeds the values to the callback, e.g., `.forEach()`. Generators enable reusing traversal code via external iteration, yielding values instead of passing them to callbacks.

# Prerequisites

- **iteration-protocol** -- external iteration uses it
- **generator-function** -- generators bridge internal traversals to external iteration

# Key Properties

1. External (pull): for-of, iterator protocol -- consumer controls pace
2. Internal (push): .forEach(), callbacks -- producer controls pace
3. Generators convert internal traversals to external iterators
4. External iteration enables lazy processing and composition

# Construction / Recognition

```js
// External iteration (pull)
for (const x of ['a', 'b']) { console.log(x); }

// Internal iteration (push)
['a', 'b'].forEach((x) => { console.log(x); });
```

# Context & Application

The distinction matters when reusing traversal logic. Generators make external iteration practical for complex traversals (e.g., file trees), enabling composition with for-of, spread, and iterator methods.

# Examples

```js
// Internal iteration (push) - callback-based
function visitPaths(dir, callback) {
  for (const fileName of fs.readdirSync(dir)) {
    const filePath = path.join(dir, fileName);
    callback(filePath);
    if (fs.statSync(filePath).isDirectory()) {
      visitPaths(filePath, callback);
    }
  }
}

// External iteration (pull) - generator-based
function* iterPaths(dir) {
  for (const fileName of fs.readdirSync(dir)) {
    const filePath = path.join(dir, fileName);
    yield filePath;
    if (fs.statSync(filePath).isDirectory()) {
      yield* iterPaths(filePath);
    }
  }
}
const paths = Array.from(iterPaths('mydir'));
```

(Chapter 33, Section 33.3, lines 469-614)

# Relationships

## Builds Upon
- **iteration-protocol** -- external iteration
- **generator-function** -- enables pull-based traversal

## Enables
- Reusable traversal patterns

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Using `.forEach()` when needing to break early.
  **Correction**: Use for-of (external iteration) which supports `break` and `continue`.

# Common Confusions

- **Confusion**: External and internal iteration produce different results.
  **Clarification**: They produce the same values; the difference is who controls the iteration flow.

# Source Reference

Chapter 33: Synchronous generators (advanced), Section 33.3, lines 469-614.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly contrasted with side-by-side examples
- Cross-reference status: verified
