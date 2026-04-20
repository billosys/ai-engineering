---
# === CORE IDENTIFICATION ===
concept: ESLint Linter Class
slug: eslint-linter-class

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
section: "Linter"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Linter class"
  - "ESLint browser API"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint-node-api
extends: []
related:
  - eslint-class
contrasts_with:
  - eslint-class

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I lint code in the browser or without filesystem access?"
  - "What is the difference between verify() and verifyAndFix()?"
  - "How do I get suppressed messages from the Linter?"
---

# Quick Definition
The `Linter` class is a lightweight, browser-compatible API that parses and evaluates JavaScript code in memory without filesystem operations. It provides `verify()` for linting and `verifyAndFix()` for auto-fixing.

# Core Definition
The `Linter` class does the actual evaluation of JavaScript code without any filesystem operations -- it does not read configuration files or access the file system. This makes it suitable for browser environments (e.g., eslint.org/demo). It accepts a single constructor option: `cwd` (accessible to rules via `context.cwd`). The primary method `verify(code, config, options)` takes source code (string or SourceCode instance), a configuration object or array, and optional settings (filename, preprocess/postprocess functions, disableFixes, allowInlineConfig, reportUnusedDisableDirectives, ruleFilter). It returns an array of lint message objects. The `verifyAndFix(code, config)` method additionally runs autofix logic, returning `{ fixed, output, messages }`. Helper methods include `getSuppressedMessages()`, `getSourceCode()`, `getTimes()`, `getFixPassCount()`, and `hasFlag()`.

# Prerequisites
- eslint-node-api -- The Linter class is part of the Node.js API (also usable in browsers)

# Key Properties
1. **verify(code, config, options)** -- Core linting method; returns array of message objects with `ruleId`, `severity`, `line`, `column`, `message`, `fix`, `suggestions`
2. **verifyAndFix(code, config)** -- Lints and auto-fixes; returns `{ fixed: boolean, output: string, messages: [] }`
3. **getSuppressedMessages()** -- Returns messages suppressed by `eslint-disable` directives from the previous `verify()` call
4. **getSourceCode()** -- Returns the `SourceCode` instance from the last `verify()` run
5. **No filesystem dependency** -- Does not read config files or access fs; configuration must be passed directly
6. **Browser-compatible** -- Can run in browser environments
7. **cwd option** -- Sets `context.cwd` for rules; defaults to `process.cwd()` in Node.js, `undefined` in browsers
8. **Linter.version** -- Static and instance property with ESLint's semantic version string

# Construction / Recognition
```js
const { Linter } = require("eslint");
const linter = new Linter();

// Basic linting
const messages = linter.verify("var foo;", {
  rules: { semi: 2 }
}, { filename: "foo.js" });
// => [{ ruleId: "semi", severity: 2, message: "Expected a semicolon.", ... }]

// Auto-fix
const result = linter.verifyAndFix("var foo", {
  rules: { semi: 2 }
});
// => { fixed: true, output: "var foo;", messages: [] }

// Suppressed messages
const messages = linter.verify(
  "var foo = bar; // eslint-disable-line -- Needed",
  { rules: { semi: ["error", "never"] } }
);
const suppressed = linter.getSuppressedMessages();
```

# Context & Application
The `Linter` class is used when you need to lint code in memory without touching the filesystem -- browser-based playgrounds, online code editors, embedded linting in web applications, and unit testing rule implementations. For most Node.js server-side integrations, the `ESLint` class is preferred because it handles configuration resolution automatically.

# Examples
From integrate/nodejs-api.md:
- `linter.verify("var foo;", { rules: { semi: 2 } })` -- lint with inline config
- `linter.verifyAndFix("var foo", { rules: { semi: 2 } })` -- returns `{ fixed: true, output: "var foo;", messages: [] }`
- `linter.getSuppressedMessages()` -- returns suppressed directive messages with justification
- `linter.version` / `Linter.version` -- e.g., `"9.0.0"`

# Relationships
## Builds Upon
- eslint-node-api (part of the API surface)
## Contrasts With
- eslint-class (ESLint class depends on fs, reads config files, provides `lintFiles()`; Linter has no fs dependency)

# Common Errors
1. Expecting `Linter` to read config files -- it does not; you must pass configuration directly
2. Calling `getSuppressedMessages()` before `verify()` -- returns an empty array

# Common Confusions
1. **Linter vs ESLint class** -- Linter is stateless and in-memory only; ESLint class wraps Linter with file system and configuration resolution
2. **verify vs verifyAndFix** -- `verify` only reports; `verifyAndFix` also applies fixes and returns the modified source

# Source Reference
- integrate/nodejs-api.md, "Linter" section: Constructor, verify(), verifyAndFix(), helper methods

# Verification Notes
Directly documented with code examples and return type descriptions. High confidence.
