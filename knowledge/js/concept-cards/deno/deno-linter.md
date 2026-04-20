---
concept: Deno Linter
slug: deno-linter
category: toolchain
subcategory: code quality
tier: foundational
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/linting_and_formatting.md"
chapter_number: null
pdf_page: null
section: "Linting"
extraction_confidence: high
aliases:
  - "deno lint"
  - "Deno built-in linter"
prerequisites:
  - deno-configuration
extends: []
related:
  - deno-formatter
  - deno-lint-plugins
  - deno-test-runner
contrasts_with: []
answers_questions:
  - "What is Deno's built-in linter?"
  - "How do I lint code in Deno?"
---

# Quick Definition

`deno lint` is Deno's built-in linter that analyzes TypeScript and JavaScript code for potential errors, bugs, and stylistic issues using a recommended set of rules derived from ESLint — requiring no external dependencies or configuration.

# Core Definition

Deno ships with a fast, built-in linter invoked via the `deno lint` command. It supports a recommended set of rules from ESLint and provides comprehensive feedback on code quality, identifying syntax errors, enforcing coding conventions, and highlighting potential bugs.

By default, `deno lint` analyzes all TypeScript and JavaScript files in the current directory and subdirectories. Specific files or directories can be passed as arguments. The linter is configured through the `lint` field in `deno.json`, where you can specify:

- **`include`/`exclude`**: Paths and glob patterns for file selection
- **`rules.tags`**: Rule sets to apply (e.g., `["recommended"]`)
- **`rules.include`**: Additional rules to enable (e.g., `"ban-untagged-todo"`)
- **`rules.exclude`**: Rules to disable (e.g., `"no-unused-vars"`)
- **`plugins`**: Custom lint plugin modules

# Prerequisites

- `deno-configuration` — linter settings are defined in `deno.json`

# Key Properties

1. **Zero dependency**: Built into the Deno runtime; no npm packages or configuration files needed.
2. **ESLint-derived rules**: Uses recommended rules from ESLint for comprehensive code analysis.
3. **Fast and performant**: Integrated directly into the runtime for speed.
4. **Configurable**: Rules, include/exclude paths, and plugins all configurable in `deno.json`.
5. **Extensible**: Supports custom lint plugins for project-specific rules.
6. **Workspace-aware**: In workspaces, lint rules merge between root and members, with member settings taking priority.

# Construction / Recognition

Basic usage:
```sh
deno lint          # Lint all files
deno lint src/     # Lint specific directory
```

Configuration in `deno.json`:
```json
{
  "lint": {
    "include": ["src/"],
    "exclude": ["src/testdata/"],
    "rules": {
      "tags": ["recommended"],
      "include": ["ban-untagged-todo"],
      "exclude": ["no-unused-vars"]
    }
  }
}
```

# Context & Application

The built-in linter eliminates the need to install and configure ESLint separately for Deno projects. It integrates with CI pipelines and IDE extensions. For projects needing ESLint specifically (e.g., for ecosystem plugin compatibility), Deno also supports running ESLint via `deno run -A npm:eslint`.

# Examples

**CI integration** (from `runtime/fundamentals/linting_and_formatting.md`):

ESLint can also be used with Deno when needed:
```sh
deno run -A npm:eslint .
```

Or as a task in `deno.json`:
```json
{
  "tasks": { "eslint": "eslint . --ext .ts,.js" }
}
```

# Relationships

- **Related**: `deno-formatter` — complementary code quality tool
- **Related**: `deno-lint-plugins` — extends the linter with custom rules
- **Related**: `deno-configuration` — lint settings defined in `deno.json`

# Common Errors

1. **Forgetting to configure rules**: Without `rules.tags: ["recommended"]`, the default recommended rules still apply, but custom rule additions require explicit `rules.include`.

# Common Confusions

- **deno lint vs ESLint**: `deno lint` is a separate linter that ships with Deno and supports a recommended ESLint rule set. It is not ESLint itself and does not support all ESLint plugins directly (use lint plugins or run ESLint via npm for that).

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/linting_and_formatting.md`, section "Linting".

# Verification Notes

All features described are explicitly documented in the source file. Extraction confidence is high.
