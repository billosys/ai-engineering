---
# === CORE IDENTIFICATION ===
concept: Exception
slug: exception

# === CLASSIFICATION ===
category: error-handling
subcategory: exception-handling
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Bugs and Errors"
chapter_number: 8
pdf_page: null
section: "Exceptions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - exception handling
  - error handling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - scope
extends: []
related:
  - try-catch
  - throw-statement
  - error-class
  - stack-trace
contrasts_with:
  - error-propagation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an exception?"
  - "How do I handle errors with try/catch?"
---

# Quick Definition
Exceptions are a mechanism for code that encounters a problem to raise (throw) an error value that jumps out of the current function and all its callers until caught by a `try/catch` block.

# Core Definition
Haverbeke explains: "Exceptions are a mechanism that makes it possible for code that runs into a problem to *raise* (or *throw*) an exception. An exception can be any value. Raising one somewhat resembles a super-charged return from a function: it jumps out of not just the current function but also its callers, all the way down to the first call that started the current execution. This is called *unwinding the stack*." (Ch 8, "Exceptions")

# Prerequisites
- **Functions**: Exceptions unwind the function call stack
- **Scope**: Understanding function call nesting is essential

# Key Properties
1. An exception can be any value (but usually an Error object)
2. Throwing jumps out of the current function and all callers
3. Caught by `try/catch` blocks set as "obstacles" along the stack
4. Functions between the error source and handler can ignore the error
5. This is the big advantage: error-handling code is only needed where errors occur and are handled

# Construction / Recognition
Exceptions are raised with `throw` and caught with `try/catch`.

# Context & Application
Exceptions are preferred over special return values when errors are rare or when many intermediate functions would need to pass error values through.

# Examples
```javascript
function promptDirection(question) {
  let result = prompt(question);
  if (result.toLowerCase() == "left") return "L";
  if (result.toLowerCase() == "right") return "R";
  throw new Error("Invalid direction: " + result);
}

function look() {
  if (promptDirection("Which way?") == "L") {
    return "a house";
  } else {
    return "two angry bears";
  }
}

try {
  console.log("You see", look());
} catch (error) {
  console.log("Something went wrong: " + error);
}
```
Note: `look` completely ignores the possibility of errors -- "This is the big advantage of exceptions." (Ch 8, "Exceptions", lines 482-530)

# Relationships
## Builds Upon
- function, scope
## Enables
- try-catch, throw-statement, selective-catching, finally-clause
## Related
- error-class, stack-trace
## Contrasts With
- error-propagation (special return values)

# Common Errors
- **Error**: Using exceptions for expected, routine conditions
  **Correction**: Use special return values for common expected failures; reserve exceptions for truly exceptional situations

# Common Confusions
- **Confusion**: Exceptions must always be Error objects
  **Clarification**: "An exception can be any value," though Error objects are preferred because they include stack traces

# Source Reference
Chapter 8: Bugs and Errors, Section "Exceptions", lines 451-534.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with detailed examples
- Cross-reference status: verified against chapter summary
