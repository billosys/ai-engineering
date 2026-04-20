---
# === CORE IDENTIFICATION ===
concept: await Keyword
slug: await-keyword

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
extraction_confidence: high

# === VARIANTS ===
aliases:
  - await expression

# === TYPED RELATIONSHIPS ===
prerequisites:
  - async-function
  - promise
extends: []
related:
  - promise
  - then-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does async/await relate to promises?"
  - "How do I use async/await for asynchronous operations?"
---

# Quick Definition
The `await` keyword, used inside an `async` function, pauses the function's execution until a promise resolves, then returns the resolved value. If the promise rejects, it throws an exception.

# Core Definition
"Inside an `async` function, the word `await` can be put in front of an expression to wait for a promise to resolve and only then continue the execution of the function. If the promise rejects, an exception is raised at the point of the `await`." (Eloquent JavaScript, Ch. 11, lines 661-664)

# Prerequisites
- **Async function**: `await` can only be used inside `async` functions
- **Promise**: `await` operates on promises

# Key Properties
1. Pauses (freezes) the async function at the `await` point
2. Returns the resolved value of the promise
3. If the promise rejects, throws the rejection reason as an exception
4. Can be used with try/catch for error handling
5. Creates a gap in execution where other code can run

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
        }
      }
    }
  }
}
```
(lines 627-644)

# Context & Application
`await` makes asynchronous code look and behave like synchronous code, enabling the use of loops, try/catch, and other control structures with asynchronous operations.

# Examples
From the source, the async version is compared with the promise-based version: "This version more clearly shows the double loop structure of the function (the inner loop tries digit 0 to 9 and the outer loop adds digits to the passcode)." (lines 648-650)

A concurrent example with `Promise.all`:
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

# Relationships
## Builds Upon
- Async functions and promises
## Enables
- Synchronous-looking async control flow
- Try/catch error handling for async operations
## Related
- `then` method (the non-await way to handle promise values)
## Contrasts With
- `then` chaining (which requires nesting or chaining for sequential steps)

# Common Errors
- **Error**: Mutating shared state across `await` gaps
  **Correction**: "Mistakes like this are easy to make, especially when using `await`, and you should be aware of where the gaps in your code occur." (lines 1104-1105)

# Common Confusions
- **Confusion**: `await` blocks the entire program
  **Clarification**: `await` only pauses the current async function; other code (event handlers, other async functions) can run during the pause

# Source Reference
Chapter 11: Asynchronous Programming, Section "Async functions", lines 661-678 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clear definition with practical examples
- Cross-reference status: verified
