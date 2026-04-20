---
# === CORE IDENTIFICATION ===
concept: Getting Started with ESLint
slug: eslint-getting-started

# === CLASSIFICATION ===
category: usage
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/getting-started.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint setup"
  - "ESLint installation"
  - "ESLint quick start"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - eslint-cli
  - eslint-editor-integrations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I install and configure ESLint for the first time?"
  - "What are the prerequisites for running ESLint?"
  - "How do I manually set up ESLint vs using the init wizard?"
---

# Quick Definition
ESLint setup involves installing the package, generating a configuration file (`eslint.config.js`) via `npm init @eslint/config` or manually, defining rules, and running the linter on target files.

# Core Definition
ESLint requires Node.js (`^20.19.0`, `^22.13.0`, or `>=24`) with SSL support. The quickest path is `npm init @eslint/config@latest`, which runs an interactive wizard to create an `eslint.config.js` file. The wizard asks about code environment (browser/node), and optionally accepts a `--config` flag for a specific shareable config. The resulting configuration uses `defineConfig()` from `eslint/config`, imports `@eslint/js` for recommended rules, and defines file patterns, plugins, and rule overrides. Rules use three severity levels: `"off"` (0), `"warn"` (1), and `"error"` (2). After configuration, linting is run via `npx eslint [files]`. Manual setup is also supported by installing `eslint` and `@eslint/js` as dev dependencies and creating the config file by hand.

# Prerequisites
Foundational concept with no prerequisites beyond Node.js.

# Key Properties
1. **npm init @eslint/config** -- Interactive wizard that generates `eslint.config.js`; requires an existing `package.json`
2. **defineConfig()** -- Helper from `eslint/config` for type-safe configuration
3. **@eslint/js recommended** -- The `"js/recommended"` config enables all rules marked as recommended
4. **Rule severity levels** -- `"off"` / `0`, `"warn"` / `1` (no exit code impact), `"error"` / `2` (exit code 1)
5. **Flat config** -- ESLint 9+ uses `eslint.config.js` (flat config) by default, replacing `.eslintrc`
6. **Global install not recommended** -- Plugins and shareable configs must be installed locally regardless
7. **pnpm compatibility** -- Requires `.npmrc` with `auto-install-peers=true` and `node-linker=hoisted`

# Construction / Recognition
```shell
# Quick start with wizard
npm init @eslint/config@latest

# With specific shareable config
npm init @eslint/config@latest -- --config eslint-config-xo

# Manual setup
npm install eslint@latest @eslint/js@latest --save-dev
touch eslint.config.js
```

Example configuration:
```js
import { defineConfig } from "eslint/config";
import js from "@eslint/js";

export default defineConfig([
  {
    files: ["**/*.js"],
    plugins: { js },
    extends: ["js/recommended"],
    rules: {
      "no-unused-vars": "warn",
      "no-undef": "warn",
    },
  },
]);
```

# Context & Application
This is the entry point for all ESLint users. The wizard-based approach gets teams linting quickly, while manual setup offers full control. After initial configuration, users typically extend with plugins (TypeScript, React, etc.), editor integrations, and CI pipeline hooks.

# Examples
From use/getting-started.md:
- `npm init @eslint/config@latest` -- runs the interactive setup wizard
- `npx eslint yourfile.js` -- lint a single file after setup
- `npx eslint project-dir/ file.js` -- lint a directory and file

# Relationships
## Builds Upon
None -- this is the starting point for ESLint usage.
## Enables
- eslint-cli (once configured, the CLI is the primary runtime)
- eslint-editor-integrations (editors use the same configuration)
## Related
- eslint-cli (the `--init` flag also triggers the wizard)

# Common Errors
1. Running `npm init @eslint/config` without an existing `package.json` -- the wizard requires it
2. Global install confusion -- installing ESLint globally does not install plugins/configs globally; local install is recommended

# Common Confusions
1. **Flat config vs legacy** -- ESLint 9+ uses `eslint.config.js` by default; users migrating from older versions need the migration guide
2. **extends vs plugins** -- `extends` applies a preset config; `plugins` makes rules available but does not enable them

# Source Reference
- use/getting-started.md: Complete getting started guide with prerequisites, quick start, and manual setup

# Verification Notes
Directly documented with step-by-step instructions. High confidence.
