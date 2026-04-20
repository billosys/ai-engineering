---
# === CORE IDENTIFICATION ===
concept: Import Declaration
slug: import-declaration

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
  - import statement
  - import keyword

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es-module
  - export-declaration
extends: []
related:
  - named-export
  - default-export
  - dependency
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I import from another module?"
---

# Quick Definition
The `import` keyword makes bindings from another module available in the current module, using braces for named imports or omitting them for default imports.

# Core Definition
Haverbeke explains: "The `import` keyword, followed by a list of binding names in braces, makes bindings from another module available in the current module. Modules are identified by quoted strings." Imports can be renamed with `as`, and `import *` imports all bindings as properties of an object. (Ch 10, "ES modules")

# Prerequisites
- **ES modules**: Import is part of the ES module system
- **Export declarations**: You can only import what has been exported

# Key Properties
1. Named imports use braces: `import {name} from "./module.js"`
2. Default imports omit braces: `import name from "./module.js"`
3. Imports can be renamed: `import {dayName as nomDeJour} from "./dayname.js"`
4. Namespace import: `import * as mod from "./module.js"`
5. Must appear at the top level of the module body
6. Resolved before the module code executes

# Construction / Recognition
```javascript
import {dayName} from "./dayname.js";
import {dayName as nomDeJour} from "./dayname.js";
import seasonNames from "./seasonname.js";
import * as dayName from "./dayname.js";
```

# Context & Application
Import declarations specify a module's dependencies, making them explicit and enabling tooling to determine what needs to be loaded.

# Examples
```javascript
import {dayName} from "./dayname.js";
let now = new Date();
console.log(`Today is ${dayName(now.getDay())}`);
// -> Today is Monday

// Renaming
import {dayName as nomDeJour} from "./dayname.js";
console.log(nomDeJour(3));
// -> Wednesday

// Namespace import
import * as dayName from "./dayname.js";
console.log(dayName.dayName(3));
// -> Wednesday
```
(Ch 10, "ES modules", lines 137-206)

# Relationships
## Builds Upon
- es-module, export-declaration
## Enables
- Using functionality from other modules
## Related
- named-export, default-export, dependency
## Contrasts With
- N/A

# Common Errors
- **Error**: Importing a non-exported binding
  **Correction**: Only exported bindings are available for import; check the source module's exports

# Common Confusions
- **Confusion**: Import paths are always file paths
  **Clarification**: "How such a module name is resolved to an actual program differs by platform. The browser treats them as web addresses, whereas Node.js resolves them to files." (Ch 10)

# Source Reference
Chapter 10: Modules, Section "ES modules", lines 137-206.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with multiple import forms
- Cross-reference status: verified
