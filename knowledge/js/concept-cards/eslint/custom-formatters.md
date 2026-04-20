---
# === CORE IDENTIFICATION ===
concept: Custom Formatters
slug: custom-formatters

# === CLASSIFICATION ===
category: extending
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/custom-formatters.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint formatter"
  - "output formatter"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
extends:
  - eslint
related:
  - custom-rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you create a custom ESLint formatter?"
  - "What data does a formatter receive?"
  - "How do you package and distribute a custom formatter?"
  - "How can you pass arguments to a formatter?"
---

# Quick Definition
A custom ESLint formatter is a function that receives an array of lint results and a context object, and returns a string representing the formatted output.

# Core Definition
A formatter is a function with the signature `function(results, context)` that returns a string (or a promise resolving to a string for async formatters, supported since ESLint v8.4.0).

The **results** argument is an array of `LintResult` objects, each containing: `filePath`, `messages` (array of lint message objects with `ruleId`, `severity`, `message`, `line`, `column`), `errorCount`, `warningCount`, `fixableErrorCount`, `fixableWarningCount`, and `source`.

The **context** argument provides: `cwd` (current working directory), `rulesMeta` (meta property values of rules), optional `color` (boolean for terminal coloring), and optional `maxWarningsExceeded` (object with `maxWarnings` and `foundWarnings`).

# Prerequisites
- Understanding of ESLint's linting output structure

# Key Properties
1. **Function signature** -- `function(results, context)` returning a string
2. **results array** -- Array of LintResult objects with messages, counts, and file paths
3. **context.rulesMeta** -- Access to rule metadata including docs URLs
4. **Async support** -- Formatters can be async functions (ESLint v8.4.0+)
5. **Environment variables** -- Formatters can use env vars for additional configuration

# Construction / Recognition
```js
module.exports = function(results, context) {
    return JSON.stringify(results, null, 2);
};
```

Usage: `eslint -f ./my-formatter.js src/`

Packaging: npm packages named `eslint-formatter-*` with keywords `["eslint", "eslint-formatter", "eslintformatter"]`.

# Context & Application
Custom formatters are used when built-in formatters do not meet reporting needs. Examples include CI-specific output (GitLab code quality reports), custom file formats, or tool-optimized displays. Formatters can be local files (path starting with `.`) or npm packages (referenced by short name without the `eslint-formatter-` prefix).

# Examples
From extend/custom-formatters.md:
- Summary formatter: reduces results to total error/warning counts
- Detailed formatter: includes rule URLs from `context.rulesMeta[msg.ruleId].docs.url`
- Terminal-friendly format: `file:line:column` for clickable links in modern terminals

# Relationships
## Related
- eslint
- custom-rules (rule meta accessible via context.rulesMeta)

# Common Errors
1. Not handling empty results -- formatter should return an empty string or appropriate message
2. Forgetting the leading `.` for local formatters -- ESLint will look for an npm package instead

# Source Reference
- extend/custom-formatters.md: Formatter function interface, results/context arguments, packaging guidelines

# Verification Notes
- High confidence: directly extracted from the official custom formatters documentation
