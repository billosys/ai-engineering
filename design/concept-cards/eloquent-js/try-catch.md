---
# === CORE IDENTIFICATION ===
concept: Try/Catch Statement
slug: try-catch

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
  - try/catch block
  - exception handler

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception
  - function
extends: []
related:
  - throw-statement
  - finally-clause
  - selective-catching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I handle errors with try/catch?"
  - "How do I catch exceptions in JavaScript?"
---

# Quick Definition
A `try/catch` statement wraps code that might throw an exception in a `try` block, with a `catch` block that executes when an exception is thrown, binding the exception value to a variable.

# Core Definition
Haverbeke explains: "The `throw` keyword is used to raise an exception. Catching one is done by wrapping a piece of code in a `try` block, followed by the keyword `catch`. When the code in the `try` block causes an exception to be raised, the `catch` block is evaluated, with the name in parentheses bound to the exception value. After the `catch` block finishes---or if the `try` block finishes without problems---the program proceeds beneath the entire `try/catch` statement." (Ch 8, "Exceptions")

# Prerequisites
- **Exceptions**: Understanding what exceptions are and how they propagate
- **Functions**: Exceptions cross function boundaries

# Key Properties
1. `try` block contains code that might throw
2. `catch` block handles the exception; the variable receives the exception value
3. Execution continues after the entire `try/catch` statement
4. Can be combined with `finally` for cleanup
5. The catch variable name is in parentheses after `catch`

# Construction / Recognition
```javascript
try {
  // code that might throw
} catch (error) {
  // handle the error
}
```

# Context & Application
`try/catch` is the primary mechanism for handling exceptions in JavaScript. It should be used selectively -- catching only expected exception types.

# Examples
```javascript
try {
  console.log("You see", look());
} catch (error) {
  console.log("Something went wrong: " + error);
}
```
(Ch 8, "Exceptions", lines 498-503)

# Relationships
## Builds Upon
- exception, function
## Enables
- selective-catching, finally-clause, error recovery
## Related
- throw-statement, error-class
## Contrasts With
- N/A

# Common Errors
- **Error**: Using a blanket catch that swallows all errors including programmer mistakes
  **Correction**: "don't blanket-catch exceptions unless it is for the purpose of 'routing' them somewhere" (Ch 8)

# Common Confusions
- **Confusion**: `catch` only catches the specific type of error you expect
  **Clarification**: JavaScript's `catch` catches ALL exceptions; you must manually check the type inside the catch block

# Source Reference
Chapter 8: Bugs and Errors, Section "Exceptions", lines 505-513.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly explained with syntax and semantics
- Cross-reference status: verified against chapter summary
