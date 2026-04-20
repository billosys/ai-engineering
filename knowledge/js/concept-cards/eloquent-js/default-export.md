---
# === CORE IDENTIFICATION ===
concept: Default Export
slug: default-export

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
  - export default

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es-module
  - export-declaration
extends:
  - export-declaration
related:
  - named-export
  - import-declaration
contrasts_with:
  - named-export

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I export a single main value from a module?"
---

# Quick Definition
A default export (`export default`) provides a module's primary value, imported without braces, and is commonly used for modules that export a single binding.

# Core Definition
Haverbeke explains: "A module may also have a special export named `default`, which is often used for modules that only export a single binding. To define a default export, you write `export default` before an expression, a function declaration, or a class declaration." Default exports are imported "by omitting the braces around the name of the import." (Ch 10, "ES modules")

# Prerequisites
- **ES modules**: Default exports are part of the ES module system
- **Export declarations**: Default is a special form of export

# Key Properties
1. Defined with `export default` before an expression
2. Imported without braces: `import name from "./module.js"`
3. Only one default export per module
4. Often used for modules exporting a single value

# Construction / Recognition
```javascript
// Exporting
export default ["Winter", "Spring", "Summer", "Autumn"];

// Importing
import seasonNames from "./seasonname.js";
```

# Context & Application
Default exports simplify importing for modules that have a single primary export.

# Examples
```javascript
// seasonname.js
export default ["Winter", "Spring", "Summer", "Autumn"];

// Using the default export
import seasonNames from "./seasonname.js";
```
(Ch 10, "ES modules", lines 184-194)

# Relationships
## Builds Upon
- es-module, export-declaration
## Enables
- Simpler import syntax for single-export modules
## Related
- import-declaration
## Contrasts With
- named-export (uses braces, multiple per module)

# Common Errors
- **Error**: Using braces when importing a default export
  **Correction**: Default exports are imported without braces; `import name from "./mod.js"` not `import {name}`

# Common Confusions
- **Confusion**: You can have multiple default exports
  **Clarification**: Each module can have only one default export; use named exports for multiple values

# Source Reference
Chapter 10: Modules, Section "ES modules", lines 177-194.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
