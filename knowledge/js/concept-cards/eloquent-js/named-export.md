---
# === CORE IDENTIFICATION ===
concept: Named Export
slug: named-export

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es-module
  - export-declaration
extends:
  - export-declaration
related:
  - default-export
  - import-declaration
contrasts_with:
  - default-export

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I export multiple values from a module?"
---

# Quick Definition
Named exports are bindings exported with their name from a module, imported using braces `{name}` and allowing multiple exports per module.

# Core Definition
Named exports are the standard form of export in ES modules. The `export` keyword before a function, class, or binding definition creates a named export. These are imported using destructuring-like syntax: `import {name1, name2} from "./module.js"`. (Ch 10, "ES modules")

# Prerequisites
- **ES modules**: Named exports are part of the ES module system
- **Export declarations**: Named exports use the `export` keyword

# Key Properties
1. Multiple named exports per module
2. Imported with braces: `import {name} from "./module.js"`
3. Can be renamed on import: `import {name as alias}`
4. The module's interface consists of its named (and default) exports

# Construction / Recognition
```javascript
// Exporting
export function dayName(number) { ... }
export function dayNumber(name) { ... }

// Importing
import {dayName, dayNumber} from "./dayname.js";
```

# Context & Application
Named exports are the most common export form, used when a module provides multiple related functions or values.

# Examples
```javascript
export function dayName(number) {
  return names[number];
}
export function dayNumber(name) {
  return names.indexOf(name);
}

// Importing specific named exports
import {dayName} from "./dayname.js";
```
(Ch 10, "ES modules", lines 119-142)

# Relationships
## Builds Upon
- es-module, export-declaration
## Enables
- Selective importing of specific bindings
## Related
- import-declaration
## Contrasts With
- default-export (single primary value, no braces)

# Common Errors
- **Error**: Forgetting braces when importing named exports
  **Correction**: Named exports require braces: `import {dayName}` not `import dayName`

# Common Confusions
- **Confusion**: Named exports work the same as default exports
  **Clarification**: Named exports use braces in import, allow multiple per module, and require matching names (unless aliased)

# Source Reference
Chapter 10: Modules, Section "ES modules", lines 119-142.

# Verification Notes
- Definition source: synthesized from export/import description
- Confidence rationale: Clear from the examples though not separately defined
- Cross-reference status: verified
