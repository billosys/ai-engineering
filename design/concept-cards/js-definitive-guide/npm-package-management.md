---
concept: npm Package Management
slug: npm-package-management
category: tooling
subcategory: package management
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 657
section: "17.4 Package Management with npm"
extraction_confidence: high
aliases:
  - npm
  - node package manager
  - package.json
prerequisites: []
extends: []
related:
  - code-bundlers
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

npm is Node's package manager for installing, managing, and tracking third-party dependencies via `package.json` (project metadata and dependencies) and `package-lock.json` (exact dependency versions), with `node_modules/` storing installed packages.

# Core Definition

npm is bundled with Node and manages software library dependencies. `npm install` reads `package.json` and downloads all dependencies into `node_modules/`. `npm install <package>` installs a specific package and records it in `package.json`. `--save-dev` marks development-only dependencies. `-g` installs globally. `npx` runs locally installed tools. npm also supports `uninstall`, `update`, and `audit` (security) commands. Alternatives include yarn and pnpm (Flanagan, Ch. 17, pp. 657-659).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `package.json` records project metadata and dependencies.
2. `package-lock.json` locks exact dependency versions.
3. `node_modules/` stores installed packages locally.
4. `npm install` installs all recorded dependencies.
5. `--save-dev` for development dependencies.
6. `npx` runs locally installed tools without global installation.

# Construction / Recognition

```bash
$ npm init                    # Create package.json
$ npm install express         # Install and record dependency
$ npm install --save-dev jest # Development dependency
$ npx jest                    # Run locally installed tool
```

# Context & Application

The foundation of the JavaScript ecosystem. Nearly every JavaScript project uses npm or a compatible package manager.

# Examples

From the source (p. 658-659): Installing Express, which downloads 50 packages from 37 contributors and creates a lockfile. Using `npx eslint` and `npx jest` to run locally installed tools.

# Relationships

## Builds Upon
- (None - foundational tooling concept)

## Enables
- Using third-party libraries in any JavaScript project

## Related
- **code-bundlers** — Bundlers process npm-installed modules for the browser

## Contrasts With
- (None)

# Common Errors

- **Error**: Committing `node_modules/` to version control.
  **Correction**: Add `node_modules/` to `.gitignore`. Commit `package.json` and `package-lock.json` instead.

# Common Confusions

- **Confusion**: npm is only for server-side Node.js.
  **Clarification**: npm is equally useful for client-side JavaScript, managing frontend frameworks and build tools.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.4, pages 657-659.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Practical examples with real output
- Uncertainties: None
- Cross-reference status: Verified
