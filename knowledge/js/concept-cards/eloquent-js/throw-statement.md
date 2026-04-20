---
# === CORE IDENTIFICATION ===
concept: Throw Statement
slug: throw-statement

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
  - throw keyword
  - raising an exception

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception
extends: []
related:
  - try-catch
  - error-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I throw an exception in JavaScript?"
---

# Quick Definition
The `throw` keyword raises an exception, causing execution to immediately jump out of the current function and its callers until a `try/catch` block is found.

# Core Definition
Haverbeke states: "The `throw` keyword is used to raise an exception." An exception can be any value, though `Error` objects are conventional because they capture stack trace information. (Ch 8, "Exceptions")

# Prerequisites
- **Exceptions**: Understanding the exception mechanism

# Key Properties
1. `throw` followed by any value raises that value as an exception
2. Immediately exits the current function and unwinds the call stack
3. Convention is to throw `Error` objects or subclasses
4. Can be used in assertions to signal programmer mistakes

# Construction / Recognition
```javascript
throw new Error("Invalid direction: " + result);
```

# Context & Application
`throw` is used when a function encounters a condition it cannot handle -- invalid input, violated preconditions, or unexpected states.

# Examples
```javascript
function promptDirection(question) {
  let result = prompt(question);
  if (result.toLowerCase() == "left") return "L";
  if (result.toLowerCase() == "right") return "R";
  throw new Error("Invalid direction: " + result);
}
```
(Ch 8, "Exceptions", lines 483-488)

# Relationships
## Builds Upon
- exception
## Enables
- try-catch, selective-catching
## Related
- error-class
## Contrasts With
- N/A

# Common Errors
- **Error**: Throwing plain strings instead of Error objects
  **Correction**: Use `new Error("message")` to get stack trace information with the exception

# Common Confusions
- **Confusion**: `throw` returns from the function normally
  **Clarification**: `throw` immediately exits the function AND all calling functions until a `catch` is found

# Source Reference
Chapter 8: Bugs and Errors, Section "Exceptions", lines 505-507.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
