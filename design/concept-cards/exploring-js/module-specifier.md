---
concept: Module Specifier
slug: module-specifier
category: modules
subcategory: imports
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.1.4 Kinds of module specifiers"
extraction_confidence: high
aliases:
  - "import path"
  - "module path"
prerequisites:
  - ecmascript-module
extends: []
related:
  - named-import
contrasts_with: []
answers_questions:
  - "What are the different ways to identify a module in an import statement?"
---

# Quick Definition

A module specifier is the string in an import statement that identifies which module to load, coming in three kinds: absolute, relative, and bare.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, there are three kinds of module specifiers: absolute specifiers (full URLs like `'https://...'` or `'file:///...'`), relative specifiers (starting with `'/'`, `'./'`, or `'../'`, resolved against the module's URL), and bare specifiers (package names like `'lodash'` or `'@scope/name'`, resolved by the platform).

# Prerequisites

- ECMAScript module

# Key Properties

1. Absolute specifiers: full URLs (mostly for CDN-hosted libraries).
2. Relative specifiers: start with `/`, `./`, `../` (for same-codebase modules).
3. Bare specifiers: package names, optionally with subpaths (resolved by platform).
4. Bare specifiers can be scoped: `'@scope/package'`.

# Construction / Recognition

```js
import x from 'https://cdn.example.com/lib.mjs'; // absolute
import y from './sibling.mjs';                     // relative
import z from 'some-package';                      // bare
```

# Context & Application

Relative specifiers are most common for local code. Bare specifiers identify npm packages. Absolute specifiers are rare (CDN access).

# Examples

From the source text (Ch. 29, section 29.1.4):

```js
// Relative
'./sibling-module.js'
'../module-in-parent-dir.mjs'

// Bare
'some-package'
'@some-scope/scoped-name/dir/some-module.mjs'
```

# Relationships

## Related
- **Named Import** -- module specifier appears after `from`

# Source Reference

Chapter 29: Modules, Section 29.1.4, lines 230-290.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit three-kind taxonomy
- Cross-reference status: verified
