---
# === CORE IDENTIFICATION ===
concept: ESLint Editor Integrations
slug: eslint-editor-integrations

# === CLASSIFICATION ===
category: integration
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/integrations.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint integrations"
  - "ESLint editor plugins"
  - "ESLint IDE support"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint-getting-started
extends: []
related:
  - eslint-cli
  - eslint-mcp
  - eslint-integration-tutorial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which editors and IDEs have ESLint integrations?"
  - "What build tools support ESLint?"
  - "What source control integrations exist for ESLint?"
---

# Quick Definition
ESLint has community-maintained integrations for major editors (VS Code, Vim, Neovim, Emacs, Sublime Text, JetBrains IDEs), build tools (Grunt, Webpack, Rollup), command-line tools, and source control hooks.

# Core Definition
The ESLint ecosystem includes a wide range of community-maintained integrations that embed ESLint into development workflows. Editor integrations provide real-time linting feedback: VS Code uses the official ESLint Extension, Vim has ALE and Syntastic, Neovim has nvim-lspconfig and nvim-lint, Emacs uses Flycheck, Sublime Text has SublimeLinter-eslint, and JetBrains IDEs (WebStorm, IntelliJ, PhpStorm, etc.) have built-in ESLint support. Build tool plugins include grunt-eslint, eslint-webpack-plugin, and @rollup/plugin-eslint. Source control integrations support pre-commit hooks and CI aggregators like Mega-Linter. All integrations are community-maintained, not by the ESLint team.

# Prerequisites
- eslint-getting-started -- ESLint must be installed and configured for integrations to work

# Key Properties
1. **VS Code** -- ESLint Extension by dbaeumer; the most popular editor integration
2. **Vim/Neovim** -- ALE (Asynchronous Lint Engine), Syntastic, nvim-lspconfig, nvim-lint
3. **Emacs** -- Flycheck with `javascript-eslint` checker
4. **JetBrains IDEs** -- Built-in ESLint support in WebStorm, IntelliJ IDEA, PhpStorm, PyCharm, RubyMine
5. **Sublime Text** -- SublimeLinter-eslint and Build Next
6. **Webpack** -- eslint-webpack-plugin
7. **Rollup** -- @rollup/plugin-eslint
8. **Grunt** -- grunt-eslint
9. **Git hooks** -- Pre-commit hooks, overcommit, lint-staged patterns
10. **Mega-Linter** -- CI linter aggregator embedding ESLint

# Construction / Recognition
Editor integrations are typically installed via the editor's extension/plugin manager. Build tool integrations are installed via npm:
```shell
# Webpack
npm install eslint-webpack-plugin --save-dev

# Rollup
npm install @rollup/plugin-eslint --save-dev
```

# Context & Application
Editor integrations provide the most impactful developer experience improvement: real-time feedback as code is written. Build tool integrations ensure linting runs as part of the build pipeline. Source control hooks catch issues before code is committed. Together, these integrations create a multi-layered quality gate.

# Examples
From use/integrations.md:
- VS Code: Install "ESLint" extension from marketplace (dbaeumer.vscode-eslint)
- Neovim: Configure via nvim-lspconfig for LSP-based linting
- Webpack: Add `eslint-webpack-plugin` to webpack config
- Git: Pre-commit hooks that lint staged changes

# Relationships
## Builds Upon
- eslint-getting-started (integrations rely on ESLint configuration)
## Related
- eslint-cli (integrations often invoke the CLI or Node.js API)
- eslint-mcp (MCP provides AI-agent integration in editors)
- eslint-integration-tutorial (guide for building custom integrations)
## See Also
- awesome-eslint (curated list of integrations on GitHub)

# Common Errors
1. Installing ESLint globally but having plugins locally -- the integration may not find plugins
2. Not configuring the editor to use the workspace ESLint version -- may use an outdated global version

# Common Confusions
1. **Community vs official** -- All editor integrations listed in the docs are community-maintained, not by the ESLint team
2. **Extension vs configuration** -- The editor extension provides real-time feedback; the ESLint configuration file controls which rules run

# Source Reference
- use/integrations.md: Complete list of editor, build tool, CLI, and source control integrations

# Verification Notes
Directly documented with links to all integration projects. High confidence.
