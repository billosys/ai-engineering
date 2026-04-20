---
# === CORE IDENTIFICATION ===
concept: AST Selectors
slug: ast-selectors

# === CLASSIFICATION ===
category: ast-analysis
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/selectors.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint selectors"
  - "ESQuery selectors"
  - "AST query selectors"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - custom-rules
extends:
  - custom-rules
related:
  - rule-context-object
  - code-path-analysis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you use CSS-like selectors to match AST nodes?"
  - "What selector syntax does ESLint support?"
  - "How do you restrict syntax patterns without writing custom rules?"
  - "How does selector specificity work in ESLint?"
---

# Quick Definition
AST selectors are CSS-like strings that match nodes in an abstract syntax tree, used in custom rule visitor methods and the `no-restricted-syntax` rule to precisely target syntactic patterns.

# Core Definition
AST selectors use a syntax similar to CSS selectors but operate on AST nodes instead of DOM elements. They are powered by the [esquery](https://github.com/estools/esquery) library.

Supported selector syntax:
- **Node type**: `ForStatement`
- **Wildcard**: `*` (matches all nodes)
- **Attribute existence**: `[attr]`
- **Attribute value**: `[attr="foo"]`, `[attr=123]`
- **Attribute regex**: `[attr=/foo.*/]`
- **Attribute conditions**: `[attr!="foo"]`, `[attr>2]`, `[attr<3]`, `[attr>=2]`, `[attr<=3]`
- **Nested attribute**: `[attr.level2="foo"]`
- **Field**: `FunctionDeclaration > Identifier.id`
- **Positional**: `:first-child`, `:last-child`, `:nth-child(2)`, `:nth-last-child(1)`
- **Descendant**: `FunctionExpression ReturnStatement`
- **Child**: `UnaryExpression > Literal`
- **Siblings**: `VariableDeclaration ~ VariableDeclaration` (following), `Literal + SpreadElement` (adjacent)
- **Negation**: `:not(ForStatement)`
- **Matches-any**: `:matches(...)` or `:is(...)`
- **Class**: `:statement`, `:expression`, `:declaration`, `:function`, `:pattern`

Adding `:exit` to a selector triggers the listener on upward traversal. Specificity determines listener order when multiple selectors match the same node.

# Prerequisites
- Understanding of ASTs and ESLint custom rules

# Key Properties
1. **CSS-like syntax** -- Familiar combinators (descendant, child, sibling) applied to AST nodes
2. **Attribute selectors** -- Filter by node properties including nested properties and regex
3. **Class selectors** -- `:statement`, `:expression`, `:declaration`, `:function`, `:pattern`
4. **Specificity ordering** -- More class/attribute/pseudo-class selectors = higher specificity
5. **:exit modifier** -- Triggers listener during upward tree traversal
6. **no-restricted-syntax integration** -- Selectors can be used directly in config without custom rules

# Construction / Recognition
In a custom rule:
```js
return {
    "IfStatement > BlockStatement": function(node) { /* ... */ },
    "FunctionDeclaration[params.length>3]": function(node) { /* ... */ }
};
```

In configuration (no custom rule needed):
```json
{
    "rules": {
        "no-restricted-syntax": ["error", "CallExpression[callee.name='require']"]
    }
}
```

# Context & Application
Selectors provide a powerful way to target specific code patterns. In custom rules, selectors replace the need for manual parent/child checking in visitor methods. With `no-restricted-syntax`, teams can ban specific patterns (e.g., `require()` calls, `setTimeout` with wrong argument count, `if` without blocks) purely through configuration.

# Examples
From extend/selectors.md:
- `VariableDeclarator > Identifier` -- match identifiers that are direct children of variable declarators
- `CallExpression[callee.name='setTimeout'][arguments.length!=2]` -- match setTimeout calls without exactly 2 arguments
- `IfStatement > :not(BlockStatement).consequent` -- match if statements without block bodies
- `Identifier[name=/^foo/]` -- match identifiers whose names start with "foo"

# Relationships
## Used By
- custom-rules (as visitor method keys)
- rules (via no-restricted-syntax)

## Related
- rule-context-object

# Common Errors
1. Forgetting to escape regex forward slashes in selectors inside JSON -- `\/` needed, then `\\` for JSON escaping
2. Expecting `ax+b` support in `:nth-child` -- ESLint only supports simple integer arguments

# Source Reference
- extend/selectors.md: Complete selector syntax reference, specificity rules, usage examples

# Verification Notes
- High confidence: all supported selectors enumerated directly from documentation
