---
concept: Code Bundlers
slug: code-bundlers
category: tooling
subcategory: bundling
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 659
section: "17.5 Code Bundling"
extraction_confidence: high
aliases:
  - webpack
  - Rollup
  - Parcel
  - module bundler
prerequisites:
  - npm-package-management
extends: []
related:
  - tree-shaking
  - babel-transpilation
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

Code bundlers (webpack, Rollup, Parcel) follow the import tree from entry points to combine all JavaScript modules and their dependencies into a single bundle file (or a few bundles) optimized for browser delivery.

# Core Definition

A code-bundler starts at the main entry point, follows the tree of import directives to find all modules the program depends on, and combines them into a single bundle with rewritten imports/exports. Features include: multiple entry points, dynamic code splitting via `import()`, source map generation, tree shaking (dead code elimination), plugin architecture for non-JS imports (JSON, CSS), filesystem watchers for automatic rebuilds, and hot module replacement. webpack is highly configurable; Parcel is zero-configuration; Rollup balances both (Flanagan, Ch. 17, pp. 659-661).

# Prerequisites

- **npm-package-management** — Bundlers process npm-installed modules.

# Key Properties

1. Combines multiple modules into one or a few output files.
2. Source maps map bundled code back to original source locations.
3. Tree shaking removes unused exports.
4. Code splitting with `import()` creates separate chunks loaded on demand.
5. Plugin architecture supports importing non-JS assets.
6. Filesystem watchers enable automatic rebuilds on save.

# Construction / Recognition

Bundlers are configured via config files (e.g., `webpack.config.js`) or zero-config conventions (Parcel).

# Context & Application

Essential for deploying JavaScript to browsers. Even though browsers support ES6 modules, bundling typically provides better performance for production deployments.

# Examples

From the source (p. 659): Developers used bundlers for years before browsers supported ES6 modules. Modern use continues because a single medium-sized bundle loads faster than many small modules.

# Relationships

## Builds Upon
- **npm-package-management** — Bundles npm-installed modules

## Enables
- Optimized browser delivery of modular JavaScript

## Related
- **tree-shaking** — A key bundler optimization
- **babel-transpilation** — Often integrated into the bundling pipeline

## Contrasts With
- (None)

# Common Errors

- **Error**: Assuming bundling is unnecessary because browsers support modules.
  **Correction**: Bundling still provides better performance, tree shaking, and production optimizations.

# Common Confusions

- **Confusion**: All bundlers require complex configuration.
  **Clarification**: Parcel is designed as a zero-configuration alternative to webpack.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.5, pages 659-661.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: All three major bundlers described
- Uncertainties: Bundler landscape evolves rapidly
- Cross-reference status: Verified
