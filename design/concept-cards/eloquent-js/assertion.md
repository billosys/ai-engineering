---
# === CORE IDENTIFICATION ===
concept: Assertion
slug: assertion

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
section: "Assertions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - assert
  - precondition check

# === TYPED RELATIONSHIPS ===
prerequisites:
  - throw-statement
  - error-class
extends: []
related:
  - bug
  - testing
  - debugging
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an assertion?"
  - "How do assertions help find bugs?"
---

# Quick Definition
Assertions are checks inside a program that verify assumptions are correct, used to find programmer mistakes rather than to handle expected runtime errors.

# Core Definition
Haverbeke defines: "*Assertions* are checks inside a program that verify that something is the way it is supposed to be. They are used not to handle situations that can come up in normal operation but to find programmer mistakes." (Ch 8, "Assertions")

# Prerequisites
- **Throw statement**: Assertions throw errors when conditions are violated
- **Error class**: Assertions typically throw Error objects

# Key Properties
1. Verify internal program invariants, not external input
2. Throw errors when conditions are violated
3. Intended to catch programmer mistakes, not user errors
4. Should be reserved for easy-to-make mistakes, not exhaustive input validation

# Construction / Recognition
```javascript
function firstElement(array) {
  if (array.length == 0) {
    throw new Error("firstElement called with []");
  }
  return array[0];
}
```

# Context & Application
Assertions make violations loud and immediate rather than allowing silent incorrect behavior. Haverbeke advises: "I do not recommend trying to write assertions for every possible kind of bad input. That'd be a lot of work and would lead to very noisy code. You'll want to reserve them for mistakes that are easy to make (or that you find yourself making)." (Ch 8, "Assertions")

# Examples
```javascript
function firstElement(array) {
  if (array.length == 0) {
    throw new Error("firstElement called with []");
  }
  return array[0];
}
```
"instead of silently returning undefined (which you get when reading an array property that does not exist), this will loudly blow up your program as soon as you misuse it." (Ch 8, "Assertions", lines 798-812)

# Relationships
## Builds Upon
- throw-statement, error-class
## Enables
- Earlier bug detection, clearer error messages
## Related
- bug, testing, debugging
## Contrasts With
- N/A

# Common Errors
- **Error**: Writing assertions for every possible invalid input
  **Correction**: Reserve assertions for likely programmer mistakes; use proper error handling for external input validation

# Common Confusions
- **Confusion**: Assertions are the same as input validation
  **Clarification**: Assertions catch programmer errors (precondition violations); input validation handles expected bad data from users or external sources

# Source Reference
Chapter 8: Bugs and Errors, Section "Assertions", lines 785-818.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with example and usage guidelines
- Cross-reference status: verified
