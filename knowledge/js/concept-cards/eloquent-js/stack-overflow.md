---
# === CORE IDENTIFICATION ===
concept: Stack Overflow
slug: stack-overflow

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
  - blowing the stack
  - out of stack space

# === TYPED RELATIONSHIPS ===
prerequisites:
  - call-stack
  - recursion
extends: []
related:
  - recursion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

A stack overflow occurs when the call stack grows too large, typically due to infinite or excessively deep recursion, causing the computer to fail with a message like "out of stack space" or "too much recursion."

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 393-399 of 03-functions.md): "Storing this stack requires space in the computer's memory. When the stack grows too big, the computer will fail with a message like 'out of stack space' or 'too much recursion'. The following code illustrates this by asking the computer a really hard question that causes an infinite back-and-forth between two functions."

# Prerequisites

- **call-stack**: Stack overflow is the failure mode of the call stack.
- **recursion**: The most common cause of stack overflow.

# Key Properties

1. Occurs when the call stack exceeds its memory limit.
2. Most commonly caused by infinite or very deep recursion.
3. Results in a runtime error (not a compile-time error).
4. The error message varies by JavaScript engine ("out of stack space", "too much recursion", "Maximum call stack size exceeded").

# Construction / Recognition

## To Construct/Create (to demonstrate the error):
```javascript
function chicken() { return egg(); }
function egg() { return chicken(); }
console.log(chicken() + " came first.");
// → Stack overflow error
```

## To Identify/Recognize:
- Error messages mentioning stack space, recursion limits, or call stack size.

# Context & Application

Stack overflow errors are one of the most common pitfalls when writing recursive functions. Ensuring that recursive functions have proper base cases and that recursion depth is bounded prevents this error.

# Examples

**Example 1** (Ch 3, lines 401-410 of 03-functions.md):
```javascript
function chicken() {
  return egg();
}
function egg() {
  return chicken();
}
console.log(chicken() + " came first.");
// → ??
```
This causes infinite mutual recursion, overflowing the stack.

# Relationships

## Builds Upon
- **call-stack** -- Stack overflow is the call stack's failure mode.

## Enables
- Understanding why recursive functions need base cases.

## Related
- **recursion** -- The primary cause of stack overflow.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Writing a recursive function without a base case.
  **Correction**: Every recursive function must have a condition that stops the recursion.

# Common Confusions

- **Confusion**: Stack overflow is a bug in the language.
  **Clarification**: It is a consequence of finite memory. The programmer must ensure recursion terminates.

# Source Reference

Chapter 3: Functions, Section "The call stack", lines 393-410 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 393-399)
- Confidence rationale: Explicit description with example
- Cross-reference status: verified within chapter
