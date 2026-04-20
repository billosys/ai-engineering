---
# === CORE IDENTIFICATION ===
concept: ESLint CLI
slug: eslint-cli

# === CLASSIFICATION ===
category: cli
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/command-line-interface.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "eslint command line"
  - "eslint command-line interface"
  - "npx eslint"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - eslint-getting-started
  - eslint-built-in-formatters
  - eslint-node-api
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I run ESLint from the command line?"
  - "What are the key CLI flags for fixing, caching, and output?"
  - "What exit codes does ESLint return?"
---

# Quick Definition
The ESLint Command Line Interface (CLI) executes linting from the terminal, providing flags for configuration, auto-fixing, caching, output formatting, suppression management, and concurrency control.

# Core Definition
The ESLint CLI is invoked via `npx eslint [options] [file|dir|glob]*` (or equivalent pnpm/yarn commands). It organizes its options into logical groups: basic configuration (`-c`, `--no-config-lookup`, `--inspect-config`, `--ext`, `--global`, `--parser`), rules and plugins (`--plugin`, `--rule`), fix problems (`--fix`, `--fix-dry-run`, `--fix-type`), ignore files (`--no-ignore`, `--ignore-pattern`), stdin (`--stdin`, `--stdin-filename`), warnings (`--quiet`, `--max-warnings`), output (`-o`, `-f`, `--color`), inline config comments (`--no-inline-config`, `--report-unused-disable-directives`), caching (`--cache`, `--cache-location`, `--cache-strategy`), suppressing violations (`--suppress-all`, `--suppress-rule`, `--prune-suppressions`), and miscellaneous (`--init`, `--debug`, `--stats`, `--flag`, `--mcp`, `--concurrency`).

# Prerequisites
Foundational concept with no prerequisites beyond Node.js installation.

# Key Properties
1. **--fix** -- Automatically fixes as many issues as possible, writing changes to files; throws an error on piped code
2. **--fix-type** -- Restricts fix types: `problem`, `suggestion`, `layout`, `directive`
3. **--cache** -- Only checks changed files, dramatically improving performance; stored in `.eslintcache` by default
4. **--cache-strategy** -- `metadata` (default) or `content`; content is useful after git operations that reset modification times
5. **--format / -f** -- Selects output format; default is `stylish`; supports built-in, npm-installed, and local custom formatters
6. **--quiet** -- Reports errors only, suppressing warnings
7. **--max-warnings** -- Sets a warning threshold; exceeding it causes a nonzero exit code
8. **--suppress-all / --suppress-rule** -- Suppresses existing violations to `eslint-suppressions.json`, reporting only new violations in subsequent runs
9. **--concurrency** -- Controls worker thread count (`off`, `auto`, or integer); default is `off` (main thread only)
10. **Exit codes** -- `0` (success), `1` (lint errors or warnings exceeded threshold), `2` (configuration problem or internal error)

# Construction / Recognition
```shell
# Basic linting
npx eslint file.js

# Auto-fix with specific fix types
npx eslint --fix --fix-type suggestion,problem .

# Cached linting with content strategy
npx eslint --cache --cache-strategy content "src/**/*.js"

# Output JSON to file
npx eslint -f json file.js > results.json

# Suppress all existing violations
npx eslint "src/**/*.js" --suppress-all

# Multi-threaded linting
npx eslint --concurrency auto
```

# Context & Application
The CLI is the primary interface for most ESLint users, used in local development, CI pipelines, and git hooks. The `--fix` flag enables auto-formatting workflows. The `--cache` flag is critical for large codebases where re-linting unchanged files wastes time. The suppression system (`--suppress-all`, `--suppress-rule`, `--prune-suppressions`) enables gradual adoption of new rules without being overwhelmed by legacy violations.

# Examples
From use/command-line-interface.md:
- `npx eslint --fix file.js` -- auto-fix a single file
- `npx eslint --max-warnings 10 file.js` -- fail if more than 10 warnings
- `npx eslint --stdin --fix-dry-run --format json` -- fix stdin code without writing, output as JSON
- `npx eslint --init` -- run the configuration initialization wizard
- `npx eslint --print-config file.js` -- output the resolved configuration for a file

# Relationships
## Builds Upon
None -- this is a foundational concept.
## Enables
- eslint-getting-started (CLI is the primary way to run ESLint)
- eslint-built-in-formatters (selected via `--format` flag)
## Related
- eslint-node-api (programmatic alternative to the CLI)
- eslint-mcp (started via `--mcp` flag)
## Contrasts With
None.

# Common Errors
1. Using `--fix` with piped input -- `--fix` throws an error on stdin; use `--fix-dry-run` instead
2. Forgetting `--cache-location` when using `--cache` in CI -- the default `.eslintcache` may be lost between runs

# Common Confusions
1. **--fix vs --fix-dry-run** -- `--fix` writes changes to files; `--fix-dry-run` computes fixes without writing, useful for integrations and stdin
2. **--fix-type categories** -- `problem` (potential errors), `suggestion` (improvements), `layout` (formatting), `directive` (inline directives)
3. **Exit code 1 vs 2** -- `1` means lint errors were found; `2` means a configuration or internal error occurred

# Source Reference
- use/command-line-interface.md: Complete CLI reference with all options, examples, and exit codes

# Verification Notes
Directly documented with exhaustive option reference. High confidence.
