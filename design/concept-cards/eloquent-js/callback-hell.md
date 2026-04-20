---
# === CORE IDENTIFICATION ===
concept: Callback Hell
slug: callback-hell

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
  - pyramid of doom
  - nested callbacks

# === TYPED RELATIONSHIPS ===
prerequisites:
  - callback
extends:
  - callback
related:
  - promise
  - async-function
contrasts_with:
  - promise-chaining

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do promises relate to callbacks?"
---

# Quick Definition
Callback hell is the pattern of deeply nested callback functions that arises when multiple asynchronous actions must be performed in sequence, making code hard to read and maintain.

# Core Definition
"This style of programming is workable, but the indentation level increases with each asynchronous action because you end up in another function. Doing more complicated things, such as wrapping asynchronous actions in a loop, can get awkward." (Eloquent JavaScript, Ch. 11, lines 188-191)

# Prerequisites
- **Callbacks**: Understanding the callback pattern for async code

# Key Properties
1. Each sequential async step adds another level of nesting
2. Error handling becomes extremely difficult across nested callbacks
3. Code becomes harder to read and reason about as nesting grows
4. Loops and conditional logic are particularly awkward to express

# Construction / Recognition
Recognized by deeply indented code with callbacks nested inside callbacks:
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

# Context & Application
This problem motivated the creation of promises and async/await as cleaner alternatives for sequential asynchronous operations.

# Examples
From the source: the `compareFiles` function above shows just two levels of nesting. The text notes that "asynchronicity is *contagious*. Any function that calls a function that works asynchronously must itself be asynchronous, using a callback or similar mechanism to deliver its result." (lines 194-196)

# Relationships
## Builds Upon
- The callback pattern for asynchronous code
## Enables
- Motivation for promises and async/await
## Related
- Promise chaining as a flatter alternative
## Contrasts With
- Promise chaining and async/await which avoid deep nesting

# Common Errors
- **Error**: Continuing to nest callbacks when promises or async/await would be clearer
  **Correction**: Refactor nested callbacks into promise chains or async functions

# Common Confusions
- **Confusion**: Callback hell is just about indentation
  **Clarification**: The deeper problem is that error handling, control flow, and reasoning about code become much harder with nested callbacks

# Source Reference
Chapter 11: Asynchronous Programming, Section "Callbacks", lines 186-199 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: synthesized from source description
- Confidence rationale: Clearly described pattern, though the term "callback hell" is implied rather than stated explicitly
- Cross-reference status: verified
