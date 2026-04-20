---
concept: import.meta
slug: import-meta
category: modules
subcategory: metadata
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.13 `import.meta`"
extraction_confidence: high
aliases:
  - "import.meta.url"
prerequisites:
  - ecmascript-module
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I get metadata about the current module?"
---

# Quick Definition

`import.meta` (ES2020) is an object that provides metadata about the current module, most importantly `import.meta.url` which gives the module's URL.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, `import.meta` is available inside ES modules and provides platform-dependent metadata. The most important property is `import.meta.url`, which contains the URL of the current module. This can be used with the `URL` class for path resolution.

# Prerequisites

- ECMAScript module

# Key Properties

1. Introduced in ES2020.
2. Only available inside ES modules.
3. `import.meta.url` -- the module's URL as a string.
4. Useful for resolving relative paths to files.
5. Platform-dependent (additional properties may exist).

# Construction / Recognition

```js
console.log(import.meta.url);
// e.g., 'file:///home/user/project/my-module.mjs'
```

# Context & Application

Used for resolving file paths relative to the current module, especially in Node.js where `__dirname` and `__filename` are not available in ESM.

# Examples

```js
// Resolve a file path relative to the current module
const url = new URL('./data.json', import.meta.url);
```

# Relationships

## Builds Upon
- **ECMAScript Module** -- only available in modules

# Source Reference

Chapter 29: Modules, Section 29.13.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with primary property
- Cross-reference status: verified
