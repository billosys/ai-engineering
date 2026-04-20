---
# === CORE IDENTIFICATION ===
concept: Error Class
slug: error-class

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
  - Error constructor
  - Error object

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-declaration
  - exception
extends: []
related:
  - throw-statement
  - stack-trace
  - selective-catching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Error class in JavaScript?"
  - "How do I create custom error types?"
---

# Quick Definition
The `Error` constructor creates exception objects with a `message` property and a `stack` property containing the call stack trace at the time of creation.

# Core Definition
Haverbeke explains: "we used the `Error` constructor to create our exception value. This is a standard JavaScript constructor that creates an object with a `message` property. Instances of `Error` also gather information about the call stack that existed when the exception was created, a so-called *stack trace*. This information is stored in the `stack` property and can be helpful when trying to debug a problem." (Ch 8, "Exceptions")

# Prerequisites
- **Class declarations**: Error can be extended to create custom error types
- **Exceptions**: Error objects are the standard exception value

# Key Properties
1. Created with `new Error("message")`
2. Has a `message` property with the error description
3. Has a `stack` property with the call stack trace
4. Can be subclassed with `extends Error` for custom error types
5. Custom subclasses enable selective catching with `instanceof`

# Construction / Recognition
```javascript
// Standard error
throw new Error("Something went wrong");

// Custom error class
class InputError extends Error {}
throw new InputError("Invalid direction: " + result);
```

# Context & Application
Error objects provide debugging information through stack traces. Custom error classes enable selective catching of specific error types.

# Examples
```javascript
class InputError extends Error {}

function promptDirection(question) {
  let result = prompt(question);
  if (result.toLowerCase() == "left") return "L";
  if (result.toLowerCase() == "right") return "R";
  throw new InputError("Invalid direction: " + result);
}
```
The `InputError` class "doesn't define anything at all---the class is empty. `InputError` objects behave like `Error` objects, except that they have a different class by which we can recognize them." (Ch 8, "Selective catching", lines 741-758)

# Relationships
## Builds Upon
- class-declaration, exception
## Enables
- selective-catching, stack-trace
## Related
- throw-statement
## Contrasts With
- N/A

# Common Errors
- **Error**: Throwing plain strings or numbers instead of Error objects
  **Correction**: Always throw Error instances (or subclasses) to preserve stack trace information

# Common Confusions
- **Confusion**: Custom error classes need to define their own constructor
  **Clarification**: Empty subclasses work fine; they inherit the Error constructor which accepts a message string

# Source Reference
Chapter 8: Bugs and Errors, Section "Exceptions", lines 515-524, and "Selective catching", lines 741-758.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with custom subclass example
- Cross-reference status: verified
