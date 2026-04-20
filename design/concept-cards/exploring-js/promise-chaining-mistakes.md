---
concept: Promise Chaining Mistakes
slug: promise-chaining-mistakes
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.7 Tips for chaining Promises"
extraction_confidence: high
aliases:
  - Promise anti-patterns
prerequisites:
  - promise-chaining
extends: []
related:
  - promise-error-handling
contrasts_with: []
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

Common Promise chaining mistakes include: losing the tail (returning the original Promise instead of the chain), unnecessary nesting (putting `.then()` inside another `.then()`), and creating Promises instead of chaining (wrapping existing Promises in `new Promise()`).

# Core Definition

"Exploring JavaScript" Ch. 43 identifies four chaining mistakes: (1) "Losing the tail" -- returning the original Promise instead of the chain result. (2) "Nesting" -- putting `.then()` inside a callback instead of chaining flat. (3) "More nesting than necessary" -- avoidable nesting with conditional returns. (4) "Creating Promises instead of chaining" -- wrapping in `new Promise()` when chaining suffices. The text also notes: "Not all nesting is bad" -- sometimes it's needed to access variables from earlier callbacks.

# Prerequisites

- **Promise chaining** -- understanding correct chaining

# Key Properties

1. "Losing the tail": `return promise` instead of `return promise.then(...)`
2. "Nesting": `.then()` inside another `.then()` callback
3. "Creating instead of chaining": `new Promise()` wrapping an existing chain
4. Valid nesting: when inner callbacks need access to outer variables (like `connection`)

# Construction / Recognition

Losing the tail (wrong):
```js
function foo() {
  const promise = asyncFunc();
  promise.then(result => { /* ... */ });
  return promise; // should return the .then() result
}
```

Correct:
```js
function foo() {
  return asyncFunc().then(result => { /* ... */ });
}
```

(Ch. 43, Section 43.7.1, lines 2150-2176)

# Context & Application

These anti-patterns cause subtle bugs: lost error handling, unintended parallel execution, or unnecessary complexity.

# Examples

See construction example above. (Ch. 43, Section 43.7, lines 2142-2306)

# Relationships

## Builds Upon
- **Promise chaining** -- mistakes in chaining patterns

## Related
- **Promise error handling** -- mistakes often cause error handling gaps

# Common Errors

- **Error**: All four mistakes described above
  **Correction**: Chain flat, return chain results, avoid wrapping existing chains

# Common Confusions

- **Confusion**: All nesting in Promise chains is bad
  **Clarification**: Nesting is appropriate when inner callbacks need access to outer variables

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.7, lines 2142-2306.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section devoted to mistakes
- Cross-reference status: verified
