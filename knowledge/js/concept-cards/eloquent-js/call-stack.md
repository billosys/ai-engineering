---
# === CORE IDENTIFICATION ===
concept: Call Stack
slug: call-stack

# === CLASSIFICATION ===
category: functions
subcategory: execution-model
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "The call stack"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - execution stack
  - function call stack

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - return-value
extends: []
related:
  - stack-overflow
  - recursion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function?"
---

# Quick Definition

The call stack is the data structure where the computer stores the context from which each function was called, so it can return to the correct place when the function finishes.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 386-390 of 03-functions.md): "The place where the computer stores this context is the *call stack*. Every time a function is called, the current context is stored on top of this stack. When a function returns, it removes the top context from the stack and uses that context to continue execution."

# Prerequisites

- **function-definition**: The call stack tracks function calls.
- **return-value**: Functions return to the call site, which the stack tracks.

# Key Properties

1. Stores the context (return address) for each active function call.
2. Operates as a last-in-first-out (LIFO) structure.
3. Grows with each function call, shrinks with each return.
4. Requires memory -- can overflow if it grows too large.

# Construction / Recognition

## To Construct/Create:
The call stack is managed automatically by the JavaScript engine. You do not create it directly.

## To Identify/Recognize:
The schematic flow of nested function calls:
```
not in function
  in greet
    in console.log
  in greet
not in function
```

# Context & Application

Understanding the call stack helps with debugging (stack traces), understanding recursion, and diagnosing stack overflow errors.

# Examples

**Example 1** (Ch 3, lines 347-376 of 03-functions.md):
```javascript
function greet(who) {
  console.log("Hello " + who);
}
greet("Harry");
console.log("Bye");
```
Flow: call to `greet` -> calls `console.log` -> returns to `greet` -> returns to main -> calls `console.log` -> returns.

# Relationships

## Builds Upon
- **function-definition** -- The call stack tracks function invocations.

## Enables
- **stack-overflow** -- When the stack grows too large.
- **recursion** -- Each recursive call adds a frame to the stack.

## Related
- Understanding error messages and stack traces.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Ignoring stack traces when debugging errors.
  **Correction**: Stack traces show the call stack at the point of error, revealing the chain of function calls that led to the problem.

# Common Confusions

- **Confusion**: The call stack and the heap are the same thing.
  **Clarification**: The call stack tracks function call contexts; the heap stores objects and other dynamically allocated data (not discussed in this chapter).

# Source Reference

Chapter 3: Functions, Section "The call stack", lines 340-410 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 386-390)
- Confidence rationale: Explicit definition with italicized term "call stack"
- Cross-reference status: verified within chapter
