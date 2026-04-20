---
# === CORE IDENTIFICATION ===
concept: Export Declaration
slug: export-declaration

# === CLASSIFICATION ===
category: modularity
subcategory: module-syntax
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
  - export statement
  - export keyword

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es-module
extends: []
related:
  - named-export
  - default-export
  - import-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make bindings available to other modules?"
---

# Quick Definition
The `export` keyword marks bindings as part of a module's interface, making them available for other modules to import.

# Core Definition
Haverbeke explains: "The `export` keyword can be put in front of a function, class, or binding definition to indicate that that binding is part of the module's interface. This makes it possible for other modules to use that binding by importing it." (Ch 10, "ES modules")

# Prerequisites
- **ES modules**: Export is part of the ES module system

# Key Properties
1. `export` before a declaration makes it part of the interface
2. Non-exported bindings remain private to the module
3. Can export functions, classes, and variable bindings
4. `export default` for single-value modules
5. Must appear at the top level

# Construction / Recognition
```javascript
export function dayName(number) { ... }
export class MyClass { ... }
export const value = 42;
export default expression;
```

# Context & Application
Exports define a module's public API. Everything not exported is encapsulated within the module.

# Examples
```javascript
const names = ["Sunday", "Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday"];

export function dayName(number) {
  return names[number];
}
export function dayNumber(name) {
  return names.indexOf(name);
}
```
The `names` array is private; only `dayName` and `dayNumber` are accessible to other modules. (Ch 10, "ES modules", lines 119-129)

# Relationships
## Builds Upon
- es-module
## Enables
- named-export, default-export, import-declaration
## Related
- module, interface
## Contrasts With
- N/A

# Common Errors
- **Error**: Forgetting to export bindings that other modules need
  **Correction**: Add `export` before any binding that should be part of the module's interface

# Common Confusions
- **Confusion**: All bindings in a module are automatically exported
  **Clarification**: Only bindings explicitly marked with `export` are accessible; everything else is private

# Source Reference
Chapter 10: Modules, Section "ES modules", lines 131-135.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
