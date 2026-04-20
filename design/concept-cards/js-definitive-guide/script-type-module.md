---
# === CORE IDENTIFICATION ===
concept: Script type="module"
slug: script-type-module

# === CLASSIFICATION ===
category: modules
subcategory: es6-modules
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Modules"
chapter_number: 10
pdf_page: 280
section: "10.3.5 JavaScript Modules on the Web"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "module script tag"
  - "HTML module loading"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es6-module-system
extends: []
related:
  - dynamic-import
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement the module pattern in JavaScript?"
---

# Quick Definition

The HTML `<script type="module">` tag that tells the browser to treat the script as an ES6 module, enabling `import`/`export` syntax and loading the module with deferred execution.

# Core Definition

"If you want to natively use import directives in a web browser, you must tell the web browser that your code is a module by using a `<script type=\"module\">` tag" (p. 280). Module scripts are loaded with deferred execution (like the `defer` attribute), execute in strict mode, and support CORS restrictions. The `nomodule` attribute provides a fallback for older browsers.

# Prerequisites

- **es6-module-system** — Understanding ES6 modules is necessary to use module scripts

# Key Properties

1. Enables `import`/`export` syntax in browser JavaScript
2. Loaded with deferred execution by default (like `defer`)
3. Can use `async` attribute for eager execution
4. Companion `<script nomodule>` provides fallback for non-module-aware browsers
5. Cross-origin module loading requires CORS headers
6. Cannot test with `file://` URLs due to CORS restrictions

# Construction / Recognition

```html
<script type="module">import "./main.js";</script>
<script type="module" src="./app.js"></script>
<script nomodule src="./fallback-bundle.js"></script>
```

# Context & Application

Required for native ES6 module usage in browsers without a bundler. As of 2020, all modern browsers except IE support it. The `nomodule` fallback pattern enables progressive enhancement.

# Examples

From the source text (p. 280): `<script type="module">import "./main.js";</script>` is the simplest entry point for a modular program. The browser recursively loads all imported modules.

# Relationships

## Builds Upon
- **ES6 Module System** — The script tag is the browser mechanism for loading ES6 modules

## Related
- **Dynamic Import** — Can be used within module scripts for lazy loading

# Common Errors

- **Error**: Trying to export from an inline `<script type="module">` tag.
  **Correction**: While legal, there is no way to import from an inline module since it has no name or URL.

# Common Confusions

- **Confusion**: Expecting module scripts to run in the same order as regular scripts.
  **Clarification**: Module scripts are deferred by default and execute after HTML parsing is complete, in document order.

# Source Reference

Chapter 10: Modules, Section 10.3.5, pages 279-281.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — well explained
- Uncertainties: None
- Cross-reference status: Verified
