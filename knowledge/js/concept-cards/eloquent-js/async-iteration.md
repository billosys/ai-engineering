---
# === CORE IDENTIFICATION ===
concept: Async Iteration
slug: async-iteration

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
section: "Async functions"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - async loops
  - await in loops

# === TYPED RELATIONSHIPS ===
prerequisites:
  - async-function
  - await-keyword
  - promise
extends:
  - async-function
related:
  - generator
  - promise-all
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use async/await for asynchronous operations?"
---

# Quick Definition
Async iteration is the pattern of using `await` inside loops within `async` functions to process asynchronous operations sequentially, one at a time.

# Core Definition
The source demonstrates that `async` functions allow using `await` inside standard loop constructs, enabling sequential asynchronous iteration. "Because you cannot wait for a promise inside a `for` loop" (without async/await), "Carla uses a recursive function to drive this process" -- but with async/await, regular loops work naturally. (Eloquent JavaScript, Ch. 11, lines 559-560)

# Prerequisites
- **Async function**: Must be inside an async function to use await
- **Await keyword**: Understanding how await pauses execution
- **Promise**: Understanding what await operates on

# Key Properties
1. `await` inside a `for` loop processes items one at a time (sequentially)
2. Sequential processing means the next iteration waits for the current to finish
3. For concurrent processing, use `Promise.all` with `map` instead of a sequential loop
4. Standard loop constructs (for, while, for...of) all work with `await`

# Construction / Recognition
```javascript
async function crackPasscode(networkID) {
  for (let code = "";;) {
    for (let digit = 0;; digit++) {
      let newCode = code + digit;
      try {
        await withTimeout(joinWifi(networkID, newCode), 50);
        return newCode;
      } catch (failure) {
        if (failure == "Timed out") {
          code = newCode;
          break;
        } else if (digit == 9) {
          throw failure;
        }
      }
    }
  }
}
```
(lines 627-644)

# Context & Application
Async iteration is appropriate when each step depends on the result of the previous step. For independent operations, `Promise.all` provides better performance through concurrency.

# Examples
From the source, the video player uses an async loop:
```javascript
async play() {
  this.stopped = false;
  for (let i = 0; !this.stopped; i++) {
    let nextFrame = wait(this.frameTime);
    await displayFrame(this.frames[i % this.frames.length]);
    await nextFrame;
  }
}
```
(lines 917-924)

The exercises note the performance difference: "In the `async` function, just using `await` in a loop is simpler. If reading a file takes some time, which of these two approaches will take the least time to run?" (referring to sequential await vs Promise.all) (lines 1186-1188)

# Relationships
## Builds Upon
- Async functions and the await keyword
## Enables
- Sequential processing of async operations using familiar loop syntax
## Related
- Generators (also produce sequences of values)
- Promise.all (for concurrent iteration)
## Contrasts With
- Concurrent iteration with Promise.all (which processes all at once)

# Common Errors
- **Error**: Using `await` in a loop when operations are independent, causing unnecessary sequential execution
  **Correction**: Use `Promise.all` with `map` for independent operations that can run concurrently

# Common Confusions
- **Confusion**: `await` in `forEach` or `map` works the same as in `for` loops
  **Clarification**: `forEach` does not await the callback; use `for...of` or `Promise.all` with `map`

# Source Reference
Chapter 11: Asynchronous Programming, Section "Async functions", lines 559-560, 627-644, 917-924 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: synthesized from examples and discussion
- Confidence rationale: Medium -- the concept is demonstrated through examples rather than formally defined
- Cross-reference status: verified through multiple examples
