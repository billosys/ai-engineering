---
# === CORE IDENTIFICATION ===
concept: Promise.all
slug: promise-all

# === CLASSIFICATION ===
category: asynchronous-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Asynchronous Programming"
chapter_number: 11
pdf_page: null
section: "A Corvid Art Project"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Promise.all()

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - array
extends:
  - promise
related:
  - promise-any
  - async-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use async/await for asynchronous operations?"
---

# Quick Definition
`Promise.all` takes an array of promises and returns a single promise that resolves to an array of results when all input promises succeed, or rejects if any one of them fails.

# Core Definition
"`Promise` has a static method `all` that can be used to convert an array of promises into a single promise that resolves to an array of results. This provides a convenient way to have some asynchronous actions happen alongside each other, wait for them all to finish, and then do something with their results (or at least wait for them to make sure they don't fail)." (Eloquent JavaScript, Ch. 11, lines 876-881)

# Prerequisites
- **Promise**: Understanding individual promises
- **Array**: Working with arrays of promises

# Key Properties
1. Takes an array of promises as input
2. Returns a single promise that resolves to an array of all results
3. If any promise rejects, the whole `Promise.all` rejects with that reason
4. All promises run concurrently (not sequentially)

# Construction / Recognition
```javascript
function displayFrame(frame) {
  return Promise.all(frame.map((data, i) => {
    return request(screenAddresses[i], {
      command: "display",
      data
    });
  }));
}
```
(lines 884-891)

# Context & Application
Used when you have multiple independent async operations that can run in parallel and you need all of their results before proceeding.

# Examples
From the source, displaying frames on multiple screens simultaneously:
"This maps over the images in `frame` (which is an array of display data arrays) to create an array of request promises. It then returns a promise that combines all of those." (lines 895-897)

From the exercises: "Given an array of promises, `Promise.all` returns a promise that waits for all of the promises in the array to finish. It then succeeds, yielding an array of result values. If a promise in the array fails, the promise returned by `all` fails too, passing on the failure reason from the failing promise." (lines 1199-1202)

# Relationships
## Builds Upon
- Individual promises
## Enables
- Concurrent execution of independent async tasks
## Related
- `Promise.any` (resolves when any single promise succeeds)
## Contrasts With
- Sequential `await` in a loop (which runs promises one at a time)

# Common Errors
- **Error**: Mutating shared state in concurrent `Promise.all` callbacks
  **Correction**: Return new values from each promise handler rather than mutating shared variables. The source demonstrates this bug: using `+=` on a shared string in mapped async functions loses data because each starts from the same initial value. (lines 1043-1101)

# Common Confusions
- **Confusion**: `Promise.all` runs promises sequentially
  **Clarification**: All promises are started immediately and run concurrently

# Source Reference
Chapter 11: Asynchronous Programming, Sections "A Corvid Art Project" and "Building Promise.all", lines 876-1212 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples and exercise
- Cross-reference status: verified
