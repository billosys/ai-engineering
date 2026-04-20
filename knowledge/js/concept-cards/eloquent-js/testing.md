---
# === CORE IDENTIFICATION ===
concept: Testing
slug: testing

# === CLASSIFICATION ===
category: error-handling
subcategory: prevention
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Bugs and Errors"
chapter_number: 8
pdf_page: null
section: "Testing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - automated testing
  - test suite

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
extends: []
related:
  - bug
  - assertion
  - debugging
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can automated tests help find bugs?"
  - "What is a test suite?"
---

# Quick Definition
Automated testing is the process of writing programs that verify other programs behave correctly, providing rapid feedback when changes break existing functionality.

# Core Definition
Haverbeke explains: "Automated testing is the process of writing a program that tests another program. Writing tests is a bit more work than testing manually, but once you've done it, you gain a kind of superpower: it takes you only a few seconds to verify that your program still behaves properly in all the situations you wrote tests for." (Ch 8, "Testing")

# Prerequisites
- **Functions**: Tests verify function behavior

# Key Properties
1. Tests are small labeled programs that verify aspects of code
2. Test runners (test suites) help organize and run tests
3. Once written, tests provide ongoing verification
4. Code using persistent values is easier to test than code with side effects
5. Self-contained, pure functions are the easiest to test

# Construction / Recognition
```javascript
function test(label, body) {
  if (!body()) console.log(`Failed: ${label}`);
}

test("convert Latin text to uppercase", () => {
  return "hello".toUpperCase() == "HELLO";
});
```

# Context & Application
Testing is essential for maintaining code quality over time. The chapter notes: "the style of programming shown in the previous chapter, which uses self-contained persistent values rather than changing objects, tends to be easy to test." (Ch 8)

# Examples
```javascript
function test(label, body) {
  if (!body()) console.log(`Failed: ${label}`);
}

test("convert Latin text to uppercase", () => {
  return "hello".toUpperCase() == "HELLO";
});
test("convert Greek text to uppercase", () => {
  return "Xairete".toUpperCase() == "XAIRETE";
});
test("don't convert case-less characters", () => {
  return "mrhba".toUpperCase() == "MRHBA";
});
```
(Ch 8, "Testing", lines 251-265)

# Relationships
## Builds Upon
- function
## Enables
- Confidence in code changes, regression detection
## Related
- bug, assertion, debugging
## Contrasts With
- N/A

# Common Errors
- **Error**: Only testing manually
  **Correction**: Manual testing is unreliable for catching regressions; automate tests for consistent verification

# Common Confusions
- **Confusion**: Tests guarantee bug-free code
  **Clarification**: Tests only verify the specific scenarios you write them for; they reduce but don't eliminate bugs

# Source Reference
Chapter 8: Bugs and Errors, Section "Testing", lines 222-282.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
