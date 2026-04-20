---
# === CORE IDENTIFICATION ===
concept: Asynchronous Bugs
slug: asynchronous-bugs

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
section: "Asynchronous bugs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - async race conditions
  - async gaps

# === TYPED RELATIONSHIPS ===
prerequisites:
  - async-function
  - await-keyword
  - promise-all
extends: []
related:
  - event-loop
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before using promises and async/await?"
---

# Quick Definition
Asynchronous bugs arise when code incorrectly assumes that shared state remains unchanged across `await` gaps, where other code can run and modify that state.

# Core Definition
"When your program runs synchronously, in a single go, there are no state changes happening except those that the program itself makes. For asynchronous programs this is different---they may have *gaps* in their execution during which other code can run." (Eloquent JavaScript, Ch. 11, lines 1030-1034)

# Prerequisites
- **Async functions and await**: Understanding where execution pauses
- **Promise.all**: Understanding concurrent promise execution

# Key Properties
1. Each `await` creates a gap where other code can run
2. Shared mutable state can be modified by concurrent async operations during gaps
3. The `+=` operator reads a value before `await` and writes after, potentially losing updates
4. Computing new values is less error-prone than mutating shared state in async code

# Construction / Recognition
The buggy pattern:
```javascript
async function fileSizes(files) {
  let list = "";
  await Promise.all(files.map(async fileName => {
    list += fileName + ": " +
      (await textFile(fileName)).length + "\n";
  }));
  return list;
}
```
(lines 1043-1051)

# Context & Application
This pattern is a common source of subtle bugs in async JavaScript code, particularly when using `Promise.all` with shared mutable state.

# Examples
From the source: "The problem lies in the `+=` operator, which takes the *current* value of `list` at the time the statement starts executing and then, when the `await` finishes, sets the `list` binding to be that value plus the added string." (lines 1073-1076)

The fix is to return values instead of mutating:
```javascript
async function fileSizes(files) {
  let lines = files.map(async fileName => {
    return fileName + ": " +
      (await textFile(fileName)).length;
  });
  return (await Promise.all(lines)).join("\n");
}
```
(lines 1094-1101)

"As usual, computing new values is less error prone than changing existing values." (lines 1090-1091)

# Relationships
## Builds Upon
- Async/await execution model and Promise.all
## Enables
- Awareness of concurrent state modification pitfalls
## Related
- Event loop (the mechanism that allows gaps)
## Contrasts With
- Synchronous code where state changes are sequential

# Common Errors
- **Error**: Using `+=` or other read-modify-write operations on shared state across `await`
  **Correction**: Return new values from async operations and combine results after all complete

# Common Confusions
- **Confusion**: Async code in JavaScript is truly parallel
  **Clarification**: It is concurrent but single-threaded; however, interleaving of async operations still causes state-related bugs

# Source Reference
Chapter 11: Asynchronous Programming, Section "Asynchronous bugs", lines 1027-1108 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Dedicated section with detailed example
- Cross-reference status: verified
