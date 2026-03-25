---
# === CORE IDENTIFICATION ===
concept: ESTree
slug: estree

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
section: "ESTree"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESTree format"
  - "ESTree specification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-syntax-tree
extends: []
related:
  - parsers
  - esquery-and-selectors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is ESTree?"
  - "What AST format does ESLint use?"
  - "How does ESTree represent JavaScript code?"
---

# Quick Definition
ESTree is the AST format specification used by ESLint to represent JavaScript syntax as a structured tree of typed nodes.

# Core Definition
ESTree is the specific format that defines how JavaScript syntax is represented as an abstract syntax tree. Static analysis tools such as ESLint typically operate by converting syntax into an AST in the ESTree format. Each node in an ESTree AST has a `type` property indicating its syntactic role (e.g., `BinaryExpression`, `Literal`, `ExpressionStatement`) along with type-specific properties.

# Prerequisites
- abstract-syntax-tree: ESTree is a specific format for ASTs

# Key Properties
1. **Standardized format** -- Community specification for JavaScript AST representation
2. **Typed nodes** -- Each node has a `type` property (e.g., `BinaryExpression`, `Literal`)
3. **Type-specific properties** -- Nodes carry properties relevant to their type (e.g., `operator`, `value`, `left`, `right`)
4. **Open specification** -- Maintained at github.com/estree/estree

# Construction / Recognition
Example from the glossary -- the code `1 + 2;` produces:
```json
{
  "type": "ExpressionStatement",
  "expression": {
    "type": "BinaryExpression",
    "left": { "type": "Literal", "value": 1, "raw": "1" },
    "operator": "+",
    "right": { "type": "Literal", "value": 2, "raw": "2" }
  }
}
```

# Context & Application
ESTree is the standard that parsers must produce and rules must consume. When writing custom ESLint rules, developers work with ESTree node types to identify and check code patterns. The ESTree format is shared across multiple JavaScript tools beyond ESLint.

# Examples
From use/core-concepts/glossary.md:
- "The format used by ESLint for how to represent JavaScript syntax as an AST."
- "Static analysis tools such as ESLint typically operate by converting syntax into an AST in the ESTree format."
- The `1 + 2;` example showing ExpressionStatement > BinaryExpression > Literal structure

# Relationships
## Builds Upon
- abstract-syntax-tree

## Related
- parsers (produce ESTree-formatted ASTs)
- esquery-and-selectors (query ESTree nodes)
- rules (operate on ESTree nodes)

# Common Errors
1. Assuming ESTree is ESLint-specific -- it is a community specification used by many JavaScript tools

# Common Confusions
1. **ESTree vs. AST** -- ESTree is a specific AST format; "AST" is the general concept. There are other AST formats for JavaScript (e.g., Babel's AST), but ESLint uses ESTree

# Source Reference
- use/core-concepts/glossary.md: ESTree definition with example

# Verification Notes
- High confidence: Explicitly defined in the glossary with a complete JSON example
