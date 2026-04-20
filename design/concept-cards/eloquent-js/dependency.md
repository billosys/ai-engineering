---
# === CORE IDENTIFICATION ===
concept: Dependency
slug: dependency

# === CLASSIFICATION ===
category: modularity
subcategory: module-relationships
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Modules"
chapter_number: 10
pdf_page: null
section: "Modular programs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - module dependency

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module
extends: []
related:
  - import-declaration
  - package
  - npm
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a dependency?"
  - "Why should dependencies be explicit?"
---

# Quick Definition
A dependency is a relationship where one module uses functionality from another module; when clearly specified, dependencies enable automatic loading and help determine what modules are needed.

# Core Definition
Haverbeke explains: "A good module system also requires modules to specify which code *they* use from other modules. These relations are called *dependencies*. If module A uses functionality from module B, it is said to *depend* on that module. When these are clearly specified in the module itself, they can be used to figure out which other modules need to be present to be able to use a given module and to automatically load dependencies." (Ch 10, "Modular programs")

# Prerequisites
- **Modules**: Dependencies are relationships between modules

# Key Properties
1. A module depends on another when it uses that module's functionality
2. Should be explicitly declared (via import statements)
3. Enable automatic dependency loading
4. Packages also declare dependencies on other packages
5. Circular dependencies can cause problems

# Construction / Recognition
```javascript
import {dayName} from "./dayname.js";
// This module depends on dayname.js
```

# Context & Application
Explicit dependencies make code modular and composable. Without them, programs become entangled "big balls of mud."

# Examples
```javascript
// This module has two dependencies: ordinal and date-names
const ordinal = require("ordinal");
const {days, months} = require("date-names");

exports.formatDate = function(date, format) {
  // uses ordinal and date-names
};
```
(Ch 10, "CommonJS modules", lines 377-391)

# Relationships
## Builds Upon
- module
## Enables
- Automatic loading, composability
## Related
- import-declaration, package, npm
## Contrasts With
- N/A

# Common Errors
- **Error**: Creating hidden dependencies (accessing globals or side effects)
  **Correction**: Always use explicit import declarations; avoid depending on global state

# Common Confusions
- **Confusion**: Circular dependencies always cause errors
  **Clarification**: "CommonJS modules allow a limited form of cyclic dependencies. As long as the modules don't access each other's interface until after they finish loading, cyclic dependencies are okay." (Ch 10)

# Source Reference
Chapter 10: Modules, Section "Modular programs", lines 73-87.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
