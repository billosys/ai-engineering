---
# === CORE IDENTIFICATION ===
concept: ESLint Class
slug: eslint-class

# === CLASSIFICATION ===
category: integration
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "integrate/nodejs-api.md"
chapter_number: null
pdf_page: null
section: "ESLint class"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint API class"
  - "ESLint programmatic class"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint-node-api
extends: []
related:
  - eslint-linter-class
  - eslint-built-in-formatters
  - eslint-integration-tutorial
contrasts_with:
  - eslint-linter-class

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I lint files programmatically in Node.js?"
  - "What constructor options does the ESLint class accept?"
  - "How do I auto-fix and output results programmatically?"
---

# Quick Definition
The `ESLint` class is the primary Node.js API for programmatic linting. It depends on the filesystem, supports linting files and text, auto-fixing, caching, suppressions, and concurrent linting via worker threads.

# Core Definition
The `ESLint` class is instantiated with an options object covering file enumeration (`cwd`, `ignore`, `ignorePatterns`, `errorOnUnmatchedPattern`), linting (`allowInlineConfig`, `baseConfig`, `overrideConfig`, `overrideConfigFile`, `plugins`, `ruleFilter`, `stats`), autofix (`fix`, `fixTypes`), caching (`cache`, `cacheLocation`, `cacheStrategy`), suppressions (`applySuppressions`, `suppressionsLocation`), and other settings (`concurrency`, `flags`). Key instance methods include `lintFiles(patterns)`, `lintText(code, options)`, `loadFormatter(nameOrPath)`, `getRulesMetaForResults(results)`, `calculateConfigForFile(filePath)`, `findConfigFile()`, `isPathIgnored(filePath)`, and `hasFlag(flagName)`. Key static methods include `ESLint.outputFixes(results)`, `ESLint.getErrorResults(results)`, `ESLint.fromOptionsModule(optionsURL)`, and static properties `ESLint.version` and `ESLint.defaultConfig`.

# Prerequisites
- eslint-node-api -- The ESLint class is part of the Node.js API

# Key Properties
1. **lintFiles(patterns)** -- Lints files matching glob patterns; returns `Promise<LintResult[]>`
2. **lintText(code, options)** -- Lints a string of code; options include `filePath` and `warnIgnored`
3. **ESLint.outputFixes(results)** -- Static method that writes auto-fixed code back to files
4. **ESLint.getErrorResults(results)** -- Static method that filters results to errors only
5. **loadFormatter(nameOrPath)** -- Loads a built-in, npm-installed, or custom formatter
6. **calculateConfigForFile(filePath)** -- Returns the resolved configuration for a file (useful for debugging)
7. **ESLint.fromOptionsModule(optionsURL)** -- Creates an instance from an options module; enables non-cloneable options with concurrency
8. **LintResult type** -- Contains `filePath`, `messages`, `errorCount`, `warningCount`, `fixableErrorCount`, `output`, `source`, `stats`
9. **Constructor fix option** -- Accepts `boolean` or predicate `(message) => boolean` for selective fixing
10. **concurrency option** -- `"off"` (default), `"auto"`, or integer for worker thread count

# Construction / Recognition
```js
const { ESLint } = require("eslint");

// Basic usage
const eslint = new ESLint();
const results = await eslint.lintFiles(["lib/**/*.js"]);
const formatter = await eslint.loadFormatter("stylish");
console.log(formatter.format(results));

// Autofix workflow
const eslint = new ESLint({ fix: true });
const results = await eslint.lintFiles(["lib/**/*.js"]);
await ESLint.outputFixes(results);

// Lint text with override config
const eslint = new ESLint({
  overrideConfigFile: true,
  overrideConfig: {
    languageOptions: { ecmaVersion: 2018, sourceType: "commonjs" },
  },
});
const results = await eslint.lintText(testCode);
```

# Context & Application
The `ESLint` class is the recommended choice for any Node.js-based integration: editor plugins, custom CLI wrappers, CI tools, and build system plugins. It handles configuration resolution, file discovery, caching, and formatting, making it a complete programmatic interface to ESLint's capabilities.

# Examples
From integrate/nodejs-api.md:
- `await eslint.lintFiles(["lib/**/*.js"])` -- lint all JS files in lib/
- `await ESLint.outputFixes(results)` -- write fixed code to disk
- `await eslint.loadFormatter("json")` -- load the JSON formatter
- `eslint.getRulesMetaForResults(results)` -- get metadata for triggered rules
- `await eslint.calculateConfigForFile("src/index.js")` -- debug configuration resolution

# Relationships
## Builds Upon
- eslint-node-api (part of the API surface)
## Related
- eslint-integration-tutorial (step-by-step guide to using this class)
- eslint-built-in-formatters (loaded via `loadFormatter()`)
## Contrasts With
- eslint-linter-class (Linter has no filesystem access; ESLint class depends on it)

# Common Errors
1. Using in the browser -- the ESLint class requires Node.js `fs`; use `Linter` for browsers
2. Not awaiting `lintFiles()` or `lintText()` -- these are async methods returning Promises
3. Using `concurrency` with non-cloneable options -- use `ESLint.fromOptionsModule()` instead

# Common Confusions
1. **lintFiles vs lintText** -- `lintFiles` reads from the filesystem; `lintText` accepts a string directly
2. **fix option as predicate** -- `fix` can be a function `(message) => boolean` to selectively apply fixes

# Source Reference
- integrate/nodejs-api.md, "ESLint class" section: Constructor options, instance methods, static methods, and type definitions

# Verification Notes
Comprehensive API reference with type signatures and examples. High confidence.
