---
concept: Package.json Support
slug: deno-package-json-support
category: configuration
subcategory: Node.js compatibility
tier: foundational
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/configuration.md"
chapter_number: null
pdf_page: null
section: "package.json support"
extraction_confidence: high
aliases:
  - "package.json compatibility"
  - "Node.js package.json in Deno"
prerequisites:
  - deno-configuration
extends: []
related:
  - deno-configuration
  - deno-workspaces
contrasts_with: []
answers_questions:
  - "How does deno.json relate to package.json?"
  - "Can I use package.json with Deno?"
  - "What happens when both deno.json and package.json exist?"
---

# Quick Definition

Deno supports `package.json` for compatibility with Node.js projects, allowing existing Node.js projects to run in Deno without creating a `deno.json` file.

# Core Definition

Deno natively understands `package.json` files. If you have a Node.js project, it is not necessary to create a `deno.json` file — Deno will use the `package.json` to configure the project. When both files are present in the same directory, Deno understands dependencies specified in both and uses `deno.json` for Deno-specific configurations.

The `package.json` `scripts` field is also supported, with tasks runnable via `deno task`. The `dependencies` field works as expected, though it requires running `deno install` to set up the `node_modules` directory.

# Prerequisites

- `deno-configuration` — understanding of Deno's configuration system

# Key Properties

1. **Standalone usage**: A `package.json` alone is sufficient to configure a Deno project for Node.js compatibility.
2. **Coexistence**: When both `deno.json` and `package.json` are present, Deno merges dependency information from both files.
3. **Deno-specific priority**: `deno.json` takes precedence for Deno-specific settings (lint, fmt, compilerOptions, etc.).
4. **Default node_modules behavior**: When a `package.json` exists, `nodeModulesDir` defaults to `"manual"`, meaning `deno install` or `npm install` is needed.
5. **Task compatibility**: Both `package.json` `scripts` and `deno.json` `tasks` are available through `deno task`.

# Construction / Recognition

A Node.js project that works with Deno:

```json
{
  "dependencies": {
    "express": "^1.0.0"
  },
  "scripts": {
    "dev": "vite dev",
    "build": "vite build"
  }
}
```

Using it from Deno:
```ts
import express from "express";
const app = express();
```

Note: This requires running `deno install` first.

# Context & Application

Package.json support is central to Deno's Node.js compatibility story. It allows gradual migration of existing Node.js projects to Deno without requiring a complete rewrite of the project configuration. Teams can start using Deno's toolchain (linting, formatting, testing) while retaining their existing dependency management through `package.json`.

# Examples

**Coexistence** (from `runtime/fundamentals/configuration.md`):

Both files in the same directory — `deno.json` provides imports and Deno config, `package.json` provides npm dependencies:

```json title="deno.json"
{
  "imports": { "@std/assert": "jsr:@std/assert@^1.0.0" },
  "lint": { "rules": { "tags": ["recommended"] } }
}
```

```json title="package.json"
{
  "dependencies": { "express": "^1.0.0" }
}
```

# Relationships

- **Prerequisite**: `deno-configuration` — the primary Deno configuration mechanism
- **Related**: `deno-workspaces` — workspace members can be package.json-only packages

# Common Errors

1. **Forgetting `deno install`**: Unlike `deno.json` imports which resolve automatically, `package.json` dependencies require `deno install` to populate `node_modules`.
2. **Expecting automatic node_modules**: The default `nodeModulesDir` is `"manual"` with `package.json`, so dependencies must be explicitly installed.

# Common Confusions

- **imports vs dependencies**: `deno.json` `imports` is an import map (no install step needed for jsr:/npm: specifiers), while `package.json` `dependencies` requires an install step.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/configuration.md`, section "package.json support".

# Verification Notes

Explicitly documented in the source. Extraction confidence is high.
