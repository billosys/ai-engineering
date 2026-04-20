---
# === CORE IDENTIFICATION ===
concept: Debugging Configuration
slug: debugging-configuration

# === CLASSIFICATION ===
category: configuration
subcategory: debugging
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/debug.md"
chapter_number: null
pdf_page: null
section: "Debug Your Configuration"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - debug config
  - config inspector
  - print-config
  - eslint debug mode

# === TYPED RELATIONSHIPS ===
prerequisites:
  - configuration-objects
  - combining-configurations
extends: []
related:
  - define-config-helper
  - file-ignoring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I debug why ESLint isn't applying rules as expected?"
  - "How do I see the final calculated configuration for a file?"
  - "What is the ESLint config inspector?"
  - "How do I find which config file ESLint is loading?"
---

# Quick Definition
ESLint provides three debugging tools for configuration issues: `--debug` mode (identifies which config file is loaded), `--print-config` (outputs the calculated config for a specific file as JSON), and `--inspect-config` (launches an interactive config inspector UI).

# Core Definition
As ESLint configurations grow in complexity through multiple config objects, plugins, and extends, debugging why a file is or isn't linted as expected becomes necessary. ESLint offers three levels of debugging: (1) `--debug` flag outputs internal debug logs including which config file was found and loaded; (2) `--print-config <file>` outputs the final merged configuration for a specific file as JSON, showing the resolved `rules`, `languageOptions`, `linterOptions`, and `plugins` (but not `files`, `ignores`, or `name` since those are used only during calculation); (3) `--inspect-config` launches the `@eslint/config-inspector` web UI where you can test which config objects match any filename and see deprecated rules and usage statistics.

# Prerequisites
- configuration-objects (need to understand what you're debugging)
- combining-configurations (debugging often involves merged configs)

# Key Properties
1. `--debug`: shows which config file is loaded, useful for multi-config-file projects
2. `--print-config file.js`: outputs resolved JSON config for a specific file
3. `--inspect-config`: launches interactive web-based config inspector
4. `--print-config` output omits `files`, `ignores`, `name` (used only during calculation)
5. `--print-config` output includes default ESLint-applied configuration
6. Config inspector shows deprecated rules and available rule usage statistics

# Construction / Recognition
Find which config file is loaded:
```bash
npx eslint --debug file.js
# Look for: "Loading config from /path/to/eslint.config.js"
```

See calculated config for a file:
```bash
npx eslint --print-config file.js
```

Launch interactive inspector:
```bash
npx eslint --inspect-config
```

# Context & Application
Debugging tools are essential when inheriting configurations from multiple plugins and shareable configs, when rules seem to apply unexpectedly or not at all, or when working in monorepos where multiple config files may exist. The config inspector is particularly useful for understanding which config objects match specific file patterns.

# Examples
From `use/configure/debug.md`: The `--print-config` output shows the resolved state:
```json
{
  "linterOptions": { "reportUnusedDisableDirectives": 1 },
  "language": "@/js",
  "languageOptions": { "sourceType": "module", "ecmaVersion": "latest" },
  "plugins": ["@"],
  "rules": { "prefer-const": 2 }
}
```

From `use/configure/debug.md`: The `--debug` output shows the config file resolution path, useful when ESLint searches up ancestor directories in monorepos.

# Relationships
## Builds Upon
- configuration-objects (the objects being debugged)
- combining-configurations (merged configs are what you inspect)

## Enables
- Troubleshooting misconfigured rules, wrong file targeting, or parser issues

## Related
- define-config-helper (config object `name` property aids inspector readability)
- file-ignoring (debugging why files are ignored)

# Common Errors
1. Not redirecting `--debug` output to a file (it generates a lot of output)
2. Forgetting that `--print-config` requires a specific file argument
3. Expecting `files` and `ignores` to appear in `--print-config` output (they are omitted)

# Common Confusions
1. Thinking `--print-config` shows the raw config file content (it shows the calculated/merged result)
2. Not realizing `--inspect-config` installs `@eslint/config-inspector` on first use

# Source Reference
- `sources-md/eslint/use/configure/debug.md`, all sections

# Verification Notes
Extracted from the debugging configuration documentation. All three tools and their use cases verified against source.
