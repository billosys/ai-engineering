---
# === CORE IDENTIFICATION ===
concept: Custom Parsers
slug: custom-parsers

# === CLASSIFICATION ===
category: extending
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/custom-parsers.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint parser"
  - "custom parser"
  - "parseForESLint"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - custom-rules
extends:
  - eslint
related:
  - scope-manager
  - language-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you create a custom parser for ESLint?"
  - "What is the difference between parse() and parseForESLint()?"
  - "What AST requirements does ESLint impose?"
  - "How does a parser provide scope analysis or custom visitor keys?"
---

# Quick Definition
A custom ESLint parser is a JavaScript object with a `parse()` or `parseForESLint()` method that transforms source code into an ESTree-compatible AST for ESLint to analyze.

# Core Definition
A custom parser is a JavaScript object with either a `parse(code, options)` method (returning just the AST) or a `parseForESLint(code, options)` method (returning an object with `ast`, optional `services`, `scopeManager`, and `visitorKeys`).

The `parseForESLint` return object:
- **ast** (required): ESTree-based AST with `range` (0-based index array) and non-null `loc` on all nodes, `tokens` and `comments` arrays on the Program node, and `raw` on Literal nodes.
- **services** (optional): Parser-dependent services accessible as `context.sourceCode.parserServices` (e.g., type checkers).
- **scopeManager** (optional): Custom `ScopeManager` for experimental syntax. Must support `addGlobals(names)` as of ESLint v10.0.0.
- **visitorKeys** (optional): Custom traversal keys mapping node types to arrays of property names.

All AST nodes must have rewritable `parent` properties (ESLint sets these during traversal).

# Prerequisites
- Understanding of ASTs and the ESTree specification
- Understanding of ESLint's rule system

# Key Properties
1. **parse()** -- Simple interface returning only the AST
2. **parseForESLint()** -- Extended interface returning ast, services, scopeManager, visitorKeys
3. **ESTree compliance** -- All nodes need `range` and non-null `loc`; Program needs `tokens` and `comments`
4. **Parser services** -- Custom data available to rules via `context.sourceCode.parserServices`
5. **meta object** -- Recommended `name` and `version` for debugging and caching

# Construction / Recognition
```js
function parseForESLint(code, options) {
    return {
        ast: espree.parse(code, options),
        services: { foo() { console.log("foo"); } },
        scopeManager: null,
        visitorKeys: null
    };
}
module.exports = { parseForESLint };
```

Configuration:
```js
// eslint.config.js
module.exports = defineConfig([{
    languageOptions: { parser: require("./my-parser") }
}]);
```

# Context & Application
Custom parsers enable ESLint to lint languages beyond standard JavaScript. The most prominent example is `@typescript-eslint/parser`, which extends ESLint to support TypeScript. Parsers can provide type information through `services`, enabling type-aware linting rules.

# Examples
From extend/custom-parsers.md:
- Simple parser logging parse duration: `function parse(code, options) { return espree.parse(code, options); }`
- Parser providing services: `{ ast: espree.parse(code, options), services: { foo() { console.log("foo"); } } }`

# Relationships
## Depends On
- scope-manager (optionally provided by parseForESLint)

## Related
- language-system (languages subsume parsers for non-JS support)
- custom-rules (rules consume parser output)

# Common Errors
1. Omitting `range` on AST nodes -- ESLint requires `range` on all nodes
2. Setting `loc` to null -- ESLint requires non-null `loc` despite ESTree allowing it
3. Forgetting `tokens` and `comments` on the Program node -- required for rule analysis

# Source Reference
- extend/custom-parsers.md: Full parser interface specification and AST requirements

# Verification Notes
- High confidence: all interface requirements enumerated directly from documentation
