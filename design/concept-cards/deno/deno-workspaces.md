---
concept: Deno Workspaces
slug: deno-workspaces
category: configuration
subcategory: monorepos
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/workspaces.md"
chapter_number: null
pdf_page: null
section: "Workspaces and monorepos"
extraction_confidence: high
aliases:
  - "Deno monorepo"
  - "workspace members"
prerequisites:
  - deno-configuration
extends:
  - deno-configuration
related:
  - deno-package-json-support
  - deno-linter
  - deno-formatter
  - deno-test-runner
contrasts_with: []
answers_questions:
  - "How do I set up a Deno workspace?"
  - "How do Deno workspaces work?"
  - "Can I mix Deno and Node.js packages in a workspace?"
---

# Quick Definition

Deno workspaces manage multiple related packages in a monorepo, defined by a `workspace` array in the root `deno.json`, where each member has its own `deno.json` and/or `package.json` with a `name`, `version`, and `exports` enabling cross-member imports via bare specifiers.

# Core Definition

A Deno workspace is a collection of folders containing `deno.json` or `package.json` configuration files, defined by the root `deno.json`:

```json
{
  "workspace": ["./add", "./subtract"]
}
```

Each workspace member directory can contain:
- Only a `deno.json` (Deno-first package)
- Both a `deno.json` and `package.json` (hybrid package)
- Only a `package.json` (Node-first package)

Members are referenced across the workspace by their `name` field (e.g., `@scope/add`). The root `imports` are inherited by all members, enabling shared dependency management. Each member can override dependencies and tool configurations (lint, fmt, tasks) independently.

Key workspace behaviors:
- **Bare specifier imports**: Members import each other using `name` fields (e.g., `import { add } from "@scope/add"`)
- **Configuration inheritance**: Members inherit root `imports`, `compilerOptions`, and lint/fmt rule tags
- **Member priority**: Member configurations take priority over root for lint rules, fmt options, and tasks
- **Pattern matching**: Workspace paths support glob patterns (`"packages/*"`, `"examples/*/*"`)
- **Publishing**: Members can be published individually to JSR; workspace references are automatically replaced with registry references

# Prerequisites

- `deno-configuration` — workspaces are configured in `deno.json`

# Key Properties

1. **`workspace` vs `workspaces`**: Deno uses singular `workspace` (not npm's plural `workspaces`) representing one workspace with multiple members.
2. **Mixed ecosystems**: Deno-first and Node-first packages can coexist in a single workspace.
3. **Root-only settings**: `nodeModulesDir`, `vendor`, `lock`, `unstable`, and `workspace` can only be set at the root level.
4. **Member-only settings**: `name`, `version`, and `exports` are only valid in member configurations.
5. **Workspace protocol**: `package.json` files support `workspace:*`, `workspace:~`, and `workspace:^` specifiers for inter-package dependencies.
6. **npm/pnpm compatibility**: Standard npm and pnpm workspace configurations are supported; `pnpm-workspace.yaml` can be migrated to `deno.json`.
7. **Containerization**: When dockerizing a workspace member, the root `deno.json` and all dependent workspace packages must be included.

# Construction / Recognition

Workspace file structure:
```
/
├── deno.json          # workspace: ["./add", "./subtract"]
├── main.ts
├── add/
│   ├── deno.json      # name: "@scope/add", exports: "./mod.ts"
│   └── mod.ts
└── subtract/
    ├── deno.json      # name: "@scope/subtract", exports: "./mod.ts"
    └── mod.ts
```

Root configuration:
```json
{
  "workspace": ["./add", "./subtract"],
  "imports": { "chalk": "npm:chalk@5" }
}
```

Member configuration:
```json
{
  "name": "@scope/add",
  "version": "0.1.0",
  "exports": "./mod.ts"
}
```

# Context & Application

Workspaces enable monorepo development where multiple related packages are developed, tested, and published together. They support gradual migration from Node.js by allowing `package.json`-only members alongside Deno-first members. Commands like `deno test`, `deno fmt`, and `deno lint` run across all workspace members from the root, respecting each member's configuration.

# Examples

**Cross-member imports** (from `runtime/fundamentals/workspaces.md`):
```ts
import chalk from "chalk";             // From root imports
import { add } from "@scope/add";      // From workspace member
import { subtract } from "@scope/subtract";
```

**Workspace tasks** (from `runtime/fundamentals/workspaces.md`):
```sh
deno task --cwd=add build    # Run task in specific member
deno test                     # Run tests across all members
deno fmt                      # Format all members
```

**Multiple exports** (from `runtime/fundamentals/workspaces.md`):
```json
{
  "exports": {
    ".": "./mod.ts",
    "./foo": "./foo.ts",
    "./other": "./dir/other.ts"
  }
}
```

# Relationships

- **Extends**: `deno-configuration` — workspaces are a `deno.json` feature
- **Related**: `deno-package-json-support` — members can be `package.json`-only
- **Related**: `deno-linter`, `deno-formatter`, `deno-test-runner` — all run across workspace members

# Common Errors

1. **Setting `nodeModulesDir` in members**: This is a root-only setting and will produce warnings in member configs.
2. **Nested workspaces**: Not supported — only the root can define a `workspace` field.
3. **Missing workspace member in Docker**: When containerizing, forgetting to include the root `deno.json` or dependent members breaks workspace resolution.

# Common Confusions

- **`workspace` (Deno) vs `workspaces` (npm)**: Deno's field is singular, representing one workspace; npm's is plural, listing member patterns.
- **Member dependency resolution**: Member-specific dependencies are scoped to that member's folder only. Outside member folders, the root import map is used.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/workspaces.md`, all sections.

# Verification Notes

All features described are explicitly documented in the source file. Extraction confidence is high.
