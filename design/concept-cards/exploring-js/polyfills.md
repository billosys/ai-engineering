---
concept: Polyfills
slug: polyfills
category: modules
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.17 Polyfills: emulating native web platform features"
extraction_confidence: high
aliases:
  - "polyfill"
  - "shim"
prerequisites:
  - ecmascript-module
extends: []
related:
  - javascript-package
contrasts_with: []
answers_questions:
  - "What is a polyfill and why would I use one?"
---

# Quick Definition

A polyfill is a piece of code (usually a library) that emulates a native web platform feature on older platforms that don't support it, enabling the use of modern APIs everywhere.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, polyfills emulate native web platform features so that code using those features runs on older platforms. They are typically installed as packages and imported into projects.

# Prerequisites

- ECMAScript module (for importing polyfills)

# Key Properties

1. Emulates missing native features.
2. Distributed as packages.
3. Imported at application startup.
4. Only needed on platforms that lack the feature.
5. Enables writing modern code that works everywhere.

# Construction / Recognition

```js
// Import a polyfill for a missing feature
import 'core-js/features/array/flat-map';

// Now Array.prototype.flatMap works on older platforms
```

# Context & Application

Used to support older browsers or Node.js versions. Common polyfill libraries include `core-js` for ECMAScript features.

# Examples

Typical usage pattern:
```js
// At application entry point
import 'core-js/stable';
import 'regenerator-runtime/runtime';
```

# Relationships

## Related
- **JavaScript Package** -- polyfills are distributed as packages

# Source Reference

Chapter 29: Modules, Section 29.17.

# Verification Notes

- Definition source: direct
- Confidence rationale: Brief but explicit definition
- Cross-reference status: verified
