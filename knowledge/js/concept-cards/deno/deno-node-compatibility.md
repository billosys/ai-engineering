---
# === CORE IDENTIFICATION ===
concept: Node.js Compatibility
slug: deno-node-compatibility

# === CLASSIFICATION ===
category: compatibility
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/node.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Node.js compat"
  - "Node compatibility"
  - "npm compatibility"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - deno-npm-specifiers
  - ecmascript-modules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Deno relate to Node.js?"
  - "How do I use npm packages in Deno?"
  - "What distinguishes Deno from Node.js?"
---

# Quick Definition
Deno is Node-compatible: most Node.js projects run with little or no change, npm packages work via `npm:` specifiers, Node built-in APIs are available via `node:` specifiers, and CommonJS is supported.

# Core Definition
Deno provides a comprehensive compatibility layer for running Node.js code and consuming npm packages. This compatibility has three main pillars:

1. **npm package support** -- Deno natively imports npm packages using `npm:` specifiers (e.g., `import chalk from "npm:chalk@5"`). No `npm install` is needed; packages are resolved from a global cache.
2. **Node built-in API support** -- Node.js built-in modules (fs, path, os, etc.) are available via `node:` specifiers (e.g., `import path from "node:path"`).
3. **CommonJS support** -- Deno runs `.cjs` files directly and supports `require()` via the `.cjs` extension, the `"type": "commonjs"` field in `package.json`, or `createRequire` from `node:module`.

Deno also understands `package.json` for declaring dependencies, running scripts via `deno task`, and resolving module types.

# Prerequisites
- deno: Understanding of Deno as a runtime

# Key Properties
1. **npm: specifiers** -- Import npm packages directly: `import { Hono } from "npm:hono"`
2. **node: specifiers** -- Access Node built-in modules: `import * as os from "node:os"`
3. **No npm install needed** -- Dependencies resolve from Deno's global cache by default
4. **CommonJS via .cjs** -- Files with `.cjs` extension are treated as CommonJS
5. **package.json support** -- First-class support for dependencies, scripts, and type field
6. **Node globals** -- `process` is available globally (with lint warnings recommending explicit import)
7. **Conditional exports** -- Resolves with conditions `["deno", "node", "import", "default"]`
8. **node_modules modes** -- Three modes: none (default), auto, and manual
9. **Node-API addons** -- Supported with `--allow-ffi` when a local `node_modules` is present

# Construction / Recognition
```ts
// Import npm package
import chalk from "npm:chalk@5";

// Use Node built-in
import path from "node:path";

// CommonJS file (main.cjs)
const express = require("express");
```

Migration from Node.js typically requires:
1. Adding `node:` prefix to built-in module imports
2. Importing `Buffer` explicitly from `node:buffer`
3. Using `.cjs` extension or `createRequire` for CommonJS code

# Context & Application
Node.js compatibility is critical for Deno's adoption, as it allows developers to migrate existing projects incrementally and use the vast npm ecosystem. Most Node.js projects run in Deno with minimal changes, primarily adding `node:` prefixes to built-in imports. Deno provides helpful error messages and lint rules that guide developers through the migration.

The `node_modules` directory is not created by default (Deno uses a global cache), but can be enabled via `"nodeModulesDir": "auto"` or `"nodeModulesDir": "manual"` in `deno.json` for frameworks and tools that expect it.

# Examples
From runtime/fundamentals/node.md:
- npm import: `import * as emoji from "npm:node-emoji";` runs with `deno run main.js` (no npm install)
- Node built-in: `import * as os from "node:os"; console.log(os.cpus());` produces the same output as Node.js
- Node-to-Deno cheatsheet includes: `node file.js` -> `deno file.js`, `ts-node file.ts` -> `deno file.ts`, `npm run` -> `deno task`, `eslint` -> `deno lint`, `prettier` -> `deno fmt`

# Relationships
## Builds Upon
- deno (compatibility layer is built into the runtime)

## Enables
- Migration of existing Node.js projects to Deno
- Access to the npm ecosystem from Deno

## Related
- deno-npm-specifiers (the specific mechanism for importing npm packages)
- ecmascript-modules (Deno's default module system)

## Contrasts With
- Node.js (Deno is compatible but architecturally different: secure by default, ESM-first, built-in toolchain)

# Common Errors
1. Importing Node built-ins without `node:` prefix -- Deno requires the `node:` prefix and provides helpful error messages
2. Expecting `node_modules` by default -- Deno uses a global cache; set `nodeModulesDir` in `deno.json` if needed
3. Using `Buffer` without importing -- Must import from `node:buffer` explicitly

# Common Confusions
1. **require() availability** -- `require()` works in `.cjs` files and via `createRequire`, but is not available in ESM files by default
2. **__filename and __dirname** -- Not available in Deno; use `import.meta.filename` and `import.meta.dirname` instead
3. **Full compatibility vs. identical behavior** -- Deno is compatible with most Node.js code but is not a drop-in replacement; the permission system still applies

# Source Reference
- runtime/fundamentals/node.md: Comprehensive guide to Node.js and npm compatibility, CommonJS support, migration, and cheatsheet

# Verification Notes
- High confidence: Compatibility features are explicitly documented with extensive examples
- Cheatsheet provides a clear mapping of Node.js to Deno equivalents
