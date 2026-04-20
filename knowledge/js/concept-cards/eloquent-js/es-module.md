---
# === CORE IDENTIFICATION ===
concept: ES Module
slug: es-module

# === CLASSIFICATION ===
category: modularity
subcategory: module-systems
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Modules"
chapter_number: 10
pdf_page: null
section: "ES modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ECMAScript module
  - ESM

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module
  - function
extends:
  - module
related:
  - import-declaration
  - export-declaration
  - commonjs-module
contrasts_with:
  - commonjs-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a module?"
  - "What must I know before writing a module system?"
---

# Quick Definition
ES modules are JavaScript's built-in module system (since ECMAScript 2015) that uses `import` and `export` keywords, with each module getting its own separate scope.

# Core Definition
Haverbeke explains: "Since ECMAScript 2015, JavaScript supports two different types of programs. *Scripts* behave in the old way: their bindings are defined in the global scope. *Modules* get their own separate scope and support the `import` and `export` keywords, which aren't available in scripts, to declare their dependencies and interface. This module system is usually called *ES modules* (where *ES* stands for ECMAScript)." (Ch 10, "ES modules")

# Prerequisites
- **Modules**: Understanding the concept of modules
- **Functions**: Modules contain function definitions

# Key Properties
1. Each module has its own scope (not global)
2. Uses `import` and `export` keywords
3. Import/export declarations must be at the top level (not inside functions or loops)
4. Imports are resolved before the module code runs
5. Module names are resolved differently per platform (URLs in browsers, files in Node.js)
6. Code inside modules is automatically strict

# Construction / Recognition
ES modules are identified by the use of `import` and `export` keywords at the top level of a file.

# Context & Application
ES modules are now the standard module system for JavaScript. "there is no real reason to write new programs in [CommonJS] style anymore." (Ch 10)

# Examples
```javascript
// dayname.js - exporting
const names = ["Sunday", "Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday"];
export function dayName(number) {
  return names[number];
}

// main.js - importing
import {dayName} from "./dayname.js";
let now = new Date();
console.log(`Today is ${dayName(now.getDay())}`);
// -> Today is Monday
```
(Ch 10, "ES modules", lines 119-142)

# Relationships
## Builds Upon
- module, function
## Enables
- import-declaration, export-declaration, default-export, named-export
## Related
- module-scope
## Contrasts With
- commonjs-module (older, function-based system)

# Common Errors
- **Error**: Placing import/export inside functions or conditionals
  **Correction**: "Import and export declarations cannot appear inside of functions, loops, or other blocks." (Ch 10)

# Common Confusions
- **Confusion**: ES modules and CommonJS modules are interchangeable
  **Clarification**: They have different syntax and semantics; ES module imports are resolved before execution, while CommonJS `require` is a runtime function call

# Source Reference
Chapter 10: Modules, Section "ES modules", lines 88-206.

# Verification Notes
- Definition source: direct
- Confidence rationale: Extensively defined as the modern standard
- Cross-reference status: verified against chapter summary
