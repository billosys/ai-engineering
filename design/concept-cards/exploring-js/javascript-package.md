---
concept: JavaScript Package
slug: javascript-package
category: modules
subcategory: packages
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.10 Packages: JavaScript's units for software distribution"
extraction_confidence: high
aliases:
  - "npm package"
  - "package"
prerequisites:
  - ecmascript-module
extends: []
related:
  - module-specifier
contrasts_with: []
answers_questions:
  - "What is a JavaScript package and how does it relate to modules?"
---

# Quick Definition

A package is a directory with a standardized layout (including `package.json`) that serves as JavaScript's unit for software distribution, containing modules, dependencies, and metadata.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, a package is a directory that can contain JavaScript code, libraries, tests, shell scripts, and other artifacts. Every package has a `package.json` file with metadata (name, version, author) and a dependency list. Dependencies are installed into `node_modules/`. Package names can be global (`lodash`) or scoped (`@babel/core`). Packages are distributed via registries like npm.

# Prerequisites

- ECMAScript module

# Key Properties

1. Every package has a `package.json` file.
2. Dependencies installed in `node_modules/`.
3. Package names: global (`mocha`) or scoped (`@babel/core`).
4. `package-lock.json` records exact dependency versions.
5. Published via package registries (npm, JSR).
6. Can be published or unpublished (internal projects).

# Construction / Recognition

```
my-package/
  package.json
  node_modules/
  src/
  index.mjs
```

# Context & Application

Packages are the fundamental unit of code distribution in the JavaScript ecosystem. Every library, tool, and application is organized as a package.

# Examples

From the source text (Ch. 29, section 29.10.3):

```json
{
  "name": "my-package",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  }
}
```

# Relationships

## Builds Upon
- **ECMAScript Module** -- packages contain modules

## Related
- **Module Specifier** -- bare specifiers resolve to packages

# Source Reference

Chapter 29: Modules, Section 29.10, lines 1204-1349.

# Verification Notes

- Definition source: direct
- Confidence rationale: Detailed description of package structure
- Cross-reference status: verified
