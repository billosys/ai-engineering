---
# === CORE IDENTIFICATION ===
concept: ESLint Integration Tutorial
slug: eslint-integration-tutorial

# === CLASSIFICATION ===
category: integration
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "integrate/integration-tutorial.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint Node.js API tutorial"
  - "building an ESLint integration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint-class
extends: []
related:
  - eslint-node-api
  - eslint-editor-integrations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I build a custom integration using the ESLint Node.js API?"
  - "What are the steps to programmatically lint and fix files?"
  - "What use cases benefit from a custom ESLint integration?"
---

# Quick Definition
The ESLint integration tutorial walks through building a Node.js project that uses the `ESLint` class to programmatically lint files, apply auto-fixes, and output results -- a pattern applicable to editor plugins, custom linter tools, code review tools, and learning platforms.

# Core Definition
The tutorial demonstrates a five-step pattern for building ESLint integrations: (1) create an `ESLint` instance with `overrideConfigFile: true`, `overrideConfig`, and `fix: true`; (2) call `eslint.lintFiles(filePaths)` to lint target files; (3) call `ESLint.outputFixes(results)` to write fixed code back to disk; (4) process results by aggregating `errorCount` and `warningCount`; (5) export the integration function. The tutorial identifies five primary use cases: code editors/IDEs, custom linter tools, code review tools, learning platforms, and developer tool integration (bundlers, testing frameworks).

# Prerequisites
- eslint-class -- The tutorial uses the ESLint class API

# Key Properties
1. **Five-step pattern** -- Import/configure, lint files, output fixes, process results, export
2. **overrideConfigFile: true** -- Prevents ESLint from searching for config files; uses provided config only
3. **overrideConfig** -- Inline configuration object with `languageOptions` and `rules`
4. **ESLint.outputFixes(results)** -- Static method to write fixes back to files
5. **Result aggregation** -- Sum `errorCount` and `warningCount` across results to determine total problems
6. **eslint as dependency** -- Install as a regular dependency (not dev), since the integration ships ESLint

# Construction / Recognition
```js
const { ESLint } = require("eslint");

function createESLintInstance(overrideConfig) {
  return new ESLint({
    overrideConfigFile: true,
    overrideConfig,
    fix: true,
  });
}

async function lintAndFix(eslint, filePaths) {
  const results = await eslint.lintFiles(filePaths);
  await ESLint.outputFixes(results);
  return results;
}

function outputLintingResults(results) {
  const problems = results.reduce(
    (acc, result) => acc + result.errorCount + result.warningCount, 0
  );
  if (problems > 0) {
    console.log("Linting errors found!");
    console.log(results);
  } else {
    console.log("No linting errors found.");
  }
  return results;
}

async function lintFiles(filePaths) {
  const overrideConfig = {
    languageOptions: { ecmaVersion: 2018, sourceType: "commonjs" },
    rules: { "no-console": "error", "no-unused-vars": "warn" },
  };
  const eslint = createESLintInstance(overrideConfig);
  const results = await lintAndFix(eslint, filePaths);
  return outputLintingResults(results);
}

module.exports = { lintFiles };
```

# Context & Application
This pattern is the foundation for building any tool that programmatically uses ESLint: editor plugins that show real-time errors, CI tools that report on pull requests, code review bots, educational platforms with live linting feedback, and build system plugins that fail on lint errors.

# Examples
From integrate/integration-tutorial.md:
- Complete working example in `example-eslint-integration.js`
- Use cases: editor plugins, custom linters, code review tools, learning platforms, bundler plugins

# Relationships
## Builds Upon
- eslint-class (uses ESLint class API directly)
## Related
- eslint-node-api (the tutorial demonstrates practical API usage)
- eslint-editor-integrations (editor plugins follow this pattern)

# Common Errors
1. Installing eslint as a dev dependency for an integration -- it should be a regular dependency since it ships with the tool
2. Not calling `ESLint.outputFixes()` after `lintFiles()` when `fix: true` -- fixes are computed but not written

# Common Confusions
1. **overrideConfigFile: true vs string** -- `true` means "don't search for config files"; a string provides a specific config file path
2. **fix in constructor vs fix in results** -- Setting `fix: true` in the constructor makes `lintFiles()` compute fixes; `outputFixes()` writes them

# Source Reference
- integrate/integration-tutorial.md: Step-by-step tutorial with complete code
- integrate/index.md: Integration overview

# Verification Notes
Complete tutorial with working code examples. High confidence.
