---
concept: Promise.any()
slug: promise-any
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 378
section: "13.2.5 Promises in Parallel"
extraction_confidence: medium
aliases: []
prerequisites:
  - promise-object
extends: []
related:
  - promise-race
  - promise-all
contrasts_with:
  - promise-race
answers_questions:
  - "How does `Promise.all()` relate to `Promise.race()`?"
---

# Quick Definition

A static method that returns a Promise which fulfills as soon as any one of the input Promises fulfills, ignoring rejections unless all input Promises reject (in which case it rejects with an AggregateError).

# Core Definition

Promise.any() is the complement of Promise.all(): while all() rejects on the first rejection, any() fulfills on the first fulfillment. It only rejects if all input Promises reject. This is distinct from Promise.race(), which settles on the first settlement regardless of whether it's a fulfillment or rejection.

# Prerequisites

- **promise-object** — any() operates on Promises

# Key Properties

1. Fulfills with the first fulfillment value
2. Ignores rejections as long as at least one Promise fulfills
3. Rejects with AggregateError only if all input Promises reject
4. ES2021 feature

# Construction / Recognition

```js
Promise.any([fetch(primary), fetch(fallback)])
    .then(response => handle(response))
    .catch(e => console.error("All failed:", e.errors));
```

# Context & Application

Useful for redundancy patterns where you try multiple sources and use whichever succeeds first (e.g., multiple CDN endpoints, multiple API mirrors).

# Examples

The source text briefly mentions Promise.any() in the context of Promise.all(), Promise.allSettled(), and Promise.race() as the parallel Promise combinators (p. 378).

# Relationships

## Builds Upon
- **Promise Object** — any() operates on Promises

## Related
- **Promise.race()** — race() settles on first settlement; any() settles on first fulfillment
- **Promise.all()** — all() requires all to fulfill; any() requires just one

## Contrasts With
- **Promise.race()** — race() can reject if the first settler rejects; any() ignores rejections

# Common Errors

- **Error**: Using Promise.race() when you want to ignore rejections and get the first success.
  **Correction**: Use Promise.any() — it ignores rejections and fulfills with the first fulfillment.

# Common Confusions

- **Confusion**: Thinking Promise.any() is the same as Promise.race().
  **Clarification**: race() settles on whichever Promise settles first (fulfilled or rejected). any() only fulfills on the first fulfillment, ignoring rejections.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.5, page 378.

# Verification Notes

- Definition source: Inferred from brief mention in source text
- Confidence rationale: Medium — only briefly mentioned, full details from language spec
- Uncertainties: Source coverage is brief
- Cross-reference status: Verified against ES2021 spec
