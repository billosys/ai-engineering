---
# === CORE IDENTIFICATION ===
concept: Bundler
slug: bundler

# === CLASSIFICATION ===
category: modularity
subcategory: tooling
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Modules"
chapter_number: 10
pdf_page: null
section: "Building and bundling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - module bundler

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module
  - es-module
  - package
extends: []
related:
  - npm
  - dependency
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a bundler?"
  - "Why do web applications need bundling?"
---

# Quick Definition
Bundlers are tools that combine a program's many module files into a single large file for efficient delivery to web browsers, since fetching one big file is faster than many small ones.

# Core Definition
Haverbeke explains: "Because fetching a single big file tends to be faster than fetching a lot of tiny ones, web programmers have started using tools that combine their programs (which they painstakingly split into modules) into a single big file before they publish it to the web. Such tools are called *bundlers*." The chapter also mentions *minifiers* that "take a JavaScript program and make it smaller by automatically removing comments and whitespace, renaming bindings, and replacing pieces of code with equivalent code that take up less space." (Ch 10, "Building and bundling")

# Prerequisites
- **Modules**: Bundlers combine modules
- **ES modules**: Bundlers process module import/export declarations
- **Packages**: Bundlers resolve package dependencies

# Key Properties
1. Combines many module files into one or few files
2. Resolves import/export relationships
3. Reduces network requests for web applications
4. Often combined with minification for smaller file sizes
5. May include compilation from TypeScript or modern JS to older JS

# Construction / Recognition
Bundlers are development tools (like webpack, rollup, esbuild) that process source files before deployment.

# Context & Application
Bundlers bridge the gap between modular development (many small files) and efficient delivery (few large files). "Including a modular program that consists of 200 different files in a web page produces its own problems." (Ch 10)

# Examples
The chapter describes the general concept without specific tool examples, noting: "there are many of them, and which one is popular changes regularly. Just be aware that such things exist, and look them up when you need them." (Ch 10, "Building and bundling", lines 523-525)

# Relationships
## Builds Upon
- module, es-module, package
## Enables
- Efficient web delivery of modular programs
## Related
- npm, dependency
## Contrasts With
- N/A

# Common Errors
- **Error**: Shipping hundreds of unbundled module files to the browser
  **Correction**: Use a bundler to combine modules for production deployment

# Common Confusions
- **Confusion**: Bundlers are only for the browser
  **Clarification**: While primarily needed for web delivery, bundlers can also optimize Node.js deployments

# Source Reference
Chapter 10: Modules, Section "Building and bundling", lines 483-525.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
