---
# === CORE IDENTIFICATION ===
concept: Strict Mode
slug: strict-mode

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: language-modes
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Introduction to JavaScript"
chapter_number: 1
pdf_page: 19
section: "JavaScript: Names, Versions, and Modes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "\"use strict\""
  - strict JavaScript

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - ecmascript-versioning
extends: []
related:
  - var-declarations
  - let-and-const-declarations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is strict mode?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

Strict mode is an opt-in language mode introduced in ES5 that corrects early JavaScript mistakes and provides stricter error checking, activated by the `"use strict"` directive.

# Core Definition

As described in Chapter 1: "programs can opt in to JavaScript's strict mode in which a number of early language mistakes have been corrected. The mechanism for opting in is the 'use strict' directive." In ES6 and later, "the use of new language features often implicitly invokes strict mode. For example, if you use the ES6 class keyword or create an ES6 module, then all the code within the class or module is automatically strict, and the old, flawed features are not available in those contexts." (p. 19)

# Prerequisites

- **javascript-language-overview** — Must understand the language itself
- **ecmascript-versioning** — Strict mode was introduced in ES5 and expanded in ES6

# Key Properties

1. Opt-in via the `"use strict"` directive at the top of a script or function
2. Corrects early (pre-ES5) language mistakes
3. Maintains backward compatibility — legacy code still works without it
4. ES6 classes and modules are automatically strict
5. Prevents accidental creation of global variables from undeclared assignments

# Construction / Recognition

```javascript
"use strict";
// All code here runs in strict mode
```

Or implicitly within ES6 classes and modules:
```javascript
class MyClass { /* automatically strict */ }
```

# Context & Application

Strict mode is used to catch common coding errors early. In strict mode, assigning to an undeclared variable throws a ReferenceError rather than silently creating a global variable. Most modern JavaScript code runs in strict mode either explicitly or implicitly (via modules/classes).

# Examples

From the source text (p. 74): In strict mode, "if you attempt to use an undeclared variable, you'll get a reference error when you run your code. Outside of strict mode, however, if you assign a value to a name that has not been declared with let, const, or var, you'll end up creating a new global variable."

# Relationships

## Builds Upon
- **ecmascript-versioning** — Strict mode is an ES5 feature expanded in ES6

## Enables
- **let-and-const-declarations** — let/const behave consistently in strict mode
- **var-declarations** — Strict mode changes behavior of undeclared variables

## Related
- **var-declarations** — Strict mode prevents accidental globals from undeclared var usage

## Contrasts With
- None explicitly named within this source (contrasts with "sloppy mode" informally)

# Common Errors

- **Error**: Assuming strict mode is always active.
  **Correction**: Strict mode must be opted into with `"use strict"` unless code is inside an ES6 module or class body.

# Common Confusions

- **Confusion**: Strict mode is a completely different language.
  **Clarification**: Strict mode is the same language with stricter error checking and certain legacy features disabled.

# Source Reference

Chapter 1: Introduction to JavaScript, Section "JavaScript: Names, Versions, and Modes", page 19. Also referenced in §3.10.2, page 74.

# Verification Notes

- Definition source: Direct quotes from pp. 19, 74
- Confidence rationale: High — clearly defined with specific mechanism explained
- Uncertainties: Full differences between strict and non-strict deferred to §5.6.3
- Cross-reference status: Verified against Ch 1 and Ch 3
