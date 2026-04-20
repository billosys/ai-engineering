---
# === CORE IDENTIFICATION ===
concept: Bug
slug: bug

# === CLASSIFICATION ===
category: error-handling
subcategory: fundamentals
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Bugs and Errors"
chapter_number: 8
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - defect
  - flaw

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
extends: []
related:
  - debugging
  - testing
  - strict-mode
contrasts_with:
  - exception

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a bug?"
  - "What kinds of bugs exist?"
---

# Quick Definition
A bug is a flaw in a computer program, categorized as either confused thinking (design bugs) or mistakes in translating thought to code (implementation bugs).

# Core Definition
Haverbeke states: "Flaws in computer programs are usually called *bugs*." He categorizes them: "If a program is crystallized thought, we can roughly categorize bugs into those caused by the thoughts being confused and those caused by mistakes introduced while converting a thought to code. The former type is generally harder to diagnose and fix than the latter." (Ch 8)

# Prerequisites
- **Functions**: Bugs occur in code, typically within functions

# Key Properties
1. Confused-thought bugs: fundamental design or logic errors
2. Translation bugs: typos, wrong variable names, off-by-one errors
3. JavaScript's looseness allows many errors to pass silently
4. Silent bugs (producing `NaN` or `undefined`) can propagate far before manifesting

# Construction / Recognition
Bugs are found through testing, debugging, or encountering unexpected behavior. JavaScript's permissiveness makes some bugs hard to detect: "your nonsense computation will merely produce `NaN` (not a number) or an undefined value, while the program happily continues." (Ch 8)

# Context & Application
Bug prevention and detection is a core programming skill. The chapter discusses multiple strategies: strict mode, type checking, testing, debugging, and exception handling.

# Examples
JavaScript allows nonsensical operations without complaint:
```javascript
true * "monkey"  // NaN, no error
```
The `numberToString` bug:
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
```
(Ch 8, "Debugging", lines 310-325)

# Relationships
## Builds Upon
- function
## Enables
- Need for debugging, testing, strict-mode, exception handling
## Related
- debugging, testing, strict-mode
## Contrasts With
- exception (expected error conditions vs unintended flaws)

# Common Errors
- **Error**: Making random code changes to fix a bug
  **Correction**: "This is where you must resist the urge to start making random changes to the code to see whether that makes it better. Instead, *think*." (Ch 8)

# Common Confusions
- **Confusion**: All bugs cause error messages
  **Clarification**: Many JavaScript bugs produce wrong values silently; the program continues running with incorrect data

# Source Reference
Chapter 8: Bugs and Errors, opening section, lines 32-76.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined at the start of the chapter
- Cross-reference status: verified
