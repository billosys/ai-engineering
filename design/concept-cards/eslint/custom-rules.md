---
# === CORE IDENTIFICATION ===
concept: Custom Rules
slug: custom-rules

# === CLASSIFICATION ===
category: extending
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/custom-rules.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint custom rule"
  - "ESLint rule"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - rules
extends:
  - rules
related:
  - rule-meta-object
  - rule-context-object
  - ast-selectors
  - code-path-analysis
  - creating-plugins
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is a custom ESLint rule structured?"
  - "What are the three rule types in ESLint?"
  - "How does a rule use visitor methods to examine AST nodes?"
  - "How do you test a custom ESLint rule?"
---

# Quick Definition
A custom ESLint rule is a JavaScript object with a `meta` property (containing metadata) and a `create` function (returning visitor methods) that validates code against a specific expectation.

# Core Definition
Custom rules follow a two-part structure: a `meta` object describing the rule's type, documentation, fixability, schema, and messages; and a `create(context)` function that returns an object whose keys are AST node types (or selectors) and whose values are visitor functions called during AST traversal. Visitor functions receive the matched node and can use `context.report()` to flag problems. Rules can also listen for `:exit` events (called while going up the tree) and code path analysis events like `onCodePathStart`.

Rules have three types: `"problem"` (code that will cause errors or confusing behavior), `"suggestion"` (code that could be improved), and `"layout"` (whitespace, semicolons, and other visual aspects).

# Prerequisites
- Understanding of ESLint and its rule system
- Basic understanding of ASTs (abstract syntax trees)

# Key Properties
1. **meta object** -- Contains type, docs, fixable, schema, messages, hasSuggestions, defaultOptions, and deprecated
2. **create function** -- Receives context, returns visitor methods keyed by node type or selector
3. **Rule types** -- `"problem"`, `"suggestion"`, or `"layout"`
4. **Visitor methods** -- Called during AST traversal; `:exit` suffix triggers on upward traversal
5. **Code path events** -- `onCodePathStart`, `onCodePathEnd` for analyzing execution routes
6. **RuleTester** -- Built-in testing utility for validating rules with valid/invalid test cases

# Construction / Recognition
```js
module.exports = {
    meta: {
        type: "suggestion",
        docs: { description: "Description of the rule" },
        fixable: "code",
        schema: [],
    },
    create: function(context) {
        return {
            VariableDeclarator(node) {
                // visitor logic
            }
        };
    }
};
```

# Context & Application
Custom rules are created when ESLint's built-in rules and community-published rules do not cover a project's specific needs, such as enforcing company-specific conventions, preventing recurring bugs, or ensuring compliance with a custom style guide. Rules are distributed inside plugins as npm packages.

# Examples
From extend/custom-rule-tutorial.md:
- A rule requiring all `const foo` variables be assigned `"bar"`, using `context.report()` with a `fix` function
- Testing with `RuleTester#run()` which requires at least one valid and one invalid test case

From extend/custom-rules.md:
- "If a key is a node type or a selector, ESLint calls that visitor function while going down the tree."
- "If a key is a node type or a selector plus `:exit`, ESLint calls that visitor function while going up the tree."

# Relationships
## Part Of
- creating-plugins

## Depends On
- rule-meta-object
- rule-context-object

## Related
- ast-selectors
- code-path-analysis

# Common Errors
1. Forgetting to set `meta.fixable` when implementing a `fix` function -- ESLint will throw an error
2. Forgetting to set `meta.hasSuggestions` when providing suggestions -- ESLint will throw an error
3. Modifying shared CodePath or CodePathSegment instances in rules -- use a map of information instead

# Source Reference
- extend/custom-rules.md: Complete rule structure and API reference
- extend/custom-rule-tutorial.md: Step-by-step tutorial building a rule from scratch

# Verification Notes
- High confidence: directly extracted from the official custom rules documentation
