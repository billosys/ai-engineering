---
# === CORE IDENTIFICATION ===
concept: Async Function
slug: async-function

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
  - async/await
  - async keyword

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - function
extends:
  - promise
related:
  - await-keyword
  - generator
  - promise-chaining
contrasts_with:
  - callback

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does async/await relate to promises?"
  - "How do I use async/await for asynchronous operations?"
  - "What must I know before using promises and async/await?"
---

# Quick Definition
An `async` function is a function marked with the `async` keyword that implicitly returns a promise and can use `await` to pause execution until a promise resolves.

# Core Definition
"An `async` function is marked by the word `async` before the `function` keyword. Methods can also be made `async` by writing `async` before their name. When such a function or method is called, it returns a promise. As soon as the function returns something, that promise is resolved. If the body throws an exception, the promise is rejected." (Eloquent JavaScript, Ch. 11, lines 653-658)

# Prerequisites
- **Promise**: Async functions are built on top of promises
- **Functions**: Must understand function declaration and invocation

# Key Properties
1. Always returns a promise, even if the return value is not a promise
2. Can use `await` inside its body to pause on promises
3. Can be frozen at any `await` point and resumed later
4. Throwing inside an async function rejects the returned promise
5. Arrow functions can be async: `async () => {}`

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
Async functions are the preferred way to write asynchronous code in modern JavaScript, providing a synchronous-looking syntax for asynchronous operations.

# Examples
From the source: "JavaScript allows you to write pseudosynchronous code to describe asynchronous computation. An `async` function implicitly returns a promise and can, in its body, `await` other promises in a way that *looks* synchronous." (lines 617-620)

"Such a function no longer runs from start to completion in one go like a regular JavaScript function. Instead, it can be *frozen* at any point that has an `await` and can be resumed at a later time." (lines 667-670)

Async arrow functions: "The `async fileName =>` part shows how arrow functions can also be made `async` by putting the word `async` in front of them." (lines 1054-1056)

# Relationships
## Builds Upon
- Promises (async functions are syntactic sugar over promises)
## Enables
- Writing asynchronous code with synchronous-looking control flow
## Related
- `await` keyword (used inside async functions)
- Generators (share the pause/resume mechanism)
## Contrasts With
- Raw callback-based code
- Promise chains with `then`

# Common Errors
- **Error**: Using `await` outside of an `async` function
  **Correction**: The `await` keyword can only be used inside `async` functions (or at the top level of modules)

# Common Confusions
- **Confusion**: Async functions eliminate the need to understand promises
  **Clarification**: "You do still need an understanding of promises, since in many cases you'll still interact with them directly." (lines 674-676)

# Source Reference
Chapter 11: Asynchronous Programming, Section "Async functions", lines 602-678 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Thoroughly explained with before/after examples
- Cross-reference status: verified against chapter summary
