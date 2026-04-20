---
# === CORE IDENTIFICATION ===
concept: NPM
slug: npm

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
  - Node Package Manager
  - npmjs.com

# === TYPED RELATIONSHIPS ===
prerequisites:
  - package
  - module
extends: []
related:
  - dependency
  - bundler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is NPM?"
  - "How do I find and install JavaScript packages?"
---

# Quick Definition
NPM is both an online service for downloading and uploading JavaScript packages and a command-line program (bundled with Node.js) for installing and managing them.

# Core Definition
Haverbeke explains: "In the JavaScript world, this infrastructure is provided by NPM ([https://npmjs.com](https://npmjs.com)). NPM is two things: an online service where you can download (and upload) packages, and a program (bundled with Node.js) that helps you install and manage them." (Ch 10, "Packages")

# Prerequisites
- **Packages**: NPM manages packages
- **Modules**: Packages contain modules

# Key Properties
1. Online registry with millions of packages
2. Command-line tool for installing/managing packages
3. Bundled with Node.js
4. Handles dependency resolution
5. Most popular packages are available under open-source licenses

# Construction / Recognition
NPM is used via the `npm` command-line tool and the npmjs.com website.

# Context & Application
NPM is the central infrastructure for JavaScript package distribution. "At the time of writing, there are more than three million different packages available on NPM." (Ch 10)

# Examples
```javascript
// After installing the ini package via npm
import {parse} from "ini";
console.log(parse("x = 10\ny = 20"));
// -> {x: "10", y: "20"}
```
(Ch 10, "Packages", lines 300-305)

# Relationships
## Builds Upon
- package, module
## Enables
- Easy package installation and distribution
## Related
- dependency, bundler
## Contrasts With
- N/A

# Common Errors
- **Error**: Reinventing functionality that exists as tested NPM packages
  **Correction**: Check NPM for existing solutions before writing your own

# Common Confusions
- **Confusion**: NPM only hosts useful packages
  **Clarification**: "A large portion of those are rubbish, to be fair. But almost every useful, publicly available JavaScript package can be found on NPM." (Ch 10)

# Source Reference
Chapter 10: Modules, Section "Packages", lines 244-265.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
