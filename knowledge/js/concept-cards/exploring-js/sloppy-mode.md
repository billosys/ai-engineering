---
# === CORE IDENTIFICATION ===
concept: Sloppy Mode
slug: sloppy-mode

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: language-modes
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.10 Strict mode vs. sloppy mode"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - non-strict mode
  - normal mode

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - strict-mode
  - silent-failures
contrasts_with:
  - strict-mode

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is sloppy mode and why should it be avoided?"
---

# Quick Definition

Sloppy mode is JavaScript's default execution mode in scripts, characterized by silent failures, implicit global variable creation, and function-scoped (not block-scoped) function declarations.

# Core Definition

"Normal 'sloppy' mode is the default in scripts (code fragments that are a precursor to modules and supported by browsers)." (Ch. 9, &sect;9.10). In sloppy mode: assigning to undeclared variables creates global variables, function declarations are function-scoped (not block-scoped), and changing immutable data fails silently. "You'll rarely encounter sloppy mode in modern JavaScript code, which is almost always located in modules."

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Default mode in scripts (not modules)
2. Undeclared variable assignments create global variables
3. Function declarations are function-scoped
4. Changing immutable data fails silently (no TypeError)
5. Rarely encountered in modern JavaScript (modules are strict by default)

# Construction / Recognition

Sloppy mode is the absence of strict mode. It's the default in `<script>` tags and CommonJS modules unless `'use strict';` is specified.

# Context & Application

Sloppy mode is mainly encountered in legacy code and browser consoles. Modern code should always be in strict mode (via modules or the directive).

# Examples

From the source text (Ch. 9, &sect;9.10.2):

Sloppy mode creates accidental globals:
```js
function sloppyFunc() {
  undeclaredVar1 = 123;
}
sloppyFunc();
assert.equal(undeclaredVar1, 123); // global created
```

Sloppy mode fails silently:
```js
function sloppyFunc() {
  true.prop = 1; // fails silently
  return true.prop;
}
assert.equal(sloppyFunc(), undefined);
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- Understanding of legacy code behavior

## Related
- **silent-failures** -- sloppy mode is a major source of silent failures

## Contrasts With
- **strict-mode** -- the improved alternative that throws errors

# Common Errors

- **Error**: Accidentally running code in sloppy mode and getting unexpected behavior.
  **Correction**: Use modules or add `'use strict';` to scripts.

# Common Confusions

- **Confusion**: Thinking sloppy mode is the standard way to write JavaScript.
  **Clarification**: Modern JavaScript is written in modules (strict mode). Sloppy mode is a legacy default.

# Source Reference

Chapter 9: Syntax, Section 9.10, lines 1082-1237.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicitly contrasted with strict mode
- Cross-reference status: verified
