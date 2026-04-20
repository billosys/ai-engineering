---
# === CORE IDENTIFICATION ===
concept: Callback
slug: callback

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
section: "Callbacks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - callback function
  - continuation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - closure
extends: []
related:
  - asynchronous-programming
  - promise
  - callback-hell
contrasts_with:
  - promise

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do promises relate to callbacks?"
  - "What must I know before using promises and async/await?"
---

# Quick Definition
A callback is a function passed as an argument to an asynchronous function, which is called when the asynchronous action completes.

# Core Definition
"One approach to asynchronous programming is to make functions that need to wait for something take an extra argument, a *callback function*. The asynchronous function starts a process, sets things up so that the callback function is called when the process finishes, and then returns." (Eloquent JavaScript, Ch. 11, lines 128-132)

# Prerequisites
- **Functions as values**: Callbacks require passing functions as arguments to other functions
- **Closures**: Callbacks often need to reference variables from their enclosing scope

# Key Properties
1. The callback is invoked after the asynchronous operation completes
2. The asynchronous function returns immediately, before the callback runs
3. Asynchronicity is contagious -- any function using callbacks must itself accept a callback
4. Error handling in callbacks typically uses a convention where the first argument is an error

# Construction / Recognition
```javascript
setTimeout(() => console.log("Tick"), 500);

readTextFile("shopping_list.txt", content => {
  console.log(`Shopping List:\n${content}`);
});
```

# Context & Application
Callbacks are the most basic mechanism for asynchronous programming in JavaScript. They are used with `setTimeout`, event handlers, and Node.js-style APIs.

# Examples
From the source, nesting callbacks to compare two files:
```javascript
function compareFiles(fileA, fileB, callback) {
  readTextFile(fileA, contentA => {
    readTextFile(fileB, contentB => {
      callback(contentA == contentB);
    });
  });
}
```
(lines 178-185)

Error-first callback convention:
```javascript
someAsyncFunction((error, value) => {
  if (error) handleError(error);
  else processValue(value);
});
```
(lines 347-350)

# Relationships
## Builds Upon
- Functions as first-class values
## Enables
- Basic asynchronous programming patterns
## Related
- Callback hell (the problem of deeply nested callbacks)
## Contrasts With
- Promises, which provide a cleaner alternative to callbacks

# Common Errors
- **Error**: Forgetting to handle errors in callback-based code
  **Correction**: "Such callback functions must always check whether they received an exception and make sure that any problems they cause... are caught and given to the right function." (lines 354-357)

# Common Confusions
- **Confusion**: Callbacks are always asynchronous
  **Clarification**: A callback is just a function passed to another function; it may be called synchronously (like `Array.map`) or asynchronously (like `setTimeout`)

# Source Reference
Chapter 11: Asynchronous Programming, Section "Callbacks", lines 125-199 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Central concept with clear definition and examples
- Cross-reference status: verified against chapter content
