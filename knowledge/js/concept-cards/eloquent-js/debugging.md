---
# === CORE IDENTIFICATION ===
concept: Debugging
slug: debugging

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
section: "Debugging"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bug
  - function
extends: []
related:
  - stack-trace
  - testing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is debugging?"
  - "How do I find the source of a bug?"
---

# Quick Definition
Debugging is the process of finding, diagnosing, and fixing mistakes in programs, using techniques like strategic `console.log` calls, breakpoints, and systematic reasoning.

# Core Definition
Haverbeke defines: "The process of finding mistakes---bugs---in programs is called *debugging*." The approach is: "Analyze what is happening and come up with a theory of why it might be happening. Then make additional observations to test this theory---or, if you don't yet have a theory, make additional observations to help you come up with one." (Ch 8, "Language" and "Debugging")

# Prerequisites
- **Bugs**: You must understand what bugs are to debug them
- **Functions**: Debugging involves tracing function behavior

# Key Properties
1. Think first, don't make random changes
2. Use `console.log` strategically to observe intermediate values
3. Use browser debugger with breakpoints
4. The `debugger` statement pauses execution when developer tools are open
5. Sometimes the error location differs from where the bug originates

# Construction / Recognition
Debugging is recognized by the need to understand why a program produces unexpected output or errors.

# Context & Application
Debugging is an essential skill. The chapter quotes Kernighan: "Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it." (Ch 8 epigraph)

# Examples
The `numberToString` bug demonstrates the debugging process:
```javascript
function numberToString(n, base = 10) {
  let result = "", sign = "";
  if (n < 0) { sign = "-"; n = -n; }
  do {
    result = String(n % base) + result;
    n /= base;  // Bug: should be Math.floor(n / base)
  } while (n > 0);
  return sign + result;
}
console.log(numberToString(13, 10));
// -> 1.5e-3231.3e-3221.3e-321...
```
Adding `console.log(n)` reveals `n` takes values `13, 1.3, 0.13...` -- the fix is `n = Math.floor(n / base)`. (Ch 8, "Debugging", lines 310-360)

# Relationships
## Builds Upon
- bug, function
## Enables
- Bug fixes, improved code understanding
## Related
- stack-trace, testing
## Contrasts With
- N/A

# Common Errors
- **Error**: Making random changes hoping to fix a bug
  **Correction**: "Resist the urge to start making random changes to the code to see whether that makes it better. Instead, *think*." (Ch 8)

# Common Confusions
- **Confusion**: The line where an error occurs is always where the bug is
  **Clarification**: "Sometimes the line that triggered the problem is simply the first place where a flaky value produced elsewhere gets used in an invalid way." (Ch 8)

# Source Reference
Chapter 8: Bugs and Errors, Section "Debugging", lines 283-377.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with detailed debugging walkthrough
- Cross-reference status: verified
