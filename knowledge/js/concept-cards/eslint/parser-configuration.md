---
# === CORE IDENTIFICATION ===
concept: Parser Configuration
slug: parser-configuration

# === CLASSIFICATION ===
category: configuration
subcategory: parsing
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/parser.md"
chapter_number: null
pdf_page: null
section: "Configure a Custom Parser"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - custom parser
  - eslint parser config
  - languageOptions.parser

# === TYPED RELATIONSHIPS ===
prerequisites:
  - language-options
extends: []
related:
  - configuration-objects
  - plugin-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use a custom parser with ESLint?"
  - "What parsers are compatible with ESLint?"
  - "How do I pass options to a custom parser?"
  - "What is the default ESLint parser?"
---

# Quick Definition
Parser configuration replaces ESLint's default Espree parser with a custom parser via `languageOptions.parser`, enabling linting of TypeScript, experimental syntax, or other JavaScript variants.

# Core Definition
ESLint's default parser is Espree, which supports standard ECMAScript syntax. Custom parsers can be set via the `languageOptions.parser` property, which must be an object conforming to the parser interface (having a `parse()` or `parseForESLint()` method). Parser-specific options are passed through `languageOptions.parserOptions`. ESLint automatically passes `ecmaVersion` and `sourceType` to all parsers, providing context about the JavaScript environment.

# Prerequisites
- language-options (parser is set within languageOptions)

# Key Properties
1. Default parser: Espree (supports standard ECMAScript)
2. Custom parser set via `languageOptions.parser` (must be an object, not a string)
3. Parser options via `languageOptions.parserOptions` (parser-specific, check parser docs)
4. ESLint passes `ecmaVersion` and `sourceType` to all parsers automatically
5. Compatible third-party parsers: Esprima, `@babel/eslint-parser`, `@typescript-eslint/parser`
6. No guarantees that external parsers work correctly; ESLint does not fix third-party parser bugs

# Construction / Recognition
Using Babel parser:
```js
import babelParser from "@babel/eslint-parser";
import { defineConfig } from "eslint/config";

export default defineConfig([{
  files: ["**/*.js", "**/*.mjs"],
  languageOptions: {
    parser: babelParser,
  },
}]);
```

With parser options:
```js
export default defineConfig([{
  languageOptions: {
    parser: babelParser,
    parserOptions: {
      requireConfigFile: false,
      babelOptions: {
        babelrc: false,
        configFile: false,
        presets: ["@babel/preset-env"],
      },
    },
  },
}]);
```

# Context & Application
Custom parsers are essential for TypeScript projects (`@typescript-eslint/parser`), projects using experimental JavaScript features (`@babel/eslint-parser`), and any code that extends beyond standard ECMAScript syntax. Parser configuration is typically one of the first things set up in TypeScript ESLint configurations.

# Examples
From `use/configure/parser.md`: The Babel parser example shows how `parserOptions` are entirely parser-specific -- Babel options like `babelrc`, `configFile`, and `presets` are not ESLint concepts.

# Relationships
## Builds Upon
- language-options (parser and parserOptions are sub-properties of languageOptions)

## Enables
- TypeScript linting (via @typescript-eslint/parser)
- Experimental syntax support (via @babel/eslint-parser)

## Related
- configuration-objects (parser config lives in config objects)
- plugin-configuration (parsers often pair with corresponding plugins)

# Common Errors
1. Passing a parser as a string instead of an imported object (flat config requires objects)
2. Not installing the parser package as a dev dependency
3. Confusing parser options between different parsers (options are parser-specific)

# Common Confusions
1. Thinking ESLint's Espree parser can handle TypeScript -- it cannot; a custom parser is required
2. Assuming parser options are standardized across parsers -- they are entirely parser-dependent

# Source Reference
- `sources-md/eslint/use/configure/parser.md`, all sections

# Verification Notes
Extracted from the parser configuration documentation. Compatible parser list and parser interface requirements verified against source.
