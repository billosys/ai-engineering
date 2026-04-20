---
concept: Deno Formatter
slug: deno-formatter
category: toolchain
subcategory: code quality
tier: foundational
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/linting_and_formatting.md"
chapter_number: null
pdf_page: null
section: "Formatting"
extraction_confidence: high
aliases:
  - "deno fmt"
  - "Deno built-in formatter"
  - "dprint"
prerequisites:
  - deno-configuration
extends: []
related:
  - deno-linter
  - deno-configuration
contrasts_with: []
answers_questions:
  - "What is Deno's built-in formatter?"
  - "How do I format code in Deno?"
---

# Quick Definition

`deno fmt` is Deno's built-in opinionated code formatter, powered by the dprint engine, that automatically formats TypeScript, JavaScript, JSON, and markdown files to ensure consistent code style across a project.

# Core Definition

Deno includes a built-in formatter invoked via `deno fmt`. It uses the dprint engine to enforce consistent code style. By default, it formats all TypeScript and JavaScript files in the current directory and subdirectories. The formatter is opinionated but configurable through the `fmt` field in `deno.json`.

Configurable options include:

- **`useTabs`** — tabs vs spaces (default: `false`)
- **`indentWidth`** — indentation width (default: `2`)
- **`lineWidth`** — maximum line width (default: `80`)
- **`semiColons`** — whether to use semicolons (default: `true`)
- **`singleQuote`** — single vs double quotes (default: `false`)
- **`proseWrap`** — prose wrapping mode: `"always"`, `"never"`, or `"preserve"` (default: `"always"`)
- **`trailingCommas`** — trailing commas: `"always"` or `"never"` (default: `"always"`)
- **`include`/`exclude`** — file selection paths and globs

Additional options control JSX bracket positions, brace positions, control flow positioning, quote properties, and more.

# Prerequisites

- `deno-configuration` — formatter settings are defined in `deno.json`

# Key Properties

1. **dprint engine**: Uses the dprint formatting engine for speed and consistency.
2. **Opinionated with escape hatches**: Provides sensible defaults but allows configuration for most style preferences.
3. **Check mode**: `deno fmt --check` verifies formatting without modifying files, suitable for CI pipelines.
4. **Multi-format support**: Formats TypeScript, JavaScript, JSON, markdown, and (experimentally) Svelte, Vue, Astro, Angular, and SQL files.
5. **Workspace-aware**: In workspaces, each member can have its own formatting configuration; member settings take priority over root.
6. **VS Code integration**: Works as the default formatter in VS Code via the Deno extension.

# Construction / Recognition

Basic usage:
```sh
deno fmt              # Format all files
deno fmt src/         # Format specific directory
deno fmt --check      # Check without modifying (for CI)
```

Configuration in `deno.json`:
```json
{
  "fmt": {
    "useTabs": true,
    "lineWidth": 80,
    "indentWidth": 4,
    "semiColons": true,
    "singleQuote": true,
    "proseWrap": "preserve",
    "include": ["src/"],
    "exclude": ["src/testdata/"]
  }
}
```

# Context & Application

The built-in formatter removes the need for Prettier or other formatting tools in Deno projects. It integrates directly into CI pipelines via `deno fmt --check` and into editors via the VS Code Deno extension. For teams that prefer Prettier, it can still be used alongside Deno.

# Examples

**CI pipeline** (from `runtime/fundamentals/linting_and_formatting.md`):
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: denoland/setup-deno@v2
        with:
          deno-version: v2.x
      - run: deno fmt --check
```

# Relationships

- **Related**: `deno-linter` — complementary code quality tool
- **Related**: `deno-configuration` — formatting options defined in `deno.json`

# Common Errors

1. **Expecting Prettier compatibility**: `deno fmt` uses dprint, not Prettier. Output may differ from Prettier for the same configuration.

# Common Confusions

- **deno fmt vs Prettier**: `deno fmt` is built on dprint, not Prettier. While it shares similar concepts (opinionated formatting), the specific output and configuration options differ.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/linting_and_formatting.md`, section "Formatting".

# Verification Notes

All options and behaviors described are explicitly documented in the source file. Extraction confidence is high.
