---
# === CORE IDENTIFICATION ===
concept: ESLint Built-in Formatters
slug: eslint-built-in-formatters

# === CLASSIFICATION ===
category: usage
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/formatters/index.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint formatters"
  - "ESLint output formats"
  - "eslint --format"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint-cli
extends: []
related:
  - eslint-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What built-in formatters does ESLint provide?"
  - "How do I use a custom or third-party formatter?"
  - "What is the default ESLint output format?"
---

# Quick Definition
ESLint includes four built-in formatters -- `stylish` (default), `json`, `json-with-metadata`, and `html` -- and supports third-party and custom formatters via the `--format` CLI flag or the `loadFormatter()` API method.

# Core Definition
Formatters control the appearance of ESLint's linting results. The built-in options are: `stylish` (the default, human-readable console output), `json` (JSON-serialized results array), `json-with-metadata` (JSON results plus rule metadata in a `metadata` property), and `html` (visual HTML output for browser display). Formatters are selected via the `--format` / `-f` CLI flag or loaded programmatically via `eslint.loadFormatter()`. Third-party formatters are installed via npm and resolved with or without the `eslint-formatter-` prefix. Custom formatters can be loaded by file path (must contain a `/` to distinguish from names).

# Prerequisites
- eslint-cli -- Formatters are selected via CLI flags

# Key Properties
1. **stylish** -- Default formatter; human-readable, colorized console output
2. **json** -- JSON-serialized array of LintResult objects
3. **json-with-metadata** -- JSON output with `results` and `metadata` properties; metadata includes rule definitions
4. **html** -- HTML output suitable for browser display
5. **Third-party formatters** -- Installed via npm; resolved as `eslint-formatter-<name>` or by full package name
6. **Custom formatters** -- Loaded by file path (must contain `/` separator)
7. **--format flag** -- CLI option to select formatter; default is `stylish`

# Construction / Recognition
```shell
# Use built-in JSON formatter
npx eslint --format json file.js

# Use built-in HTML formatter and save
npx eslint -f html file.js > results.html

# Use npm-installed third-party formatter
npm install eslint-formatter-pretty
npx eslint -f pretty file.js

# Use custom local formatter
npx eslint -f ./customformat.js file.js

# Save output to file
npx eslint -f json file.js > results.json
```

# Context & Application
The default `stylish` formatter is used for interactive development. The `json` and `json-with-metadata` formatters are used for programmatic consumption by CI tools, dashboards, and integrations. The `html` formatter is useful for generating reports viewable in browsers. Third-party formatters like `eslint-formatter-pretty` provide enhanced terminal output.

# Examples
From use/formatters/index.md:
- `npx eslint --format json fullOfProblems.js` -- outputs JSON with messages including `ruleId`, `severity`, `line`, `column`, `message`, `fix`, `suggestions`
- `json-with-metadata` output contains both `results` (same as `json`) and `metadata` with rule information
- `html` formatter produces an iframe-embeddable HTML document

# Relationships
## Builds Upon
- eslint-cli (formatters are selected via CLI flags)
## Related
- eslint-class (formatters are loaded via `eslint.loadFormatter()`)

# Common Errors
1. Expecting the `json` formatter to include rule metadata -- use `json-with-metadata` for that
2. Forgetting to redirect output when using `-f json` -- without `> file.json`, output goes to stdout

# Common Confusions
1. **stylish vs json** -- `stylish` is human-readable; `json` is machine-readable. Both show the same data differently.
2. **json vs json-with-metadata** -- `json` contains only results; `json-with-metadata` adds a `metadata` property with rule information

# Source Reference
- use/formatters/index.md: Formatter reference with examples for all built-in formatters

# Verification Notes
Directly documented with sample output for each formatter. High confidence.
