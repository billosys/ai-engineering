---
# === CORE IDENTIFICATION ===
concept: ESQuery and Selectors
slug: esquery-and-selectors

# === CLASSIFICATION ===
category: ast
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/core-concepts/glossary.md"
chapter_number: null
pdf_page: null
section: "ESQuery"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESQuery"
  - "AST selectors"
  - "node selectors"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-syntax-tree
  - estree
extends: []
related:
  - rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is ESQuery?"
  - "What are AST selectors in ESLint?"
  - "How do you query specific AST nodes?"
  - "How are CSS selectors used with ASTs?"
---

# Quick Definition
ESQuery is the library used by ESLint to parse CSS-like selector syntax for querying nodes within an AST, enabling rules to target specific code patterns.

# Core Definition
ESQuery interprets CSS-like syntax for matching AST node properties. It allows ESLint rules to specify which nodes they want to examine using a familiar selector syntax. Selectors describe how to search for nodes within an AST. Rules use ESQuery selectors to find nodes that should be checked for violations.

# Prerequisites
- abstract-syntax-tree: Selectors query nodes within an AST
- estree: Selectors use ESTree node type names

# Key Properties
1. **CSS-like syntax** -- Uses a syntax similar to CSS selectors for querying tree structures
2. **Type selection** -- Select nodes by type name (e.g., `BinaryExpression`)
3. **Attribute filtering** -- Filter by node properties (e.g., `[operator='+']`)
4. **Combinators** -- Support parent/child relationships (e.g., `BinaryExpression > Literal`)
5. **Rule integration** -- Rules register selectors to specify which nodes they want to visit

# Construction / Recognition
Selector examples from the glossary:
- `BinaryExpression` -- selects all nodes of type BinaryExpression
- `BinaryExpression[operator='+']` -- selects BinaryExpression nodes whose operator is `+`
- `BinaryExpression > Literal[value=1]` -- selects Literal nodes with value 1 whose direct parent is a BinaryExpression

# Context & Application
ESQuery selectors are used by rule authors to specify which AST nodes their rule should examine. Instead of manually traversing the entire AST, rules declare selectors and ESLint calls the rule's handler when matching nodes are encountered. This makes rule authoring more declarative and efficient.

# Examples
From use/core-concepts/glossary.md:
- `BinaryExpression`: "selects all nodes of type BinaryExpression"
- `BinaryExpression[operator='+']`: "selects all BinaryExpression nodes whose operator is `+`"
- `BinaryExpression > Literal[value=1]`: "selects all Literal nodes with value `1` whose direct parent is a BinaryExpression"

# Relationships
## Builds Upon
- abstract-syntax-tree
- estree

## Related
- rules (use selectors to find nodes to check)

# Common Errors
1. Using CSS class/ID selectors (`.class`, `#id`) which do not apply to ASTs -- ESQuery uses node type names and attribute selectors
2. Forgetting that selector syntax is case-sensitive for node type names

# Common Confusions
1. **ESQuery vs. CSS selectors** -- ESQuery borrows syntax from CSS but operates on AST nodes, not DOM elements. Not all CSS selector features apply

# Source Reference
- use/core-concepts/glossary.md: ESQuery definition with selector examples, Selector definition

# Verification Notes
- High confidence: Explicitly defined in the glossary with three concrete examples
