---
# === CORE IDENTIFICATION ===
concept: Package
slug: package

# === CLASSIFICATION ===
category: modularity
subcategory: distribution
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Modules"
chapter_number: 10
pdf_page: null
section: "Packages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - library

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module
extends: []
related:
  - npm
  - dependency
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a package?"
  - "How is a package different from a module?"
---

# Quick Definition
A package is a chunk of code that can be distributed (copied and installed), may contain one or more modules, and includes information about its dependencies and documentation.

# Core Definition
Haverbeke defines: "A package is a chunk of code that can be distributed (copied and installed). It may contain one or more modules and has information about which other packages it depends on. A package also usually comes with documentation explaining what it does so that people who didn't write it might still be able to use it." (Ch 10, "Packages")

# Prerequisites
- **Modules**: Packages contain one or more modules

# Key Properties
1. Can be distributed, copied, and installed
2. May contain one or more modules
3. Specifies dependencies on other packages
4. Includes documentation
5. Can be updated to fix bugs or add features
6. Typically published under an open-source license

# Construction / Recognition
Packages are recognized by having a `package.json` file, being available on NPM, and containing distributable code with dependency information.

# Context & Application
Packages enable code reuse across projects and the JavaScript ecosystem. The chapter notes: "Having quality packages available for download is extremely valuable. It means that we can often avoid reinventing a program that 100 people have written before." (Ch 10)

# Examples
```javascript
import {parse} from "ini";

console.log(parse("x = 10\ny = 20"));
// -> {x: "10", y: "20"}
```
The `ini` package provides INI file parsing, similar to what was built in Chapter 9. (Ch 10, "Packages", lines 300-305)

# Relationships
## Builds Upon
- module
## Enables
- Code reuse, dependency management
## Related
- npm, dependency
## Contrasts With
- N/A

# Common Errors
- **Error**: Duplicating code across projects instead of using packages
  **Correction**: Extract shared functionality into packages; use existing packages from NPM when appropriate

# Common Confusions
- **Confusion**: A package is the same as a module
  **Clarification**: A package can contain multiple modules; it's a distributable unit with metadata, while a module is a single file with imports/exports

# Source Reference
Chapter 10: Modules, Section "Packages", lines 208-305.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified against chapter summary
