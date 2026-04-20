---
# === CORE IDENTIFICATION ===
concept: Strict Mode
slug: strict-mode

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
section: "Strict mode"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - use strict

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - scope
extends: []
related:
  - bug
  - this-keyword
  - class-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does strict mode relate to error prevention?"
  - "What does strict mode do in JavaScript?"
---

# Quick Definition
Strict mode is an opt-in JavaScript mode enabled by `"use strict"` that catches more errors by making certain silent failures into explicit errors.

# Core Definition
Haverbeke explains: "JavaScript can be made a *little* stricter by enabling *strict mode*. This can done by putting the string `\"use strict\"` at the top of a file or a function body." Key changes: undeclared variables throw errors, `this` is `undefined` in non-method calls, and duplicate parameters are disallowed. (Ch 8, "Strict mode")

# Prerequisites
- **Functions**: Strict mode can be applied to individual functions
- **Scope**: Strict mode changes how undeclared bindings are handled

# Key Properties
1. Enabled with `"use strict"` at top of file or function body
2. Forgetting `let` throws `ReferenceError` instead of creating a global
3. `this` is `undefined` in non-method function calls
4. Duplicate parameter names are disallowed
5. Code inside classes and modules is automatically strict
6. Removes certain problematic language features (like `with`)

# Construction / Recognition
```javascript
function canYouSpotTheProblem() {
  "use strict";
  for (counter = 0; counter < 10; counter++) {
    console.log("Happy happy");
  }
}
canYouSpotTheProblem();
// -> ReferenceError: counter is not defined
```

# Context & Application
Strict mode prevents common JavaScript pitfalls. Since classes and modules are automatically strict, most modern code runs in strict mode.

# Examples
Without strict mode, calling a constructor without `new` silently creates globals:
```javascript
function Person(name) { this.name = name; }
let ferdinand = Person("Ferdinand"); // oops
console.log(name);
// -> Ferdinand
```
With strict mode:
```javascript
"use strict";
function Person(name) { this.name = name; }
let ferdinand = Person("Ferdinand"); // forgot new
// -> TypeError: Cannot set property 'name' of undefined
```
(Ch 8, "Strict mode", lines 128-144)

# Relationships
## Builds Upon
- function, scope
## Enables
- Better error detection, safer this binding
## Related
- bug, this-keyword, class-declaration
## Contrasts With
- N/A

# Common Errors
- **Error**: Expecting strict mode to catch all types of bugs
  **Correction**: Strict mode catches only certain categories of errors (undeclared variables, bad `this` usage, duplicate parameters)

# Common Confusions
- **Confusion**: Strict mode needs to be enabled everywhere
  **Clarification**: "Code inside classes and modules is automatically strict." Only legacy scripts need explicit `"use strict"`.

# Source Reference
Chapter 8: Bugs and Errors, Section "Strict mode", lines 77-165.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with examples showing both modes
- Cross-reference status: verified
