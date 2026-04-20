---
concept: Default Import
slug: default-import
category: modules
subcategory: imports
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.7 Default exports and default imports"
extraction_confidence: high
aliases:
  - "import default"
prerequisites:
  - default-export
extends: []
related:
  - named-import
contrasts_with:
  - named-import
answers_questions:
  - "How do I import a default export?"
---

# Quick Definition

A default import uses syntax without curly braces (`import name from './module.mjs'`) to import the single default export of a module, with the importer choosing the local binding name.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, the default import syntax is `import name from './module.mjs'`. The syntactic difference from named imports is notable: no curly braces around the name, indicating we're importing "the module" rather than reaching into it. Internally, the default import accesses the named export `default`.

# Prerequisites

- Default export

# Key Properties

1. Syntax: `import name from './module.mjs'` (no curly braces).
2. Importer chooses the binding name.
3. Internally accesses the `default` named export.
4. Can also be accessed via `import { default as name } from './module.mjs'`.

# Construction / Recognition

```js
import myFunc from './my-func.mjs';
```

# Context & Application

Use when importing from modules that have a single primary export (a function or class).

# Examples

From the source text (Ch. 29, section 29.1.3):

```js
import myFunc from './my-func.mjs';
assert.equal(myFunc(), 'Hello!');
```

# Relationships

## Builds Upon
- **Default Export** -- imports the default export

## Contrasts With
- **Named Import** -- named uses curly braces; default does not

# Common Confusions

- **Confusion**: Thinking the import name must match the export name.
  **Clarification**: Default imports choose any name; they're not bound to the export's name.

# Source Reference

Chapter 29: Modules, Section 29.7, lines 872-920.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit syntax with visual distinction
- Cross-reference status: verified
