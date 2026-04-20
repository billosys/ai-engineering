---
concept: Promise.race()
slug: promise-race
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
extraction_confidence: high
aliases: []
prerequisites:
  - promise-object
extends: []
related:
  - promise-all
  - promise-any
contrasts_with:
  - promise-all
answers_questions:
  - "How does `Promise.all()` relate to `Promise.race()`?"
---

# Quick Definition

A static method that returns a Promise which settles (fulfills or rejects) as soon as the first of the input Promises settles, taking on that Promise's value or rejection reason.

# Core Definition

"Promise.race() returns a Promise that is fulfilled or rejected when the first of the Promises in the input array is fulfilled or rejected" (p. 378). If there are non-Promise values in the input array, it returns the first of those.

# Prerequisites

- **promise-object** — race() operates on Promises

# Key Properties

1. Returns as soon as the first input Promise settles
2. Takes the value/reason of the first settled Promise
3. Can fulfill OR reject (depends on which Promise settles first)
4. Non-Promise values in the array count as already fulfilled

# Construction / Recognition

```js
Promise.race([fetch(url1), fetch(url2)])
    .then(response => { /* fastest response */ });
```

# Context & Application

Used for timeouts (race a Promise against a timer Promise), selecting the fastest result from redundant sources, or implementing deadline-based patterns.

# Examples

From the source text (p. 378): Promise.race() is described as returning whichever Promise settles first, whether fulfilled or rejected.

# Relationships

## Builds Upon
- **Promise Object** — race() operates on Promises

## Related
- **Promise.all()** — all() waits for all; race() waits for first
- **Promise.any()** — any() waits for first *fulfillment* only

## Contrasts With
- **Promise.all()** — all() requires all to succeed; race() takes the first settlement of any kind

# Common Errors

- **Error**: Using race() and not handling the case where the first settler is a rejection.
  **Correction**: race() can reject if the first Promise to settle is a rejection. Always add a `.catch()`.

# Common Confusions

- **Confusion**: Thinking race() cancels the losing Promises.
  **Clarification**: race() cannot cancel Promises. The losing Promises continue to run; their results are simply ignored.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.5, page 378.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
