---
# === CORE IDENTIFICATION ===
concept: Error Propagation
slug: error-propagation

# === CLASSIFICATION ===
category: error-handling
subcategory: error-handling-strategies
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Bugs and Errors"
chapter_number: 8
pdf_page: null
section: "Error propagation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - error signaling
  - error reporting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - value
extends: []
related:
  - exception
  - try-catch
contrasts_with:
  - exception

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do functions communicate errors to their callers?"
  - "What are the alternatives to exceptions for error handling?"
---

# Quick Definition
Error propagation is the problem of communicating failure from the point where an error occurs to the code responsible for handling it, typically via special return values or exceptions.

# Core Definition
Haverbeke introduces the problem: "If your program communicates with the outside world in any way, it is possible to get malformed input, to become overloaded with work, or to have the network fail." Functions can signal errors by returning special values (like `null` or `-1`) or by throwing exceptions. (Ch 8, "Error propagation")

# Prerequisites
- **Functions**: Error propagation occurs between function calls
- **Values**: Special values like `null` can signal errors

# Key Properties
1. Special return values (null, undefined, -1) are one approach
2. Return values don't always work (function might return any value legitimately)
3. Wrapping results in objects `{failed: true}` or `{value: x}` is an alternative
4. Checking special values at every call site is tedious
5. Exceptions provide a cleaner alternative for most error propagation

# Construction / Recognition
```javascript
function promptNumber(question) {
  let result = Number(prompt(question));
  if (Number.isNaN(result)) return null;
  else return result;
}
```

# Context & Application
Error propagation is necessary whenever code interacts with external systems. The choice between special return values and exceptions depends on how common and expected the errors are.

# Examples
Special return value approach:
```javascript
function promptNumber(question) {
  let result = Number(prompt(question));
  if (Number.isNaN(result)) return null;
  else return result;
}
```

Result wrapping when any value could be valid:
```javascript
function lastElement(array) {
  if (array.length == 0) {
    return {failed: true};
  } else {
    return {value: array[array.length - 1]};
  }
}
```
(Ch 8, "Error propagation", lines 397-441)

# Relationships
## Builds Upon
- function, value
## Enables
- exception (as a better alternative)
## Related
- try-catch
## Contrasts With
- exception (exceptions jump through the stack rather than requiring explicit checks)

# Common Errors
- **Error**: Forgetting to check for special error return values
  **Correction**: Every caller must check the return value, which is why exceptions are often preferred

# Common Confusions
- **Confusion**: Always use exceptions instead of return values
  **Clarification**: "In many situations, mostly when errors are common and the caller should be explicitly taking them into account, returning a special value is a good way to indicate an error." (Ch 8)

# Source Reference
Chapter 8: Bugs and Errors, Section "Error propagation", lines 378-450.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly discussed with multiple approaches
- Cross-reference status: verified
