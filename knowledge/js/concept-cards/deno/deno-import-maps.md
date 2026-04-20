---
# === CORE IDENTIFICATION ===
concept: Import Maps
slug: deno-import-maps

# === CLASSIFICATION ===
category: modules
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/modules.md"
chapter_number: null
pdf_page: null
section: "Managing third party modules and libraries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "import map"
  - "imports field"
  - "bare specifier mapping"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ecmascript-modules
extends: []
related:
  - deno
  - jsr-registry
  - deno-npm-specifiers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Deno's module system?"
  - "How do I manage dependencies in Deno?"
---

# Quick Definition
Import maps are the `imports` field in `deno.json` that maps bare specifiers to full module URLs or registry specifiers, centralizing dependency version management based on the Import Maps Standard.

# Core Definition
The `imports` field in `deno.json` serves as an import map, based on the [Import Maps Standard](https://html.spec.whatwg.org/multipage/webappapis.html#import-maps). It allows developers to map bare specifiers (short, unqualified names) to full module URLs or registry specifiers (e.g., `jsr:`, `npm:`, `https://`). This centralizes dependency management so that version specifiers are declared once in `deno.json` rather than repeated in every import statement across the codebase.

Deno extends the standard import maps specification: when using the `imports` field in `deno.json`, you only need to specify the module specifier without a trailing `/` (the standard requires both with and without trailing `/`). The `deno add` and `deno remove` commands automatically manage entries in the import map.

# Prerequisites
- ecmascript-modules: Understanding of ESM import syntax

# Key Properties
1. **Bare specifier mapping** -- Maps short names like `"@luca/cases"` to full specifiers like `"jsr:@luca/cases@^1.0.0"`
2. **Centralized versioning** -- Version requirements declared once in `deno.json`, not repeated in source files
3. **Standards-based** -- Based on the Import Maps Standard (with Deno-specific extensions)
4. **Simplified syntax** -- In `deno.json`, trailing `/` entries are not required (unlike the raw standard)
5. **CLI management** -- `deno add` and `deno remove` commands manage import map entries
6. **Scopes support** -- The `scopes` field allows overriding specific imports for specific URL prefixes
7. **Any specifier** -- Can remap any valid specifier, not just registry packages

# Construction / Recognition
```json
// deno.json
{
  "imports": {
    "@luca/cases": "jsr:@luca/cases@^1.0.0",
    "cowsay": "npm:cowsay@^1.6.0",
    "cases": "https://deno.land/x/case/mod.ts"
  }
}
```

```ts
// main.ts (with import map)
import { camelCase } from "@luca/cases";
import { say } from "cowsay";
import { pascalCase } from "cases";
```

```sh
# Add a dependency (updates deno.json imports)
deno add jsr:@luca/cases

# Remove a dependency
deno remove @luca/cases
```

# Context & Application
Import maps are the recommended way to manage dependencies in Deno projects of any size. They replace the need for a centralized `deps.ts` file (a pattern from early Deno) and provide a standard, tooling-friendly approach to dependency management. For developers coming from Node.js, import maps serve a similar purpose to the `dependencies` field in `package.json`, but with the added flexibility of mapping to any URL or registry specifier.

The `imports` field in `deno.json` and the standalone `--import-map` flag have slightly different behaviors: `deno.json` extends the standard (no trailing `/` needed), while a standalone import map file or `importMap` reference follows the standard strictly (requiring both entries).

# Examples
From runtime/fundamentals/modules.md:
- Adding via CLI: `deno add jsr:@luca/cases` adds `"@luca/cases": "jsr:@luca/cases@^1.0.0"` to `deno.json`
- Removing: `deno remove @luca/cases` removes the entry
- Dev dependencies convention: `"@std/testing": "jsr:@std/testing@1" // dev` (comment marking)

# Relationships
## Builds Upon
- ecmascript-modules (import maps remap ESM import specifiers)

## Enables
- Centralized dependency management
- Clean import statements without version specifiers

## Related
- deno (import maps are configured in deno.json)
- jsr-registry (JSR packages are commonly mapped via import maps)
- deno-npm-specifiers (npm packages are commonly mapped via import maps)

# Common Errors
1. Using both `imports` in `deno.json` and a separate `--import-map` file without understanding their different syntax requirements
2. Forgetting to add trailing `/` entries when using a standalone import map file (not `deno.json`)

# Common Confusions
1. **deno.json vs. standalone import map** -- `deno.json` `imports` extends the standard (simpler); standalone import map files must follow the standard strictly with trailing `/` entries
2. **Import maps vs. package.json** -- Both can declare dependencies, but import maps support any URL/specifier, not just registry packages

# Source Reference
- runtime/fundamentals/modules.md, sections "Managing third party modules and libraries" and "Differentiating between imports or importMap": Import map configuration, CLI management, and standard differences

# Verification Notes
- High confidence: Import maps are explicitly described with examples and standard references
- The distinction between `deno.json` imports and standalone import maps is explicitly documented
