---
# === CORE IDENTIFICATION ===
concept: import.meta.url
slug: import-meta-url

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
pdf_page: 283
section: "10.3.7 import.meta.url"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "module metadata"
  - "import.meta"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es6-module-system
extends: []
related:
  - url-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

A special property available within ES6 modules that provides the URL from which the current module was loaded, enabling modules to reference resources relative to their own location.

# Core Definition

"Within an ES6 module, the special syntax import.meta refers to an object that contains metadata about the currently executing module. The url property of this object is the URL from which the module was loaded" (p. 283). In Node, this will be a `file://` URL.

# Prerequisites

- **es6-module-system** — import.meta is only available within ES6 modules

# Key Properties

1. Only available inside ES6 modules (not regular scripts or CommonJS modules)
2. `import.meta.url` gives the URL of the current module
3. In Node.js, the URL uses the `file://` protocol
4. Useful for resolving relative paths to resources (images, data files, localization files)

# Construction / Recognition

```js
function localStringsURL(locale) {
    return new URL(`l10n/${locale}.json`, import.meta.url);
}
```

# Context & Application

Primary use case is referencing resources stored relative to the module file. Combined with the URL constructor, it provides portable path resolution across browsers and Node.

# Examples

From the source text (p. 283): A module that loads localization files from a relative `l10n/` directory uses `new URL(\`l10n/${locale}.json\`, import.meta.url)` to resolve the path relative to the module's own location.

# Relationships

## Builds Upon
- **ES6 Module System** — Only available within ES6 modules

## Related
- **URL Class** — Commonly used with import.meta.url for path resolution

# Common Errors

- **Error**: Trying to use `import.meta` in a regular `<script>` tag or CommonJS module.
  **Correction**: `import.meta` is only defined inside ES6 modules. Use `__dirname` in Node CommonJS modules instead.

# Common Confusions

- **Confusion**: Thinking `import.meta.url` returns a string path like `__dirname`.
  **Clarification**: It returns a URL string (e.g., `file:///path/to/module.js`), not a filesystem path. Use the URL constructor to resolve relative paths.

# Source Reference

Chapter 10: Modules, Section 10.3.7, pages 283.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
