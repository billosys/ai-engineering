---
# === CORE IDENTIFICATION ===
concept: Language System
slug: language-system

# === CLASSIFICATION ===
category: languages
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/languages.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint language"
  - "Language object"
  - "multi-language linting"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - creating-plugins
extends:
  - creating-plugins
related:
  - custom-parsers
  - scope-manager
contrasts_with:
  - custom-parsers

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you extend ESLint to lint non-JavaScript languages?"
  - "What are the Language, SourceCode, and parser components?"
  - "What interface must a Language object implement?"
  - "What interface must a SourceCode object implement?"
---

# Quick Definition
The Language system (ESLint v9.7.0+) allows plugins to define complete language support -- including parsing, source code representation, and AST traversal -- enabling ESLint to lint any programming language, not just JavaScript.

# Core Definition
A language definition requires three components:

**Parser**: Converts plain text into a data structure (AST or CST). No specific format is required. Nodes should have type, location (start/end line/column), and range (start/end character index) properties.

**SourceCode object** (must implement `TextSourceCode` interface from `@eslint/core`):
- Required: `ast`, `text`, `getLoc(nodeOrToken)`, `getRange(nodeOrToken)`, `traverse()` (returns iterable of VisitTraversalStep or CallTraversalStep)
- Optional: `visitorKeys`, `applyLanguageOptions()`, `getDisableDirectives()`, `getInlineConfigNodes()`, `applyInlineConfig()`, `finalize()`
- Recommended: `lines`, `getParent(node)`, `getAncestors(node)`, `getText(node, beforeCount, afterCount)`

**Language object** (must implement `Language` interface from `@eslint/core`):
- Required: `fileType` ("text"), `lineStart` (0 or 1), `columnStart` (0 or 1), `nodeTypeKey` (usually "type" or "kind"), `validateLanguageOptions(languageOptions)`, `parse(file, context)`, `createSourceCode(file, parseResult, context)`
- Optional: `visitorKeys`, `defaultLanguageOptions`, `matchesSelectorClass(className, node, ancestry)`, `normalizeLanguageOptions(languageOptions)`

Languages are published in plugins under the `languages` key and referenced in config as `"namespace/language-name"`.

# Prerequisites
- Understanding of ESLint plugins
- Understanding of ASTs or CSTs

# Key Properties
1. **Language-agnostic core** -- ESLint's core is generic; language-specific logic lives in Language objects
2. **Three components** -- Parser, SourceCode, and Language objects work together
3. **TextSourceCode interface** -- Standard API for ESLint to interact with source code
4. **traverse() method** -- SourceCode must provide an iterable for AST/CST traversal
5. **lineStart/columnStart** -- Configurable 0-based or 1-based indexing per language
6. **nodeTypeKey** -- Configurable property name for node types (e.g., "type" vs "kind")

# Construction / Recognition
```js
const plugin = {
    meta: { name: "eslint-plugin-example", version: "1.2.3" },
    languages: { my: myLanguage },
    rules: { /* rules for this language */ }
};
```

Configuration:
```js
export default defineConfig([{
    files: ["**/*.my"],
    plugins: { example },
    language: "example/my"
}]);
```

# Context & Application
The Language system enables ESLint to move beyond JavaScript. Reference implementations include `@eslint/json` for JSON linting and `@eslint/markdown` for Markdown. The `@eslint/plugin-kit` package provides `TextSourceCodeBase` to simplify SourceCode implementation. Languages can support both ASTs (like ESTree for JS) and CSTs (like those from some parser generators).

# Examples
From extend/languages.md:
- Reference: `JSONLanguage` (github.com/eslint/json) as a basic Language class
- Reference: `JSONSourceCode` as a basic SourceCode class
- `@eslint/plugin-kit` provides `TextSourceCodeBase` for common functionality

# Relationships
## Part Of
- creating-plugins (languages are distributed in plugins)

## Replaces
- custom-parsers (for non-JS languages, the Language system is preferred over standalone parsers)

## Related
- custom-parsers
- scope-manager

# Common Errors
1. Not implementing `validateLanguageOptions()` -- required even if the language has no options
2. Omitting range information from AST nodes -- needed for autofix support
3. Forgetting `traverse()` on SourceCode -- ESLint cannot analyze the code without it

# Source Reference
- extend/languages.md: Complete Language, SourceCode, and parser interfaces; plugin integration

# Verification Notes
- High confidence: all interface requirements enumerated directly from the documentation
