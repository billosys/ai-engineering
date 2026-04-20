---
# === CORE IDENTIFICATION ===
concept: Finally Clause
slug: finally-clause

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
section: "Cleaning up after exceptions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - finally block

# === TYPED RELATIONSHIPS ===
prerequisites:
  - try-catch
  - exception
extends:
  - try-catch
related:
  - error-propagation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I ensure cleanup code runs even when exceptions occur?"
---

# Quick Definition
A `finally` block runs after a `try` block completes, regardless of whether an exception was thrown, ensuring cleanup code always executes.

# Core Definition
Haverbeke explains: "`try` statements have another feature: they may be followed by a `finally` block either instead of or in addition to a `catch` block. A `finally` block says 'no matter *what* happens, run this code after trying to run the code in the `try` block.'" He notes: "even though the `finally` code is run when an exception is thrown in the `try` block, it does not interfere with the exception. After the `finally` block runs, the stack continues unwinding." (Ch 8, "Cleaning up after exceptions")

# Prerequisites
- **Try/catch**: Finally extends the try statement
- **Exceptions**: Finally handles cleanup during exception propagation

# Key Properties
1. Runs whether the try block succeeds or throws
2. Can be used with or without a catch block
3. Does not interfere with exception propagation
4. After finally runs, the stack continues unwinding if an exception was thrown
5. Essential for maintaining consistent state in the face of exceptions

# Construction / Recognition
```javascript
try {
  // risky operation
} finally {
  // always runs
}
```

# Context & Application
Finally is critical when code has side effects that must be cleaned up regardless of success or failure, such as releasing resources or reverting partial changes.

# Examples
```javascript
function transfer(from, amount) {
  if (accounts[from] < amount) return;
  let progress = 0;
  try {
    accounts[from] -= amount;
    progress = 1;
    accounts[getAccount()] += amount;
    progress = 2;
  } finally {
    if (progress == 1) {
      accounts[from] += amount;
    }
  }
}
```
If `getAccount()` throws after money is deducted, the finally block restores it. (Ch 8, "Cleaning up after exceptions", lines 607-622)

# Relationships
## Builds Upon
- try-catch, exception
## Enables
- Safe cleanup, consistent state maintenance
## Related
- error-propagation
## Contrasts With
- N/A

# Common Errors
- **Error**: Assuming finally only runs on error
  **Correction**: Finally runs in ALL cases: normal completion, thrown exception, and even `return` from the try block

# Common Confusions
- **Confusion**: Finally catches the exception
  **Clarification**: Finally does NOT catch exceptions; it runs cleanup code, then the exception continues propagating

# Source Reference
Chapter 8: Bugs and Errors, Section "Cleaning up after exceptions", lines 535-643.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with practical example
- Cross-reference status: verified against chapter summary
