---
# === CORE IDENTIFICATION ===
concept: Strict Mode
slug: strict-mode

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
  - "'use strict'"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - sloppy-mode
  - backward-compatibility
  - block-scoping
contrasts_with:
  - sloppy-mode

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is strict mode in JavaScript and why should I use it?"
---

# Quick Definition

Strict mode is a cleaner version of JavaScript (introduced in ES5) that removes several pitfalls of "sloppy" mode, throwing errors where sloppy mode fails silently. It is the default in modules and classes.

# Core Definition

"Starting with ECMAScript 5, JavaScript has two *modes* in which JavaScript can be executed" (Ch. 9, &sect;9.10): sloppy mode (default in scripts) and strict mode (default in modules and classes). Strict mode can be enabled in scripts via `'use strict';` at the top of a file or function. Improvements include: undeclared variables throw `ReferenceError` (instead of creating globals), function declarations are block-scoped (not function-scoped), and changing immutable data throws `TypeError` (instead of failing silently).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. ^ES5^: Introduced in ECMAScript 5
2. Default in modules and classes (ES6)
3. Opt-in in scripts via `'use strict';`
4. Undeclared variable assignment throws `ReferenceError`
5. Function declarations become block-scoped
6. Changing immutable data throws `TypeError`
7. Can be applied per-file or per-function

# Construction / Recognition

```js
'use strict'; // file-level

function strictFunc() {
  'use strict'; // function-level
}
```

Modern code in modules is always strict mode automatically.

# Context & Application

Most modern JavaScript is in strict mode because it's written in modules. Consoles often run in non-strict mode, which may produce different results.

# Examples

From the source text (Ch. 9, &sect;9.10.2):

Sloppy mode creates global variables on typos:
```js
function sloppyFunc() {
  undeclaredVar1 = 123;
}
sloppyFunc();
assert.equal(undeclaredVar1, 123); // global created!
```

Strict mode throws:
```js
function strictFunc() {
  'use strict';
  undeclaredVar2 = 123; // ReferenceError!
}
```

Strict mode block-scopes function declarations:
```js
function strictFunc() {
  'use strict';
  {
    function foo() { return 123 }
  }
  return foo(); // ReferenceError: foo is not defined
}
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **block-scoping** -- function declarations become block-scoped in strict mode

## Related
- **backward-compatibility** -- strict mode is a compatibility-safe improvement

## Contrasts With
- **sloppy-mode** -- the default in scripts, with more pitfalls

# Common Errors

- **Error**: Forgetting that consoles run in sloppy mode.
  **Correction**: Test code in modules or files with `'use strict';` for accurate behavior.

# Common Confusions

- **Confusion**: Thinking `'use strict';` is needed in ES modules.
  **Clarification**: Modules are automatically in strict mode; the directive is only needed in scripts.

# Source Reference

Chapter 9: Syntax, Section 9.10, lines 1082-1237.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed with three improvement examples
- Cross-reference status: verified against Ch. 5 (&sect;5.6) and Ch. 10
