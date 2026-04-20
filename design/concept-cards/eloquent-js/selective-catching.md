---
# === CORE IDENTIFICATION ===
concept: Selective Catching
slug: selective-catching

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
section: "Selective catching"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - specific error catching
  - typed exception handling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - try-catch
  - error-class
  - instanceof-operator
extends:
  - try-catch
related:
  - inheritance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I catch only specific types of exceptions?"
  - "Why is blanket-catching exceptions dangerous?"
---

# Quick Definition
Selective catching is the practice of checking the type of a caught exception (using `instanceof`) and rethrowing unrecognized exceptions, preventing accidental suppression of unexpected errors.

# Core Definition
Haverbeke warns: "JavaScript (in a rather glaring omission) doesn't provide direct support for selectively catching exceptions: either you catch them all or you don't catch any." The solution is to define custom error classes and use `instanceof` to check exception types, rethrowing unmatched ones. (Ch 8, "Selective catching")

# Prerequisites
- **Try/catch**: The mechanism for catching exceptions
- **Error class**: Custom error classes enable type-based differentiation
- **instanceof operator**: Used to check exception types

# Key Properties
1. JavaScript `catch` catches ALL exceptions, not specific types
2. Define custom error classes (e.g., `class InputError extends Error {}`)
3. Use `instanceof` in the catch block to identify expected error types
4. Rethrow unexpected exceptions with `throw e`
5. Blanket-catching hides bugs and makes debugging harder

# Construction / Recognition
```javascript
try {
  // ...
} catch (e) {
  if (e instanceof InputError) {
    // handle expected error
  } else {
    throw e;  // rethrow unexpected errors
  }
}
```

# Context & Application
Selective catching prevents the common bug of accidentally catching and suppressing programmer errors (like typos in variable names).

# Examples
Bad (blanket catch hides a typo bug):
```javascript
for (;;) {
  try {
    let dir = promtDirection("Where?"); // typo!
    console.log("You chose ", dir);
    break;
  } catch (e) {
    console.log("Not a valid direction. Try again.");
  }
}
```

Good (selective catch):
```javascript
for (;;) {
  try {
    let dir = promptDirection("Where?");
    console.log("You chose ", dir);
    break;
  } catch (e) {
    if (e instanceof InputError) {
      console.log("Not a valid direction. Try again.");
    } else {
      throw e;
    }
  }
}
```
(Ch 8, "Selective catching", lines 693-778)

# Relationships
## Builds Upon
- try-catch, error-class, instanceof-operator
## Enables
- Safer error handling, better debugging
## Related
- inheritance
## Contrasts With
- N/A

# Common Errors
- **Error**: Catching all exceptions without checking their type
  **Correction**: Always check exception types in catch blocks; rethrow unknown exceptions

# Common Confusions
- **Confusion**: JavaScript can selectively catch by type like Java or Python
  **Clarification**: JavaScript has only one catch clause; selective catching must be done manually with `instanceof` checks

# Source Reference
Chapter 8: Bugs and Errors, Section "Selective catching", lines 644-783.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined as a recommended practice with detailed examples
- Cross-reference status: verified
