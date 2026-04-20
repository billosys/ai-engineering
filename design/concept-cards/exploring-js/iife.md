---
concept: Immediately Invoked Function Expression
slug: iife
category: modules
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.3 Before we had modules, we had scripts"
extraction_confidence: high
aliases:
  - "IIFE"
  - "revealing module pattern"
prerequisites:
  - ordinary-function
extends: []
related:
  - scripts-vs-modules
  - ecmascript-module
contrasts_with:
  - ecmascript-module
answers_questions:
  - "How were modules simulated before ES6?"
---

# Quick Definition

An IIFE (Immediately Invoked Function Expression) is a function expression that is defined and called immediately, historically used to create private scopes before modules existed.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, before ES6 modules, IIFEs were used to simulate modules by wrapping code in a function to create a private scope. Because `var` is function-scoped (not block-scoped), the only way to create new scopes was via functions. The *revealing module pattern* returns an object with exported values from the IIFE. This approach had limitations: global variables for imports/exports, no explicit dependency declaration.

# Prerequisites

- Ordinary function

# Key Properties

1. Function expression defined and called immediately.
2. Creates a private scope (essential for `var` before `let`/`const`).
3. Revealing module pattern: returns object with exports.
4. Superseded by ECMAScript modules.
5. Term coined by Ben Alman.

# Construction / Recognition

```js
var myModule = (function () {
  var privateVar = 'private';
  function exportedFunc() { return privateVar; }
  return { exportedFunc: exportedFunc };
})();
```

# Context & Application

Historical pattern for module simulation. Understanding IIFEs helps comprehend legacy code and appreciate why modules were introduced.

# Examples

From the source text (Ch. 29, section 29.3):

```js
var myModule = (function () {
  var importedFunc1 = otherModule1.importedFunc1;
  function exportedFunc() { importedFunc1(); }
  return { exportedFunc: exportedFunc };
})();
```

# Relationships

## Contrasts With
- **ECMAScript Module** -- modules provide built-in scoping, explicit dependencies, no global variables

# Source Reference

Chapter 29: Modules, Section 29.3, lines 475-547.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with historical context
- Cross-reference status: verified
