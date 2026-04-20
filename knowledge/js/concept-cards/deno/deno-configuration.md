---
concept: Deno Configuration
slug: deno-configuration
category: configuration
subcategory: project setup
tier: foundational
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/configuration.md"
chapter_number: null
pdf_page: null
section: "deno.json and package.json"
extraction_confidence: high
aliases:
  - "deno.json"
  - "deno.jsonc"
  - "Deno configuration file"
prerequisites: []
extends: []
related:
  - deno-package-json-support
  - deno-workspaces
  - deno-linter
  - deno-formatter
contrasts_with: []
answers_questions:
  - "What is deno.json?"
  - "How do I configure a Deno project?"
  - "How does deno.json relate to package.json?"
---

# Quick Definition

`deno.json` (or `deno.jsonc`) is the central configuration file for Deno projects, controlling TypeScript compiler options, import maps, tasks, linting, formatting, permissions, and other tool settings.

# Core Definition

Deno automatically detects a `deno.json` or `deno.jsonc` file in the current working directory or parent directories. The file configures the TypeScript compiler, linter, formatter, and other Deno tools. It supports both `.json` and `.jsonc` (JSON with comments) extensions. A different configuration file can be specified using the `--config` flag.

The key fields in `deno.json` include:

- **`imports`** — an import map for mapping bare specifiers to URLs or file paths, enabling dependency management
- **`tasks`** — custom commands runnable via `deno task`, analogous to npm scripts
- **`lint`** — linter configuration including rules, include/exclude paths
- **`fmt`** — formatter configuration with style options like tabs, line width, semicolons
- **`compilerOptions`** — TypeScript compiler settings
- **`lock`** — lockfile configuration for dependency integrity
- **`nodeModulesDir`** — controls local `node_modules` directory behavior (`"none"`, `"auto"`, or `"manual"`)
- **`unstable`** — array of unstable feature flags to enable
- **`permissions`** — named permission sets usable with `-P` flag
- **`exports`** — public entry points for package consumers
- **`workspace`** — workspace member directories for monorepo setups
- **`links`** — local package overrides, similar to `npm link`

# Prerequisites

None. This is the foundational configuration mechanism for Deno projects.

# Key Properties

1. **Auto-detection**: Deno walks up the directory tree to find `deno.json` or `deno.jsonc` automatically.
2. **Import maps**: The `imports` field maps bare specifiers (e.g., `"@std/assert"`) to `jsr:`, `npm:`, or file paths.
3. **Custom path mappings**: Supports both exact specifier mappings and directory prefix mappings (e.g., `"bar/": "./some/folder/bar/"`).
4. **Include/exclude**: Most tool configurations support `include` and `exclude` arrays with glob patterns, including negated globs (`"!dist"`).
5. **Top-level exclude**: A root `exclude` array prevents Deno from processing directories across all subcommands and the LSP.
6. **Named permissions**: The `permissions` field defines reusable permission sets invoked with `--permission-set` or `-P`.
7. **JSON Schema**: A versioned schema is available for editor autocompletion.

# Construction / Recognition

A minimal `deno.json` with dependency management:

```json
{
  "imports": {
    "@std/assert": "jsr:@std/assert@^1.0.0",
    "chalk": "npm:chalk@5"
  }
}
```

A comprehensive configuration example:

```json
{
  "compilerOptions": { "allowJs": true, "strict": true },
  "imports": { "oak": "jsr:@oak/oak" },
  "tasks": { "start": "deno run --allow-read main.ts" },
  "lint": { "include": ["src/"], "rules": { "tags": ["recommended"] } },
  "fmt": { "useTabs": true, "lineWidth": 80, "singleQuote": true },
  "lock": false,
  "nodeModulesDir": "auto",
  "unstable": ["webgpu"],
  "exclude": ["dist/"]
}
```

# Context & Application

`deno.json` is the single source of truth for project-wide configuration. It replaces the need for separate `tsconfig.json`, `.eslintrc`, `.prettierrc`, and other config files common in Node.js projects. The import map in `deno.json` serves as the dependency manifest, mapping bare specifiers to registry packages (`jsr:` and `npm:` protocols) or local files.

# Examples

**Custom path mapping** (from `runtime/fundamentals/configuration.md`):
```json
{
  "imports": {
    "@/": "./"
  }
}
```
This allows `import { MyUtil } from "@/util.ts"` to resolve relative to the project root.

**Named permissions** (from `runtime/fundamentals/configuration.md`):
```json
{
  "permissions": {
    "default": { "read": true, "env": { "allow": true, "ignore": ["API_KEY"] } }
  }
}
```
Run with `deno run -P main.ts` to apply the default permission set.

# Relationships

- **Related**: `deno-package-json-support` — Node.js compatibility via package.json
- **Related**: `deno-workspaces` — multi-package monorepo configuration
- **Related**: `deno-linter` — lint rules configured in the `lint` field
- **Related**: `deno-formatter` — formatting options configured in the `fmt` field

# Common Errors

1. **Forgetting `-P` with permissions**: When `permissions` are defined in `deno.json`, `deno run` or `deno test` requires explicit `-P` or `--allow-*` flags.
2. **Confusing `imports` with Node dependencies**: The `imports` field is an import map, not a package manifest. Dependencies use `jsr:` or `npm:` protocol prefixes.
3. **Using `nodeModulesDir` in workspace members**: This setting only works at the workspace root; specifying it in members produces warnings.

# Common Confusions

- **deno.json vs tsconfig.json**: Deno uses `compilerOptions` within `deno.json` rather than a separate `tsconfig.json`. The default TypeScript configuration is recommended.
- **Import map vs package.json dependencies**: The `imports` field is an import map (bare specifier to URL/path mapping), while `package.json` `dependencies` require `deno install` to set up.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/configuration.md`, sections "Dependencies", "Tasks", "Linting", "Formatting", "Permissions", "Exports".

# Verification Notes

All fields and behaviors described are explicitly documented in the source file. Extraction confidence is high.
