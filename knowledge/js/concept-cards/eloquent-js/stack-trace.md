---
# === CORE IDENTIFICATION ===
concept: Stack Trace
slug: stack-trace

# === CLASSIFICATION ===
category: error-handling
subcategory: diagnosis
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
  - call stack trace
  - error stack

# === TYPED RELATIONSHIPS ===
prerequisites:
  - error-class
  - function
extends: []
related:
  - debugging
  - exception
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a stack trace?"
  - "How does a stack trace help debugging?"
---

# Quick Definition
A stack trace is information gathered by an Error object about the call stack at the time the exception was created, showing which functions were active and helping identify where problems originated.

# Core Definition
Haverbeke states: "Instances of `Error` also gather information about the call stack that existed when the exception was created, a so-called *stack trace*. This information is stored in the `stack` property and can be helpful when trying to debug a problem: it tells us the function where the problem occurred and which functions made the failing call." (Ch 8, "Exceptions")

# Prerequisites
- **Error class**: Stack traces are captured by Error objects
- **Functions**: The trace shows the chain of active function calls

# Key Properties
1. Stored in the `stack` property of Error objects
2. Shows the chain of function calls active when the error was created
3. Identifies both where the error occurred and who called the failing code
4. Displayed automatically by browser consoles for unhandled exceptions

# Construction / Recognition
Stack traces appear automatically when Error objects are created. They're visible in browser developer tools or by accessing `error.stack`.

# Context & Application
Stack traces are essential for debugging, especially when errors originate in deep call chains. They show the path from the error to the entry point.

# Examples
When an Error is created, it captures the current call stack:
```javascript
throw new Error("Something went wrong");
// The error.stack property contains something like:
// Error: Something went wrong
//   at promptDirection (file.js:3)
//   at look (file.js:8)
//   at file.js:13
```
(Ch 8, "Exceptions", lines 515-523)

# Relationships
## Builds Upon
- error-class, function
## Enables
- debugging
## Related
- exception
## Contrasts With
- N/A

# Common Errors
- **Error**: Throwing non-Error values (strings, numbers) that lack stack traces
  **Correction**: Always throw Error objects to get stack trace information

# Common Confusions
- **Confusion**: The stack trace shows where the error was caught
  **Clarification**: The stack trace shows where the error was CREATED (thrown), not where it was caught

# Source Reference
Chapter 8: Bugs and Errors, Section "Exceptions", lines 515-523.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
