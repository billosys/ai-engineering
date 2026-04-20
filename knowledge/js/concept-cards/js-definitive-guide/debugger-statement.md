---
# === CORE IDENTIFICATION ===
concept: debugger Statement
slug: debugger-statement

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 139
section: "5.6.2 debugger"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `debugger` statement acts as a breakpoint: when a debugger is active, execution pauses, allowing inspection of variables and the call stack. Otherwise, it has no effect.

# Core Definition

"The debugger statement normally does nothing. If, however, a debugger program is available and is running, then an implementation may (but is not required to) perform some kind of debugging action. In practice, this statement acts like a breakpoint." (Ch. 5, §5.6.2)

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. No effect if no debugger is active.
2. Acts like a programmatic breakpoint when developer tools are open.
3. Does not start the debugger — a debugger must already be running.

# Construction / Recognition

```js
debugger;
```

# Context & Application

Used for debugging during development. Insert `debugger;` at a suspicious point to pause execution and inspect state.

# Examples

From the source text (§5.6.2, p. 139):

```js
function f(o) {
    if (o === undefined) debugger;  // Temporary line for debugging
    // The rest of the function goes here.
}
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- Runtime debugging workflows

## Related
- No related concepts

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Leaving `debugger` statements in production code.
  **Correction**: Remove or comment out `debugger` statements before deploying.

# Common Confusions

- **Confusion**: Expecting `debugger` to automatically open the browser's developer tools.
  **Clarification**: `debugger` only pauses if developer tools are already open.

# Source Reference

Chapter 5: Statements, Section 5.6.2, page 139.

# Verification Notes

- Definition source: Direct quote from §5.6.2
- Confidence rationale: High — simple concept, clearly defined
- Uncertainties: None
- Cross-reference status: Verified
