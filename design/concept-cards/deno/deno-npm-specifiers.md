---
# === CORE IDENTIFICATION ===
concept: npm Specifiers
slug: deno-npm-specifiers

# === CLASSIFICATION ===
category: modules
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/node.md"
chapter_number: null
pdf_page: null
section: "Using npm packages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "npm: specifier"
  - "npm: prefix"
  - "npm: import"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
  - ecmascript-modules
extends: []
related:
  - deno-node-compatibility
  - jsr-registry
  - deno-import-maps
contrasts_with:
  - jsr-registry

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use npm packages in Deno?"
  - "What distinguishes jsr: from npm: specifiers?"
---

# Quick Definition
The `npm:` specifier is Deno's mechanism for importing npm packages directly in import statements, with the format `npm:<package-name>[@<version>][/<sub-path>]`, requiring no prior installation.

# Core Definition
npm specifiers allow Deno programs to import npm packages directly using a special URL-like prefix. The format is `npm:<package-name>[@<version-requirement>][/<sub-path>]`. When Deno encounters an `npm:` specifier, it resolves and downloads the package from the npm registry, caches it globally, and makes it available to the program -- all without requiring a prior `npm install` step or creating a `node_modules` directory. Packages imported via `npm:` specifiers are subject to Deno's permission system.

# Prerequisites
- deno: Understanding of Deno as a runtime
- ecmascript-modules: Understanding of ESM import syntax

# Key Properties
1. **No install step** -- No `npm install` is necessary; packages are resolved on demand
2. **No node_modules by default** -- Dependencies are cached globally, not in a local directory
3. **Version specifiers** -- Support semver ranges: `npm:chalk@5`, `npm:chalk@^5.0.0`
4. **Sub-path imports** -- Access specific exports: `npm:cowsay@1.5.0/cowthink`
5. **Binary execution** -- Can run npm CLI tools directly: `deno run -A npm:create-next-app@latest`
6. **Subject to permissions** -- npm packages are sandboxed by Deno's permission system
7. **Import map compatible** -- Can be mapped to bare specifiers via the `imports` field in `deno.json`

# Construction / Recognition
```ts
// Direct import with version
import chalk from "npm:chalk@5";

// Import with sub-path
import { say } from "npm:cowsay@1.6.0";

// In deno.json import map
// { "imports": { "@mycompany/package": "npm:@mycompany/package@1.0.0" } }
```

```sh
# Run npm binary directly
deno run -A npm:create-next-app@latest

# Specifier format
npm:<package-name>[@<version-requirement>][/<sub-path>]
```

# Context & Application
npm specifiers are Deno's primary mechanism for accessing the npm ecosystem without adopting Node.js's dependency management workflow. They enable a zero-install development experience where dependencies are resolved and cached transparently. For larger projects, npm specifiers are typically mapped to bare specifiers in the `imports` field of `deno.json` to centralize version management.

npm specifiers also serve as an alternative to `npx`, allowing direct execution of npm CLI tools without global installation.

# Examples
From runtime/fundamentals/node.md:
- Basic import: `import * as emoji from "npm:node-emoji";` followed by `deno run main.js` outputs emoji
- Running binaries: `deno run --allow-read npm:cowsay@1.5.0 "Hello there!"` displays ASCII art
- Sub-path binary: `deno run --allow-read npm:cowsay@1.5.0/cowthink "What to eat?"` runs a different binary from the same package

# Relationships
## Builds Upon
- deno (npm specifiers are a built-in Deno feature)
- ecmascript-modules (npm specifiers are used within ESM import syntax)

## Related
- deno-node-compatibility (npm specifiers are part of the broader Node compatibility story)
- deno-import-maps (npm specifiers can be mapped to bare specifiers)

## Contrasts With
- jsr-registry / `jsr:` specifiers (JSR is Deno's preferred registry; `npm:` is for the npm ecosystem)
- Traditional `npm install` workflow (Deno does not require a prior install step)

# Common Errors
1. Running `npm install` before using `npm:` specifiers -- this is unnecessary; Deno resolves packages automatically
2. Expecting `node_modules` to exist -- Deno caches packages globally by default

# Common Confusions
1. **npm: vs. jsr:** -- `npm:` imports from the npm registry; `jsr:` imports from the JavaScript Registry (JSR). Deno recommends JSR for new projects
2. **npm: vs. bare specifiers** -- `npm:chalk` is a direct npm specifier; `"chalk"` as a bare specifier requires an import map entry in `deno.json`

# Source Reference
- runtime/fundamentals/node.md, sections "Using npm packages" and "Run npm binaries": Format specification, examples, and binary execution

# Verification Notes
- High confidence: npm specifier format and behavior are explicitly documented with examples
- Format string `npm:<package-name>[@<version-requirement>][/<sub-path>]` taken directly from source
